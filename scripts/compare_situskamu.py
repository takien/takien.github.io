#!/usr/bin/env python3
import os
import glob
import json
import re

posts_dir = os.path.join(os.path.dirname(__file__), "..", "src", "content", "posts")
existing_slugs = set()
existing_files = glob.glob(os.path.join(posts_dir, "*.md"))

# Map of slug -> file
slug_to_file = {}

for f in existing_files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    # Check if this file is a corrupted "Wayback Machine" placeholder
    is_corrupt = 'title: "Wayback Machine"' in c or "title: 'Wayback Machine'" in c
    
    m = re.search(r'slug:\s*["\']?([^"\']+)["\']?', c)
    if m:
        base_slug = m.group(1).split("/")[-1]
        if not is_corrupt:
            existing_slugs.add(base_slug)
            existing_slugs.add(m.group(1))
        slug_to_file[base_slug] = (f, is_corrupt)
    
    fname = os.path.basename(f).replace(".md", "")
    fname_clean = re.sub(r'^\d{4}_\d{2}_\d{2}_', '', fname)
    if not is_corrupt:
        existing_slugs.add(fname_clean)

situskamu_file = "/Users/wak./.gemini/antigravity-ide/brain/3d5222ab-dfd2-4bc9-83d6-89221970652a/scratch/situskamu_posts.json"
with open(situskamu_file) as fp:
    situskamu = json.load(fp)

already_exists = []
to_replace_corrupt = []
to_import_new = []

for slug, url in situskamu.items():
    if slug in slug_to_file and slug_to_file[slug][1]:
        to_replace_corrupt.append((slug, url, slug_to_file[slug][0]))
    elif slug in existing_slugs:
        already_exists.append(slug)
    else:
        to_import_new.append((slug, url))

print(f"Total in situskamu: {len(situskamu)}")
print(f"Already valid in takien.com: {len(already_exists)}")
for s in already_exists:
    print(f"  [EXISTS] {s}")

print(f"\nCorrupted in takien.com, can be restored from situskamu: {len(to_replace_corrupt)}")
for s, u, f in to_replace_corrupt:
    print(f"  [FIX] {s} ({f}) -> {u}")

print(f"\nBrand new from blog.situskamu.com to import: {len(to_import_new)}")
for s, u in to_import_new:
    print(f"  [NEW] {s} -> {u}")
