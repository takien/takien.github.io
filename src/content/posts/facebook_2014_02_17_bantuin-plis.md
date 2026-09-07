---
title: "Bantuin plis"
date: "2014-02-17T11:00:00Z"
categories: ["WordPress"]
tags: ["facebook", "Belajar WordPress", "wordpress"]
slug: "2014/02/17/bantuin-plis"
legacyUrl: "/2014/02/17/bantuin-plis/"
source: "facebook.com"
author: "Wak Jek"
group: "Belajar WordPress"
comments: [{"author": "Heri Hehe Setiawan", "date": "Monday 17 February 2014 at 11:00", "text": "cache"}, {"author": "Wak Jek", "date": "Monday 17 February 2014 at 11:01", "text": "cache dari mana coy, w3total cache? wait"}, {"author": "Wak Jek", "date": "Monday 17 February 2014 at 11:04", "text": "problem not solved,\ncache nya kan gk pake disk, tapi pake X-cache,\njadi gak tau dimana cachenya"}, {"author": "Heri Hehe Setiawan", "date": "Monday 17 February 2014 at 11:09", "text": "coba searchnya case sensitive wp_unregister_GLOBALS *saran nubi*"}, {"author": "Wak Jek", "date": "Monday 17 February 2014 at 11:11", "text": "udah masvro, kyknya bukan kasus redeclared function biasa, misal fungsi itu udah di fix, tar fungsi lain yang eror, seterusnya.\n\nyang udah dilakukan:\n1. disable all theme\n2. disable all plugins\n3, replace semua wordpress core dengan file2 baru\n\nhasilnya tetep aja masih gitu heheh"}, {"author": "Heri Hehe Setiawan", "date": "Monday 17 February 2014 at 11:14", "text": "coba tidur."}, {"author": "Wak Jek", "date": "Monday 17 February 2014 at 11:16", "text": "hooh"}, {"author": "Wak Jek", "date": "Monday 17 February 2014 at 11:30", "text": "almot solved, masalhanay di server, bukan script maupun wpnya"}, {"author": "Bambang Catur Pamungkas", "date": "Monday 17 February 2014 at 11:38", "text": "memantau"}, {"author": "Aris Sandi", "date": "Monday 17 February 2014 at 11:41", "text": "debug dah aktif?"}, {"author": "Wak Jek", "date": "Monday 17 February 2014 at 11:49", "text": "aktif donk, klo gk aktif kan kaga tau errornya"}, {"author": "Wak Jek", "date": "Monday 17 February 2014 at 11:50", "text": "bukan, udah solved, masalahna di PHP-cgi, njinx"}, {"author": "Aris Sandi", "date": "Monday 17 February 2014 at 11:56", "text": "naon njinx?"}, {"author": "Saifullah", "date": "Monday 17 February 2014 at 20:22", "text": "masalahnya duplicate cache, mcache+php-apc..,"}]
---

<p>Bantuin plis</p>

<p>Fatal error: Cannot redeclare wp_unregister_globals() in /home/xxxx/public_html/wp-includes/load.php on line 17</p>

<p>kok bisa duplikat, oke ane cek fungsi yang sejenis, tidak ada<br/>
bahkan ane download seluruh file2 trus ane search di lokal, emang gk ada fungsi lain yang bernama wp_unregister_globals(),<br/>
kenapa kira2, dah lebih 1 jam blom nemu solusi</p>

<p><img src="/images/facebook/fb_17_0_9c01ad6003.jpg" alt="Bantuin plis" title="Bantuin plis" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>
