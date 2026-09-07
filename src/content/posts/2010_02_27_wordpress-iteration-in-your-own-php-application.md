---
title: "WordPress Iteration in Your Own PHP Application"
date: "2010-02-27T15:10:00.000Z"
categories: ["WordPress","PHP"]
tags: []
slug: "2010/02/27/wordpress-iteration-in-your-own-php-application"
legacyUrl: "/2010/02/27/wordpress-iteration-in-your-own-php-application/"
source: "takien.com"
author: "takien"
comments: [{"author":"Kacang Hijau","date":"","text":"Sial, kok titlenya “Pedagang bubur kacang ijo” :ngakak\nBro btw nggak install emoticon kaskus?"},{"author":"takien","date":"","text":"Pedagang buburnya antar benua bro, mau kan \nEmo kaskus, hmm.. gk cocok ama theme nya dong hehhe"},{"author":"Fauzie","date":"","text":"nice post dude… just what i needed…"},{"author":"dholie","date":"","text":"ko ane coba ga bisa ya gan? ga ada tampilan na, cuma keluar  klo di liat view page na,., :’(\nquery na ane isi biasa, “select * from post” apa bukan gitu ya?\nboleh minta script yg dah jagi ga? sama struktur db na?\nthanks sebelum na"},{"author":"takien","date":"","text":"FYI, kode ini bukan untuk wordpress…\ntapi untuk php buatan sendiri yang mau nampilin isi database dengan cara seperti yang dilakukan wordpress…\nuntuk query nya terserah,\ntapi untuk menjalankan contoh diatas, at least tabel mempunyai kolom Title dan Content\nkarena akan di panggil di sini:\n[php]\nfunction the_title() {\n    global $post;\n    return $post->Title; //field Title\n}\nfunction the_content() {\n    global $post;\n    return $post->Content; //field Content\n}[/php]"},{"author":"dholie","date":"","text":"ga bisa jg gan,., :’(\nane coba pake database field na : ID, Title, Content\nquery na aku pake “select * from table”\ntapi tetep ga bisa, ga keluar apa2 cuma layar putih duank :’("},{"author":"takien","date":"","text":"Seharusnya bisa loh..\natau coba query langsung dulu, nampil gak\njangan2.. isi database nya emang kosong heheh.."},{"author":"dholie","date":"","text":"database na ada isi na lah gan :’( yg keluar cuma tag h2 duank (klo diliat source page na)\noh iya ane mo nanya, knp ga pake mysql_fetch_array ya? ato script diatas itu ada pengganti mysql_fetch_array? klo iya, yg bagian mana ya,.,\nsorry banyak nnya,., biar ga sesat di dunia maya"},{"author":"takien","date":"","text":"hmmm… bentar,ku cek lagi"},{"author":"iroel","date":"","text":"Tahu fungsi parse_str kan gan? Klo mo bikin gitu kayak gimana yah? Jadi outputnya bisa ditaruh di argumen ato variabel global. Jawabnya di kaskus trid PHP ya gan. Jarang mampir ke sini soalnya. Ini aja mampir pertama kli"},{"author":"takien","date":"","text":"hehe, aku gk pernah pake parse_str bro, tapi pake nya wp_parse_str, yang ada di WP.. coba deh.. keren n lebih lengkap.."},{"author":"Prast Rahastu","date":"","text":"gan"},{"author":"Domain register","date":"","text":"Nice presentation Thank you for this information, for a website now a days very much important all the user"},{"author":"sisme bebek","date":"","text":"Great review"}]
---

Wordpress has its own way to loop the posts, that is different than what other CMS does. I think it’s great because of flexibility and usability reason. It would seem easy later, when you want to manipulate the result before it is displayed to the browser.

So you want to implement the WordPress-style loop in your own PHP application? You have to say yes. :D

The following PHP code contains some basic functions to make your own WordPress Loop.

### Code

**Wordpress-style Loop**

```
$posts = mysql_query('YOUR SQL QUERY HERE'); 
$post = null; 
$post_count = 0; 
$post_index = 0; 
 
function have_post() { 
 global $posts, $post_count, $post_index; 
 
 if ($posts && ($post_index < = $post_count)){ 
 $post_count = count($posts); 
 return true; 
 } 
 else { 
 $post_count = 0; 
 return false; 
 } 
} 
 
function the_post() { 
 global $posts, $post, $post_count, $post_index; 
 
 // make sure all the posts haven't already been looped through 
 if ($post_index > $post_count) { 
 return false; 
 } 
 
 // retrieve the post data for the current index 
 $post = $posts[$post_index+1]; 
 
 // increment the index for the next time this method is called 
 $post_index++; 
 return $post; 
 
} 
 
function the_title() { 
 global $post; 
 return $post->Title; 
} 
 
function the_content() { 
 global $post; 
 return $post->Content; 
} 
 
//and the output... tada.... 
 
if(have_post()) : while(have_post()) : the_post(); 
echo "<h2>".the_title()."</h2>"; 
echo the_content(); 
endwhile; endif; 
```

The **advantage**of using this iteration is:
 1. Easy to implement with templating system.
 2. Easy to filter output through PHP function, no need edit the template file.
 3. Every output element is a function rather than a variable. It accepts parameter, you can do more things.
 4. Want to display next post or previous post? that's no a pain.

**Disadvantage:**
 Of course, that code confusing me at the first time :D

Information Thanks to [Matt Huggins](http://blackbooksingles.com/) post at [Stackoverflow](http://stackoverflow.com/questions/1516181/how-to-make-my-own-while-loop-just-like-wordpress-loop) and [xrvel](http://kacanghijau.com/) post at [kaskus](http://www.kaskus.us/showpost.php?p=174087163&postcount=8470)
