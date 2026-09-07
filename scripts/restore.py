#!/usr/bin/env python3
"""
restore.py - Scraper and Content Converter for takien.com restoration.
Downloads HTML from Wayback Machine, extracts article content, metadata,
static comments, and images, and saves clean Markdown files into Astro content collection.
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

os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(POSTS_DIR, exist_ok=True)

HEADERS = [
    "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
]

def is_valid_post_html(html):
    if not html or len(html) < 800:
        return False
    if "godaddy.com/park" in html or "parking-lander" in html:
        return False
    if "Account Suspended" in html and "takien" not in html:
        return False
    if "<title>Wayback Machine</title>" in html and "takien" not in html:
        return False
    if not any(x in html for x in ["takien", "article", "entry-content", "post-title", "comment"]):
        return False
    return True

def fetch_url(url, max_time=25):
    cmd = ["curl", "-s", "-L", "--max-time", str(max_time), "--retry", "2"] + HEADERS + [url]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.stdout

def fetch_post_html(path, info):
    cache_key = re.sub(r'[^a-zA-Z0-9_]', '_', path).strip('_') + ".html"
    cache_file = os.path.join(CACHE_DIR, cache_key)
    if os.path.exists(cache_file) and os.path.getsize(cache_file) > 1000:
        with open(cache_file, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
            if is_valid_post_html(c):
                return c

    clean_path = path.strip().lstrip('/')
    no_blog_path = re.sub(r'^blog/', '', clean_path)

    # Prioritized URLs to try
    urls_to_try = []
    # 1. Exact full_url discovered from working index page
    if info.get("full_url"):
        urls_to_try.append(info["full_url"])
    # 2. Timegate automatic redirect
    urls_to_try.append(f"https://web.archive.org/web/http://takien.com/{clean_path}")
    urls_to_try.append(f"https://web.archive.org/web/20160501000000/http://takien.com/{clean_path}")
    if no_blog_path != clean_path:
        urls_to_try.append(f"https://web.archive.org/web/http://takien.com/{no_blog_path}")
        urls_to_try.append(f"https://web.archive.org/web/20160501000000/http://takien.com/{no_blog_path}")
    else:
        urls_to_try.append(f"https://web.archive.org/web/20150101000000/http://takien.com/blog/{clean_path}")

    for u in urls_to_try:
        html = fetch_url(u)
        if is_valid_post_html(html):
            with open(cache_file, "w", encoding="utf-8") as f:
                f.write(html)
            return html
        time.sleep(0.2)

    return ""

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
        wb_img_url = f"https://web.archive.org/web/20160501000000im_/{img_url}"

    cmd = ["curl", "-s", "-L", "--max-time", "15", "--retry", "2"] + HEADERS + [wb_img_url, "-o", dest_path]
    subprocess.run(cmd)

    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 100:
        return "/images/" + local_rel_path.lstrip("/")
    return img_url

def clean_html_content(raw_html, orig_path):
    content = raw_html
    # Strip unwanted elements
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<ins[^>]*>.*?</ins>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    content = re.sub(r'<header[^>]*>.*?</header>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<footer[^>]*>.*?</footer>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<div[^>]*class=[\"\'][^\"\']*(?:social|share|widget|ikl-|ad-|dsq-|comments?|nav-|postmeta|entry-meta)[^\"\']*[\"\'][^>]*>.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<div id=[\"\'](?:dsq-content|comments|disqus_thread)[\"\'][^>]*>.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<div class=[\"\']social_bookmark[\"\']>.*', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<span class=[\"\']dsq-postid[\"\'][^>]*>.*?</span>', '', content, flags=re.DOTALL | re.IGNORECASE)

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
        if ym_match:
            subfolder = f"{ym_match.group(1)}/{ym_match.group(2)}"
        else:
            subfolder = "misc"

        local_rel = f"{subfolder}/{filename}"
        local_web_path = download_image(src, local_rel)

        return f'<img src="{local_web_path}" alt="{alt}" title="{title}" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" />'

    content = re.sub(r'<img[^>]+>', replace_img, content)

    # Clean archive links to relative paths
    content = re.sub(
        r'https?://web\.archive\.org/web/\d+(?:im_|cs_|js_)?/https?://(?:www\.)?takien\.com(/[^\"\'\s>*)\]]*)?',
        lambda m: m.group(1) if m.group(1) else "/",
        content
    )
    content = re.sub(
        r'https?://(?:www\.)?takien\.com(/[^\"\'\s>*)\]]*)?',
        lambda m: m.group(1) if m.group(1) else "/",
        content
    )

    # Remove attachment page links wrapping images
    def unwrap_attachment_links(m):
        full_a = m.group(0)
        attrs = m.group(1)
        img = m.group(2)
        href_m = re.search(r'href=[\"\']([^\"\']+)[\"\']', attrs)
        href = href_m.group(1) if href_m else ''
        if ('rel="attachment' in attrs or "rel='attachment" in attrs or
            'wp-att-' in attrs or
            re.search(r'(?:/blog)?/\d{4}/\d{2}/\d{2}/[^/\"\'\s>]+/[^/\"\'\s>]+/?$', href) or
            re.search(r'/\d+/[^/\"\'\s>]+\.php/[^/\"\'\s>]+/?$', href)):
            return img
        return full_a

    content = re.sub(r'<a\s+([^>]*)>(\s*<img[^>]+>\s*)</a>', unwrap_attachment_links, content)

    # Convert code blocks [php]...[/php] or <pre class="brush: ...">
    content = re.sub(r'\[(php|javascript|js|css|html|bash|sh)\](.*?)\[/\1\]', r'<pre><code class="language-\1">\2</code></pre>', content, flags=re.DOTALL | re.IGNORECASE)

    content = re.sub(r'<p>\s*(?:&nbsp;)?\s*</p>', '', content)
    content = re.sub(r'<div>\s*</div>', '', content)
    return content.strip()

def extract_comments(html):
    comments = []
    
    # 1. Disqus comments
    dsq_pattern = r'<li[^>]*class=[\"\'][^\"\']*comment[^\"\']*[\"\'][^>]*id=[\"\'](?:comment-|dsq-comment-)(\d+)[\"\']>(.*?)</li>\s*<!--\s*#comment-##\s*-->'
    matches = re.findall(dsq_pattern, html, re.DOTALL)
    
    if not matches:
        # 2. Standard WordPress comments
        wp_pattern = r'<li[^>]*id=[\"\'](?:comment-)(\d+)[\"\'][^>]*>(.*?)(?=<li[^>]*id=[\"\']comment-|\s*</ol>|\s*</ul>)'
        matches = re.findall(wp_pattern, html, re.DOTALL)

    for cid, body in matches:
        # Author: support <b class="fn">, <cite class="fn">, <span class="fn">, or dsq-author
        author_m = re.search(r'<span[^>]*id=[\"\']dsq-author-user-\d+[\"\'][^>]*>(.*?)</span>', body)
        if not author_m:
            author_m = re.search(r'<(?:b|span|cite)[^>]*class=[\"\'][^\"\']*(?:fn|author)[^\"\']*[\"\'][^>]*>(.*?)</(?:b|span|cite)>', body)
        author = author_m.group(1).strip() if author_m else 'Anonymous'
        author = re.sub(r'<[^>]+>', '', author).strip()

        # Date: support <time>, .comment-metadata, or dsq-comment-header
        date_m = re.search(r'<time[^>]*datetime=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</time>', body)
        if date_m:
            cdate = date_m.group(2).strip()
        else:
            time_tag = re.search(r'<time[^>]*>(.*?)</time>', body, re.DOTALL)
            if time_tag:
                cdate = re.sub(r'<[^>]+>', '', time_tag.group(1)).strip()
            else:
                raw_date = re.search(r'class=[\"\'][^\"\']*(?:comment-meta|comment-date|dsq-comment-header)[^\"\']*[\"\'][^>]*>.*?(\d{1,2}\s+[A-Za-z]+\s+\d{4}|\d{4}-\d{2}-\d{2}|[A-Za-z]+\s+\d{1,2},\s+\d{4})', body, re.DOTALL)
                cdate = raw_date.group(1).strip() if raw_date else ""

        # Message: support .comment-content, .dsq-comment-message, .comment-body
        msg_m = re.search(r'<div[^>]*class=[\"\'][^\"\']*comment-content[^\"\']*[\"\'][^>]*>(.*?)</div>', body, re.DOTALL)
        if not msg_m:
            msg_m = re.search(r'class=[\"\'][^\"\']*(?:dsq-comment-message|comment-body)[^\"\']*[\"\'][^>]*>(.*?)</div>', body, re.DOTALL)
        msg = msg_m.group(1).strip() if msg_m else body
        msg = re.sub(r'<br\s*/?>', '\n', msg)
        msg = re.sub(r'<p>', '', msg)
        msg = re.sub(r'</p>', '\n\n', msg)
        msg = re.sub(r'<[^>]+>', '', msg).strip()

        if author and msg and len(msg) > 1 and not author.startswith("http://"):
            comments.append({
                "author": unescape(author),
                "date": cdate,
                "text": unescape(msg)
            })

    return comments

def parse_post(html, orig_path):
    title_m = re.search(r'<h[12][^>]*class=[\"\'][^\"\']*(?:entry-title|post-title)[^\"\']*[\"\'][^>]*>(.*?)</h[12]>', html, re.DOTALL)
    if not title_m:
        title_m = re.search(r'<meta property=[\"\']og:title[\"\'] content=[\"\']([^\"\']+)[\"\']', html)
    if not title_m:
        title_m = re.search(r'<title>(.*?)</title>', html)
    
    raw_title = title_m.group(1) if title_m else "Untitled"
    title = re.sub(r'<[^>]+>', '', raw_title).strip()
    title = re.sub(r'\s*(&bull;|&middot;|•|-|\|)\s*takien.*$', '', title).strip()
    title = unescape(title)

    date = ""
    pub_m = re.search(r'article:published_time[\"\'] content=[\"\']([^\"\']+)[\"\']', html)
    if pub_m:
        date = pub_m.group(1)
    else:
        ymd_m = re.search(r'(\d{4})/(\d{2})/(\d{2})', orig_path)
        if ymd_m:
            date = f"{ymd_m.group(1)}-{ymd_m.group(2)}-{ymd_m.group(3)}T00:00:00Z"
        else:
            meta_date_m = re.search(r'class=[\"\'][^\"\']*(?:meta__date|entry-date|published)[^\"\']*[\"\'][^>]*>(.*?)</span>', html)
            if meta_date_m:
                date = re.sub(r'<[^>]+>', '', meta_date_m.group(1)).strip()

    categories = []
    tags = []
    for cat in re.findall(r'article:section[\"\'] content=[\"\']([^\"\']+)[\"\']', html):
        categories.append(unescape(cat))
    for tg in re.findall(r'article:tag[\"\'] content=[\"\']([^\"\']+)[\"\']', html):
        tags.append(unescape(tg))

    if not categories:
        for cl in re.findall(r'rel=[\"\']category(?: tag)?[\"\'][^>]*>(.*?)</a>', html):
            categories.append(unescape(re.sub(r'<[^>]+>', '', cl).strip()))
    if not tags:
        for tl in re.findall(r'rel=[\"\']tag[\"\'][^>]*>(.*?)</a>', html):
            tags.append(unescape(re.sub(r'<[^>]+>', '', tl).strip()))

    categories = sorted(list(set([c for c in categories if c and len(c) < 50])))
    tags = sorted(list(set([t for t in tags if t and len(t) < 50])))
    if not categories:
        categories = ["Uncategorized"]

    comments = extract_comments(html)

    article_m = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    if not article_m:
        article_m = re.search(r'class=[\"\'][^\"\']*(?:entry-content|post-content)[^\"\']*[\"\'][^>]*>(.*?)</div>\s*<!--\s*(?:\.entry-content|post)', html, re.DOTALL)
    if not article_m:
        article_m = re.search(r'class=[\"\'][^\"\']*(?:entry-content|post-content)[^\"\']*[\"\'][^>]*>(.*?)</div>', html, re.DOTALL)
    
    raw_body = article_m.group(1) if article_m else "<p>Konten tidak dapat dimuat dari arsip.</p>"
    clean_body = clean_html_content(raw_body, orig_path)

    clean_slug = orig_path.strip().lstrip('/').rstrip('/')
    canonical_slug = re.sub(r'^blog/', '', clean_slug)
    legacy_url = f"/{clean_slug}/"

    return {
        "title": title,
        "date": date,
        "categories": categories,
        "tags": tags,
        "slug": canonical_slug,
        "legacyUrl": legacy_url,
        "comments": comments,
        "content": clean_body
    }

def process_all():
    disc_file = os.path.join(WORKSPACE_DIR, "scratch", "discovered_posts.json")
    if not os.path.exists(disc_file):
        print(f"Error: {disc_file} not found")
        return

    with open(disc_file, "r") as f:
        posts_data = json.load(f)

    static_pages = ["about", "contact", "wordpress-plugins", "jquery-plugins"]
    for sp in static_pages:
        if sp not in posts_data and f"{sp}/" not in posts_data:
            posts_data[f"{sp}/"] = {
                "title": sp.replace("-", " ").title(),
                "path": f"{sp}/",
                "full_url": f"https://web.archive.org/web/20160501000000/http://takien.com/{sp}/"
            }

    total_items = len(posts_data)
    print(f"Starting polite sequential restoration of {total_items} items (with local caching)...")

    success_count = 0
    total_comments = 0
    failed = []

    t0 = time.time()
    for idx, (path, info) in enumerate(posts_data.items(), 1):
        file_slug = re.sub(r'[^a-zA-Z0-9_-]', '_', re.sub(r'^blog/', '', path.strip().lstrip('/').rstrip('/'))).strip('_')
        md_file = os.path.join(POSTS_DIR, f"{file_slug}.md")

        # If already restored and valid, skip
        if os.path.exists(md_file) and os.path.getsize(md_file) > 500:
            success_count += 1
            continue

        print(f"[{idx}/{total_items}] Fetching: {path} ...", end=" ", flush=True)
        html = fetch_post_html(path, info)

        if not html:
            failed.append(path)
            print("FAIL")
            time.sleep(0.3)
            continue

        post = parse_post(html, path)
        cm_count = len(post["comments"])
        total_comments += cm_count

        fm_comments = json.dumps(post["comments"], ensure_ascii=False)
        fm_cats = json.dumps(post["categories"], ensure_ascii=False)
        fm_tags = json.dumps(post["tags"], ensure_ascii=False)

        md_content = f"""---
title: {json.dumps(post["title"], ensure_ascii=False)}
date: "{post['date']}"
categories: {fm_cats}
tags: {fm_tags}
slug: "{post['slug']}"
legacyUrl: "{post['legacyUrl']}"
comments: {fm_comments}
---

{post['content']}
"""
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(md_content)

        success_count += 1
        print(f"OK ({cm_count} comments) -> \"{post['title'][:40]}\"")
        time.sleep(0.3)

    elapsed = time.time() - t0
    print(f"\n==========================================")
    print(f"Restoration finished in {elapsed:.1f}s!")
    print(f"Success: {success_count}/{total_items}")
    print(f"Failed: {len(failed)}")
    if failed:
        print(f"Failed items: {failed}")
    print(f"Total static comments preserved: {total_comments}")
    print(f"Markdown articles saved in: {POSTS_DIR}")
    print(f"==========================================")

if __name__ == "__main__":
    process_all()
