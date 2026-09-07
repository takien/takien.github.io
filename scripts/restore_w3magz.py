import os
import re
import html
import json
import urllib.request
import urllib.parse
from datetime import datetime

os.makedirs("public/images/w3magz", exist_ok=True)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

def download_image(url):
    if not url.startswith("http"):
        if url.startswith("/web/"):
            url = "http://web.archive.org" + url
        else:
            return url
            
    # Extract filename
    clean_url = url.split("?")[0]
    fname = os.path.basename(clean_url)
    if not fname or fname.endswith(".php") or fname.endswith(".html"):
        fname = f"img_{abs(hash(url)) % 1000000}.jpg"
        
    local_path = os.path.join("public/images/w3magz", fname)
    public_url = f"/images/w3magz/{fname}"
    
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        return public_url
        
    # Download
    candidates = [url]
    # Check if we can extract the original un-archived url
    orig_match = re.search(r"http://web\.archive\.org/web/\d+[a-z_]*/(https?://.+)$", url)
    if orig_match:
        orig_url = orig_match.group(1)
        # Try Wayback availability API
        try:
            api_url = f"https://archive.org/wayback/available?url={urllib.parse.quote(orig_url, safe=':/?=')}"
            api_req = urllib.request.Request(api_url, headers=headers)
            with urllib.request.urlopen(api_req, timeout=5) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
            closest = res_data.get("archived_snapshots", {}).get("closest", {})
            if closest.get("available") and closest.get("url"):
                wb_url = closest.get("url")
                # Add im_ flag
                wb_url_im = re.sub(r"/web/(\d+)/", r"/web/\1im_/", wb_url)
                candidates.append(wb_url_im)
                candidates.append(wb_url)
        except Exception:
            pass

    for cand in candidates:
        try:
            req = urllib.request.Request(cand, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
            if len(data) > 200:
                with open(local_path, "wb") as f:
                    f.write(data)
                print(f"Downloaded image: {fname} ({len(data)} bytes)")
                return public_url
        except Exception:
            continue
            
    print(f"Image not available on archive.org: {fname}")
    return public_url

urls = [
    "http://web.archive.org/web/20150407015734/http://w3magz.com/865/kalau-sudah-lancar-bahasa-pemrograman-terus-kenapa.html",
    "http://web.archive.org/web/20141209045055/http://w3magz.com/858/tentang-telkom-speedy-dan-push-ad-u-ad-info.html",
    "http://web.archive.org/web/20131210021817/http://w3magz.com/798/serunya-menggunakan-facebook-messenger-for-firefox.html",
    "http://web.archive.org/web/20150403203335/http://w3magz.com/900/deviantart-berganti-logo-nyeleneh-dan-kreatif-namun-menuai-kontroversi.html",
    "http://web.archive.org/web/20150406003535/http://w3magz.com/822/apakah-design-website-anda-responsive.html",
    "http://web.archive.org/web/20140721140425/http://w3magz.com/775/dot-pw-untuk-professional-web.html",
    "http://web.archive.org/web/20140205105834/http://w3magz.com/196/mengambil-data-dari-url-lain-menggunakan-curl.html",
    "http://web.archive.org/web/20140112073749/http://w3magz.com/468/mengambil-dan-mengirim-data-menggunakan-curl.html",
    "http://web.archive.org/web/20140602202046/http://w3magz.com/681/hal-hal-yang-harus-diperhatikan-ketika-interview-kerja-sebagai-web-programmer.html",
    "http://web.archive.org/web/20140502095116/http://w3magz.com/690/paypal-mengakuisisi-card-io.html",
    "http://web.archive.org/web/20140516044809/http://w3magz.com/739/memasang-facebook-recommendation-bar-pada-wordpress.html"
]

months_en = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
}

