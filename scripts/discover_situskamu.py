#!/usr/bin/env python3
import urllib.request
import re
import time
import json
import os

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

def get_html(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

discovered = {}

# 1. Check archive pages and pagination from snapshot 20090415013338
base = "http://web.archive.org/web/20090415013338/http://blog.situskamu.com/"

print("=== Scanning blog.situskamu.com pages ===")
for page in range(1, 25):
    page_url = base if page == 1 else f"{base}page/{page}/"
    print(f"Checking page {page}: {page_url}")
    html = get_html(page_url)
    if not html:
        break
    
    # Extract links like http://blog.situskamu.com/some-post-slug/
    links = re.findall(r'href=[\"\'](?:http://web\.archive\.org/web/\d+/)?http://blog\.situskamu\.com/([a-zA-Z0-9_\-]+)/?[\"\']', html)
    new_found = 0
    for slug in links:
        if slug in ["feed", "about", "contact", "category", "tag", "wp-login", "wp-content", "comments", "page"]:
            continue
        if slug not in discovered:
            discovered[slug] = f"http://web.archive.org/web/20090415013338/http://blog.situskamu.com/{slug}/"
            new_found += 1
    
    print(f"  Page {page} found {new_found} new posts. Total so far: {len(discovered)}")
    if new_found == 0 and page > 2:
        print("No more new posts found. Stopping pagination.")
        break
    time.sleep(0.5)

# 2. Also check monthly archives
months = ["2009/02", "2008/12", "2008/06", "2008/05", "2007/10", "2007/09", "2007/04"]
for m in months:
    m_url = f"{base}{m}/"
    print(f"Checking monthly archive: {m_url}")
    html = get_html(m_url)
    if html:
        links = re.findall(r'href=[\"\'](?:http://web\.archive\.org/web/\d+/)?http://blog\.situskamu\.com/([a-zA-Z0-9_\-]+)/?[\"\']', html)
        for slug in links:
            if slug in ["feed", "about", "contact", "category", "tag", "wp-login", "wp-content", "comments", "page"]:
                continue
            if slug not in discovered:
                discovered[slug] = f"http://web.archive.org/web/20090415013338/http://blog.situskamu.com/{slug}/"
                print(f"  Found from archive {m}: {slug}")
    time.sleep(0.5)

# 3. Also check earlier snapshots of blog.situskamu.com if any (e.g. 20080601, 20071001)
earlier_snapshots = [
    "http://web.archive.org/web/20080601000000/http://blog.situskamu.com/",
    "http://web.archive.org/web/20071001000000/http://blog.situskamu.com/",
]
for snap in earlier_snapshots:
    print(f"Checking snapshot: {snap}")
    html = get_html(snap)
    if html:
        links = re.findall(r'href=[\"\'](?:http://web\.archive\.org/web/\d+/)?http://blog\.situskamu\.com/([a-zA-Z0-9_\-]+)/?[\"\']', html)
        for slug in links:
            if slug in ["feed", "about", "contact", "category", "tag", "wp-login", "wp-content", "comments", "page"]:
                continue
            if slug not in discovered:
                discovered[slug] = f"http://web.archive.org/web/20080601000000/http://blog.situskamu.com/{slug}/"
                print(f"  Found from earlier snapshot: {slug}")
    time.sleep(0.5)

out_file = "/Users/wak./.gemini/antigravity-ide/brain/3d5222ab-dfd2-4bc9-83d6-89221970652a/scratch/situskamu_posts.json"
with open(out_file, "w", encoding="utf-8") as fp:
    json.dump(discovered, fp, indent=2)

print(f"\nDiscovery complete! Total unique posts discovered: {len(discovered)}")
print(f"Saved to {out_file}")
