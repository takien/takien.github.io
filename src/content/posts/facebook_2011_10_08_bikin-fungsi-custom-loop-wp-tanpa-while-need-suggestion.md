---
title: "Bikin Fungsi Custom Loop WP Tanpa While (Need Suggestion)"
date: "2011-10-08T01:12:00Z"
categories: ["WordPress"]
tags: ["facebook", "wordpress"]
slug: "2011/10/08/bikin-fungsi-custom-loop-wp-tanpa-while-need-suggestion"
legacyUrl: "/2011/10/08/bikin-fungsi-custom-loop-wp-tanpa-while-need-suggestion/"
source: "facebook.com"
author: "Wak Jek"
comments: [{"author": "Wak Jek", "date": "Saturday 8 October 2011 at 01:14", "text": "cc dulu Asep Bagja Heri Hehe Setiawan Kecoa Ngamuk Kecoa Jeffri Tjin Dicky Kurniawan Ian Hehe Lubis dkkm"}, {"author": "Jeffri Tjin", "date": "Saturday 8 October 2011 at 01:38", "text": "Ribet bikin dan maintenance html nya ntar berhubung html nya kan dalam string - ga kena syntax coloring di editor...\n\nMending bikin instance baru WP_Query. Kalo males pake while loop, page foreach aja... hehe\n\nUntuk tampilan kalo ga salah udah ada fitur post format, tapi ane belum pernah pake."}, {"author": "Wak Jek", "date": "Saturday 8 October 2011 at 01:41", "text": "hahaha. emang sih, jadi grayscale semua formatnya :D\n\ndulu ane pak WP_Query, sekarng gk pernah lagi, lebih simple pake query_posts() , emang sih harus selalu direset at the end of loop. :D"}, {"author": "Wak Jek", "date": "Saturday 8 October 2011 at 01:47", "text": "hmm. sbnrya tujuan nya, untuk yang simple2 aja. bukan untuk format html yang rumit.\nkadang kan ada di bbrp bagian cuma nampilin 1 post doangk. :D…See more"}, {"author": "Jeffri Tjin", "date": "Saturday 8 October 2011 at 01:50", "text": "Yup, kalo mau simple yah pake get_posts. Tapi get_posts querynya ada yang beda sendiri dari WP_Query. Secara pribadi sih ane lebih suka pake WP_Query, kan bisa reusable dan lebih aman dari kesalahan2 kecil kayak pake query_posts (misalnya lupa reset, trus stress beberapa jam cuman buat nemuin errornya disitu)... :)"}, {"author": "Wak Jek", "date": "Saturday 8 October 2011 at 01:56", "text": "oh ia ya, salah satu contoh get_posts pake 'numberposts' bukan posts_per_page.\n\nane prefer query_posts, karena itu kan sbnry apake clas WP_Query juga. kelebihannya adlah gk pelu pake $posts->have_posts(), cukup langsung have_posts() …See more"}, {"author": "Jeffri Tjin", "date": "Saturday 8 October 2011 at 01:59", "text": "Kan bisa gini:\n\n$myposts = new WP_Query('blablabla');…See more"}, {"author": "Wak Jek", "date": "Saturday 8 October 2011 at 02:00", "text": "oh baru tau ane bisa gitu.\ntetep aja $myposts = new WP_Query('blablabla'); lebih panjang daripada query_posts('blablabla');"}, {"author": "Jeffri Tjin", "date": "Saturday 8 October 2011 at 02:03", "text": "Kalo buat ane sih agak panjang gpp, ntar maintenance nya lebih mudah... ga kebingungan kalo ada banyak query dalam 1 page. :)"}, {"author": "Wak Jek", "date": "Saturday 8 October 2011 at 02:28", "text": "ane dlu jg pake WP_Query kok, tapi ntah kenapa skrg gk mau lagi.\n:trauma  WP_Query,"}, {"author": "Heri Hehe Setiawan", "date": "Saturday 8 October 2011 at 05:58", "text": "hati-hati, bikin loop dalam function, trus manggil function nya lagi ini bikin page load lebih lambat loh :P , ya mungkin kalau cuma 1 atau 2 query yang data-datanya sedikit ga terlalu terasa sih.. hehe"}]
---

<p>Bikin Fungsi Custom Loop WP Tanpa While (Need Suggestion)</p>

<p>Ane bikin fungsi ini untuk memanggil Loop wp tanpa harus mengulang2 nulis if, while, endif dan reset query karena udah dikumpulkan dalam satu fungsi dan bisa dipake berulang2.</p>

<p><?php</p>

<p>//function custom loop</p>

<p>function my_custom_loop($query,$format){</p>

<p>query_posts($query);</p>

<p>$return = false;</p>

<p>if (have_posts()) while (have_posts()) : the_post();</p>

<p>//definisikan semua fungsi2 yang akan direplace, ane cuma kasi contoh 3 aja, title,content,excerpt</p>

<p>$replace = Array(</p>

<p>'the_title'       => get_the_title(),</p>

<p>'the_content' => get_the_content(),</p>

<p>'the_excerpt' => get_the_excerpt()</p>

<p>);</p>

<p>$return .= str_replace(array_keys($replace), array_values($replace), $format);</p>

<p>endwhile;</p>

<p>wp_reset_query();</p>

<p>return $return;</p>

<p>}</p>

<p>?></p>

<p>========= .Cara memanggilnya.=========</p>

<p><?php</p>

<p>//contoh ambil 5 post,dari categori dgn slug 'example', menampilkan judul dan excerpt. (parameter lainnya bisa lihat di codex WP_Query)</p>

<p>$query = Array(</p>

<p>'posts_per_page'=>5,</p>

<p>'category_name  =>'example''</p>

<p>);</p>

<p>$format = '<h2>the_title</h2></p>

<p><p>the_excerpt</p> ';</p>

<p>echo my_custom_loop($query,$format);</p>

<p>?></p>

<p>So far, udah work like a charm body fit.</p>

<p>MASALAHNYA ADALAH:</p>

<p>Gimana cara memasukkan parameter, jika kita perlu menambahkan parameter di fungsi2 yang direplace tersebut? Ada solusi?</p>
