---
title: "Tutorial #1 - WP_Query"
date: "2013-05-08T11:51:00Z"
categories: ["WordPress"]
tags: ["facebook", "wordpress"]
slug: "2013/05/08/tutorial-1-wpquery"
legacyUrl: "/2013/05/08/tutorial-1-wpquery/"
source: "facebook.com"
author: "Wak Jek"
comments: [{"author": "Bagus Fikri Yuliono", "date": "Wednesday 8 May 2013 at 11:52", "text": "nah saya jadi gasusah2 nyari wkwkkw makasii baang wak hehe"}, {"author": "Yanuar Arifianto", "date": "Wednesday 8 May 2013 at 18:14", "text": "Wah keren! <-- *padahal nggak sampai otaknya*"}, {"author": "Bambang Catur Pamungkas", "date": "Wednesday 8 May 2013 at 18:25", "text": "abis ini request tutor taxonomy ya om Wak Hehe Jek."}, {"author": "Prast Rahastu", "date": "Wednesday 8 May 2013 at 19:32", "text": "keren"}, {"author": "Bagus Fikri Yuliono", "date": "Thursday 23 May 2013 at 15:47", "text": "om, kalau kasus sedekahberjamaah.com itu kan ada section2 misal tentang kami, beberapa manfaat, itu bisa pake custom query?"}, {"author": "Wak Jek", "date": "Thursday 23 May 2013 at 15:49", "text": "bisa"}, {"author": "Wak Jek", "date": "Thursday 23 May 2013 at 15:49", "text": "itu per section nya di bikin page aja, bukan post"}, {"author": "Wak Jek", "date": "Thursday 23 May 2013 at 15:50", "text": "ntar di section yang bersangkutan bikin gini :\n\nMisal ini untuk section Tentang Kami…See more"}, {"author": "Wak Jek", "date": "Thursday 23 May 2013 at 15:51", "text": "param nya, bisa pake pagename, atau page_id, kalau page_id, masukkan ID page yang bersangkutan, klo pagename berarti slug nya."}, {"author": "Bagus Fikri Yuliono", "date": "Thursday 23 May 2013 at 15:52", "text": "code :\n\n<?php…See more"}, {"author": "Wak Jek", "date": "Thursday 23 May 2013 at 15:52", "text": "dan kamu cukup bikin file index.php aja, file2 lain gk perlu kyknya."}, {"author": "Bagus Fikri Yuliono", "date": "Thursday 23 May 2013 at 15:54", "text": "sorry yah blm mudeng coba ntar praktek langsung aja"}]
---

<p>Tutorial #1 - WP_Query</p>

<p>Apa WP_Query itu?</p>

<p>WP Query adalah, apapun itu yang penting gunanya untuk berinteraksi dengan database di WordPress, khususnya untuk membaca table wp_posts.<br/>
Sekali lagi ini untuk membaca, bukan untuk menulis atau mengedit.</p>

<p>Jenis WP_Query:<br/>
1. Main query<br/>
2. Custom query</p>

<p>1. Main Query<br/>
Main query atau query utama adalah query standard untuk menampilkan post/page/archive, dsb.<br/>
Query ini menerima default parameter, biasanya dari URL yang sedang diakses.<br/>
misalnya kita buka single post. index.php?p=100, berarti parameternya adalah post dengan ID 100.</p>

<p>Mana contohnya? Contohnya yaitu The loop berikut ini.</p>

<p><?php<br/>
while ( have_posts() ) : the_post();?><br/>
<h1><?php the_title();?></h1><br/>
<?php the_content();?><br/>
<?php endwhile;?></p>

<p>Kode itu biasanya ada di setiap template. Itu dapat digunakan secara universal, tergantung URL nya, apakah itu home, arcive, single, page atau search.</p>

<p>2. Custom Query</p>

<p>Hampir sama dengan Main Query, cuma bedanya kalau custom kita bisa memberi parameter sendiri, tidak tergantung URL yang sedang diakses.<br/>
Misalnya akan menampilkan post dengan ID xxx, sejumlah x, di sidebar atau di home,dsb.</p>

<p>Caranya? Kita sedikit modifikasi main query diatas.</p>

<p><?php<br/>
$param = Array(<br/>
'posts_per_page' => 10,<br/>
'post_type' => 'post'<br/>
);<br/>
$query = new WP_Query ($param);<br/>
while ( $query->have_posts() ) : $query->the_post();?><br/>
<h1><?php the_title();?></h1><br/>
<?php the_content();?><br/>
<?php endwhile;?></p>

<p>Kode diatas akan menampilkan 10 post, dimanapun dia berada.</p>

<p>Diatas terlihat variable $param yagn berisi Array, nah disitu bisa apa aja param nya, tergantung data yang mau ditampilkan.</p>

<p>Parameter nya ada banyak, selengkapnya lihat di http://codex.wordpress.org/Class_Reference/WP_Query#Parameters</p>

<p>Custom WP_Query ini sangat berguna ketika:<br/>
1. Ingin menampilkan list post di mana aja dengan parameter tertentu<br/>
2. Menampilkan slideshow/carousel atau attachment<br/>
3. dll</p>
