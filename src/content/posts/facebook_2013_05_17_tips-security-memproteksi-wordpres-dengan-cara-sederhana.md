---
title: "Tips Security - Memproteksi WordPres dengan Cara Sederhana"
date: "2013-05-17T11:01:00Z"
categories: ["WordPress"]
tags: ["facebook", "wordpress", "plugin", "theme"]
slug: "2013/05/17/tips-security-memproteksi-wordpres-dengan-cara-sederhana"
legacyUrl: "/2013/05/17/tips-security-memproteksi-wordpres-dengan-cara-sederhana/"
source: "facebook.com"
author: "Wak Jek"
comments: [{"author": "Uchan Utchanovsky", "date": "Friday 17 May 2013 at 11:04", "text": "ane cobain yah gan xD"}, {"author": "Wak Jek", "date": "Friday 17 May 2013 at 11:05", "text": "oke, ntar kasi tau URL nya biar ane coba work atau gk. hehe"}, {"author": "Fitrah Ajah", "date": "Friday 17 May 2013 at 11:09", "text": "ntu bener kk., ko kayanya ada yg kurang ya... logika if $secret == 'something' ga ada ya.. :bingung"}, {"author": "Fitrah Ajah", "date": "Friday 17 May 2013 at 11:10", "text": "ato if $_get['secret']==$secret_key CMIIW"}, {"author": "Wak Jek", "date": "Friday 17 May 2013 at 11:10", "text": "coba aja dulu. :D"}, {"author": "Wak Jek", "date": "Friday 17 May 2013 at 11:11", "text": "Fitrah Ajah,  kyk gitu bisa juga,\ntapi cara aksesnya ntar wp-login.php?secret=something"}, {"author": "Ferry Fernando", "date": "Friday 17 May 2013 at 11:12", "text": "(y)"}, {"author": "Fitrah Ajah", "date": "Friday 17 May 2013 at 11:13", "text": "ooo ic ic ane baru tau klo ?something ntu bisa dijadiin parameter jadi lebih simpel ya., klo tadi ane nangkepnya jadi get aja ?secret=something (y)"}, {"author": "Wak Jek", "date": "Friday 17 May 2013 at 11:24", "text": "udah diupdate docs nya, ada bbrp tambahan hehe"}, {"author": "Muh Mahaja Yuliart", "date": "Monday 3 June 2013 at 09:13", "text": "wahh sangatt membantuu cobaa dulu WP ane abiss kenak Devicee aselole"}, {"author": "Wira AlFine", "date": "Wednesday 5 June 2013 at 21:58", "text": ":: mantap nih, tengkyu banyak gan, saya udah coba yg .htaccess,,,"}, {"author": "Ari Setiawan Abimanyu", "date": "Monday 10 June 2013 at 11:43", "text": "okeh. ntar klo dah jadi prakteknya"}, {"author": "Fitrah Ajah", "date": "Tuesday 11 June 2013 at 00:39", "text": "iyeu mang Aris Kapisa"}, {"author": "Wak Jek", "date": "Monday 24 June 2013 at 12:47", "text": "Bs jg sih oom Abah Sidi,\ntapi hanya berlaku untuk apache, klo nginx gmn?"}, {"author": "Achmad Tantowi", "date": "Tuesday 2 July 2013 at 21:30", "text": "untuk cara nomor 1 itu scriptnya d taro mana ya?  # masih pemula"}, {"author": "Wak Jek", "date": "Tuesday 2 July 2013 at 22:17", "text": "di functions.php di theme nya.\n\nbtw code no #1 udah ane revisi, sekarang pake action 'init', bukan 'login_head'"}, {"author": "Semut Saurus", "date": "Friday 5 July 2013 at 16:41", "text": "ada versi wp 3.5.2 yang baru http://wordpress.org/download/release-archive/ gimana kira-kira bang"}, {"author": "Lukman Hakim", "date": "Sunday 22 March 2015 at 11:42", "text": "wahh sip juga ini.. bisa dipraktekkan... tapi, security tidak akan bisa 100% aman,"}, {"author": "Wak Jek", "date": "Sunday 22 March 2015 at 11:47", "text": "ya, emang gk ada kok yang 100% aman :D"}, {"author": "Lukman Hakim", "date": "Sunday 22 March 2015 at 11:48", "text": "karena kesempurnaan milik Tuhan :D hehee"}]
---

<p>Tips Security - Memproteksi WordPres dengan Cara Sederhana</p>

<p>Berikut ini ada beberapa cara untuk meningkatkan keamanan website berbasis WordPress anda.</p>

<p>=================================<br/>
1. Memproteksi Login Page dengan Secret Key<br/>
=================================</p>

<p>Caranya dengan menambahkan query tertentu ke URL wp-login.php, jika query tersebut tidak ditambahkan ketika mengakses wp-login, maka otomatis akan redirect kembali ke home.</p>

<p>Contoh berikut kita menambahkan secret key 'something'</p>

<p>add_action('init','login_protection');</p>

<p>function login_protection () {<br/>
$secret_key = 'something';</p>

<p>if($_SERVER['PHP_SELF'] == '/wp-login.php')<br/>
if(!isset($_GET[$secret_key])) {<br/>
wp_redirect(site_url());<br/>
}<br/>
}</p>

<p>Untuk mengakses login dengan cara http://websiteanda.com/wp-login.php?something</p>

<p>'something' ini bisa apa aja, asal jangan diberitahu ke siapapun. hehe.</p>

<p>===============================<br/>
2. Mencegah directory listing (Apache only)<br/>
===============================</p>

<p>Apache secara default menampilkan isi folder jika di folder tersebut tidak ada index.php atau index.html</p>

<p>Daripada anda harus membuat index.html di setiap folder, sebaiknya pake .htacces aja.</p>

<p>bikin file .htaccess di direktori wp-contents, isinya:</p>

<p>Options -Indexes</p>

<p>Dengan membuat .htaccess tersebut, secara otomatis maka direktori listing di folder upload, plugin, themes dan semua folder di bawah wp-contents tidak akan terindex.</p>

<p>NB: Jika setelah memasang .htacess ini file2 wp-contents tidak bisa diakses atau, error 500, berarti server anda tidak memperbolehkan mengganti option -indexes. sebaiknya hapus aja .htaccess tersebut.</p>

<p>Jika pake webserver Nginx, tidak perlu trik ini karena secara default nginx tidak menampilkan direktori listing.</p>

<p>====================================<br/>
3. Mencegah file template /plugin diakses langsung<br/>
====================================</p>

<p>Coba akses langsung salah satu file theme Anda. misalnya<br/>
http://example.com/wp-content/themes/mytheme/index.php</p>

<p>Biasanya akan muncul error seperti ini.</p>

<p>Fatal error:  Call to undefined function get_header() in /username/public_html/wp-content/themes/mytheme/index.php on line 1</p>

<p>Wow, berarti username cpanel Anda akan kelihatan, dan bisa saja disalahgunakan orang lain.</p>

<p>Solusi:<br/>
Ketika membuat theme/plugin, sebaiknya disetiap awal file tambahkan</p>

<p>defined('ABSPATH') or die();<br/>
?></p>

<p>Dengan begitu file2 theme tidak bisa diakses langsung.</p>

<p>---------------<br/>
Disclaimer: Tidak ada jaminan bahwa cara ini dapat mengamankan website Anda 100%.</p>
