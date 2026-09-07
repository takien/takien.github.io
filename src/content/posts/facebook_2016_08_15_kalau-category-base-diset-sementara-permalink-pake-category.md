---
title: "Kalau category base diset, sementara permalink pake %category% dan custom..."
date: "2016-08-15T04:30:00Z"
categories: ["WordPress"]
tags: ["facebook", "wordpress", "plugin"]
slug: "2016/08/15/kalau-category-base-diset-sementara-permalink-pake-category"
legacyUrl: "/2016/08/15/kalau-category-base-diset-sementara-permalink-pake-category/"
source: "facebook.com"
author: "Wak Jek"
comments: [{"author": "Wak Jek", "date": "Monday 15 August 2016 at 04:30", "text": "gist aja deh\n\nhttps://gist.github.com/.../21a9209fe867f8d5fe4d58a62a0cb79d"}, {"author": "Yanuar Arifianto", "date": "Monday 15 August 2016 at 05:15", "text": "Wak Jek biar WP di catrgory ga muncul contentnya yang diedit di mana ya? Maksudnya biar muncul judulnya aja."}, {"author": "Aris Sandi", "date": "Monday 15 August 2016 at 05:55", "text": "kalo aktifkan theme baru, kan suka ada flush_rewrite_rules bawaan theme nya. ngaruh ga? ato function diatas dibikin plugin tersendiri."}]
---

<p>Kalau category base diset, sementara permalink pake %category% dan custom base, itu emang tidak bisa. Ini bug di WordPress sepertinya.</p>

<p>Misalnya:<br/>
category base : berita<br/>
permalink structure: berita/%category%/%post_name%</p>

<p>Ini akan menghasilkan halaman 404 (not found)</p>

<p>Ini dikarenakan, rule untuk permalink (post) di WP priority nya low, sehingga ketika running, sistem akan memproses struktur kategori dulu. Dikarenakan rule untuk post, sama dengan kategori, maka post akan dianggap kategori, ini yang menyebabkan 404 (not found).</p>

<p>Sebenarnya ini bisa diatasi dengan plugin Rewrite yang pernah kubuat dulu (https://wordpress.org/plugins/rewrite/). Dengan cara me-reorder rule-rule rewrite/memindahkan rule post ke atas (top priority), namun sayangnya saya tidak merekomendasikan untuk menggunakan plugin tersebut saat ini, karena plugin tsb cara kerjanya merubah database langsung (tidak menggunakan filter). Dan saya belum sempat lagi memperbaikinya</p>

<p>Solusi sementara dengan menggunakan fungsi custom rewrite rule yang ada di komentar di bawah ini.</p>

<p>Fungi tersebut membuat ulang rule untuk post, dan menenmpatkannya di atas (top priority).</p>
