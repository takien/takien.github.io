#!/usr/bin/env python3
import json
import re
import os
import hashlib
from datetime import datetime

months = {
    "january": 1, "januari": 1, "jan": 1,
    "february": 2, "februari": 2, "feb": 2,
    "march": 3, "maret": 3, "mar": 3,
    "april": 4, "apr": 4,
    "may": 5, "mei": 5,
    "june": 6, "juni": 6, "jun": 6,
    "july": 7, "juli": 7, "jul": 7,
    "august": 8, "agustus": 8, "aug": 8, "agt": 8,
    "september": 9, "sep": 9,
    "october": 10, "oktober": 10, "oct": 10, "okt": 10,
    "november": 11, "nov": 11,
    "december": 12, "desember": 12, "dec": 12, "des": 12
}

def parse_fb_date(d_str):
    if not d_str:
        return None
    s = d_str.strip().lower()
    s = re.sub(r"(\d{1,2})\.(\d{2})", r"\1:\2", s)
    m = re.search(r"(\d{1,2})\s+([a-z]+)\s+(\d{4})(?:\s+(?:at|pukul)?\s+(\d{1,2}):(\d{2}))?", s)
    if m:
        day = int(m.group(1))
        month_str = m.group(2)
        year = int(m.group(3))
        hour = int(m.group(4)) if m.group(4) else 12
        minute = int(m.group(5)) if m.group(5) else 0
        month = months.get(month_str)
        if month:
            return datetime(year, month, day, hour, minute)
    return None

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text).strip("-")
    return text[:60].strip("-") or "post"

def detect_category_and_tags(content, group_name):
    c_lower = content.lower()
    tags = ["facebook"]
    
    if group_name and not group_name.startswith("Wak Jek"):
        tags.append(group_name)
    
    if "wordpress" in c_lower or "wp" in c_lower or "theme" in c_lower or "plugin" in c_lower or (group_name and "wordpress" in group_name.lower()):
        cat = "WordPress"
        if "wordpress" not in [t.lower() for t in tags]:
            tags.append("wordpress")
        if "plugin" in c_lower:
            tags.append("plugin")
        if "theme" in c_lower:
            tags.append("theme")
    elif any(k in c_lower for k in ["php", "javascript", "jquery", "css", "html", "nginx", "code", "coding", "debug", "vps", "node.js", "nodejs", "ubuntu", "mysql"]):
        cat = "Programming"
        if "programming" not in [t.lower() for t in tags]:
            tags.append("programming")
    elif any(k in c_lower for k in ["facebook", "google", "internet", "browser", "chrome", "firefox", "domain", "hosting"]):
        cat = "Internet"
        if "internet" not in [t.lower() for t in tags]:
            tags.append("internet")
    else:
        cat = "Pribadi"
        tags.append("pribadi")
        
    return cat, tags

def get_dedup_key(p):
    c = p.get("content", "").strip()
    if c:
        return c[:120]
    imgs = p.get("images", [])
    if imgs:
        return "img:" + imgs[0].split("?")[0]
    comms = p.get("comments", [])
    if comms:
        return "comm:" + comms[0].get("text", "")[:50]
    return "empty"

