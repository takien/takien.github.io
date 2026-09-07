---
title: "[WP Ajax Basic] Membuat Contact Form  di WordPress"
date: "2013-01-20T13:39:00Z"
categories: ["WordPress"]
tags: ["facebook", "wordpress", "plugin", "theme"]
slug: "2013/01/20/wp-ajax-basic-membuat-contact-form-di-wordpress"
legacyUrl: "/2013/01/20/wp-ajax-basic-membuat-contact-form-di-wordpress/"
source: "facebook.com"
author: "Wak Jek"
comments: [{"author": "Anonim", "date": "Sunday 20 January 2013 at 14:32", "text": "wew,,,\nGokil kak,,,\ngak menduga wp bisa buat ntu,,,"}, {"author": "Sabihul Anwary", "date": "Sunday 20 January 2013 at 16:31", "text": "ane selama ini cuma pake php sederhana aja om :v\nkalo gak plugin form :v"}, {"author": "Uchan Utchanovsky", "date": "Sunday 20 January 2013 at 16:36", "text": "izin nyimak gan :D\n\nbtw ga pake captcha2-an gan? atau postingan di sesi berikutnya :v"}, {"author": "Wak Jek", "date": "Sunday 20 January 2013 at 16:46", "text": "jangan lihat fiturnya, tapi lihat pembelajarannya."}, {"author": "Anonim", "date": "Sunday 20 January 2013 at 17:19", "text": "(y)"}, {"author": "Prast Rahastu", "date": "Sunday 20 January 2013 at 17:27", "text": "pembelajaran yang baik"}, {"author": "Semut Saurus", "date": "Sunday 20 January 2013 at 20:11", "text": "manstab nice turto  (y)  agan Wak Hehe Jek ! ane ucapin terima kasih banyak gan..!"}, {"author": "Bagus Fikri Yuliono", "date": "Friday 24 May 2013 at 22:58", "text": "bro kalo formnya ke gini gmn nih , bisa help gak .____. pliiis\n\nhttp://redpen.io/zxn3hv"}, {"author": "Wak Jek", "date": "Friday 24 May 2013 at 23:00", "text": "bisa aja, tinggal sesuaikan tag htmlnya"}, {"author": "Bagus Fikri Yuliono", "date": "Friday 24 May 2013 at 23:01", "text": "bingung bos yg select gmn ?"}, {"author": "Wak Jek", "date": "Friday 24 May 2013 at 23:08", "text": "<select>\n<option>1</option>\n<option>2</option>…See more"}, {"author": "Bagus Fikri Yuliono", "date": "Friday 24 May 2013 at 23:09", "text": "iii bukan html nya tp caranya o.o kasih dong bos di atas checkbox sama select jg biar aku mudeng .___."}, {"author": "Bagus Fikri Yuliono", "date": "Friday 24 May 2013 at 23:09", "text": "biar berfungsi jg kaya text / email / textarea ?"}, {"author": "Wak Jek", "date": "Friday 24 May 2013 at 23:10", "text": "ya sama aja, yang didetek ntar name=\"\" nya"}, {"author": "Bagus Fikri Yuliono", "date": "Friday 24 May 2013 at 23:11", "text": "kalau punya aku kan\n\n<select id=\"select01\">…See more"}, {"author": "Bagus Fikri Yuliono", "date": "Friday 24 May 2013 at 23:12", "text": "di kasih name di bagian <select> ya?"}, {"author": "Wak Jek", "date": "Friday 24 May 2013 at 23:12", "text": "dikasi name, <select id=\"blabla\" name=\"bagus\">"}, {"author": "Bagus Fikri Yuliono", "date": "Friday 24 May 2013 at 23:13", "text": "menurut http://wp.tutsplus.com/.../adaptive-blog-theme-page.../...\n\nitu bentuknya di 1 page itu kayane masbro ga nyentuh function, gmn tuh ?"}, {"author": "Bagus Fikri Yuliono", "date": "Friday 24 May 2013 at 23:13", "text": "di custom page maksudnya"}, {"author": "Wak Jek", "date": "Friday 24 May 2013 at 23:14", "text": ">"}, {"author": "Wak Jek", "date": "Friday 24 May 2013 at 23:14", "text": "?"}, {"author": "Wak Jek", "date": "Friday 24 May 2013 at 23:15", "text": "gini, functions.php itu optional, klo gk ada gpp,\ntapi kalau ada file itu, otomatis akan keload. gk perlu di include2 lagi."}, {"author": "Bagus Fikri Yuliono", "date": "Friday 24 May 2013 at 23:18", "text": "define('ACF_PAGE_SLUG', 'contact');  berarti custom page nya namanya page-contact.php trus di admin panel bikin page namanya contact ?"}, {"author": "Wak Jek", "date": "Friday 24 May 2013 at 23:19", "text": "ia.\ncustom page optional tuh, klo gk ada page-contact.php maka yang dipake adalah page.php\nklo page.php gk ada, maka yang dipake index.php"}, {"author": "Bagus Fikri Yuliono", "date": "Friday 24 May 2013 at 23:22", "text": "yup klo yg itu uda paham hihihi.. sipsipsip, paling tidak kebutuhanku uda terpenuhi lah :3 yg lain menyusul semisal custom post typenya :3"}]
---

<p>[WP Ajax Basic] Membuat Contact Form  di WordPress</p>

<p>Kali ini kita akan membuat WordPress Ajax Contact Form sederhana di WordPress. selanjutnya kita singkat menjadi ACF.</p>

