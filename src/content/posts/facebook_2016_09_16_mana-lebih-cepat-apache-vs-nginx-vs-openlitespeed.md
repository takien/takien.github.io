---
title: "Mana lebih cepat? Apache vs Nginx vs OpenLiteSpeed?"
date: "2016-09-16T16:16:00Z"
categories: ["Programming"]
tags: ["facebook", "programming"]
slug: "2016/09/16/mana-lebih-cepat-apache-vs-nginx-vs-openlitespeed"
legacyUrl: "/2016/09/16/mana-lebih-cepat-apache-vs-nginx-vs-openlitespeed/"
source: "facebook.com"
author: "Wak Jek"
comments: [{"author": "Aris Presley", "date": "Friday 16 September 2016 at 16:16", "text": "ijin parker wak"}, {"author": "Rifqi Habibi", "date": "Friday 16 September 2016 at 16:24", "text": "nunggu tutornya pak"}, {"author": "Omarseda", "date": "Friday 16 September 2016 at 16:38", "text": "ulik thread/process ... dan oknum2nya: prefork worker eventloop maka akan tau #mudah2an kenapa yg satu lebih cepet dri yg lain.. tapi lebih cepetpun dlm kondisi trtntu malah lambat.. kenapa suka ada 404 dri server nginx... kenapa apache ga kuat handel 100000 koneksi simultan .. apa bedanya sama cgi/fastcgi .. nanti bakal ... ooooh... gitu ya  #kaboooorr"}, {"author": "Omarseda", "date": "Friday 16 September 2016 at 16:40", "text": "kenapa haproxy ga diajakin... dan openresty...  openresty cepet loh ..."}, {"author": "Aris Presley", "date": "Friday 16 September 2016 at 16:41", "text": "openresty stabil ?"}, {"author": "Wak Jek", "date": "Friday 16 September 2016 at 17:02", "text": "HHVM udah coba blom oom Omarseda,\nane baru instaled dan working aja, blom tau gmn gmn gmn kedepannya"}, {"author": "Dodi San", "date": "Friday 16 September 2016 at 17:06", "text": "pasang tenda hhvm nya om heee"}, {"author": "Ojo Terlalu Dipikir", "date": "Friday 16 September 2016 at 17:06", "text": "HHVM kalah cepet sama PHP7 wak"}, {"author": "Omarseda", "date": "Friday 16 September 2016 at 17:19", "text": "dan.... IIS ...  kenapa iis ga diajakin..  #tidakSopanIISgaDiajak"}, {"author": "Ronald Simanjuntak", "date": "Friday 16 September 2016 at 17:25", "text": "lnyimak aja deh"}, {"author": "Adam", "date": "Friday 16 September 2016 at 17:35", "text": "Noffi Andian Mohammad Naufal Fadil light speed sampah"}, {"author": "Wak Jek", "date": "Friday 16 September 2016 at 17:56", "text": "bener juga Muhamad Surya Iksanudin"}, {"author": "Yayan S", "date": "Friday 16 September 2016 at 18:02", "text": "Puciinngg...  Pakai standard ajalah XAMPP. Kumplit"}, {"author": "Wak Jek", "date": "Friday 16 September 2016 at 18:09", "text": "ini cara enable php7 di HHVM\n/etc/hhvm/php.ini\ntambahin\nhhvm.php7.all = 1\nservice hhvm restart"}, {"author": "Restu Indera", "date": "Saturday 17 September 2016 at 06:50", "text": "Om, ijin comot gambar boleh gak"}, {"author": "Fajar Setiawan Siagian", "date": "Saturday 17 September 2016 at 08:09", "text": "tinggi bner om pengunaan HHVM + nginx"}, {"author": "Zae Makhrus", "date": "Saturday 17 September 2016 at 08:49", "text": "nging"}, {"author": "Ferri Sutanto", "date": "Wednesday 21 September 2016 at 13:57", "text": "Keren gannnn"}]
---

<p>Mana lebih cepat? Apache vs Nginx vs OpenLiteSpeed?</p>

<p>Yang paling cepat tentu Apache, tinggal beli shared hosting atau VPS dan install LAMP, cepat deh jadinya hehhee. #eh</p>

<p>Tapi kalau mau sedikit 'repot', bisa instal Nginx, gak repot-repot amat sih, bahkan di beberapa sisi lebih mudah Nginx daripada apache.</p>

<p>Dalam artikel yang akan saya sebutkan di bawah ini membandingkan performa antara konfigurasi:</p>

<p>- Apache 2.4 + mod_php<br/>
- Apache + mod_php + disable Apache modules<br/>
- Apache + mod_fcgid<br/>
- Apache + PHP-FPM<br/>
- Nginx + PHP-FPM<br/>
- Nginx + PHP-FPM + Opcache<br/>
- Apache + PHP-FPM + Opcache<br/>
- OpenLiteSpeed<br/>
- HHVM + Nginx</p>

<p>Dalam artikel tersebut dilakukan test performa request-per-second di masing-masing konfigurasi. Terlihat mereka menunjukkan hasil yang hampir sama, kecuali 3 konfigurasi terakhir. Dan yang paling signifikan adalah kombinasi HHVM + Nginx.</p>

<p>Buat yang belum tahu, HHVM adalah HipHop Virtual Machine (yang diinisialisasi oleh developer Facebook), sebuah opensource yang dibuat untuk menjalankan script PHP dan Hack Lang.</p>

<p>Sebenarnya HHVM secara default sudah membawa webservernya sendiri selayaknya Apache atau Nginx. Namun HHVM juga dapat dipakai sebagai proxy saja untuk Nginx atau Apache.</p>

<p>Bahkan HHVM ada mode yang lebih makyos lagi untuk urusan performa yaitu Repo Authoritative, dimana PHP script dicompile dulu ke dalam repo dan kemudian dijalankan menerima user request. Tanpa harus mengcompile script-per-script secara on the fly.</p>

<p>Untuk HHVM Repo Authoritative saya belum coba sih, sepertinya menarik juga</p>

<p>Untuk yang belum tahu instalasi dan setup Nginx+HHVM, Insha Allah dalam waktu dekat akan kubuat tutorialnya.</p>

<p>https://www.conetix.com.au/.../apache-vs-nginx-vs...</p>

<p><img src="/images/facebook/fb_33_0_6fd5941746.jpg" alt="Mana lebih cepat? Apache vs Nginx vs OpenLiteSpeed?" title="Mana lebih cepat? Apache vs Nginx vs OpenLiteSpeed?" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>

<p><img src="/images/facebook/fb_33_1_ada72337a2.jpg" alt="Mana lebih cepat? Apache vs Nginx vs OpenLiteSpeed?" title="Mana lebih cepat? Apache vs Nginx vs OpenLiteSpeed?" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>
