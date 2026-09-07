---
title: "Memperbaiki ‘Title Case’ Bahasa Indonesia dalam Judul Artikel di WordPress"
date: "2013-12-02T00:00:00Z"
categories: ["Wordpress"]
tags: []
slug: "2013/12/02/memperbaiki-title-case-bahasa-indonesia-dalam-judul-artikel-di-wordpress"
legacyUrl: "/blog/2013/12/02/memperbaiki-title-case-bahasa-indonesia-dalam-judul-artikel-di-wordpress/"
comments: [{"author": "Nicholas Sihotang", "date": "", "text": "Mantap ini, bang. Bukti nyata, ada programmer yang juga peduli sama bahasa Indonesia (gak cuma bahasa pemrograman) 😀"}, {"author": "takien", "date": "", "text": "Bug found, perampokan tidak akan dirubah menjadi Perampokan, karena ada per-nya.\n\nFix dlu ea…"}, {"author": "ArieL FX", "date": "", "text": "wah keren, patut di coba"}, {"author": "okedeh", "date": "", "text": "gan gan, di wp ada file fungsi autoload gak"}, {"author": "aprilia awaludin", "date": "", "text": "Bang, saya mau donasikan uang saya yang $5,000,4499 untuk biaya jadi programmer"}]
---

<div style="float:left;margin-right:10px;margin-bottom:10px;">

</div>
						<figure class="image-missing-placeholder" role="img" aria-label="Letters (source: pixabay.com)">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Letters (source: pixabay.com)</span>
  </div>
</figure>
<p>Tidak dapat dipungkiri bahwa masih banyak penulis (biasanya penulis pemula) yang melakukan kesalahan dalam penulisan judul artikel. Terutama kesalahan dalam penulisan kapitalisasi huruf di judul sesuai dengan EYD (Ejaaan yang Disempurnakan).</p>
<p>Sebagaimana diketahui, semua huruf pada awal kata di judul harus ditulis dengan huruf besar atau kapital, kecuali kata-kata berikut ini:</p>
<ul class="three-cols">
<li>atau</li>
<li>dan</li>
<li>dengan</li>
<li>ke</li>
<li>per</li>
<li>oleh</li>
<li>ala</li>
<li>buat</li>
<li>tetapi</li>
<li>setelah</li>
<li>tapi</li>
<li>untuk</li>
<li>bagi</li>
<li>dari</li>
<li>di</li>
<li>kepada</li>
<li>dalam</li>
<li>pun</li>
<li>sebelum</li>
<li>tentang</li>
<li>yang</li>
<li>daripada</li>
<li>karena</li>
<li>pada</li>
<li>sampai</li>
<li>tanpa</li>
</ul>
<p>Jika Anda menggunakan platform WordPress, saya telah membuatkan sebuah filter sederhana untuk memperbaiki penulisan judul yang salah.  Berikut kodenya:</p>



```php
/**
* Fix Indonesia Titlecase
* @author: takien
*/
add_filter('the_title','wakpress_fix_indonesia_titlecase');
function wakpress_fix_indonesia_titlecase( $title ) {
$except = Array('atau','dan','dengan','ke','per', 'oleh', 'ala', 'buat', 'tetapi', 'setelah', 'tapi', 'untuk', 'bagi',
	'dari', 'di', 'kepada', 'dalam', 'pun', 'sebelum', 'tentang', 'yang', 'daripada', 'karena', 'pada','sampai', 'tanpa'
);
	return ucfirst(preg_replace(array_map('wakpress_titlecase_keyword_map',array_values($except)),array_values($except), ucwords($title)));
}
function wakpress_titlecase_keyword_map( $key ) {
      return '/'.$key.'\b/i';
}
```


<p>Paste/tempelkan kode tersebut di file <code>functions.php</code> pada tema yang sedang Anda gunakan.</p>

<div id="jp-relatedposts" class="jp-relatedposts">
	<h3 class="jp-relatedposts-headline"><em>Related</em></h3>
</div>
