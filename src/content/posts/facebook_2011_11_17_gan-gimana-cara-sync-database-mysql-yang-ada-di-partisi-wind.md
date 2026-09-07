---
title: "Gan gimana cara sync database mysql yang ada di partisi windows dengan..."
date: "2011-11-17T22:47:00Z"
categories: ["Programming"]
tags: ["facebook", "ME-Linux-AN", "programming"]
slug: "2011/11/17/gan-gimana-cara-sync-database-mysql-yang-ada-di-partisi-wind"
legacyUrl: "/2011/11/17/gan-gimana-cara-sync-database-mysql-yang-ada-di-partisi-wind/"
source: "facebook.com"
author: "Wak Jek"
group: "ME-Linux-AN"
comments: [{"author": "Putu Shinoda", "date": "Thursday 17 November 2011 at 22:47", "text": "di linux makek xampp ato lamp?"}, {"author": "Wak Jek", "date": "Thursday 17 November 2011 at 22:52", "text": "di windows pake wampserver,\ndi linux pake instal manual\nfolder www nya udah bisa sync, tinggal db nya.\nane pake cara ini :\nhttp://www.apachefriends.org/f/viewtopic.php?p=136633"}, {"author": "Wak Jek", "date": "Friday 18 November 2011 at 03:34", "text": "db nya udah bisa,\ncuma tables nya gk muncul, karena ownernya masih root gk bisa diset ke mysql.\ngmn ya."}, {"author": "Anggha Sanjaya", "date": "Friday 18 November 2011 at 11:53", "text": "Ane baru pernah denger.. -,-a\n\nIni dalam satu komputer ya ?"}, {"author": "Wak Jek", "date": "Friday 18 November 2011 at 11:54", "text": "ia, dual boot"}, {"author": "Anggha Sanjaya", "date": "Friday 18 November 2011 at 11:56", "text": "Berarti saat jalan di ubuntu yg online itu server mysql ubuntu toh ?\n\nSedangkan server mysql di windows udah pasti ga jalan khan ?\n\nGa mungkin kayaknya gan...\nTerbentur masalah filesystem...."}, {"author": "Wak Jek", "date": "Friday 18 November 2011 at 12:00", "text": "ia benar.\ndatabase nya udah kebaca sih, cuma tabel nya belom (karena file tabel nya masih milik root:root).\nkyknya cuma masalah chown symlink , tapi belum dapat solusinya"}, {"author": "Anggha Sanjaya", "date": "Friday 18 November 2011 at 12:07", "text": "ya... pake solusi dump sql aja klo bgitu...\n\nrepot-lah..."}, {"author": "Wak Jek", "date": "Friday 18 November 2011 at 12:12", "text": "hehe kalau gitu sih bisa, tapi repot, banyak kok,\nlagian emang mau pake 2 os, krn blom bisa 100% pake ubuntu (setidaknya untuk saat ini krn masih newbie )"}]
---

<p>Gan gimana cara sync database mysql yang ada di partisi windows dengan yang ada di Ubuntu.<br/>
udah pke link tapi di phpmyadmin linux tetep gk muncul</p>
