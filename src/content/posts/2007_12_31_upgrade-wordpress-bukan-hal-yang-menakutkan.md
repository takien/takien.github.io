---
title: "Upgrade WordPress, Bukan Hal yang Menakutkan"
date: "2007-12-31T00:00:00Z"
categories: ["Wordpress"]
tags: ["upgrade wordpress", "wordpress upgrade"]
slug: "2007/12/31/upgrade-wordpress-bukan-hal-yang-menakutkan"
legacyUrl: "/2007/12/31/upgrade-wordpress-bukan-hal-yang-menakutkan/"
comments: [{"author": "great_ww", "date": "", "text": "pake sistem manual bisa ga yah upgrade nya?\n\nmaksudnya, semua file di server didownload, dan diutak atik scr offline baru setelah beres diupload lagi semua … he he he"}, {"author": "takien.com", "date": "", "text": "@great_ww\n\nkenapa pulak begitu?"}, {"author": "great_ww", "date": "", "text": "@namakamu…\n\nmasih blon sempat & rada2 takut buat upgrade… he he he … thaks btw…"}, {"author": "rizkyonline", "date": "", "text": "kapan2 coba ah"}, {"author": "Ghprod", "date": "", "text": "thnx"}, {"author": "Blog-nya Raja", "date": "", "text": "Pertanyaannya adalah: “Sebutkan nama file tersebut!”"}, {"author": "takien.com", "date": "", "text": "file nya .htaccess"}]
---

<p><figure class="image-missing-placeholder" role="img" aria-label="Wordpress Logo">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Wordpress Logo</span>
  </div>
</figure>Mengupgrade WordPress bukanlah suatu hal yang sulit apalagi menakutkan, meskipun banyak orang yang malas untuk melakukannya. Padahal sudah jelas upgrade ini sangat penting dilakukan secara berkala seiring dengan ditemukannya kesalahan/bug pada versi yang ada. Seperti halnya CMS yang lain, wordpress juga akan memberitahukan jika versi yang kita pakai sudah out-of-date alias perlu diupgrade.</p>
<p>Barusan buka dashboard blog ini, kok rasanya ada yang lain di bagian footer dimana ada kalimat yang menyuruh aku untuk segera mengupdate versi wordpress. Waduh, gak jadi deh acara postingnya, diganti dengan acara upgrade nih. Acara upgrade berarti ada acara backup, download dan upload dong! <span id="more-209"></span>Ya udah deh gak apa-apa.  Lalu aku mempersiapkan peralatan perang yaitu FileZilla yang perlu diinstal lagi (cape deh, karena ini komputer warnet yang pakai deepfreeze, selain FTP portabel aku yang di flashdisk sudah digrogoti virus sehari sebelumnya).</p>
<p>Sesuai dengan anjuran team wordpress, bahwa sebelum mengupgrade kita dianjurkan untuk membackup file lama dan me-nonaktif-kan plugin yang terinstal. Tapi karena aku yakin tidak akan terjadi sesuatu yang tidak diinginkan, aku hanya mendisable plugin, tapi tidak membackup file lama.</p>
<p>Kebetulan aku udah hapal dimana harus download wordpress terbaru, kalau gak di <a href="https://web.archive.org/web/20140717233728/http://wordpress.org/latest.zip" title="Download Latest WordPress in .zip Format" target="_blank">wordpress.org/latest.zip</a> ya <a href="wordpress.org/latest.tar.gz" title="Download Latest WordPress in .tar.gz Format" target="_blank">wordpress.ogr/latest.tar.gz</a>. Tapi entah kenapa lebih memilih yang kedua, secara .tar.gz itu ekstensi file arsip yang biasa digunakan di sistem operasi linux, jadi menurutku lebih keren gitu loh. Setelah selesai download, kemudian file nya ku ekstrak, terus buka <a href="https://web.archive.org/web/20140717233728/http://filezilla-project.org/" title="FileZilla Project Download" target="_blank">FileZilla </a>(perhatian, karakter ke-5 tidak boleh diganti dengan hurup G, apapun alasannya). Menghapus file-file lama kecuali yang ada di folder wp-contents dan file wp-config.php, setelah itu baru mengupload file wordpress versi terbaru.</p>
<p>Setelah proses upload selesai, langkah selanjutya adalah mengeksekusi file <code>wp-admin/upgrade.php</code>  dan kembali mengaktifkan plugin.</p>
<blockquote><p><em> Visit the upgrade page. It will be at a URL like <code>http://example.com/wordpress/wp-admin/upgrade.php</code>. This updates your database to be compatible with the latest code, and before you do this your blog might look funny. </em></p></blockquote>
<p>Wakakakaka, menurutku malah kata-kata tersebut yang funny. Padahal sebenarnya aku nyesal juga nggak sempat melihat bagaimana tampilan blog aku sebelum menjalankan file upgrade.php tadi.  😀 </p>
<p><em>Tambahan:</em><br/>
Setelah tulisan ini selesai diposting ternyata muncul masalah baru, ketika diklik readmore aku malah diberi bonus sebesar $404 alias Not Found. Rupanya waktu asyik menghapus tadi, ada satu file yang tidak mau disebutkan namanya ikut terhapus. Kenapa file tersebut tidak mau disebutkan namanya? Karena memang file tersebut tidak punya nama tapi hanya punya ekstensi saja. 😀 </p>
