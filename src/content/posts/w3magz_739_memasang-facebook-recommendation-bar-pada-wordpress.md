---
title: "Memasang Facebook Recommendation Bar pada WordPress"
date: "2012-12-26T18:39:46+00:00"
categories: ["WordPress"]
tags: ["facebook", "seo"]
slug: "2012/12/26/memasang-facebook-recommendation-bar-pada-wordpress"
legacyUrls: ["739/memasang-facebook-recommendation-bar-pada-wordpress.html", "739/memasang-facebook-recommendation-bar-pada-wordpress", "w3magz/739/memasang-facebook-recommendation-bar-pada-wordpress.html", "w3magz/739/memasang-facebook-recommendation-bar-pada-wordpress"]
source: "w3magz.com"
author: "Wak Jek"
comments: []
---

<p><strong>Recommendation Bar</strong> atau bar rekomendasi adalah salah satu plugin Facebook untuk website yang memungkinkan pengguna untuk menyukai konten, mendapatkan rekomendasi, dan berbagi apa yang mereka baca dengan teman-teman mereka. Selain itu Recommendation Bar juga dapat meningkatkan page views (jumlah halaman yang dilihat).</p>
<div id="attachment_752" style="width: 429px" class="wp-caption aligncenter"><img src="/images/w3magz/00-recommendation-bar-sample.png" alt="Facebook Recommendation Bar" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><p class="wp-caption-text">Facebook Recommendation Bar</p></div>
<p>Recomendation Bar berbentuk kotak kecil yang biasanya terletak di sebelah kiri atau kanan bawah pada sebuah Website, yang berisi tautan yang direkomendasikan kepada pengguna atau pengunjung website. Recomendation Bar tidak serta merta muncul ketika halaman selesai di muat, akan tetapi muncul setelah periode waktu tertentu atau ketika pengguna menggulung halaman ke bawah. Hal ini bertujuan agar tidak menggangu, juga diasumsikan bahwa pengguna telah selesai membaca konten di halaman yang bersangkutan.</p>
<p>Jika Anda pengguna WordPress, memasang Recommendation Bar dapat dilakukan dengan mudah, berikut langkah-langkah nya:</p>
<ol>
<li>Install plugin Facebook untuk WordPress</li>
<li>Membuat aplikasi Facebook untuk mendapatkan kode App ID dan App Secret</li>
<li>Melakukan konfigurasi terhadap tampilan Recommendation Bar</li>
</ol>
<h2>1. Pasang plugin Facebook untuk WordPress</h2>
<p>Untuk memasang plugin Facebook di WordPress cukuplah mudah, caranya klik menu Plugin, kemudian Add New. Pada kotak pencarian ketik &#8220;Facebook&#8221; lalu klik &#8220;Search Plugin&#8221;.</p>
<figure class="image-missing-placeholder" role="img" aria-label="Pencarian plugin">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Pencarian plugin</span>
  </div>
</figure>
<p>Setelah muncul beberapa plugin yang berhubungan dengan Facebook, klik &#8220;Install Now&#8221; pada plugin dengan nama &#8220;Facebook&#8221;, biasanya terletak paling atas. Jika ada konfirmasi klik OK.</p>
<figure class="image-missing-placeholder" role="img" aria-label="Install Facebook plugin">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Install Facebook plugin</span>
  </div>
</figure>
<p>Tunggu beberapa saat ketika proses mengunduh plugin berlangsung, jika proses selesai akan ada tautan &#8220;Activate Plugin&#8221;, klik tautan tersebut untuk mengaktifkan plugin. Jika tidak ada masalah maka akan ada pemberitahuan &#8220;Plugin Activated&#8221; dan plugin sudah dapat digunakan. Pada daftar plugin pilih plugin Facebook dan klik &#8220;Setting&#8221; untuk menuju halaman pengaturan.</p>
<figure class="image-missing-placeholder" role="img" aria-label="Setting Facebook plugin">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Setting Facebook plugin</span>
  </div>
