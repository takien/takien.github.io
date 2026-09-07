---
title: "Membuat Theme WP #2 - index.php"
date: "2012-11-14T22:33:00Z"
categories: ["WordPress"]
tags: ["facebook", "wordpress", "plugin", "theme"]
slug: "2012/11/14/membuat-theme-wp-2-indexphp"
legacyUrl: "/2012/11/14/membuat-theme-wp-2-indexphp/"
source: "facebook.com"
author: "Wak Jek"
comments: [{"author": "Utomo A", "date": "Wednesday 14 November 2012 at 22:34", "text": "nah.. ini dia yg ditunggu...\nmari belajar"}, {"author": "Bambang Catur Pamungkas", "date": "Wednesday 14 November 2012 at 22:36", "text": "bikin github ato gist aja om wak, biar bisa collab :)"}, {"author": "Wak Jek", "date": "Wednesday 14 November 2012 at 22:45", "text": "ntar instal git dulu, dah lama gk pake stelah inul OS"}, {"author": "Bambang Catur Pamungkas", "date": "Wednesday 14 November 2012 at 22:46", "text": "github kan udah ada client nya buat wedus om..bikin user pake imel grup (keknya ada kan imel grup)\nlumayan buat naroh snippet :D"}, {"author": "Wak Jek", "date": "Wednesday 14 November 2012 at 22:52", "text": "kan tinggal fork fork :D pake akun masing2 jg gpp"}, {"author": "Bambang Catur Pamungkas", "date": "Wednesday 14 November 2012 at 22:56", "text": "boleh juga :D\nditunggu inopasinya :D"}, {"author": "Wak Jek", "date": "Wednesday 14 November 2012 at 23:25", "text": "repo gigit https://github.com/takien/Belajar-Membuat-Theme-WordPress"}, {"author": "Andri", "date": "Thursday 15 November 2012 at 02:49", "text": "nice share om B)\nizin nyicip yaaaa,,,,"}, {"author": "Jeffri Tjin", "date": "Thursday 15 November 2012 at 13:43", "text": "<section id=\"main-content\"> menurut ane lebih baik pake <div> aja gan. Soalnya itu kan wrapper, jadi ga ada arti semantic nya. :)"}, {"author": "Uchan Utchanovsky", "date": "Thursday 15 November 2012 at 18:47", "text": "gan, header.php biasanya disendiriin apa enaknya kek di atas digabung ke index.php?"}, {"author": "Anonim", "date": "Thursday 15 November 2012 at 19:20", "text": "Learning by doing  ITu Moto saya , lanjut (y)"}, {"author": "Wak Jek", "date": "Thursday 15 November 2012 at 21:21", "text": "Jeffri Hong, oke sip thx :)"}, {"author": "Wak Jek", "date": "Thursday 15 November 2012 at 21:22", "text": "Uchan Utchanovsky,\ndisendiriin, pada contoh diatas ane sengaja gabungin dulu, biar gk bingung bwt pemula. :D"}, {"author": "Bagus Fikri Yuliono", "date": "Thursday 23 May 2013 at 15:42", "text": "lha mana ni yg nomer 3 dst :o ?"}, {"author": "Wak Jek", "date": "Thursday 23 May 2013 at 15:43", "text": "lagi sibuk :D"}, {"author": "Ali Imron", "date": "Thursday 23 May 2013 at 16:41", "text": "ditunggu kelanjutannya om :)"}, {"author": "Jeffry Gunawan", "date": "Thursday 23 May 2013 at 16:59", "text": "*kasih minum biar bisa update"}]
---

<p>Membuat Theme WP #2 - index.php</p>

<p>Setelah style.css, selanjutnya file index.php</p>

<p>file index.php adalah penting, karena file ini adalah penting ? weleh.</p>

<p>-----------------------------------------------------------------------------------------------------------</p>

<p>[disclaimer]</p>

<p>Untuk mengikuti tutorial ini, diharapkan Anda minimal sudah paham dengan WordPress.</p>

<p>Jadi, yang basic-basic nya tidak saya jelaskan lagi.</p>

<p>[/disclaimer]</p>

<p>-----------------------------------------------------------------------------------------------------------</p>

<p>Struktur umum dari index.php adalah sebagai berikut.</p>

<p>* header</p>

<p>* menu</p>

<p>* mainsection</p>

<p>* comment</p>

<p>* sidebar</p>

<p>* footer</p>

