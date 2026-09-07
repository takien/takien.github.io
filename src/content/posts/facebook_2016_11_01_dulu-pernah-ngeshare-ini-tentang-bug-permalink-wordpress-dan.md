---
title: "Dulu pernah ngeshare ini, tentang bug permalink WordPress dan solusinya..."
date: "2016-11-01T19:21:00Z"
categories: ["WordPress"]
tags: ["facebook", "wordpress"]
slug: "2016/11/01/dulu-pernah-ngeshare-ini-tentang-bug-permalink-wordpress-dan"
legacyUrl: "/2016/11/01/dulu-pernah-ngeshare-ini-tentang-bug-permalink-wordpress-dan/"
source: "facebook.com"
author: "Wak Jek"
comments: [{"author": "Andita Sely Bestoro", "date": "Tuesday 1 November 2016 at 19:21", "text": "Ndak ngerti om"}]
---

<p>Dulu pernah ngeshare ini, tentang bug permalink WordPress dan solusinya, nah solusi saya tersebut waktu itu cukup panjang karena harus memodifikasi permalink rules.</p>

<p>Nah, ada solusi lain nih yang lebih sederhana.</p>

<p>Jika belum tau tujuannya mau ngapain, nih seperti ini:</p>

<p>Misal kita ingin membuat permalink seperti ini:</p>

<p>Untuk single:<br/>
example.com/artikel/nama-kategori/slug-artikel</p>

<p>Untuk kategori (kategory base 'artikel') :<br/>
example.com/artikel/nama-kategori</p>

<p>Secara default, post single akan menjadi 404 (not found), penjelasannya ada dalam postingan saya sebelumnya (terlampir).</p>

<p>SOLUSI, di setingan permalink:</p>

<p>custom structure: /artikel/%category%/%postname%/<br/>
category base : . ( tanda titik saja, seperti ketika kita mau menghilangkan kategori base)</p>

<p>Filter, ya, cuma dengan merubah link kategori dan menyisipkan categori base disini. Dan tadaaa...ajaib, semua work as expected</p>

<p>// ============<br/>
function cektkp_custom_category_link($termlink, $term, $taxonomy) {<br/>
if('category' == $taxonomy){<br/>
$termlink = str_replace( site_url('/'), site_url('/artikel/'), $termlink);<br/>
}<br/>
return $termlink;<br/>
}<br/>
// ===========</p>

<p>selamat mencoba</p>