<p>Langkah2nya:</p>

<p>1. define some constants.</p>

<p><?php</p>

<p>define('ACF_PAGE_SLUG', 'contact'); /* page slug dimana nanti form akan dirender*/</p>

<p>define('ACF_EMAIL_RECEIVER','mymail@example.com'); /* email penerima contact*/</p>

<p>define('ACF_SUCCESS_MESSAGE','Pesan anda berhasil dikirim, terimakasih.');</p>

<p>define('ACF_ERROR_MESSAGE','Terjadi kesalahan, email tidak terkirim.');</p>

<p>?></p>

<p>2. Render langsung script nya di footer, kalau udah Advanced sebaiknya pakai wp_enqueue_script (external file)</p>

<p><?php</p>

<p>add_action('wp_footer', 'acf_form_js');</p>

<p>function acf_form_js(){ ?></p>

<p><script></p>

<p>jQuery(document).ready(function($) {</p>

<p>var ajaxurl = '<?php echo admin_url('admin-ajax.php');?>';</p>

<p>$('#contact-form').submit(function(){</p>

<p>var data = $(this).serialize();</p>

<p>$.post(ajaxurl, data, function(response) {</p>

<p>if(response.code == 1){</p>

<p>/* jika susccess*/</p>

<p>alert(response.message);</p>

<p>}</p>

<p>else {</p>

<p>/*jika error*/</p>

<p>alert(response.message);</p>

<p>}</p>

<p>});</p>

<p>return false;</p>

<p>});</p>

<p>});</p>

<p></script></p>

<p><?php</p>

<p>}</p>

<p>?></p>

<p>3. Form HTML nya,</p>

<p><?php</p>

<p>/* pake filter the_content, supaya nantinya form akan otomatis nempel di page dengan slug 'contact' atau whatever terserah anda, sesuai dengan ACF_PAGE_SLUG di atas*/</p>

<p>add_filter('the_content','render_contact_form');</p>

<p>function render_contact_form($content) {</p>

<p>if(is_page(ACF_PAGE_SLUG)) {</p>

<p>?></p>

<p><form id="contact-form" action="" method="post"></p>

<p><label for="nama">Nama:</label><input id="nama" type="text" required="required"value="" name="nama" /><br></p>

<p><label for="email">Email:</label><input id="email" type="email" required="required" value="" name="email" /><br></p>

<p><label for="subject">Subject:</label><input id="subject" type="text" required="required" value="" name="subject" /><br></p>

<p><label for="message">Message:</label><textarea required="required" name="message"></textarea><br></p>

<p><input type="hidden" name="action" value="acf_form_submit"/></p>

<p><input type="submit" value="Send" name="submit_form" /></p>

<p></form></p>

<p><?php</p>

<p>}</p>

<p>else {</p>

<p>return $content;</p>

<p>}</p>

<p>}</p>

<p>?></p>

<p>3. Sekarang bikin Ajax Callback nya.</p>

<p><?php</p>

<p>add_action('wp_ajax_acf_form_submit',        'acf_callback');</p>

<p>add_action('wp_ajax_nopriv_acf_form_submit', 'acf_callback');</p>

<p>function acf_callback() {</p>

<p>if($_SERVER['HTTP_X_REQUESTED_WITH'] == 'XMLHttpRequest'){</p>

<p>$name       = trim(strip_tags($_POST['name']));</p>

<p>$email      = trim(strip_tags($_POST['email']));</p>

<p>$subject    = trim(strip_tags($_POST['subject']));</p>

<p>$message    = trim(htmlentities($_POST['message']));</p>

<p>$to         = ACF_EMAIL_RECEIVER;</p>

<p>$header     = "From: $email\r\n" .</p>

<p>"Reply-To: $email\r\n";</p>

<p>$result = Array(</p>

<p>'code'=>0,</p>

<p>'message'=>ACF_ERROR_MESSAGE);</p>

<p>if(!empty($email) AND !empty($message)){</p>

<p>if(@mail($to,$subject,$message,$header)){</p>

<p>$result['code']    = 1;</p>

<p>$result['message'] = ACF_SUCCESS_MESSAGE;</p>

<p>}</p>

<p>}</p>

<p>header('content-type: application/json; charset=utf-8');</p>

<p>echo json_encode($result);</p>

<p>}</p>

<p>exit;</p>

<p>}</p>

<p>?></p>

<p>4. Cara Pakai</p>

<p>Bikin page/halaman dengan slug 'contact' atau lainnya, yang penting harus sesuai dengan ACF_PAGE_SLUG di atas.</p>

<p>Cara 1: Paste langsung di functions.php</p>

<p>Paste code2 diatas di functions.php di folder theme.</p>

<p>Cara 2: Jadikan sebagai plugin.</p>

<p>Jika ingim menjadikan script ini sebagai plugin, sehingga mudah di aktifkan/nonaktifkan. caranya cukup mudah, cukup menambahkan info Plugin Name pada file dan simpan ke folder wp-content/plugins</p>

<p>contoh info plugin</p>

<p><?php</p>

<p>/*</p>

<p>Plugin Name: Ajax Contact Form</p>

<p>Author: takien</p>

<p>Author URI: http://takien.com/</p>

<p>*/</p>

<p>Code lengkap/yang udah jadi plugin bisa di lihat di https://github.com/takien/WordPress-Ajax-Contact-Form</p>
