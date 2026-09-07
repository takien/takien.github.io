---
title: "Coba menggabungkan nodejs dengan apache, jadi file index.html dan app.js..."
date: "2012-05-11T22:57:00Z"
categories: ["Programming"]
tags: ["facebook", "Node.js Indonesia", "programming"]
slug: "2012/05/11/coba-menggabungkan-nodejs-dengan-apache-jadi-file-indexhtml"
legacyUrl: "/2012/05/11/coba-menggabungkan-nodejs-dengan-apache-jadi-file-indexhtml/"
source: "facebook.com"
author: "Wak Jek"
group: "Node.js Indonesia"
comments: [{"author": "Mohammad Naufal Fadil", "date": "Friday 11 May 2012 at 22:57", "text": "socket.io kan di port lain jadi ga masalah asal ga kbentur sama port 80"}, {"author": "Mohammad Naufal Fadil", "date": "Friday 11 May 2012 at 22:58", "text": "selain itu socket.io sekuritas nya masih kurang yah? atau bsa pake security lain. soalnya itu Cross site script jadi mau di pasang di web lain jg tetep terekesusi"}, {"author": "Wak Jek", "date": "Friday 11 May 2012 at 23:00", "text": "ia krn kyknya tadi ada yang nanya gmn klo digabungin sama apache. soal sekuriti ntar cari info lagi."}, {"author": "Wak Jek", "date": "Friday 11 May 2012 at 23:02", "text": "nemu nih authorizing *oket.io https://github.com/LearnBoost/socket.io/wiki/Authorizing"}, {"author": "Saifullah", "date": "Saturday 12 May 2012 at 01:11", "text": "ane dah coba pake html aja, trus ane linkkan ke server nodejs, bisa jalan.."}]
---

<p>coba menggabungkan nodejs dengan apache, jadi file index.html dan app.js nya saya letakkan di d:\wamp\www\nodejs (dimana ini adalah direktori apache), dan node js dijalankan dari situ dengan cara ketik "node app.js"<br/>
pada index.html arahkan script socket.io ke port nya node js yaitu localhost:8888 (lihat yang diborder merah). aplikasi dijalankan dari http://localhost/nodejs (apache).<br/>
gk tau apakah ini cara yang benar atau tidak atau mempengahuri performance atau tidak, yang jelas it works.<br/>
lihat gambar.</p>

<p><img src="/images/facebook/fb_new_29_0_50ae142c01.jpg" alt="Coba menggabungkan nodejs dengan apache, jadi file index.html dan app.js..." title="Coba menggabungkan nodejs dengan apache, jadi file index.html dan app.js..." class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>
