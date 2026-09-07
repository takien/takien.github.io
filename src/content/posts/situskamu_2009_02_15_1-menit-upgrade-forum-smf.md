---
title: "<1 Menit Upgrade Forum SMF"
date: "2009-02-15T12:00:00Z"
categories: ["CMS", "SMF", "website"]
tags: ["2007", "2008", "blog", "blogger", "Browser", "cara menginstall wordpress", "cari duit", "city", "css", "custom block", "custom region", "div", "domain", "domain parking", "Drupal", "drupal theme", "forum", "Google", "htaccess", "html", "integration", "Internet", "Internet Explorer", "kaleidoskop", "kilas balik", "layout", "mini city", "mod rewrite", "parked domain", "review", "security", "SEO", "SMF", "Spyware", "table", "tutorial wordpress", "upgrade wordpress", "Web 2.0", "Webdesign", "website", "WordPress", "wordpress plugin", "Wordpress theme", "wordpress upgrade", "xampp"]
slug: "2009/02/15/1-menit-upgrade-forum-smf"
legacyUrl: "/1-menit-upgrade-forum-smf/"
source: "blog.situskamu.com"
comments: [
  {
    "author": "Anonymous",
    "date": "Jun 10, 08 at 11:29 am",
    "text": "klo bikin portal si SMF gimana ya?? sekalian tutorialnya dong  \n\nnamakamu reply on June 11th, 2008:\n\nPakai tinyportal bro, http://tinyportal.net\n\njust install and go."
  }
]
---

<figure class="image-missing-placeholder" role="img" aria-label="smf">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">smf</span>
  </div>
</figure>Dari sekian cara upgrade <a href="/category/cms/">CMS</a> kuposting sebelumnya, baik <a href="/mengupdate-drupal-caraku/">Drupal</a> maupun <a href="/upgrade-wordpress-bukan-hal-yang-menakutkan/">Wordpress</a> (pake <a href="/wordpress-automatic-upgrade-otomatis-jadi-version-25/">automatic upgrade</a> sekalipun) adalah upgrade SMF yang menurutku paling mudah. Selain itu juga cepat, gak ada istilah download, upload apalagi login FTP segala. <span id="more-127"></span></p>
<p>1. Langkah pertama, aktifkan Maintenance Mode, terutama kalau forumnya sudah ramai dan selalu user online. Tujuannya untuk menghindari kemungkinan-kemungkinan tertentu yang bisa terjadi ketika proses upgrade dikarenakan adanya member yang sedang melakukan posting dan sebagainya. Caranya Masuk ke Admin, pilih Server Settings. Berikan centang pada Maintenance Mode, pesan maintenance bisa diganti sesuka nya.</p>
<p><span style="color: #ffffff;">.</span><br/>
<figure class="image-missing-placeholder" role="img" aria-label="001-300x236.png">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">001-300x236.png</span>
  </div>
</figure>
<p><span style="color: #ffffff;">.</span></p>
<p>2. Masih di halaman Admin, klik menu Packages di sebelah kiri. Di halaman kanan akan ada peringatan bahwa forum mesti diupgrade untuk alasan keamanan dan sebagainya. klik Instal This Patch.</p>
<p><span style="color: #ffffff;">.</span><br/>
<figure class="image-missing-placeholder" role="img" aria-label="002-300x101.png">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">002-300x101.png</span>
  </div>
</figure></p>
<p><span style="color: #ffffff;">.</span></p>
<p>3. SMF akan mengecek file-file yang berubah ketika proses upgrade, pastikan semua file kondisinya Test Successfull. Jika ada yang failed, perhatikan chmod file yang bersangkutan. Setelah semua dipastikan successfull, klik Install Now dan proses upgrade akan dimulai.</p>
<p><span style="color: #ffffff;">.</span><br/>
<figure class="image-missing-placeholder" role="img" aria-label="003-276x300.png">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">003-276x300.png</span>
  </div>
</figure></p>
<p><span style="color: #ffffff;">.</span></p>
<p>4. Selesai coba refresh halaman dan lihat bagian footer, versi SMF sudah berganti dengan yang terbaru. Jangan lupa, non aktifkan lagi Maintenance Mode di Servers Settings.</p>
<p><span style="color: #ffffff;">.</span><br/>
<figure class="image-missing-placeholder" role="img" aria-label="005-300x36.png">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">005-300x36.png</span>
  </div>
</figure></p>
<p>NB:</p>
<p><em>Biasanya ini hanya berlaku untuk upgrade kecil, untuk upgrade besar-besaran misalnya dari smf 1.x.x ke 2.0 kemungkinan caranya berbeda.</em></p>