def main():
    path1 = "_source/fb_posts_1788633061987.json"
    path2 = "_source/fb_export_1788657490647.json"

    posts1 = []
    posts2 = []
    if os.path.exists(path1):
        with open(path1, "r", encoding="utf-8") as f:
            posts1 = json.load(f)
    if os.path.exists(path2):
        with open(path2, "r", encoding="utf-8") as f:
            posts2 = json.load(f)

    print(f"Loaded Batch 1: {len(posts1)} posts, Batch 2: {len(posts2)} posts.")

    # Remove existing generated facebook posts (except custom admin page from 2011)
    out_dir = "src/content/posts"
    for fname in os.listdir(out_dir):
        if fname.startswith("facebook_") and fname != "facebook_2011_01_30_wordpress-custom-admin-page-by-me.md":
            os.remove(os.path.join(out_dir, fname))

    # Merge and deduplicate
    merged = []
    seen = set()

    for i, p in enumerate(posts1):
        k = get_dedup_key(p)
        if k not in seen:
            seen.add(k)
            merged.append(("fb", i, p))

    for i, p in enumerate(posts2):
        k = get_dedup_key(p)
        if k not in seen:
            seen.add(k)
            merged.append(("fb_new", i, p))

    print(f"Total unique posts to import: {len(merged)}")

    images_dir = "public/images/facebook"
    used_slugs = set()
    created_count = 0

    for prefix, original_idx, p in merged:
        raw_author = p.get("author", "Wak Jek").strip() or "Wak Jek"
        group_name = ""
        if not raw_author.startswith("Wak Jek"):
            group_name = raw_author

        raw_date = p.get("date", "").strip()
        dt = parse_fb_date(raw_date)

        # Jika date post lebih baru daripada first comment (atau jika dt kosong), samakan post date dengan first comment date
        first_comment_dt = None
        for c in p.get("comments", []):
            first_comment_dt = parse_fb_date(c.get("date"))
            if first_comment_dt:
                break

        if first_comment_dt:
            if not dt or dt > first_comment_dt:
                dt = first_comment_dt

        # Fallback for special known posts
        content = p.get("content", "").strip()
        if not dt:
            if "Lesson #1" in content:
                dt = datetime(2012, 11, 1, 10, 0, 0)
            elif "memperkenalkan group baru" in content:
                dt = datetime(2012, 5, 10, 11, 0, 0)
            elif "mendisable socket.io" in content:
                dt = datetime(2012, 5, 9, 15, 0, 0)
            elif not content and p.get("images"):
                dt = datetime(2012, 11, 16, 23, 19, 0)
            else:
                dt = datetime(2013, 1, 1, 12, 0, 0)

        iso_date = dt.strftime("%Y-%m-%dT%H:%M:%SZ")

        lines = [line.strip() for line in content.split("\n") if line.strip()]
        if lines:
            first_line = lines[0]
            first_line = re.sub(r"^[\"\']|[\"\']$", "", first_line)
            if len(first_line) > 75:
                cut = first_line[:75].rsplit(" ", 1)[0]
                title = cut.strip(" ,.-:") + "..."
            else:
                title = first_line.strip(" ,.-:")
        else:
            if p.get("images"):
                title = "Uji Coba Firefox OS Simulator"
            else:
                title = f"Status Facebook {dt.strftime('%d %B %Y')}"

        if not title:
            title = f"Status Facebook {dt.strftime('%d %B %Y')}"

        title = title[0].upper() + title[1:] if len(title) > 1 else title.upper()

        base_slug = slugify(title)
        slug_date = dt.strftime("%Y/%m/%d")
        full_slug = f"{slug_date}/{base_slug}"
        if full_slug in used_slugs:
            full_slug = f"{full_slug}-{created_count}"
        used_slugs.add(full_slug)

        cat, tags = detect_category_and_tags(content, group_name)

        # Format body
        body_paras = []
        raw_paras = content.split("\n\n")
        for rp in raw_paras:
            rp_clean = rp.strip()
            if not rp_clean:
                continue
            rp_html = rp_clean.replace("\n", "<br/>\n")
            body_paras.append(f"<p>{rp_html}</p>")

        # Append images if available
        images = p.get("images", [])
        for idx, img_url in enumerate(images):
            if not img_url:
                continue
            url_clean = img_url.split("?")[0]
            ext = os.path.splitext(url_clean)[1] or ".jpg"
            h = hashlib.md5(img_url.encode()).hexdigest()[:10]
            fname = f"{prefix}_{original_idx}_{idx}_{h}{ext}"
            img_path = os.path.join(images_dir, fname)
            if os.path.exists(img_path):
                body_paras.append(
                    f'<p><img src="/images/facebook/{fname}" alt="{title}" title="{title}" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>'
                )

        full_content_html = "\n\n".join(body_paras)

        # Prepare comments with deduplication
        formatted_comments = []
        seen_comments = set()
        for c in p.get("comments", []):
            c_author = c.get("author", "Pengunjung").strip()
            c_text = c.get("text", "").strip()
            c_date = c.get("date", "").strip()
            if c_author and c_text:
                comm_key = (c_author, c_date, c_text)
                if comm_key not in seen_comments:
                    seen_comments.add(comm_key)
                    formatted_comments.append({
                        "author": c_author,
                        "date": c_date,
                        "text": c_text
                    })

        comments_json = json.dumps(formatted_comments, ensure_ascii=False)
        categories_json = json.dumps([cat], ensure_ascii=False)
        tags_json = json.dumps(tags, ensure_ascii=False)

        safe_title = title.replace('"', '\\"')
        safe_group = group_name.replace('"', '\\"') if group_name else ""
        group_yaml = f'\ngroup: "{safe_group}"' if group_name else ""

        md_content = f"""---
title: "{safe_title}"
date: "{iso_date}"
categories: {categories_json}
tags: {tags_json}
slug: "{full_slug}"
legacyUrl: "/{full_slug}/"
source: "facebook.com"
author: "Wak Jek"{group_yaml}
comments: {comments_json}
---

{full_content_html}
"""

        filename = f"facebook_{dt.strftime('%Y_%m_%d')}_{base_slug}.md"
        file_path = os.path.join(out_dir, filename)
        counter = 1
        while os.path.exists(file_path):
            filename = f"facebook_{dt.strftime('%Y_%m_%d')}_{base_slug}-{counter}.md"
            file_path = os.path.join(out_dir, filename)
            counter += 1

        with open(file_path, "w", encoding="utf-8") as out_f:
            out_f.write(md_content)

        created_count += 1

    print(f"Successfully generated {created_count} unified Facebook posts!")

if __name__ == "__main__":
    main()
