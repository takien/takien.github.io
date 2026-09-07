#!/usr/bin/env python3
"""
restore_situskamu_and_fixes.py
Comprehensive restoration script:
1. Restores all missing articles from blog.situskamu.com to src/content/posts/
2. Repairs corrupted 'Wayback Machine' posts by finding alternate snapshots across archive.org
"""

import os
import re
import json
import time
import subprocess
import urllib.parse
from html import unescape

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(WORKSPACE_DIR, ".cache_html")
IMAGES_DIR = os.path.join(WORKSPACE_DIR, "public", "images")
POSTS_DIR = os.path.join(WORKSPACE_DIR, "src", "content", "posts")
SITUSKAMU_JSON = os.path.join(WORKSPACE_DIR, "scratch", "situskamu_posts.json")
if not os.path.exists(SITUSKAMU_JSON):
    SITUSKAMU_JSON = "/Users/wak./.gemini/antigravity-ide/brain/3d5222ab-dfd2-4bc9-83d6-89221970652a/scratch/situskamu_posts.json"

os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(POSTS_DIR, exist_ok=True)

HEADERS = [
    "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
]

def fetch_url(url, max_time=25):
    # Ensure HTTPS for archive.org to prevent connection refused on port 80
    clean_url = url
    if clean_url.startswith("http://web.archive.org"):
        clean_url = clean_url.replace("http://web.archive.org", "https://web.archive.org", 1)
    elif clean_url.startswith("http://archive.org"):
        clean_url = clean_url.replace("http://archive.org", "https://archive.org", 1)

    cmd = ["curl", "-s", "-L", "--max-time", str(max_time), "--retry", "2"] + HEADERS + [clean_url]
    res = subprocess.run(cmd, capture_output=True)
    try:
        return res.stdout.decode("utf-8")
    except UnicodeDecodeError:
        return res.stdout.decode("latin1", errors="replace")

def get_available_snapshot(target_url):
    api = f"https://archive.org/wayback/available?url={urllib.parse.quote(target_url, safe=':/?=')}"
    res = fetch_url(api, max_time=10)
    try:
        data = json.loads(res)
        snap = data.get("archived_snapshots", {}).get("closest")
        if snap and snap.get("available") and snap.get("url"):
            u = snap.get("url")
            if u.startswith("http://"):
                u = u.replace("http://", "https://", 1)
            return u
    except Exception:
        pass
    return None

def download_image(img_url, local_rel_path):
    dest_path = os.path.join(IMAGES_DIR, local_rel_path.lstrip("/"))
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 100:
        return "/images/" + local_rel_path.lstrip("/")

    wb_img_url = img_url
    if "web.archive.org/web/" in wb_img_url:
        if "im_/" not in wb_img_url:
            wb_img_url = re.sub(r"/web/(\d+)(?:cs_|js_)?/", r"/web/\1im_/", wb_img_url)
    else:
        wb_img_url = f"https://web.archive.org/web/20140501000000im_/{img_url}"

    if wb_img_url.startswith("http://"):
        wb_img_url = wb_img_url.replace("http://", "https://", 1)

    cmd = ["curl", "-s", "-L", "--max-time", "15", "--retry", "2"] + HEADERS + [wb_img_url, "-o", dest_path]
    subprocess.run(cmd)

    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 100:
        return "/images/" + local_rel_path.lstrip("/")
    return img_url

