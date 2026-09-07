---
title: "Gagal Upgrade Wordpress 2.7.1? Ini Solusinya"
date: "2008-05-01T12:00:00Z"
categories: ["WordPress"]
tags: []
slug: "2008/05/01/gagal-upgrade-wordpress-271-ini-solusinya"
legacyUrl: "/gagal-upgrade-wordpress-271-ini-solusinya/"
source: "blog.situskamu.com"
comments: [
  {
    "author": "Anonymous",
    "date": "Feb 19, 09 at 4:00 am",
    "text": "Wahhh… ãñÐrî malah blm [merasa perlu] update ke 2.7.1, salah satunya karena alasan discspace yang dah mau limit, hiks   ikutan nangis.\n\nAlasan lain, karena selama ini blm [terasa] terganggu dengan 68 ticket yang telah diperbaiki di wp paling gress ini *udah ditune up dikit-dikit lahhh, hohoohoooo \n\nSalam kenal…\n\nNice post, keep share & CU Arround :mrgreen:"
  },
  {
    "author": "Anonymous",
    "date": "Apr 6, 09 at 7:11 pm",
    "text": "blm upgrade2 msh setia ama 2.7"
  },
  {
    "author": "Anonymous",
    "date": "Apr 12, 09 at 11:57 pm",
    "text": "wah… untungnya saya udah langsung pake wordpress 2.7.1 walaupun untuk subdomainnya nya.\n\ntapi keren abis kok…."
  }
]
---

<p>Setelah dulunya sempat bersenang-senang dengan sebuah plugin wordpress yang mantab abis,<a href="/wordpress-automatic-upgrade-otomatis-jadi-version-25/"> Upgrade Wordpress Automatically</a>, ternyata hal itu tidak terjadi lagi sekarang. Why? Ketika login ke dashboard situs ini, ada notifikasi bahwa telah tersedia versi wordpress yang terbaru dan dianjurkan untuk melakukan upgrade. <span id="more-167"></span></p>
<figure class="image-missing-placeholder" role="img" aria-label="wordpress 2.7.1 upgrade">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">wordpress 2.7.1 upgrade</span>
  </div>
</figure>
<p>Setelah mengeklik link Please upgrade now, wordpress memberikan dua pilihan, mengupgrade wordpress secara otomatis dan mendownload file wordpress dan mengupgrade secara manual. Hari gini upgrade manual? Sorry lah yaw&#8230; 😉 </p>
<p>Ok, ternyata wordpress 2.7 dengan baik hati telah menambahkan fitur upgrade otomatis secara default. Dan tentu saja saya memilih opsi yang pertama, upgrade otomatis.</p>
<figure class="image-missing-placeholder" role="img" aria-label="wordpress 2.7.1 upgrade">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">wordpress 2.7.1 upgrade</span>
  </div>
</figure>
<p>Namun, oops&#8230; sepertinya ada sesuatu yang tidak beres di sini.</p>
<figure class="image-missing-placeholder" role="img" aria-label="wordpress 2.7.1 upgrade">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">wordpress 2.7.1 upgrade</span>
  </div>
</figure>
<p>Setelah pada proses <em>Unpacking the core update</em>, kemudian tidak terjadi apa-apa, ketika halaman di refresh, ternyata wordpress tidak terupgrade. Wah&#8230; <figure class="image-missing-placeholder" role="img" aria-label=";-(">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">;-(</span>
  </div>
</figure> nangis dulu bentar</p>
<p>Kemudian teringat suatu pepatah, &#8220;menemui masalah, ingatlah mbah <a href="http://web.archive.org/web/20090420125224/http://google.com/">Google</a>&#8220;. Benar saja, saya menemukan blog yang memberikan solusi untuk <a href="http://web.archive.org/web/20090420125224/http://bassmadrigal.com/blog/2009/02/11/wordpress-271-upgrade-failed/">upgrade Wordpress 2.7.1 yang gagal</a> yaitu dengan menambahkan baris <strong>AddType x-mapp-php5 .php</strong> di file htaccess. Dan ternyata solusi tersebut tidak lah manjur, halaman upgrade malah menampilkan kode-kode aneh. Hehehe.</p>
<p>Kecurigaan saya yaitu kepada plugin<a href="/wordpress-automatic-upgrade-otomatis-jadi-version-25/"> Wordpress Automatic Upgrade</a> seperti yang sudah pernah saya bahas sebelumnya. Beberapa komentar di blog tersebut juga menyebutkan bahwa plugin tersebut tidak lagi kompatibel dengan wordpress sejak versi 2.7. Ketika mencoba mengupgrade menggunakan plugin ini, malah mengatakan bahwa Wordpress nya uptodate alias tidak perlu diupgrade. 😀 </p>
<figure class="image-missing-placeholder" role="img" aria-label="wordpress 2.7.1 upgrade">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">wordpress 2.7.1 upgrade</span>
  </div>
</figure>
<p>Akhirnya saya memutuskan untuk mendisable plugin yang sebelumnya sudah cukup berjasa dalam proses upgrade wordpress tersebut. Dan mengulang proses automatis upgrade bawaan dari Wordpress.</p>
<figure class="image-missing-placeholder" role="img" aria-label="wordpress 2.7.1 upgrade">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">wordpress 2.7.1 upgrade</span>
  </div>
</figure>
<p>Wow ternyata berhasil 🙂 </p>
<figure class="image-missing-placeholder" role="img" aria-label="wordpress 2.7.1 upgrade">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">wordpress 2.7.1 upgrade</span>
  </div>
</figure>
<p>Dan wordpress pun telah menjadi versi 2.7.1 <figure class="image-missing-placeholder" role="img" aria-label="(Y)">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">(Y)</span>
  </div>
</figure> <br/>
Selamat tinggal plugin Wordpress Automatic Upgrade, jasa-jasamu akan selalu kukenang <figure class="image-missing-placeholder" role="img" aria-label="(W)">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">(W)</span>
  </div>
</figure> </p>
