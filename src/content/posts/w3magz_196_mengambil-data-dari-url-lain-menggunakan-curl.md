---
title: "Mengambil Data dari URL Lain Menggunakan cURL"
date: "2010-12-18T11:45:51+00:00"
categories: ["PHP"]
tags: []
slug: "2010/12/18/mengambil-data-dari-url-lain-menggunakan-curl"
legacyUrls: ["196/mengambil-data-dari-url-lain-menggunakan-curl.html", "196/mengambil-data-dari-url-lain-menggunakan-curl", "w3magz/196/mengambil-data-dari-url-lain-menggunakan-curl.html", "w3magz/196/mengambil-data-dari-url-lain-menggunakan-curl"]
source: "w3magz.com"
author: "Wak Jek"
comments: [{"author": "rawiz", "date": "", "text": "pertamax.. \n mangstab… ditunggu part berikutnya…   \nrikues, studi kasus sederhana, mengambil info kurs terkini dari website2 perbankan.. :ngacir:"}, {"author": "ianlubis", "date": "", "text": "Saya tambahkan untuk installasi curl pada APPSERV \n Pertama, masuk ke folder appserv di install C:AppServphp5 \nlalu cari file : \n    * ssleay32.dll \n    * libeay32.dll \n Setelah itu copy kedua file tersebut ke directory C:windowssystem32 \nLalu buka PHP.INI melalui start > program > appserv > configuration server > PHP edit the php.ini Configuration File \nlalu cari tulisan ;from extension=php_curl.dll hapus tanda titik koma setelah itu restart komputer anda"}, {"author": "Tegarmaji", "date": "", "text": "klo yg dari om ianlubis ini jd artikel baru, \nberarti artikel om takien jd part 2. \npart 1nya skalian diisi lengkap cara instalasinya"}, {"author": "ianlubis", "date": "", "text": "Oh…. tidak bisa….. artikel om Takien adalah part 1, saya cuma menambahkan ajah kok… kebetulan saya tau dikit…."}, {"author": "dieka2501", "date": "", "text": "kerennn,,,,, walah,,, ane jadi bisa balajar bnyak inih.."}, {"author": "FeRRi", "date": "", "text": "mantaabb bgt om    \n lengkap ada xampp ama wamp lg"}, {"author": "abonk", "date": "", "text": "mantap ini mah hehe, tak cobain ngecurl takien.com bisa ga ya hehe"}, {"author": "Bintangweb", "date": "", "text": "Dari dulu belajar curl gak ngerti-ngerti. \nUntung ada artikel bro takien.   \nJadi semangat belajar lagi."}, {"author": "heru", "date": "", "text": "sebelum tahu curl,, saya sering menggunakan iframe,,"}, {"author": "tian", "date": "", "text": "wah keren tutorialnya, \nterima kasih"}, {"author": "Jeff Hadianto", "date": "", "text": "mas kalau menampilkan file gambar dengan cURL gmana ya?"}]
---

<p><strong>Penggunaan cURL di PHP <em>(bagian 1)</em></strong></p>
<p>Secara umum, <em>cURL</em> adalah perangkat lunak yang digunakan untuk mentransfer data dari dan ke server. Sebenarnya ada banyak perangkat transfer data layaknya cURL, namun cURL memiliki fitur yang lebih lengkap diantara perangkat-perangkat lainnya. Diantaranya dukungan terhadap HTTP, FTP, SFTP, SOCKS, TFTP, IMAP, POP3, SMTP  dan lain-lain.</p>
<p>Agar dapat menggunakan cURL pada pemrograman PHP, kita harus menginstal ekstensi libcurl. Tapi tidak usah panik, karena biasanya cURL ini sudah terinstal pada sebagian besar webhosting yang support PHP maupun pada paket instalasi WAMP (Windows Apache MySQL, PHP) seperti Wampserver, XAMPP, PHPThriad dan sebagainya.</p>
<p>Untuk memastikan apakah ekstensi cURL sudah terinstal di PHP, ketikkan perintah berikut di file PHP dan preview di browser Anda.</p>

```php
<?php

echo 'cURL '.(function_exists('curl_init') ? ' sudah' : ' tidak').'  terinstal';

?>
```

