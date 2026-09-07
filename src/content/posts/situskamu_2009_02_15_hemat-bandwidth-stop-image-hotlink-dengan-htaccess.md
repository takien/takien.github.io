---
title: "Hemat bandwidth, stop image hotlink dengan htaccess"
date: "2009-02-15T12:00:00Z"
categories: ["Internet", "website"]
tags: ["2007", "2008", "blog", "blogger", "Browser", "cara menginstall wordpress", "cari duit", "city", "css", "custom block", "custom region", "div", "domain", "domain parking", "Drupal", "drupal theme", "forum", "Google", "htaccess", "html", "integration", "Internet", "Internet Explorer", "kaleidoskop", "kilas balik", "layout", "mini city", "mod rewrite", "parked domain", "review", "security", "SEO", "SMF", "Spyware", "table", "tutorial wordpress", "upgrade wordpress", "Web 2.0", "Webdesign", "website", "WordPress", "wordpress plugin", "Wordpress theme", "wordpress upgrade", "xampp"]
slug: "2009/02/15/hemat-bandwidth-stop-image-hotlink-dengan-htaccess"
legacyUrl: "/hemat-bandwidth-stop-image-hotlink-dengan-htaccess/"
source: "blog.situskamu.com"
comments: [
  {
    "author": "Anonymous",
    "date": "Apr 3, 08 at 7:07 am",
    "text": "siiip mantaps bro gw masukin lin ke sini"
  },
  {
    "author": "Anonymous",
    "date": "Apr 3, 08 at 12:21 pm",
    "text": "wahh perlu juga ni om…\n\niya bener donk, kl BW unlimited ga perlu khawatir donk share link image kita…betul ga ?\n\ntapi, kali ini postingan om bagus cekali om..\n\n:two thumbs up:"
  },
  {
    "author": "Anonymous",
    "date": "Apr 3, 08 at 6:44 pm",
    "text": "nanya, itu social bookmarking pake plugin apa yach\n\ntrims  \n\nnamakamu reply on April 5th, 2008:\n\nPake plugin social bookmarks, download di sini http://www.dountsis.com/"
  },
  {
    "author": "Anonymous",
    "date": "Apr 3, 08 at 9:32 pm",
    "text": "Gw mau pamer sedikit heheh…\n\nMAKANYA KALO BELI HOSTING JANGAN YANG BANDWITH DI LIMITED DONK hahahah\n\ntapi bagus juga neh ide nya…..\n\nijin copas juragan… cendol menyusul\n\nnamakamu reply on April 5th, 2008:"
  },
  {
    "author": "Anonymous",
    "date": "May 24, 08 at 10:22 pm",
    "text": "kalo ga mau repot…\n\npake imageshack aja \n\nkalo upload gambar dari wordpress suka keindex di google juga soalnya, padahal mungkin ga kita kasih konten sedikitpun.."
  },
  {
    "author": "Anonymous",
    "date": "Jun 14, 08 at 9:32 pm",
    "text": "belum pernah ngalamin sekalipun bandwith exceed (situs yang sepi  hahahaha). Jadi gila sendiri\n\nNice info gan (sory lom iso 2000, gak bisa naro ijo2 di mari)\n\nnamakamu reply on June 18th, 2008:\n\nmari kita ramai-ramaikan situsnya"
  },
  {
    "author": "Anonymous",
    "date": "Jun 17, 08 at 5:12 pm",
    "text": "Bagus juga, tapi kan kita bisa pake imge hosting\n\nnamakamu reply on June 18th, 2008:\n\nemang bisa kok..   tapi kadang karena alasan tertentu, seperti kecepatan akses dsb, di upload di server sendiri"
  },
  {
    "author": "Anonymous",
    "date": "Jun 27, 08 at 12:58 am",
    "text": "Thx y… Gak kpkiran tuh smpi ksana.. Otak2 standar kaya gw mmg prlu info2 kyk gini… Cari obat dl y.. Dah pusing nih..\n\nnamakamu reply on June 27th, 2008:\n\nHEHE.. minum dolo bro"
  },
  {
    "author": "Anonymous",
    "date": "Jul 16, 08 at 9:58 pm",
    "text": "sebentar om,.\n\nfile htaccess lokasi dimana yah,.??\n\naye,. lum pernah utak-atik,..\n\nnamakamu reply on July 17th, 2008:\n\ndimana saja, pokoknya di dalam folder \n\nmisalnya .htaccess kita letakkan di folder public_html/ maka semua setingan di file tersebut akan mempengaruhi seluruh isi public_html, dan sub foldernya… begitu seterusnya."
  }
]
---

<p><figure class="image-missing-placeholder" role="img" aria-label="Hotlinking Image, hotlink protection">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Hotlinking Image, hotlink protection</span>
  </div>