</figure>
<p style="text-align: left;">Pada halaman pengaturan plugin Facebook, terdapat dua kotak isian yakni App ID dan App Secret. Untuk mendapatkan App ID dan App Secret tersebut terlebih dahulu kita harus membuat sebuah Aplikasi Facebook.</p>
<h2>2. Membuat aplikasi Facebook untuk mendapatkan kode App ID dan App Secret</h2>
<p>Pada langkah pertama di atas kita sampai pada halaman kotak isian App ID dan App Secret, sementara abaikan kotak tersebut. Klik tautan &#8220;Create a new Facebook application or associate [namablog] with and existing Facebook application&#8221; untuk menuju halaman Facebook Developer.</p>
<figure class="image-missing-placeholder" role="img" aria-label="Plugin setting app ID">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Plugin setting app ID</span>
  </div>
</figure>
<p>Klik tombol &#8220;Create New App&#8221; pada kanan atas.</p>
<figure class="image-missing-placeholder" role="img" aria-label="Create Facebook Application">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Create Facebook Application</span>
  </div>
</figure>
<p>Pada kotak dialog yang muncul isikan App Name dengan nama aplikasi yang Anda inginkan, abaikan isian yang lainnya kemudian klik &#8220;Continue&#8221;.</p>
<figure class="image-missing-placeholder" role="img" aria-label="Facebook Application name">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Facebook Application name</span>
  </div>
</figure>
<p>Jika diminta mengisi kode keamanan, isikan sesuai dengan gambar yang muncul lalu klik Continue.</p>
<figure class="image-missing-placeholder" role="img" aria-label="Facebook Application captcha">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Facebook Application captcha</span>
  </div>
</figure>
<p>Akan muncul halaman konfigurasi app, abaikan kotak-kotak isian karena di sini App ID dan App Secret kita sudah berhasil di buat. Salin kedua nilai tersebut ke pengaturan plugin Facebook WordPress.</p>
<figure class="image-missing-placeholder" role="img" aria-label="Facebook Application App ID and App Secret">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Facebook Application App ID and App Secret</span>
  </div>
</figure>
<h2>3. Melakukan konfigurasi terhadap tampilan Recommendation Bar</h2>
<p>Setelah mendapat App ID dan App Secret seperti pada langkah ke 2 di atas, salin ke halaman pengaturan plugin Facebook di WordPress lalu klik Save Changes.</p>
<figure class="image-missing-placeholder" role="img" aria-label="Facebook Application App ID and App Secret">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Facebook Application App ID and App Secret</span>
  </div>
</figure>
<p>Perhatikan menu-menu di samping kiri, di bawah menu Facebook, di situ sudah terdapat menu baru bernama Recommendations Bar, klik tautan tersebut untuk menuju halaman pengaturan Recommendation Bar.<br/>
Lakukan pengaturan seperlunya, berikut penjelasan masing-masing opsi:</p>
<ul>
<li>Show on: menentukan dimana Recommendation Bar akan ditampilkan, contoh nya di post, page atau attachment.</li>
<li>Side: letak Recommendation Bar, kiri atau kanan.</li>
<li>Action: teks aksi yang akan ditampilkan pada tombol seperti Like atau Recommend</li>
<li>Trigger atau pemicu munculnya Recommendation Bar, di sini ada tiga pilihan yaitu:<br/>
* On visible: Recommendation bar akan muncul ketika halaman di muat.<br/>
* After a visitor scroll through x% of the total page height, Recommendation Bar akan ditampilkan ketika pengguna menggulung halaman sejauh x% dari total tinggi halaman.<br/>
* Manual, jika Anda ingin menampilkan Recommendation Bar secara manual menggunakan JavaScript.</li>
<li>Read time: Interval waktu dalam detik sebelum Recommendation bar akan membentang.</li>
<li>Number of recommendations: Jumlah maksimal tautan yang akan ditampilkan.</li>
<li>Maximum age: Maksimal umur artikel ( dalam hari ) yang akan dijadikan rekomendasi, isikan 0 jika ingin merekomendasikan semua artikel.</li>
</ul>
<figure class="image-missing-placeholder" role="img" aria-label="Facebook Recommendation Bar Setting">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Facebook Recommendation Bar Setting</span>
  </div>
</figure>
<p>Setelah pengaturan dikira cukup, kemudian klik Save Changes.<br/>
Buka salah satu artikel atau postingan blog Anda dan lihat hasilnya.<br/>
Selamat mencoba 😊 </p>
<p>NB: Untuk memasang Recommendation Bar pada website selain WordPress, dalam hal ini Facebook telah menyediakan script yang siap disalin, juga tersedia beberapa pengaturan. Selengkapnya dapat dilihat di http://developers.facebook.com/docs/reference/plugins/recommendationsbar/</p>