def clean_html_content(raw_html):
    content = raw_html
    # Strip scripts, styles, ins, comments, headers, footers
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<ins[^>]*>.*?</ins>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    content = re.sub(r'<header[^>]*>.*?</header>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<footer[^>]*>.*?</footer>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<div[^>]*class=[\"\'][^\"\']*(?:social|share|widget|ikl-|ad-|dsq-|comments?|nav-)[^\"\']*[\"\'][^>]*>.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<div id=[\"\'](?:dsq-content|comments|disqus_thread)[\"\'][^>]*>.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)

    # Process images
    def replace_img(match):
        img_tag = match.group(0)
        src_m = re.search(r'src=[\"\']([^\"\']+)[\"\']', img_tag)
        if not src_m:
            return ""
        src = src_m.group(1)
        if any(x in src for x in ["gravatar.com", "w.org", "1x1", "pixel", "banner"]):
            return ""

        alt_m = re.search(r'alt=[\"\']([^\"\']*)[\"\']', img_tag)
        alt = alt_m.group(1) if alt_m else ""
        title_m = re.search(r'title=[\"\']([^\"\']*)[\"\']', img_tag)
        title = title_m.group(1) if title_m else ""

        parsed = urllib.parse.urlparse(src)
        filename = os.path.basename(parsed.path)
        if not filename or '.' not in filename:
            filename = f"img_{abs(hash(src))}.jpg"
        filename = re.sub(r'[^a-zA-Z0-9_\.-]', '_', filename)

        ym_match = re.search(r'/(\d{4})/(\d{2})/', src)
        subfolder = f"{ym_match.group(1)}/{ym_match.group(2)}" if ym_match else "misc"

        local_rel = f"{subfolder}/{filename}"
        local_web_path = download_image(src, local_rel)

        return f'<img src="{local_web_path}" alt="{alt}" title="{title}" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" />'

    content = re.sub(r'<img[^>]+>', replace_img, content)

    # Clean archive links to relative paths
    content = re.sub(
        r'https?://web\.archive\.org/web/\d+(?:im_|cs_|js_)?/https?://(?:www\.)?(?:takien\.com|blog\.situskamu\.com)(/[^\"\'\s>*)\]]*)?',
        lambda m: m.group(1) if m.group(1) else "/",
        content
    )
    content = re.sub(
        r'https?://(?:www\.)?(?:takien\.com|blog\.situskamu\.com)(/[^\"\'\s>*)\]]*)?',
        lambda m: m.group(1) if m.group(1) else "/",
        content
    )

    # Convert code blocks [php]...[/php]
    content = re.sub(r'\[(php|javascript|js|css|html|bash|sh)\](.*?)\[/\1\]', r'<pre><code class="language-\1">\2</code></pre>', content, flags=re.DOTALL | re.IGNORECASE)

    content = re.sub(r'<p>\s*(?:&nbsp;)?\s*</p>', '', content)
    content = re.sub(r'<div>\s*</div>', '', content)
    return content.strip()

def extract_comments_from_html(html):
    comments = []
    # 1. Disqus
    dsq_pattern = r'<li[^>]*class=[\"\'][^\"\']*comment[^\"\']*[\"\'][^>]*id=[\"\'](?:comment-|dsq-comment-)(\d+)[\"\']>(.*?)</li>\s*<!--\s*#comment-##\s*-->'
    matches = re.findall(dsq_pattern, html, re.DOTALL)
    
    if not matches:
        # 2. WordPress standard
        wp_pattern = r'<li[^>]*id=[\"\']comment-(\d+)[\"\'][^>]*>(.*?)(?=<li[^>]*id=[\"\']comment-|\s*</ol>|\s*</ul>)'
        matches = re.findall(wp_pattern, html, re.DOTALL | re.IGNORECASE)

    for cid, body in matches:
        author_m = re.search(r'<(?:cite|b|span)[^>]*class=[\"\'][^\"\']*(?:fn|author)[^\"\']*[\"\'][^>]*>(.*?)</(?:cite|b|span)>', body, re.DOTALL | re.IGNORECASE)
        if not author_m:
            author_m = re.search(r'<span[^>]*id=[\"\']dsq-author-user-\d+[\"\'][^>]*>(.*?)</span>', body, re.DOTALL | re.IGNORECASE)
        author = re.sub(r'<[^>]+>', '', author_m.group(1)).strip() if author_m else 'Anonymous'

        date_m = re.search(r'<time[^>]*datetime=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</time>', body, re.DOTALL | re.IGNORECASE)
        if date_m:
            cdate = re.sub(r'<[^>]+>', '', date_m.group(2)).strip()
        else:
            date_m = re.search(r'<a[^>]*#comment-\d+[\"\'][^>]*>(.*?)</a>', body, re.DOTALL | re.IGNORECASE)
            if date_m:
                cdate = re.sub(r'<[^>]+>', '', date_m.group(1)).strip()
            else:
                cdate = ''

        msg_m = re.search(r'<div[^>]*class=[\"\'][^\"\']*(?:comment-content|comment-text|comment-body|dsq-comment-message)[^\"\']*[\"\'][^>]*>(.*?)</div>', body, re.DOTALL | re.IGNORECASE)
        if not msg_m:
            p_m = re.findall(r'<p>(.*?)</p>', body, re.DOTALL | re.IGNORECASE)
            msg = "\n\n".join(p_m) if p_m else body
        else:
            msg = msg_m.group(1)

        msg = re.sub(r'<br\s*/?>', '\n', msg)
        msg = re.sub(r'<p>', '', msg)
        msg = re.sub(r'</p>', '\n\n', msg)
        msg = re.sub(r'<[^>]+>', '', msg).strip()

        if author and msg and len(msg) > 1 and not author.startswith("http://"):
            comments.append({
                "author": unescape(author),
                "date": unescape(cdate),
                "text": unescape(msg)
            })

    return comments

def parse_post_content(html, slug):
    # Title
    title_m = re.search(r'<h[12][^>]*class=[\"\'][^\"\']*(?:entry-title|post-title|post__title|title)[^\"\']*[\"\'][^>]*>(.*?)</h[12]>', html, re.DOTALL | re.IGNORECASE)
    if not title_m:
        title_m = re.search(r'<meta property=[\"\']og:title[\"\'] content=[\"\']([^\"\']+)[\"\']', html)
    if not title_m:
        title_m = re.search(r'<title>(.*?)</title>', html)
    raw_title = title_m.group(1) if title_m else slug.replace('-', ' ').title()
    title = re.sub(r'<[^>]+>', '', raw_title).strip()
    title = re.sub(r'\s*(&bull;|&middot;|•|-|\|)\s*(?:takien|blog\.situskamu).*$', '', title).strip()
    title = unescape(title)

    # Date
    date = ""
    pub_m = re.search(r'article:published_time[\"\'] content=[\"\']([^\"\']+)[\"\']', html)
    if pub_m:
        date = pub_m.group(1)
    else:
        # Check date tags e.g. <small class="date">May 15th, 2008</small>
        date_tag = re.search(r'<(?:small|span|div)[^>]*class=[\"\'][^\"\']*date[^\"\']*[\"\'][^>]*>(.*?)</(?:small|span|div)>', html, re.DOTALL | re.IGNORECASE)
        if date_tag:
            raw_d = re.sub(r'<[^>]+>', '', date_tag.group(1)).strip()
            raw_d_clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', raw_d)
            try:
                from datetime import datetime
                for fmt in ["%B %d, %Y", "%b %d, %Y", "%d %B %Y", "%d %b %Y", "%Y/%m/%d"]:
                    try:
                        dt = datetime.strptime(raw_d_clean.strip(), fmt)
                        date = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
                        break
                    except Exception:
                        pass
            except Exception:
                date = raw_d
    
    # Categories & Tags
    categories = []
    tags = []
    for cat in re.findall(r'rel=[\"\']category tag[\"\'][^>]*>(.*?)</a>', html, re.IGNORECASE):
        c_clean = re.sub(r'<[^>]+>', '', cat).strip()
        if c_clean and c_clean not in categories:
            categories.append(unescape(c_clean))
    for cat in re.findall(r'article:section[\"\'] content=[\"\']([^\"\']+)[\"\']', html):
        if cat not in categories:
            categories.append(unescape(cat))
    if not categories:
        categories = ["Uncategorized"]

    for tg in re.findall(r'rel=[\"\']tag[\"\'][^>]*>(.*?)</a>', html, re.IGNORECASE):
        t_clean = re.sub(r'<[^>]+>', '', tg).strip()
        if t_clean and t_clean not in tags:
            tags.append(unescape(t_clean))

    # Entry content body
    entry_m = re.search(r'<div[^>]*class=[\"\'][^\"\']*(?:entry-content|post-content|entry)[^\"\']*[\"\'][^>]*>(.*?)(?:<!--\s*(?:entry-content|\.entry-content|end entry)|<div class=[\"\'](?:postmetadata|comments|tags)|<footer|<div id=[\"\']comments)', html, re.DOTALL | re.IGNORECASE)
    if not entry_m:
        entry_m = re.search(r'<div[^>]*class=[\"\']entry[\"\'][^>]*>(.*?)</div>', html, re.DOTALL | re.IGNORECASE)
    if not entry_m:
        entry_m = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)

    raw_body = entry_m.group(1) if entry_m else ""
    clean_body = clean_html_content(raw_body)
    comments = extract_comments_from_html(html)

    return {
        "title": title,
        "date": date,
        "categories": categories,
        "tags": tags,
        "body": clean_body,
        "comments": comments
    }

