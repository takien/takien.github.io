import os
import re
import glob

emoji_map = {
    ":)": "🙂", ":-)": "🙂", ":D": "😀", ":-D": "😀",
    ";)": "😉", ";-)": "😉", ":P": "😛", ":-P": "😛", ":p": "😛",
    ":(": "🙁", ":-(": "🙁", ":o": "😮", ":-o": "😮",
    "8)": "😎", "8-)": "😎", ":|": "😐", ":-|": "😐",
    ":?:": "❓", ":!:": "❗", ":arrow:": "➡️"
}

def clean_placeholder(block):
    st = re.search(r"<strong>(.*?)</strong>", block)
    label = st.group(1).strip() if st else ""
    
    if label in emoji_map:
        return emoji_map[label]
    
    clean_label = label if label else "Gambar tidak tersedia"
    return f'''<figure class="image-missing-placeholder" role="img" aria-label="{clean_label}">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">{clean_label}</span>
  </div>
</figure>'''

posts = sorted(glob.glob("src/content/posts/*.md"))
updated_count = 0

for filepath in posts:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    orig = content

    # 1. Replace old <div class="image-missing-placeholder">...</div></div>
    content = re.sub(
        r"<div class=\"image-missing-placeholder\">.*?</div>\s*</div>",
        lambda m: clean_placeholder(m.group(0)),
        content,
        flags=re.DOTALL
    )

    # 2. Specific fix for photobucket broken image in 2007_08_05_differences-and-similarities.md
    if "s152.photobucket.com/albums/s182/fotoburket/umum/browser.png" in content:
        content = re.sub(
            r"<p><img[^>]*photobucket[^>]*></p>",
            '''<figure class="image-missing-placeholder" role="img" aria-label="differences and similarities browser">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">differences and similarities browser</span>
  </div>
</figure>''',
            content
        )
        content = content.replace("mini list :)", "mini list 🙂")

    # 3. Clean up unneeded wrapping <p> or <figure> around <figure class="image-missing-placeholder">
    content = re.sub(
        r"<p>\s*(<figure class=\"image-missing-placeholder\"[^>]*>.*?</figure>)\s*</p>",
        r"\1",
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r"<figure id=\"attachment_[^\"]*\"[^>]*>\s*(<figure class=\"image-missing-placeholder\"[^>]*>.*?</figure>)\s*</figure>",
        r"\1",
        content,
        flags=re.DOTALL
    )
    # Remove orphan <p></p>
    content = re.sub(r"<p>\s*</p>", "", content)

    if content != orig:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1

print(f"Updated {updated_count} files.")