def clean_code_block(code_raw, lang="php"):
    # extract from <pre> if wrapped
    pre_m = re.search(r"<pre[^>]*>(.*?)</pre>", code_raw, flags=re.DOTALL | re.IGNORECASE)
    if pre_m:
        code_text = pre_m.group(1)
    else:
        code_text = code_raw
        
    code_text = re.sub(r"<br\s*/?>", "\n", code_text, flags=re.IGNORECASE)
    code_text = re.sub(r"</?p>", "\n", code_text, flags=re.IGNORECASE)
    code_text = re.sub(r"<[^>]+>", "", code_text)
    
    code_text = html.unescape(code_text)
    code_text = html.unescape(code_text)
    
    code_text = code_text.replace("‘", "\x27").replace("’", "\x27")
    code_text = code_text.replace("“", "\"").replace("”", "\"")
    
    lines = code_text.split("\n")
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    clean_code = "\n".join(lines)
    return f"\n\n```{lang}\n{clean_code}\n```\n\n"

for u in urls:
    m_url = re.search(r"/(\d+)/([^/]+)\.html", u)
    if not m_url:
        continue
    post_id = m_url.group(1)
    post_slug = m_url.group(2)
    cached_fn = f"{post_id}_{post_slug}.html"
    cached_path = os.path.join("scratch/w3magz", cached_fn)
    
    if not os.path.exists(cached_path):
        print(f"Skipping {cached_fn}, file not found")
        continue
        
    with open(cached_path, "r", encoding="utf-8", errors="replace") as f:
        c = f.read()
        
    # 1. Title
    t_m = (re.search(r"<h1[^>]*class=[\"\x27]entry-title[\"\x27][^>]*>(.*?)</h1>", c, re.I | re.DOTALL) or
           re.search(r"<h1 id=[\"\x27]post-title[\"\x27][^>]*>(.*?)</h1>", c, re.I | re.DOTALL) or
           re.search(r"<meta property=[\"\x27]og:title[\"\x27] content=[\"\x27](.*?)[\"\x27]", c, re.I) or
           re.search(r"<title>(.*?)</title>", c, re.I))
    title = re.sub(r"<[^>]+>", "", t_m.group(1)).replace(" | W3Magz", "").replace("»", "").strip() if t_m else post_slug.replace("-", " ").title()
    title = html.unescape(title).strip()
    
    # 2. Date
    date_str = ""
    d_m = re.search(r"<meta property=[\"\x27](?:article|og):published_time[\"\x27] content=[\"\x27](.*?)[\"\x27]", c, re.I)
    if d_m:
        date_str = d_m.group(1).strip()
    else:
        time_m = re.search(r"<time[^>]+datetime=[\"\x27]([^\"\x27]+)[\"\x27]", c, re.I)
        if time_m:
            date_str = time_m.group(1).strip()
        else:
            pda_m = re.search(r"<p class=\"post-date-author\">(.*?)</p>", c, re.I | re.DOTALL)
            if pda_m:
                text = re.sub(r"<[^>]+>", " ", pda_m.group(1)).strip()
                date_match = re.search(r"([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})", text)
                if date_match:
                    m_name, day, year = date_match.groups()
                    m_num = months_en.get(m_name.lower(), 1)
                    date_str = f"{year}-{m_num:02d}-{int(day):02d}T00:00:00Z"
                    
    # Parse date to year/month/day
    try:
        # Handle ISO date
        clean_date_str = date_str[:10]
        dt = datetime.strptime(clean_date_str, "%Y-%m-%d")
        y = f"{dt.year:04d}"
        m = f"{dt.month:02d}"
        d = f"{dt.day:02d}"
    except Exception:
        y, m, d = "2014", "01", "01"
        
    canonical_slug = f"{y}/{m}/{d}/{post_slug}"
    
    # 3. Category
    cat_m = (re.search(r"rel=[\"\x27]category tag[\"\x27][^>]*>(.*?)</a>", c, re.I) or
             re.search(r"<span class=\"glyphicon glyphicon-folder-open\"></span>\s*([^<]+)", c, re.I))
    cat_raw = re.sub(r"<[^>]+>", "", cat_m.group(1)).strip() if cat_m else "General"
    category = html.unescape(cat_raw).strip()
    if category.lower() == "wordpress":
        category = "WordPress"
    elif category.lower() == "webhosting & domain":
        category = "Domain"
        
    # 4. Tags
    tags = [html.unescape(t.strip()) for t in re.findall(r"rel=[\"\x27]tag[\"\x27][^>]*>([^<]+)</a>", c, re.I)]
    
    # 5. Body
    body = ""
    art_m = re.search(r"<article[^>]*class=[\"\x27][^\"\x27]*post-entry[^\"\x27]*[\"\x27][^>]*>(.*?)</article>", c, re.DOTALL | re.I)
    if art_m:
        raw_art = art_m.group(1)
        hdr_m = re.search(r"</header>", raw_art, re.I)
        if hdr_m:
            raw_art = raw_art[hdr_m.end():]
        cut_m = re.search(r"(?:<div[^>]*class=[\"\x27][^\"\x27]*(?:sharedaddy|share-post|post-meta|robots-nocontent)[^\"\x27]*[\"\x27]|<footer)", raw_art, re.I)
        if cut_m:
            raw_art = raw_art[:cut_m.start()]
        body = raw_art.strip()
    else:
        ac_m = re.search(r"<div class=\"article-content\">(.*?)(?:<div class=\"sharedaddy|<div class=\"robots-nocontent|<div class=\"post-meta\"|<footer|<div id=\"comments\")", c, re.DOTALL | re.I)
        if ac_m:
            raw_art = ac_m.group(1)
            cut_hdr = re.search(r"<hr\s*/?>", raw_art, re.I)
            if cut_hdr:
                raw_art = raw_art[cut_hdr.end():]
            body = raw_art.strip()
            
    # Clean adsense & ad blocks
    body = re.sub(r"\[adsense\]", "", body, flags=re.IGNORECASE)
    body = re.sub(r"<img[^>]*src=[\"\x27][^\"\x27]*ads-[^\"\x27]*[\"\x27][^>]*>", "", body, flags=re.IGNORECASE)
    
    # Download and rewrite images
    def repl_img(m):
        full_tag = m.group(0)
        src = m.group(1)
        if ("web.archive.org" in src and "_static" in src) or "pixel.wp.com" in src or "gravatar" in src:
            return ""
        if "icon_smile.gif" in src or "icon_biggrin.gif" in src:
            return "😊"
        local_src = download_image(src)
        
        alt_m = re.search(r"alt=[\"\x27](.*?)[\"\x27]", full_tag)
        alt = alt_m.group(1) if alt_m else ""
        title_m = re.search(r"title=[\"\x27](.*?)[\"\x27]", full_tag)
        title_attr = title_m.group(1) if title_m else ""
        
        return f'<img src="{local_src}" alt="{alt}" title="{title_attr}" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" />'
        
    body = re.sub(r"<img[^>]+src=[\"\x27]([^\"\x27]+)[\"\x27][^>]*>", repl_img, body, flags=re.IGNORECASE)
    
    # Unlink images wrapped in <a>...</a>
    body = re.sub(r"<a[^>]*>\s*(<img[^>]+>)\s*</a>", r"\1", body, flags=re.IGNORECASE)
    
    # Convert code blocks [php]...[/php] or [code]...[/code]
    def repl_php_tag(m):
        return clean_code_block(m.group(1), "php")
    body = re.sub(r"(?:<p>\s*)?\[php\](.*?)\[/php\](?:\s*</p>)?", repl_php_tag, body, flags=re.DOTALL | re.IGNORECASE)
    
    def repl_code_tag(m):
        full = m.group(0)
        lang_m = re.search(r"\[code(?:\s+lang=(?:&#8221;|\"|”|&quot;|\x27)?([a-zA-Z0-9_\-]+)(?:&#8221;|\"|”|&quot;|\x27)?)?[^\]]*\]", full, flags=re.IGNORECASE)
        lang = lang_m.group(1).lower().strip() if (lang_m and lang_m.group(1)) else "php"
        lang = re.sub(r"[&#0-9;\"“”\x27]", "", lang).strip()
        inner_m = re.search(r"\[code[^\]]*\](.*?)\[/code\]", full, flags=re.DOTALL | re.IGNORECASE)
        code_raw = inner_m.group(1) if inner_m else ""
        return clean_code_block(code_raw, lang)
    body = re.sub(r"(?:<p>\s*)?\[code[^\]]*\].*?\[/code\](?:\s*</p>)?", repl_code_tag, body, flags=re.DOTALL | re.IGNORECASE)
    
    # Convert <pre> blocks if any
    def repl_pre_tag(m):
        code_raw = m.group(1)
        lang = "sql" if "SELECT" in code_raw or "WHERE" in code_raw else "php"
        return clean_code_block(code_raw, lang)
    body = re.sub(r"<pre[^>]*>(.*?)</pre>", repl_pre_tag, body, flags=re.DOTALL | re.IGNORECASE)
    
    # Clean empty tags
    body = re.sub(r"<p>\s*</p>", "", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    
    # 6. Comments
    comments = []
    for m in re.finditer(r"<li[^\>]*class=[\"\x27][^\"]*comment[^\"]*[\"\x27][^\>]*id=[\"\x27](?:comment-|dsq-comment-)(\d+)[\"\x27]\>(.*?)(?=<li[^\>]*class=[\"\x27][^\"]*comment|</ul>|</ol>|$)", c, re.DOTALL | re.I):
        c_body = m.group(2)
        a_m = re.search(r"<span id=\"dsq-author-user-\d+\">(.*?)</span>", c_body, re.I | re.DOTALL)
        if not a_m:
            a_m = re.search(r"<span[^>]*class=[\"\x27][^\"]*comment-author[^\"]*[\"\x27][^>]*>(.*?)</span>", c_body, re.I | re.DOTALL)
        if not a_m:
            a_m = re.search(r"<cite[^>]*>(.*?)</cite>", c_body, re.I | re.DOTALL)
            
        c_author = re.sub(r"<[^>]+>", "", a_m.group(1)).strip() if a_m else "Anonim"
        # If c_author contains url, remove url
        c_author = re.sub(r"https?://[^\s]+", "", c_author).strip()
        c_author = html.unescape(c_author).strip()
        if not c_author:
            c_author = "Anonim"
            
        time_cm = re.search(r"<time[^>]+datetime=[\"\x27]([^\"\x27]+)[\"\x27]", c_body, re.I)
        c_date = time_cm.group(1) if time_cm else ""
        
        msg_m = re.search(r"<div[^>]*class=[\"\x27][^\"\x27]*(?:comment-content|comment-text|comment-body|dsq-comment-message)[^\"\x27]*[\"\x27][^>]*>(.*?)</div>", c_body, re.I | re.DOTALL)
        c_msg = ""
        if msg_m:
            c_msg = re.sub(r"<[^>]+>", " ", msg_m.group(1)).strip()
            c_msg = html.unescape(c_msg).strip()
            
        if c_msg:
            comments.append({
                "author": c_author,
                "date": c_date,
                "text": c_msg
            })
            
    # Legacy URLs
    legacy_urls = [
        f"{post_id}/{post_slug}.html",
        f"{post_id}/{post_slug}",
        f"w3magz/{post_id}/{post_slug}.html",
        f"w3magz/{post_id}/{post_slug}"
    ]
    
    # Create frontmatter
    comments_json = json.dumps(comments, ensure_ascii=False)
    categories_json = json.dumps([category], ensure_ascii=False)
    tags_json = json.dumps(tags, ensure_ascii=False)
    legacy_json = json.dumps(legacy_urls, ensure_ascii=False)
    
    escaped_title = title.replace('"', '\\"')
    
    post_md = f"""---
title: "{escaped_title}"
date: "{date_str}"
categories: {categories_json}
tags: {tags_json}
slug: "{canonical_slug}"
legacyUrls: {legacy_json}
source: "w3magz.com"
author: "Wak Jek"
comments: {comments_json}
---

{body.strip()}
"""

    out_fn = f"w3magz_{post_id}_{post_slug}.md"
    out_path = os.path.join("src/content/posts", out_fn)
    with open(out_path, "w", encoding="utf-8") as out_f:
        out_f.write(post_md)
        
    print(f"Created {out_fn} -> {canonical_slug} (Category: {category}, Comments: {len(comments)})")

print("\nDone restoring w3magz articles!")
