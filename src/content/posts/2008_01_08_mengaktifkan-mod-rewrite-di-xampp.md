---
title: "Mengaktifkan Mod Rewrite di XAMPP"
date: "2008-01-08T01:26:33+00:00"
categories: ["Tips & Tutorial"]
tags: ["htaccess", "mod rewrite", "xampp"]
slug: "2008/01/08/mengaktifkan-mod-rewrite-di-xampp"
legacyUrl: "/2008/01/08/mengaktifkan-mod-rewrite-di-xampp/"
comments: []
---

<div class="content-wrap">
					<div class="add">

</div>
<p><a href="https://web.archive.org/web/20160318202710/http://www.apachefriends.org/en/xampp.html" title="Pergi ke Website XAMPP" target="_blank"><img src="/images/2008/01/xampp.jpg" alt="XAMPP Logo" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" />XAMPP </a>adalah webserver opensource yang biasa aku pakai saat ini selain Appserver.  Salah satu kelebihan xammpp adalah portabilitasnya alias mudah dibawa kemana-mana tanpa diinstal. Tapi yang akan aku bahas disini adalah mengaktifkan mod rewrite di xampp. Untuk mengaktifkan mod rewrite apache di xampp tidak terlalu sulit, yang perlu dilakukan hanyalah mengedit file <em>httpd.conf</em> <span id="more-216"></span></p>
<p>Langkah-langkahnya:</p>
<ol>
<li>Buka file  httpd.conf<em> </em>yang berlokasi di <em>xampp\apache\conf\httpd.conf </em>menggunakan text editor tradisional seperti notepad.</li>
<li>Hilangkan tanda komentar ( # ) sebelum baris berikut:
<pre>#LoadModule rewrite_module modules/mod_rewrite.so</pre>
<p>Sehingga menjadi:</p>
<pre>LoadModule rewrite_module modules/mod_rewrite.so</pre>
</li>
<li>Edit baris berikut:
<pre>AllowOverride None</pre>
<p>Menjadi:</p>
<pre>AllowOverride All</pre>
</li>
<li>Restart Apache, Selesai</li>
</ol>
<p><img src="/images/misc/simple-smile.png" alt=":)" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>
<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/htaccess/">htaccess</a> <a class="label label-default" href="/tag/mod-rewrite/">mod rewrite</a> <a class="label label-default" href="/tag/xampp/">xampp</a> </div>										
									</div>