def main():
    print("=== Restoring blog.situskamu.com Posts and Repairing Corrupt Pages ===")

    # 1. Gather all existing posts
    existing_slugs = set()
    corrupt_files = {} # slug -> filepath

    for fname in os.listdir(POSTS_DIR):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(POSTS_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as fp:
            c = fp.read()
        m = re.search(r'slug:\s*["\']?([^"\']+)["\']?', c)
        slug_val = m.group(1) if m else ""
        base_slug = slug_val.split("/")[-1]

        if 'title: "Wayback Machine"' in c or "title: 'Wayback Machine'" in c:
            corrupt_files[base_slug] = (fpath, slug_val)
        else:
            existing_slugs.add(base_slug)
            existing_slugs.add(slug_val)

    print(f"Existing valid posts: {len(existing_slugs)}")
    print(f"Corrupted posts: {len(corrupt_files)}")

    # 2. Process blog.situskamu.com
    with open(SITUSKAMU_JSON) as fp:
        situskamu_map = json.load(fp)

    imported_situskamu = 0
    for slug, default_url in situskamu_map.items():
        is_corrupt_target = slug in corrupt_files
        if slug in existing_slugs and not is_corrupt_target:
            continue

        print(f"\n[SITUSKAMU] Resolving snapshot for '{slug}'...")
        # Step A: Query Wayback availability API for best available snapshot
        snap_url = get_available_snapshot(f"http://blog.situskamu.com/{slug}/")
        if not snap_url:
            snap_url = get_available_snapshot(f"http://blog.situskamu.com/{slug}")
        if not snap_url:
            snap_url = default_url.replace("http://", "https://")

        print(f"  Fetching: {snap_url}")
        html = fetch_url(snap_url)
        if not html or len(html) < 600 or "parking-lander" in html:
            print(f"  [WARN] Failed to get valid HTML for {slug}")
            continue

        post_data = parse_post_content(html, slug)
        if not post_data["body"] or len(post_data["body"]) < 50:
            print(f"  [WARN] Body too short or empty for {slug}")
            continue

        # Determine date & canonical path
        d_str = post_data["date"]
        year, month, day = "2008", "05", "01"
        ymd_m = re.search(r'(\d{4})-(\d{2})-(\d{2})', d_str)
        if ymd_m:
            year, month, day = ymd_m.group(1), ymd_m.group(2), ymd_m.group(3)
        elif "2007" in snap_url:
            year, month, day = "2007", "10", "15"
        elif "2008" in snap_url:
            year, month, day = "2008", "06", "15"
        elif "2009" in snap_url:
            year, month, day = "2009", "02", "15"

        if not d_str:
            d_str = f"{year}-{month}-{day}T12:00:00Z"

        canonical_slug = f"{year}/{month}/{day}/{slug}"

        md_content = f"""---
title: {json.dumps(post_data['title'], ensure_ascii=False)}
date: "{d_str}"
categories: {json.dumps(post_data['categories'], ensure_ascii=False)}
tags: {json.dumps(post_data['tags'], ensure_ascii=False)}
slug: "{canonical_slug}"
legacyUrl: "/{slug}/"
source: "blog.situskamu.com"
comments: {json.dumps(post_data['comments'], ensure_ascii=False, indent=2)}
---

{post_data['body']}
"""
        if is_corrupt_target:
            target_path = corrupt_files[slug][0]
            print(f"  [REPAIR] Overwriting corrupt file: {target_path}")
            del corrupt_files[slug]
        else:
            fname = f"situskamu_{year}_{month}_{day}_{slug}.md"
            target_path = os.path.join(POSTS_DIR, fname)
            print(f"  [NEW] Saved to {target_path} (Title: {post_data['title']})")

        with open(target_path, "w", encoding="utf-8") as fp:
            fp.write(md_content.strip() + "\n")

        imported_situskamu += 1
        time.sleep(0.4)

    print(f"\nFinished blog.situskamu.com: {imported_situskamu} articles restored!")

    # 3. Repair remaining corrupt posts from takien.com
    print(f"\nRemaining corrupted posts to check: {len(corrupt_files)}")
    for slug_key, (fpath, slug_val) in list(corrupt_files.items()):
        print(f"\n[REPAIR] Checking '{slug_val}' ({os.path.basename(fpath)})...")
        clean_slug = slug_val.strip("/")
        base_slug = clean_slug.split("/")[-1]

        # Prioritized URL patterns to search across archive.org
        search_urls = [
            f"http://takien.com/{clean_slug}/",
            f"http://takien.com:80/{clean_slug}/",
            f"http://takien.com/blog/{clean_slug}/",
            f"http://blog.situskamu.com/{base_slug}/",
            f"http://blog.situskamu.com/{base_slug}"
        ]

        found_html = ""
        used_url = ""
        for surl in search_urls:
            snap_url = get_available_snapshot(surl)
            if snap_url:
                print(f"  Checking snapshot: {snap_url}")
                html_cand = fetch_url(snap_url, max_time=20)
                if len(html_cand) > 1000 and "parking-lander" not in html_cand:
                    if "<title>Wayback Machine</title>" not in html_cand or "entry-content" in html_cand or "post__title" in html_cand:
                        found_html = html_cand
                        used_url = snap_url
                        break
            time.sleep(0.3)

        if found_html:
            post_data = parse_post_content(found_html, base_slug)
            if post_data["title"] and post_data["title"] != "Wayback Machine" and post_data["body"] and len(post_data["body"]) > 50:
                with open(fpath, "r", encoding="utf-8") as fp:
                    old_c = fp.read()
                
                # Check source
                src_note = 'source: "blog.situskamu.com"\n' if "situskamu" in used_url else ""
                
                new_c = re.sub(r'title:\s*["\'][^"\']+["\']', f'title: {json.dumps(post_data["title"], ensure_ascii=False)}', old_c)
                if post_data["date"]:
                    new_c = re.sub(r'date:\s*["\'][^"\']*["\']', f'date: "{post_data["date"]}"', new_c)
                if post_data["categories"] and post_data["categories"] != ["Uncategorized"]:
                    new_c = re.sub(r'categories:\s*\[[^\]]*\]', f'categories: {json.dumps(post_data["categories"], ensure_ascii=False)}', new_c)
                if post_data["comments"]:
                    new_c = re.sub(r'comments:\s*\[[^\]]*\]', f'comments: {json.dumps(post_data["comments"], ensure_ascii=False, indent=2)}', new_c)
                if src_note and "source:" not in new_c:
                    new_c = new_c.replace("comments:", f"{src_note}comments:")

                new_c = re.sub(r'---\n\n.*$', f'---\n\n{post_data["body"]}', new_c, flags=re.DOTALL)

                with open(fpath, "w", encoding="utf-8") as fp:
                    fp.write(new_c.strip() + "\n")
                print(f"  [SUCCESS] Repaired '{post_data['title']}' in {fpath}")
            else:
                print(f"  [WARN] Content parsed was not clean enough for {slug_val}")
        else:
            print(f"  [NOT FOUND] No usable snapshot for {slug_val}")

    print("\n=== All Restoration Tasks Completed! ===")

if __name__ == "__main__":
    main()
