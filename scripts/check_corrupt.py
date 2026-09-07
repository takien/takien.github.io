#!/usr/bin/env python3
import urllib.request
import json
import time

corrupt_slugs = [
    "2007/08/05/differences-and-similarities",
    "2007/08/05/quick-scroll",
    "2013/09/28/google-adsense-ad-serving-has-been-disabled-what-should-i-do",
    "2014/05/28/use-wordpress-auto-draft-as-future-post-id-since-it-cant-be-disabled",
    "2014/08/10/alasan-mengapa-saya-tidak-suka-karya-anak-bangsa",
    "2011/09/19/sekilas-review-windows-8-developer-preview",
    "2010/07/28/jquery-twitter-marquee",
    "2014/10/30/how-to-backup-your-wordpress-site-into-dropbox",
    "2014/01/14/pixabay-provides-high-quality-professional-photo-stocks-for-free-with-no-hassle",
    "2010/01/29/cerita-remaja-kini",
    "2010/01/27/this-is-a-child-post",
    "2009/08/04/mbah-surip-tidur-tidak-bangun-lagi",
    "2009/07/29/amr-to-mp3-converter",
    "2009/07/15/all-in-one-seo-pack-a-smart-and-stupid-plugin",
    "2008/01/20/internet-explorer-sepertinya-kita-harus-berpisah"
]

for slug in corrupt_slugs:
    clean_slug = slug.strip("/")
    # Try different URL patterns
    test_urls = [
        f"http://takien.com/{clean_slug}/",
        f"http://takien.com/blog/{clean_slug}/",
        f"http://blog.situskamu.com/{clean_slug.split('/')[-1]}/"
    ]
    found = None
    for u in test_urls:
        api = f"https://archive.org/wayback/available?url={u}"
        req = urllib.request.Request(api, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                snap = data.get("archived_snapshots", {}).get("closest")
                if snap and snap.get("available"):
                    found = (u, snap.get("url"), snap.get("timestamp"))
                    break
        except Exception as e:
            pass
        time.sleep(0.3)
    
    if found:
        print(f"[FOUND] {slug} -> {found[1]}")
    else:
        print(f"[NOT FOUND] {slug}")
