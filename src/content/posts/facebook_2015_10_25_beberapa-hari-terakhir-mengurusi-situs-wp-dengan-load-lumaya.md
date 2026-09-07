---
title: "Beberapa hari terakhir mengurusi situs WP dengan load lumayan (upto..."
date: "2015-10-25T12:00:00Z"
categories: ["WordPress"]
tags: ["facebook", "Belajar WordPress", "wordpress", "plugin"]
slug: "2015/10/25/beberapa-hari-terakhir-mengurusi-situs-wp-dengan-load-lumaya"
legacyUrl: "/2015/10/25/beberapa-hari-terakhir-mengurusi-situs-wp-dengan-load-lumaya/"
source: "facebook.com"
author: "Wak Jek"
group: "Belajar WordPress"
comments: [{"author": "Sandi Asa Wiguna", "date": "Sunday 25 October 2015 at 12:00", "text": "mastah"}, {"author": "Rudhi Maya", "date": "Sunday 25 October 2015 at 12:04", "text": "Gila lo dro..."}, {"author": "Wak Jek", "date": "Sunday 25 October 2015 at 12:05", "text": "dari sini jadi tau ternyata gk usah teriming2i dengan tawaran CDN, karena CDN itu hanya ngehost static file, hemat bandwidth = iya, hemat resource = tidak"}, {"author": "Ian Hehe Lubis", "date": "Sunday 25 October 2015 at 12:07", "text": "bro config nya di rubah dikit."}, {"author": "Abonk Farouk", "date": "Sunday 25 October 2015 at 12:08", "text": "idealnya memang gini untuk site bertrapik tinggi wak, harusnya pupns pake sistem ini deh, kalau mau lebih ok lagi, tambahin satu server lagi untuk image... makin ringan ituh"}, {"author": "Heri Hehe Setiawan", "date": "Sunday 25 October 2015 at 12:44", "text": "mastah, ajarin saya plis."}, {"author": "Wahyudi Hidayat", "date": "Sunday 25 October 2015 at 13:07", "text": "Web server nya pakai apa gan?"}, {"author": "Wak Jek", "date": "Sunday 25 October 2015 at 13:29", "text": "nah karena static masih ada di host lama (vps 3GB / server 2) maka akan ane pindahin ke server 3 (1GB saja /testing).\nmaka ane bikin 1 server lagi (server 3) dengan memasang script yang sama.\nkemudian domain akan saya arahkan ke server 3.\nclient yang masih proses propagasi domain tidak akan kehilangan moment karena server 2 masih ada dan masih menyediakan konten yang sama"}, {"author": "Abdul Latif Syafi'i", "date": "Sunday 25 October 2015 at 13:33", "text": "bikin static html nya pake apa gan?"}, {"author": "Jeffry Gunawan", "date": "Sunday 25 October 2015 at 13:48", "text": "Wp d server A, html static d server B. Pake w3 total cache bisa mindahin cache ke server lain ya?"}, {"author": "Marda Faqruradi", "date": "Sunday 25 October 2015 at 13:58", "text": "plugin w3tc emank terkenal plugin plg tidak direkomendasi. Uda saya test tapi mlhn hasilnya lbh parah mengakibatkan beberapa plugin lain tdk bs bekerja"}, {"author": "Timothy Leviano Mangapul Malau", "date": "Sunday 25 October 2015 at 15:20", "text": "tutorialnya dong om"}, {"author": "Ar", "date": "Sunday 25 October 2015 at 18:28", "text": "up up nggu tutor"}, {"author": "Javanesse Acinonyx Jubatus", "date": "Sunday 25 October 2015 at 20:05", "text": "nah ini ni.... ane masih belum paham gimana caranya ngambil cache dri server lain. mohon bantuannya ya gan, buat faktor keamanan juga sih...makasih wak jek"}, {"author": "Fajar Setiawan Siagian", "date": "Sunday 25 October 2015 at 20:34", "text": "busyeet server nya dipisah bah"}, {"author": "Rizqy Hidayat", "date": "Sunday 25 October 2015 at 21:22", "text": "ditunggu tutorialnya mas.  kalo sy sering baca\" di do sih hehe https://www.digitalocean.com/.../horizontally-scaling.../"}, {"author": "Jeffri Tjin", "date": "Sunday 25 October 2015 at 22:01", "text": "CDN yah tujuannya bukan meminimalisir load server, tapi untuk improve latency buat visitor biar load di visitor lebih cepat."}, {"author": "Wak Jek", "date": "Saturday 31 October 2015 at 15:10", "text": "nih gan statistik resource nya Ian Mustafa,\npage views minimal 40ribuan"}, {"author": "Agus Suhartono", "date": "Monday 2 November 2015 at 01:28", "text": "dahsyad nih\ngenerate STATIC nya pakai apa Om Wak Jek  ?"}]
---

<p>Beberapa hari terakhir mengurusi situs WP dengan load lumayan (upto 1000-2000 realtime views di Google Analytics).</p>

<p>- Pake shared hosting jelas gk bisa<br/>
- W3 Total Cache tidak banyak membantu<br/>
- Upgrade ke VPS RAM 3GB + W3 Total Cache, tumbang juga<br/>
- VPS + W3 Total Cache + CDN (Max CDN), tumbang juga<br/>
- Udah order VPS RAM 8GB, tapi tiba2 dapat ide lama yang bersemi kembali, yaitu memisahkan antara database dan homepage menjadi 2 server yang berbeda.</p>

<p>Akhirnya cara terakhir yang dipake, WP diinstal di VPS RAM 1GB saja, sementara output HTML static di VPS segitu juga (di server dan provider lain).<br/>
hasilnya lancar jaya</p>

<p>Untuk cara terakhir plugin W3 Total Cache/CDN sama sekali tidak perlu lagi, dan bisa dihapus saja.</p>

<p>Kelebihan cara ini uptime jadi lebih terjamin, bahkan ketika WP mengalami error / maintenance, visitor tetap dapat membuka website.</p>

<p>Tapi ini juga masih tahap testing apakah lancar seterusnya dan masih dicari bug di script nya.</p>

<p><img src="/images/facebook/fb_27_0_4cb9a5c5f6.jpg" alt="Beberapa hari terakhir mengurusi situs WP dengan load lumayan (upto..." title="Beberapa hari terakhir mengurusi situs WP dengan load lumayan (upto..." class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>

<p><img src="/images/facebook/fb_27_1_becfcfae04.jpg" alt="Beberapa hari terakhir mengurusi situs WP dengan load lumayan (upto..." title="Beberapa hari terakhir mengurusi situs WP dengan load lumayan (upto..." class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>
