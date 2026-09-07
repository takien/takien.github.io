---
title: "Mengupdate Drupal, Caraku"
date: "2008-03-31T00:20:34+00:00"
categories: ["Tips & Tutorial"]
tags: ["CMS", "Drupal", "Website"]
slug: "2008/03/31/mengupdate-drupal-caraku"
legacyUrl: "/2008/03/31/mengupdate-drupal-caraku/"
comments: [{"author": "nink", "date": "April 30, 2008 at 6:07 pm", "text": "caranya bikin cms gimana siiiyy???\n\nplissss…. ;-("}, {"author": "Rainbow Studio", "date": "November 21, 2008 at 2:35 pm", "text": "yup! it’s really good"}, {"author": "joy", "date": "February 9, 2009 at 2:02 pm", "text": "makasi boz infonya.."}]
---

<div class="content-wrap">
					<div class="add">

</div>
<p><img src="/images/2008/03/drupalorgpng.jpg" alt="drupal" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" />Udah lama nggak ngomongin <a title="Posting lama, hehe" href="/membuat-custom-block-region-di-drupal/">Drupal</a>, kangen euy. Setelah beberapa waktu lalu release Drupal 5.7 baru kali ini aku sempat mengupdate ke versi tersebut. Tapi kali ini aku gak mengikuti salah satu persyaratan &#8216;wajib&#8217; proses upgrade, <u>backup database</u>; hanya backup file aja hehe. Backup file nya dengan membuat folder <em>lama </em>di public_html dan mengcopy semua file ke folder tersebut. Proses pengcopyan bisa dilakukan dengan mudah (drag-and-drop) , kan menggunakan File Managernya cPanel 11.xx. <span id="more-256"></span></p>
<p><a title="membuat folder baru dengan nama lama" href="/wp-content/uploads/2008/03/001.png"><img src="/images/2008/03/001.png" alt="membuat folder baru dengan nama lama" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>Selepas itu mendownload Drupal terbaru dan mengextract ke folder <em>Drupal-5.7</em><br/>
Hapus semua file yang telah dibackup, kecuali: <em>.htaccess</em>, <em>sites</em>, <em>themes</em>, <em>files </em>( jika ada). Copykan isi folder Drupal-5.7 kecuali .<em>htaccess</em>, <em>sites</em>, dan <em>themes</em> ke <em>public_html.</em></p>
<p>Sepertinya sudah beres, oops.. masih ada yang ketinggalan, yaitu <em>modules</em>. Ya, beberapa modul tambahan yang pernah di instal di Drupal sebelumnya juga perlu di kembalikan. Caranya, kembali ke folder backup <em>lama</em>, kemudian masuk ke folder <em>modules</em>, pilihlah modul yang bukan modul standard Drupal dan kemudian copykan ke folder <em>modules </em>di Drupal yang baru di <em>public_html. </em></p>
<p>Kalau sudah siap, sekarang waktunya eksekusi, hahaha. macam betol aja&#8230;<br/>
Buka tab/window baru dan eksekusi file update.php, e.g. http://example.com/update.php</p>
<p>Oops.. Access Denied, karena belum login sebagai admin, kalau begitu login dulu deh. 🙂</p>
<p><a title="access denied drupal update" href="/wp-content/uploads/2008/03/003.png"><img src="/images/2008/03/003.png" alt="access denied drupal update" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>Kalau males login juga boleh, tapi mesti mengedit file update.php</p>
<pre>// Enforce access checking?
$access_check = TRUE;</pre>
<p>Diganti dengan:</p>
<pre>// Enforce access checking?
$access_check = FALSE;</pre>
<p>Tapi jangan lupa nanti dibalikin lagi ke TRUE setelah selesai.</p>
<p><a title="run the database upgrade script" href="/wp-content/uploads/2008/03/004.png"><img src="/images/2008/03/004.png" alt="run the database upgrade script" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>Setelah tampilan seperti gambar di atas, klik pada <em>run the database upgrade script </em>untuk memulai proses update.</p>
<p><a title="update drupal" href="/wp-content/uploads/2008/03/005.png"><img src="/images/2008/03/005.png" alt="update drupal" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>Klik Update</p>
<p><a title="Drupal updated successfully" href="/wp-content/uploads/2008/03/006.png"><img src="/images/2008/03/006.png" alt="Drupal updated successfully" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>Selesai.</p>
<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/cms/">CMS</a> <a class="label label-default" href="/tag/drupal/">Drupal</a> <a class="label label-default" href="/tag/website/">Website</a> </div>										
									</div>
