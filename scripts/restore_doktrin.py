#!/usr/bin/env python3
import subprocess
import re
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.restore_situskamu_and_fixes import clean_html_content, extract_comments_from_html

url = "https://web.archive.org/web/20140626162012/http://takien.com/blog/2013/12/16/doktrin-doktrin-menyesatkan-di-industri-kreatif/"
res = subprocess.run(["curl", "-s", "-L", "-A", "Mozilla/5.0", url], capture_output=True)
html = res.stdout.decode("utf-8", errors="replace")

pos = html.find('id="post-1372"')
end_pos = html.find('</article>', pos)
article_html = html[pos:end_pos]
header_end = article_html.find('</header>')
raw_body = article_html[header_end + len('</header>'):].strip()

clean_body = clean_html_content(raw_body)
comments = extract_comments_from_html(html)

title = "Doktrin-doktrin Menyesatkan di Industri Kreatif"
date = "2013-12-16T23:49:21+00:00"

md_content = f"""---
title: {json.dumps(title, ensure_ascii=False)}
date: "{date}"
categories: ["Story"]
tags: ["industri kreatif", "pekerja kreatif"]
slug: "2013/12/16/doktrin-doktrin-menyesatkan-di-industri-kreatif"
legacyUrl: "/blog/2013/12/16/doktrin-doktrin-menyesatkan-di-industri-kreatif/"
comments: {json.dumps(comments, ensure_ascii=False, indent=2)}
---

{clean_body}
"""

target_file = "/Users/wak./Projects/GoogleAI/takien.com/src/content/posts/2013_12_16_doktrin-doktrin-menyesatkan-di-industri-kreatif.md"
with open(target_file, "w", encoding="utf-8") as fp:
    fp.write(md_content.strip() + "\n")

print(f"Successfully wrote {target_file} ({len(clean_body)} chars)")