<p>Jika hasil outputnya adalah “cURL sudah terinstal” maka Anda sudah dapat menggunakan cURL, namun jika hasilnya adalah “cURL tidak terinstal” berarti cURL belum diinstal atau belum diaktifkan.</p>
<p><strong>Mengaktifkan cURL di Localhost</strong></p>
<ol>
<li>Bukalah 	file <strong>php.ini</strong> menggunakan notepad atau text editor Anda. File php.ini dapat 	ditemukan di folder instalasi sever lokal Anda, biasanya di folder 	<strong>C:xamppbinphpphp.ini </strong>(xampp) 	atau di <strong>C:wampbinphpphp.x.xphp.ini</strong> (wampserver, x.x adalah versi PHP yang digunakan)</li>
<li>Setelah 	file php.ini terbuka, carilah baris ;<strong>extension=php_curl.dll</strong> dan hapuslah tanda titik koma (;) di depan baris tersebut, sehingga 	menjadi <em>extension=php_curl.dll</em></li>
<li>Restart Apache dan lakukan pengecekan lagi seperti di atas.</li>
</ol>
<p>Tips: <em>Pada wampserver anda dapat dengan mudah mengaktifkan cURL tanpa harus mengedit file php.ini, yakni dengan cara klik icon wampserver di systray, pilih menu PHP =&gt; PHP extension =&gt; php_curl. Pastikan menu php_curl di ceklist.</em></p>
<p><strong>Fungsi-fungsi cURL</strong></p>
<p>Sebelum memulai penggunaan cURL, ada baiknya memahami fungsi-fungsi dasar dari cURL yang umum digunakan. Fungsi-fungsi tersebut diantaranya:</p>
<ul>
<li><em>curl_init</em> = memulai sesi cURL</li>
<li><em>curl_setopt 		=</em> menentukan opsi-opsi sebelum menjalankan cURL.</li>
<li><em>curl_exec 		= </em>menjalankaan 	cURL.</li>
<li><em>curl_close 		= </em>menutup 	sesi cURL.</li>
</ul>
<p><strong>Menggunakan cURL untuk Mengambil Data</strong></p>
<p>Setelah mengaktifkan cURL di PHP dan mengetahui beberapa fungsi-fungsi cURL, sekarang kita coba menggunakan fasilitas cURL yang paling sederhana, yaitu mengambil data dari URL.  Langkah-langkahnya adalah sebagai berikut:</p>
<p><strong>1. </strong>Buatlah 	sebuah file PHP di localhost, beri nama dengan <strong>data.php,</strong> isinya sebagai berikut:</p>

```php
<?php

echo "Ini adalah data di file data.php";

?>
```

<p>Pastikan file tersebut dapat diakses dari <span style="color: #000080;"><span style="text-decoration: underline;">http://localhost/test/curl/data.php</span></span><em><strong> </strong></em>(nama folder sesuaikan dengan keinginan).  Lihat gambar berikut:</p>
<figure class="image-missing-placeholder" role="img" aria-label="gambar1">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">gambar1</span>
  </div>
</figure>
<p><strong>2. </strong>Kemudian 	buatlah file <strong>latihan-curl-1.php</strong> dimana kita akan memasukkan fungsi curl di sini.Isinya 	sebagai berikut:</p>

```php
<?php

$ch = curl_init();

curl_setopt($ch,CURLOPT_URL,'http://localhost/test/curl/data.php');

curl_exec($ch);

curl_close($ch);

?>
```

<p>Penjelasan:</p>
<p>[php firstline="2"]$ch = curl_init();[/php]</p>
<ul>
<li>Memulai 	sesi cURL, untuk memulai sesi cURL dengan menggunakan fungsi 	<strong>curl_init()</strong> dan 	menyimpannya pada variabel $ch.</li>
</ul>
<p>[php firstline="2"]<br/>
$ch = curl_init();<br/>
curl_setopt($ch,CURLOPT_URL,&#8217;http://localhost/test/curl/data.php&#8217;);[/php]</p>
<ul>
<li>Menentukan 	opsi curl, untuk menentukan opsi gunakan fungsi <strong>curl_setopt()</strong></li>
<li>$ch adalah resource dari 	curl_init() yang kita simpan sebelumnya.</li>
<li>CURLOPT_URL, adalah opsi untuk 	menentukan URL yang akan diambil datanya.</li>
<li><span style="font-family: Courier New,monospace;">http://localhost/test/curl/data.php</span> adalah URL dari website yang akan diambil datanya.</li>
</ul>
<p>[php firstline="4"]curl_exec($ch);[/php]</p>
<ul>
<li>Mengeksekusi 	cURL  dengan curl_exec() dan menampilkannya ke browser..</li>
</ul>
<p>[php firstline="5"]curl_close($ch);[/php]</p>
<ul>
<li>Menutup sesi cURL dengan curl_close($ch))</li>
</ul>
<p><strong>3. </strong>Sekarang 	saatnya melihat hasil cURL nya dengan megarahkan browse ke URL 	<em>http://localhost/test/curl/latihan-curl-1.php. </em>Lihat gambar berikut:</p>
<figure class="image-missing-placeholder" role="img" aria-label="gambar2">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">gambar2</span>
  </div>
</figure>
<p>Nah, hasil output dari file 	<em>latihan-curl-1.php</em> adalah sama persis dengan hasil output 	dari file <em>data.php. </em>Berarti 	kita berhasil mengambil data dari URL 	<em>http://localhost/test/curl/data.php</em> menggunakan cURL.</p>
<p>Sekian dulu bahasan kita kali ini tentang dasar-dasar penggunaan cURL di php. Dengan menggunakan cURL kita dapat mengambil data dari URL lain dan menampilkannya di PHP.</p>
<p>Sebenarnya data yang dapat diambil tidak terbatas pada data pada domain yang sama, tapi bisa juga untuk mengambil data dari URL/domain lain di internet. Namun hal tersebut akan kita bahas pada artikel di edisi mendatang. <em>(takien@w3magz.com)</em></p>
<p><em>Bersambung&#8230;<br/>
</em></p>
<p><strong>Referensi:</strong></p>
<p>http://curl.haxx.se</p>
<p>http://php.net/manual/en/book.curl.php</p>

