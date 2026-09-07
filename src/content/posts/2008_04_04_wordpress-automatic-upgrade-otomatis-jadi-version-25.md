---
title: "WordPress Automatic upgrade, otomatis jadi Version 2.5"
date: "2008-04-04T15:53:52+00:00"
categories: ["Tips & Tutorial"]
tags: ["CMS", "Internet", "Website", "WordPress", "upgrade wordpress", "wordpress plugin", "wordpress upgrade"]
slug: "2008/04/04/wordpress-automatic-upgrade-otomatis-jadi-version-25"
legacyUrl: "/2008/04/04/wordpress-automatic-upgrade-otomatis-jadi-version-25/"
comments: []
---

<div class="content-wrap">
					<div class="add">

</div>
<p><a href="/wp-content/uploads/2008/04/wordpress-25-logo.jpg"><img src="/images/2008/04/wordpress-25-logo.jpg" alt="wordpress-25-logo" title="wordpress-25-logo" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>Rasanya terlalu kemaruk kalau setiap upgrade wordpress diposting. Bukankah mengupgrade wordpress atau cms lainnya adalah perbuatan yang lumrah dimana &#8216;<a href="#/stories/upgrade-successful/">setiap orang</a>&#8216; melakukannya!? Tapi kali ini janggal rasanya kalau nggak diposting, karena aku baru saja mendapat pengalaman yang berbeda dalam mengupgrade wordpress. Pertama karena versi terbaru ini (2.5) mempunyai fitur dan tampilan admin yang berbeda, dan yang kedua proses upgrade ini tidak lagi menggunakan <a href="/upgrade-wordpress-bukan-hal-yang-menakutkan/">cara kuno</a> seperti yang kulakukan sebelumnya. </p>
<p>Ya, dengan plugin WordPress Automatic upgrade, proses pembaruan script wordpress menjadi lebih mudah dan cepat, bahkan bisa lebih otomatis lagi kalau kita pilih opsi <span style="text-decoration: underline;">automa</span><span style="text-decoration: underline;">ted version</span>. Langkah pertama adalah dengan mendownload (karena aku nggak suka bilang mengunduh) plugin tersebut <a href="https://web.archive.org/web/20160611164942/http://wordpress.org/extend/plugins/wordpress-automatic-upgrade/">di sini</a>, mengupload dan mengekstraknya ke folder <em>/wp-content/plugins/</em> dan mengaktifkannya di <em>dashboard -&gt; plugins</em>. Kemudian memulai proses upgrade melalui menu <em>Manage -&gt;&gt; Automatic Upgrade.</em> Ada dua pilihan disini:</p>
<p><a href="/wp-content/uploads/2008/04/01-initial-step.jpg"><img src="/images/2008/04/01-initial-step.jpg" alt="" title="01-initial-step-automatic-upgrade" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><br/>
Karena masih baru dalam menggunakan vitur ini, aku memilih yang <em>Click here</em> daripada <em>automated version</em>. Setelah diklik, plugin ini akan memulai membackup file dan menyarankan untuk mendownload backupnya sebelum melanjutkan ke langkah selanjutnya.</p>
<p><a href="/wp-content/uploads/2008/04/02-files-successfully-backed-up-wordpress-automatic-upgrade.jpg"><img src="/images/2008/04/02-files-successfully-backed-up-wordpress-automatic-upgrade.jpg" alt="02-files-successfully-backed-up-wordpress-automatic-upgrade" title="02-files-successfully-backed-up-wordpress-automatic-upgrade" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><br/>
Klik pada <span style="text-decoration: underline;">Click here</span> untuk memulai proses backup database, kemudian klik Sart DB Backup, download backup db nya.</p>
<p><a href="/wp-content/uploads/2008/04/03-download-db-backup-automatic-upgrade2.jpg"><img src="/images/2008/04/03-download-db-backup-automatic-upgrade2.jpg" alt="03-download-db-backup-automatic-upgrade2" title="03-download-db-backup-automatic-upgrade2" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>Klik pada <span style="text-decoration: underline;">CLICK HERE </span>untuk memulai mengambil versi terakhir wordpress.<br/>
<a href="/wp-content/uploads/2008/04/03a-ready-to-download-latest-wordpress-upgrade.jpg"><img src="/images/2008/04/03a-ready-to-download-latest-wordpress-upgrade.jpg" alt="03a-ready-to-download-latest-wordpress-upgrade" title="03a-ready-to-download-latest-wordpress-upgrade" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><br/>
klik <span style="text-decoration: underline;">Let&#8217;s Go</span> untuk mulai mentransfer wordpress terbaru dari http://wordpress.org/latest.zip<br/>
<a href="/wp-content/uploads/2008/04/04-successfully-downloaded-and-unzipped-from-wordpressorg.jpg"><img src="/images/2008/04/04-successfully-downloaded-and-unzipped-from-wordpressorg.jpg" alt="04-successfully-downloaded-and-unzipped-from-wordpressorg" title="04-successfully-downloaded-and-unzipped-from-wordpressorg" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>Proses transfer file wordpress selesai, klik <span style="text-decoration: underline;">CLICK HERE</span> untuk mengeset situs ke maintenance mode. Sukses maitenance mode ditandai dengan pesan berikut ketika mengetikkan alamat url:<br/>
<a href="/wp-content/uploads/2008/04/04-maintenance-mode-wordpress-upgrade.jpg"><img src="/images/2008/04/04-maintenance-mode-wordpress-upgrade.jpg" alt="04-maintenance-mode-wordpress-upgrade" title="04-maintenance-mode-wordpress-upgrade" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p><em>We succesfully completed the task which, Puts the site into maintenance mode. Next Task -&gt; De-activate</em><em>s all the plugins Please <span style="text-decoration: underline;"><span style="color: #0000ff;"><a href="#">CLICK HERE</a></span></span> to go to the next task. </em>( Sorry bagian ini screenshotnya hilang, atau lupa?)<br/>
Klik <span style="text-decoration: underline;">CLICK HERE</span> untuk menonaktifkan semua plugin aktif.<br/>
<a href="/wp-content/uploads/2008/04/05-plugin-have-been-deactivated.jpg"><img src="/images/2008/04/05-plugin-have-been-deactivated.jpg" alt="05-plugin-have-been-deactivated" title="05-plugin-have-been-deactivated" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>Tugas selanjutnya mengupgrade file instalasi, klik <span style="text-decoration: underline;">CLICK HERE</span> untuk mengupgrade file-file.<br/>
<a href="/wp-content/uploads/2008/04/06-complete-final-step-automatic-upgrade-wordpress.jpg"><img src="/images/2008/04/06-complete-final-step-automatic-upgrade-wordpress.jpg" alt="06-complete-final-step-automatic-upgrade-wordpress" title="06-complete-final-step-automatic-upgrade-wordpress" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>*) File upgrade sukses, klik <span style="text-decoration: underline;">CLICK HERE TO COMPLETE THE FINAL STEP</span> (terbuka di jendela baru) untuk menjalankan file <em>/wp-admin/upgrade.php </em>yang bertugas mengupgrade database.</p>
<p><a href="/wp-content/uploads/2008/04/07-upgrade-wordpress-database.jpg"><img src="/images/2008/04/07-upgrade-wordpress-database.jpg" alt="07-upgrade-wordpress-database" title="07-upgrade-wordpress-database" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>Klik, <span style="text-decoration: underline;">Upgra</span><span style="text-decoration: underline;">de WordPress.</span><br/>
<a href="/wp-content/uploads/2008/04/08-upgrade-complete-wordpress.jpg"><img src="/images/2008/04/08-upgrade-complete-wordpress.jpg" alt="08-upgrade-complete-wordpress" title="08-upgrade-complete-wordpress" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><br/>
Continue.</p>
<p><a href="/wp-content/uploads/2008/04/09-wordpress-login.jpg"><img src="/images/2008/04/09-wordpress-login.jpg" alt="09-wordpress-login" title="09-wordpress-login" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><br/>
Login.</p>
<p>Kemudian kembali ke langkah *) di atas, klik pada Please <span style="text-decoration: underline;">CLICK HERE</span> to go to next task untuk mengaktifkan kembali plugin-plugin.</p>
<p><a href="/wp-content/uploads/2008/04/10-upgrade-succes-activate-plugin.jpg"><img src="/images/2008/04/10-upgrade-succes-activate-plugin.jpg" alt="10-upgrade-succes-activate-plugin" title="10-upgrade-succes-activate-plugin" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>Plugin telah kembali aktif, klik pada link <span style="text-decoration: underline;">CLICK HERE</span> untuk melihat bahwa proses upgrade selesai disertai dengan laporan (log) perubahan selama proses upgrade.</p>
<p><a href="/wp-content/uploads/2008/04/12-upgrade-wordpress-done.jpg"><img src="/images/2008/04/12-upgrade-wordpress-done.jpg" alt="12-upgrade-wordpress-done" title="12-upgrade-wordpress-done" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>Selesai! Hmm.. mudah kan, no more than just click, click, and click. Sepertinya plugin Automatic Upgrade ini jadi bawaan WordPress pada versi-versi selanjutnya. Buktinya di versi 2.5 ini WordPress sudah ada fitur Automatic Plugin Update, sehingga proses update plugin bisa dilakukan hanya dengan sekali klik.</p>
<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/cms/">CMS</a> <a class="label label-default" href="/tag/internet/">Internet</a> <a class="label label-default" href="/tag/upgrade-wordpress/">upgrade wordpress</a> <a class="label label-default" href="/tag/website/">Website</a> <a class="label label-default" href="/tag/wordpress/">WordPress</a> <a class="label label-default" href="/tag/wordpress-plugin/">wordpress plugin</a> <a class="label label-default" href="/tag/wordpress-upgrade/">wordpress upgrade</a> </div>										
									</div>
