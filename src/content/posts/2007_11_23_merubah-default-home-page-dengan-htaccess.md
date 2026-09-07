---
title: "Merubah Default Home Page dengan .htaccess"
date: "2007-11-23T00:00:00Z"
categories: ["Website"]
tags: []
slug: "2007/11/23/merubah-default-home-page-dengan-htaccess"
legacyUrls: ["10/merubah-default-home-page-dengan-htaccess.php", "10/merubah-default-home-page-dengan-htaccess", "blog/2007/11/23/merubah-default-home-page-dengan-htaccess", "merubah-default-home-page-dengan-htaccess"]
source: "takien.com"
comments: [
  {
    "author": "xrvel",
    "date": "",
    "text": "wah sip sip tipsnya&#8230;"
  },
  {
    "author": "Ghprod",
    "date": "",
    "text": "berguna bgt .. thnx bro"
  },
  {
    "author": "bangJo",
    "date": "",
    "text": "sep deh infonya bang&#8230;thanks"
  },
  {
    "author": "jawir",
    "date": "",
    "text": "Langsung praktek gan"
  }
]
---

<p>Kata orang-orang dulu, salah satu langkah yang tidak boleh terlewatkan dalam membuat situs adalah membuat file <em>index.htm, index.html, atau index.php</em> di direktori root.<br/>
Kenapa harus ada file index? Ya, karena file inilah yang pertama kali<br/>
ditampilkan ketika orang membuka situs kita, dan di file inilah kita bisa<br/>
meletakkan berbagai link (dulu hyperlink) ke halaman-halaman lainnya.</p>
<p>Sebenernya kita bisa menentukan sendiri file mana yang akan menjadi<br/>
index dan tidak harus bernama index.htm, index.html, ataupun index.php Untuk menentukan file apa<br/>
yang akan menjadi index kita cukup menambahkan baris berikut di <em>.htaccess</em></p>
<blockquote><p><code>DirectoryIndex namafile.ext</code></p></blockquote>
<p>Gantilah ekstensi .ext sesuai dengan skrip yang digunakan, misalnya<em> .htm(l)</em> maupun <em>.php</em>.<br/>
Kita juga bisa menentukan sekaligus beberapa nama file yang akan menjadi index dengan menuliskannya secara berurutan dalam satu baris dan dipisahkan dengan spasi. <span id="more-10"></span></p>
<blockquote><p><code>DirectoryIndex namafile1.ext namafile2.ext namafile3.ext</code></p></blockquote>
<p>Dimana server akan membacanya secara berurutan, maksudnya<br/>
jika file <em>namafile1.ext</em> tidak ditemukan maka yang akan menjadi index adalah <em>namafile2.ext</em> dan seterusnya.</p>