</figure>Mempunyai situs yang ramai pengunjung adalah dambaan setiap orang. Akan tetapi menjadi kurang menarik kalau pengujung yang banyak itu akhirnya mendapati halaman website dengan pesan error Bandwidth Exceeded alias kehabisan bandwidth. Okelah, kalau penyebab habisnya bandwidth tersebut memang karena kebanyakan pengunjung, tentu saja sebagai pemilik situs tidak keberatan untuk menambah quota bandwidthnya. Tapi kalau itu terjadi karena pencurian bandwidth atau <u>bandwidth stealing</u> akan lain lagi ceritanya, sudah barang tentu si empunya situs akan merasa dirugikan. <span id="more-105"></span></p>
<p><font color="#ffffff">/</font></p>
<p>Mengapa bisa terjadi pencurian bandwidth? Pencurian bandwidth lebih banyak terjadi pada website yang memuat gambar-gambar. Dimana pengunjung website dengan sengaja melakukan hotlinking ke gambar-gambar tersebut untuk di tampilkan di halaman website mereka atau mempostingnya di forum. Ketika halaman website atau forum tersebut diakses, maka secara langsung ia memanggil source gambar dari website ‘korban’. Dan jika ini terjadi terus menerus dengan jumlah request page yang banyak, kemungkinan bandwidth website pemilik gambar akan terkuras habis. Selain disebut pencurian bandwidth sebenarnya hal ini termasuk <u>pencurian gambar</u> itu sendiri.</p>
<p><font color="#ffffff">/</font></p>
<p>Hal ini bisa diatasi dengan sedikit trik yaitu penambahan baris anti image hotlink di file htaccess dengan syarat server yang bersangkutan sudah terinstal modul rewrite. Misalnya situs yang akan di tutup hotlink nya adalah <strong>situskamu.com</strong>, berikut ini adalah baris yang perlu ditambahkan di <em>htaccess</em>.</p>
<p><font color="#ffffff">/</font></p>
<pre>RewriteEngine on<o:p></o:p></pre>
<pre>RewriteCond %{HTTP_REFERER} !^http://(.+\.)?<strong>situskamu\.com</strong>/ [NC]<o:p></o:p></pre>
<pre>RewriteCond %{HTTP_REFERER} !^$<o:p></o:p></pre>
<pre>RewriteRule .*\.(<strong>jpeg|gif|bmp|png|jpg</strong>)$ /<strong>gambar/dilarangmencuri.jpe</strong> [L]</pre>
<pre><font color="#ffffff">/</font></pre>
<pre></pre>
<ul type="disc">
<li class="MsoNormal">Baris pertama untuk      mengaktifkan mod rewrite.<o:p></o:p></li>
<li class="MsoNormal">Baris kedua menyatakan      hanya domain <em>situskamu.com</em> yang diperbolehkan hotlink.</li>
<li class="MsoNormal">Baris ketiga menyatakan diperbolehkannya akses langsung ke image. (klik      kanan, <em>view image</em> kalau di browser Firefox).<o:p></o:p></li>
<li class="MsoNormal">Baris keempat, parameter      ekstensi gambar apa saja yang tidak boleh di hotlink, dan menentukan      lokasi gambar penggantinya.<br/>
Jangan lupa untuk menyediakan file gambar pengganti misalnya ditempatkan      dalam path <strong>/gambar/dilarangmencuri.jpe</strong>. File pengganti memakai      ekstensi <strong>.jpe</strong> supaya<br/>
tidak ikut terblokir, untuk membuatnya cukup <em>rename </em>file berektensi      jpg menjadi jpe.</li>
</ul>
<p><font color="#ffffff">/</font></p>
<p>Untuk mencegah hotlink dari situs-situs tertentu saja, misalnya blogspot atau wordpress (karena kebanyakan mereka melakukan hotlink 😀 ) dan memperbolehkan situs lainnya untuk melakukan hotlink, kode htaccess-nya adalah sebagai berikut:</p>
<p><font color="#ffffff">/</font></p>
<pre>RewriteEngine On<o:p></o:p></pre>
<pre>RewriteCond %{HTTP_REFERER} ^http://(.+\.)?<strong>wordpress\.com</strong>/ [NC,OR]<o:p></o:p></pre>
<pre>RewriteCond %{HTTP_REFERER} ^http://(.+\.)?<strong>blogspot\.com</strong>/ [NC,OR]<o:p></o:p></pre>
<pre>RewriteCond %{HTTP_REFERER} ^http://(.+\.)?<strong>blogsome\.com</strong>/ [NC]<o:p></o:p></pre>
<pre>RewriteRule .*\.(<strong>jpeg|gif|bmp|png|jpg</strong>)$ /<strong>gambar/dilarangmencuri.jpe</strong> [L]</pre>
<pre><font color="#ffffff">/</font></pre>
<pre></pre>
<p>Hal ini sekaligus menjawab kenapa gambar yang diupload di imageshack, akan berubah menjadi kodok ketika diposting di forum kaskus.us. Jelas saja, kaskus <st1:state w:st="on"><st1:place w:st="on">kan</st1:place></st1:state> trafiknya nauzubillah. 😀 </p>
<p><font color="#ffffff">/</font></p>
<p><strong><em>Catatan:</em></strong><br/>
- Hal ini bisa juga dilakukan dari cPanel dari menu <a href="https://web.archive.org/web/20090502000851/http://www.cpanel.net/docs/cpanel/cp11/Security/HotLink_Protection.htm" target="_blank">Hotlink Protection</a><br/>
- Anehnya, salah seorang temanku malah menyebarkan gambarnya dimana-mana untuk menghabiskan bandwidth nya lho. Nggak akan habis karena unlimited, katanya 😀 </p>