<p>Sepertinya tidak perlu dijelaskan satu persatu, I know, people hate to read. Langsung praktek aja.</p>

<p>Struktur ini menggunakan HTML5, buat yang udah paham HTML5 tolong dikoreksi kode berikut jika ada salah.</p>

<p><!DOCTYPE HTML></p>

<p><html lang="en-US"></p>

<p><head></p>

<p><meta charset="UTF-8"></p>

<p><title></p>

<p><?php wp_title( '|', true, 'right' );</p>

<p>bloginfo( 'name' );</p>

<p>?></title></p>

<p><link href="<?php bloginfo('stylesheet_url');?>" rel="stylesheet"></p>

<p><?php wp_head();?></p>

<p></head></p>

<p><body></p>

<p><header></p>

<p><hgroup></p>

<p><h1><?php bloginfo('name');?></h1></p>

<p><h2><?php bloginfo('description');?></h2></p>

<p></hgroup></p>

<p></header></p>

<p><nav></p>

<p><?php wp_nav_menu()?></p>

<p></nav></p>

<p><section id="maincontent"></p>

<p><?php if(have_posts()) : while(have_posts()) : the_post();?></p>

<p><article></p>

<p><header></p>

<p><h1><?php the_title();?></h1></p>

<p></header></p>

<p><?php the_content();?></p>

<p></article></p>

<p><?php</p>

<p>endwhile;</p>

<p>else :</p>

<p>?></p>

<p><h1>Not found</h1></p>

<p><?php</p>

<p>endif;</p>

<p>?></p>

<p><section id="comments"></p>

<p><?php comments_template( '', true ); ?></p>

<p></section></p>

<p></section></p>

<p><aside></p>

<p><?php dynamic_sidebar();?></p>

<p></aside></p>

<p><footer></p>

<p><p>Copyright &copy; <?php echo date('Y');?> - <?php bloginfo('name');?></p></p>

<p></footer></p>

<p><?php</p>

<p>wp_footer();</p>

<p>?></p>

<p></body></p>

<p></html></p>

<p>Seperti biasa, saya tidak akan menjelaskan HTML dan atau CSS nya di sini.  Tapi cukup PHP nya aja ya.</p>

<p>* wp_title() , menampilkan judul dokumen, judul akan tertera pada title bar browser, peletakannya biasanya di dalam tag <title></title></p>

<p>* bloginfo('whatever'), menampilkan berbagai info blog, seperti nama blog, deskripsi dll. selengkapnya mengenai bloginfo(), silakan merujuk ke http://codex.wordpress.org/Function_Reference/bloginfo</p>

<p>* wp_head(), ini untuk memanggil hook do_action('wp_head"); yang fungsinya macem-macem, contohnya untuk menempatkan script maupun stylesheet secara dinamis melalui plugin dsb.</p>

<p>* wp_nav_menu();  ini untuk menampilkan menu, karena terlalu kompleks maka untuk detailnya akan dijelaskan di kesempatan lain.</p>

<p>* the_title(), menampilkan judul blogpost atau page</p>

<p>* the_content(), menampikan isi post/page</p>

<p>* comments_template( '', true ); untuk menampikan comment form. Comment form hanya akan muncul jika berada di single post/page.</p>

<p>* dynamic_sidebar(); menampilkan widget sidebar dinamis, akan dijelaskan di kesempatan lain.</p>

<p>* wp_footer(); hampir sama dengan wp_head(), beda nya karena letaknya di bawah.</p>

<p>* <?php if(have_posts()) : while(have_posts()) : the_post();?></p>

<p>// content, title, comment, etc</p>

<p><?php  endwhile;   else :  ?></p>

<p>// pesan not found.</p>

<p><?php endif;  ?></p>

<p>Wow apaan itu bro?, hehe, itu adalah WP Loop, wp loop itu apa ya... nganu...</p>

<p>Nah itu penting, untuk memanggil isi post dari database ke dalam template.</p>

<p>Kacau kode nya, oke, udah ane upload di Google Docs kok, silakan cekidot:</p>

<p>https://docs.google.com/folder/d/0B9kp0euLs-_VX3ZKZmp6QXhiaVE/edit</p>

<p>No Pic = Hoax.</p>

<p>Oke ini pic nya bahwa theme tersebut sudah jalan:</p>

<p><img src="http://i.imgur.com/PpA1g.png" /></p>

<p>Kalau ada yang kurang jelas silakan ditanyakan.</p>
