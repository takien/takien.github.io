import os
import re
import glob
import html

bwp_pattern = re.compile(
    r"<div class=\"bwp-syntax-block[^>]*>.*?<table class=\"([^\"]+)\".*?<div class=\"bwp-syntax-source\">\s*<pre class=\"no-parse\">(.*?)</pre>\s*</div>\s*</div>",
    re.DOTALL
)

lang_map = {
    "php": "php",
    "javascript": "javascript",
    "css": "css",
    "html4strict": "html",
    "html": "html",
    "js": "javascript"
}

def clean_code(raw_code):
    code = html.unescape(raw_code)
    code = re.sub(r"<\s+\?php", "<?php", code)
    return code.strip("\r\n")

posts = sorted(glob.glob("src/content/posts/*.md"))
updated_bwp = 0
updated_other_pre = 0

for filepath in posts:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    orig = content

    # 1. Convert bwp-syntax-block
    if "bwp-syntax-block" in content:
        def repl_bwp(m):
            raw_lang = m.group(1).lower().strip()
            l = lang_map.get(raw_lang, raw_lang)
            code = clean_code(m.group(2))
            return f"\n\n```{l}\n{code}\n```\n\n"

        content = bwp_pattern.sub(repl_bwp, content)
        # Clean stray </p> right after code block
        content = re.sub(r"```\s*</p>", "```\n\n", content)
        updated_bwp += 1

    # 2. Convert <pre><code class="language-([^"]+)">...</code></pre>
    def repl_pre_code(m):
        raw_lang = m.group(1).lower().strip()
        l = lang_map.get(raw_lang, raw_lang)
        code = clean_code(m.group(2))
        return f"\n\n```{l}\n{code}\n```\n\n"

    content = re.sub(
        r"<pre>\s*<code class=\"language-([^\"]+)\">\s*(.*?)\s*</code>\s*</pre>",
        repl_pre_code,
        content,
        flags=re.DOTALL
    )

    # 3. Convert <pre class="brush:\s*([^"]+)">...</pre>
    def repl_brush(m):
        raw_lang = m.group(1).lower().strip()
        l = lang_map.get(raw_lang, raw_lang)
        # Remove any html tags inside brush pre
        code = re.sub(r"<[^>]+>", "", m.group(2))
        code = clean_code(code)
        return f"\n\n```{l}\n{code}\n```\n\n"

    content = re.sub(
        r"<pre class=\"brush:\s*([^\"]+)\">\s*(.*?)\s*</pre>",
        repl_brush,
        content,
        flags=re.DOTALL
    )

    # 4. Clean up double figure with attachment caption around image-missing-placeholder
    content = re.sub(
        r"<figure id=\"attachment_[^\"]*\"[^>]*>\s*(<figure class=\"image-missing-placeholder\"[^>]*>.*?</figure>)\s*(?:<figcaption[^>]*>.*?</figcaption>\s*)?</figure>",
        r"\1",
        content,
        flags=re.DOTALL
    )

    if content != orig:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        updated_other_pre += 1

print(f"Finished: {updated_bwp} bwp files updated, total {updated_other_pre} files modified.")
