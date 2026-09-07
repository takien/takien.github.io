import os, re, html

post_dir = "src/content/posts"

def clean_code_block(match):
    full = match.group(0)
    # extract lang from tag
    lang_m = re.search(r"\[code(?:\s+lang=(?:&#8221;|\"|”|&quot;|\x27)?([a-zA-Z0-9_\-]+)(?:&#8221;|\"|”|&quot;|\x27)?)?[^\]]*\]", full, flags=re.IGNORECASE)
    lang = lang_m.group(1).lower().strip() if (lang_m and lang_m.group(1)) else ""
    lang = re.sub(r"[&#0-9;\"“”\x27]", "", lang).strip()
    
    # extract inner code
    inner_m = re.search(r"\[code[^\]]*\](.*?)\[/code\]", full, flags=re.DOTALL | re.IGNORECASE)
    code_raw = inner_m.group(1) if inner_m else ""
    
    # determine lang if missing
    if not lang:
        if "RewriteRule" in code_raw or ".htaccess" in code_raw:
            lang = "bash"
        elif "yepnope" in code_raw or "loadAndWait" in code_raw or "head.js" in code_raw or "document.documentElement" in code_raw:
            lang = "javascript"
        elif "{" in code_raw and ":" in code_raw and ("padding" in code_raw or "text-align" in code_raw or "font-size" in code_raw):
            lang = "css"
        else:
            lang = "php"
    elif lang == "js":
        lang = "javascript"
        
    # extract from <pre> if wrapped
    pre_m = re.search(r"<pre[^>]*>(.*?)</pre>", code_raw, flags=re.DOTALL | re.IGNORECASE)
    if pre_m:
        code_text = pre_m.group(1)
    else:
        code_text = code_raw
        
    # replace <br/>, <br>, <br /> with newline
    code_text = re.sub(r"<br\s*/?>", "\n", code_text, flags=re.IGNORECASE)
    # replace <p> and </p> with \n
    code_text = re.sub(r"</?p>", "\n", code_text, flags=re.IGNORECASE)
    # strip remaining HTML tags like <span ...>, </span>, etc.
    code_text = re.sub(r"<[^>]+>", "", code_text)
    
    # unescape HTML entities (twice for potential double escapes)
    code_text = html.unescape(code_text)
    code_text = html.unescape(code_text)
    
    # fix smart quotes in programming code
    code_text = code_text.replace("‘", "\x27").replace("’", "\x27")
    code_text = code_text.replace("“", "\"").replace("”", "\"")
    
    # strip leading and trailing whitespace/empty lines
    lines = code_text.split("\n")
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    clean_code = "\n".join(lines)
    
    return f"\n\n```{lang}\n{clean_code}\n```\n\n"

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content

    # 1. Remove [adsense]
    content = re.sub(r"\[adsense\]", "", content, flags=re.IGNORECASE)

    # 2. Clean outer residual WordPress wrappers if present
    # Remove top duplicate h2 title if it links to itself
    content = re.sub(r"<h2><a href=\"[^\"]*\">.*?</a></h2>\s*", "", content, flags=re.IGNORECASE)
    # Remove <div class="entry-content clearfix">
    content = re.sub(r"<div class=\"entry-content clearfix\">\s*", "", content, flags=re.IGNORECASE)
    # Remove <div class="posttags">...</div>
    content = re.sub(r"<div class=\"posttags\">.*?</div>\s*", "", content, flags=re.DOTALL | re.IGNORECASE)

    # 3. Transform [code] blocks
    content = re.sub(r"(?:<p>\s*)?\[code[^\]]*\].*?\[/code\](?:\s*</p>)?", clean_code_block, content, flags=re.DOTALL | re.IGNORECASE)

    # 4. Clean up trailing closing divs that were matching entry-content
    # Check if closing div at end is unmatched
    parts = content.split("---", 2)
    if len(parts) > 2:
        frontmatter = parts[1]
        body = parts[2]
        # Clean trailing </div> if unmatched
        open_divs = len(re.findall(r"<div\b", body, flags=re.IGNORECASE))
        close_divs = len(re.findall(r"</div\b", body, flags=re.IGNORECASE))
        while close_divs > open_divs and re.search(r"</div>\s*$", body.strip(), flags=re.IGNORECASE):
            body = re.sub(r"</div>\s*$", "", body.strip(), flags=re.IGNORECASE)
            close_divs -= 1
        
        # Clean multiple empty paragraphs
        body = re.sub(r"<p>\s*</p>", "", body)
        body = re.sub(r"\n{3,}", "\n\n", body)
        content = f"---{frontmatter}---\n\n{body.strip()}\n"

    if content != orig_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

modified_count = 0
for fn in sorted(os.listdir(post_dir)):
    if not fn.endswith(".md"):
        continue
    p = os.path.join(post_dir, fn)
    if process_file(p):
        modified_count += 1
        print(f"Updated: {fn}")

print(f"Done! Modified {modified_count} files.")
