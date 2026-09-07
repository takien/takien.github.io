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

def detect_category_and_tags(content):
    c_lower = content.lower()
    tags = ["facebook"]
    
    if "wordpress" in c_lower or "wp" in c_lower or "theme" in c_lower or "plugin" in c_lower:
        cat = "WordPress"
        tags.append("wordpress")
        if "plugin" in c_lower:
            tags.append("plugin")
        if "theme" in c_lower:
            tags.append("theme")
    elif any(k in c_lower for k in ["php", "javascript", "jquery", "css", "html", "nginx", "code", "coding", "debug", "vps"]):
        cat = "Programming"
        tags.append("programming")
    elif any(k in c_lower for k in ["facebook", "google", "internet", "browser", "chrome", "firefox", "domain", "hosting"]):
        cat = "Internet"
        tags.append("internet")
    else:
        cat = "Pribadi"
        tags.append("pribadi")
        
    return cat, tags

def main():
    json_path = "_source/fb_posts_1788633061987.json"
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        posts = json.load(f)

    print(f"Loaded {len(posts)} posts from JSON.")

    out_dir = "src/content/posts"
    os.makedirs(out_dir, exist_ok=True)
    images_dir = "public/images/facebook"

    used_slugs = set()
    created_files = []

    for i, p in enumerate(posts):
        author = p.get("author", "Wak Jek").strip() or "Wak Jek"
        raw_date = p.get("date", "").strip()
        dt = parse_fb_date(raw_date)

        # Fallback to comment dates
        if not dt:
            for c in p.get("comments", []):
                dt = parse_fb_date(c.get("date"))
                if dt:
                    break

        # Fallback for post 21 (Lesson #1)
        if not dt and i == 21:
            dt = datetime(2012, 11, 1, 10, 0, 0)
        elif not dt:
            dt = datetime(2013, 1, 1, 12, 0, 0)

        iso_date = dt.strftime("%Y-%m-%dT%H:%M:%SZ")

        content = p.get("content", "").strip()
        lines = [line.strip() for line in content.split("\n") if line.strip()]
        first_line = lines[0] if lines else "Status Facebook"
        first_line = re.sub(r"^[\"\']|[\"\']$", "", first_line)

        # Title formatting
        if len(first_line) > 75:
            cut = first_line[:75].rsplit(" ", 1)[0]
            title = cut.strip(" ,.-:") + "..."
        else:
            title = first_line.strip(" ,.-:")

        if not title:
            title = f"Status Facebook {dt.strftime('%d %B %Y')}"

        # Clean title capitalization
        title = title[0].upper() + title[1:] if len(title) > 1 else title.upper()

        # Generate unique slug
        base_slug = slugify(title)
        slug_date = dt.strftime("%Y/%m/%d")
        full_slug = f"{slug_date}/{base_slug}"
        if full_slug in used_slugs:
            full_slug = f"{full_slug}-{i}"
        used_slugs.add(full_slug)

        cat, tags = detect_category_and_tags(content)

        # Format body content
        body_paras = []
        raw_paras = content.split("\n\n")
        for rp in raw_paras:
            rp_clean = rp.strip()
            if not rp_clean:
                continue
            # convert single newlines to <br/>
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
            fname = f"fb_{i}_{idx}_{h}{ext}"
            img_path = os.path.join(images_dir, fname)
            if os.path.exists(img_path):
                body_paras.append(
                    f'<p><img src="/images/facebook/{fname}" alt="{title}" title="{title}" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>'
                )

        full_content_html = "\n\n".join(body_paras)

        # Prepare comments
        formatted_comments = []
        for c in p.get("comments", []):
            c_author = c.get("author", "Pengunjung").strip()
            c_text = c.get("text", "").strip()
            c_date = c.get("date", "").strip()
            if c_author and c_text:
                formatted_comments.append({
                    "author": c_author,
                    "date": c_date,
                    "text": c_text
                })

        # Frontmatter
        comments_json = json.dumps(formatted_comments, ensure_ascii=False)
        categories_json = json.dumps([cat], ensure_ascii=False)
        tags_json = json.dumps(tags, ensure_ascii=False)

        # Escape double quotes in title
        safe_title = title.replace('"', '\\"')

        md_content = f"""---
title: "{safe_title}"
date: "{iso_date}"
categories: {categories_json}
tags: {tags_json}
slug: "{full_slug}"
legacyUrl: "/{full_slug}/"
source: "facebook.com"
comments: {comments_json}
---

{full_content_html}
"""

        filename = f"facebook_{dt.strftime('%Y_%m_%d')}_{base_slug}.md"
        # ensure filename uniqueness
        file_path = os.path.join(out_dir, filename)
        counter = 1
        while os.path.exists(file_path):
            filename = f"facebook_{dt.strftime('%Y_%m_%d')}_{base_slug}-{counter}.md"
            file_path = os.path.join(out_dir, filename)
            counter += 1

        with open(file_path, "w", encoding="utf-8") as out_f:
            out_f.write(md_content)

        created_files.append((file_path, full_slug, title))

    print(f"Successfully created {len(created_files)} Markdown posts.")
    print("First 3 created:")
    for fpath, slug, title in created_files[:3]:
        print(f"  {slug} -> {title}")
    print("Last 3 created:")
    for fpath, slug, title in created_files[-3:]:
        print(f"  {slug} -> {title}")

if __name__ == "__main__":
    main()
