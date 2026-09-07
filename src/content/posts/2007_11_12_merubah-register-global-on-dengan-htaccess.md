---
title: "Merubah Register Global On dengan .htaccess?"
date: "2007-11-12T11:22:47+00:00"
categories: ["Article"]
tags: ["htaccess"]
slug: "2007/11/12/merubah-register-global-on-dengan-htaccess"
legacyUrl: "/2007/11/12/merubah-register-global-on-dengan-htaccess/"
comments: []
---

<div class="content-wrap">
					<div class="add">

</div>
<p>Beberapa script CMS ada yang mengharuskan kita mengeset Register Global ke posisi On. Namun, karena alasan security, sebagian besar webhosting telah mengeset register global Off, meskipun kita masih bisa mengeditnya dari file php.ini (pada baris, <em>register_globals=on</em>) tapi ada beberapa hosting yang tidak mengizinkan kita mengedit file tersebut.</p>
<p>Untuk mengatasinya kita bisa memasukkan parameter tertentu di file .htaccess (biasa terdapat di root folder situs). Pada file .htaccess tersebut tambahkan baris berikut:</p>
<blockquote><p><em>php_flag register_globals on</em></p></blockquote>
<p>Trik ini tidak boleh terapkan di server yang menjalankan phpsuexec kecuali anda mau menerima bonus sebesar Rp. 500,- setiap membuka situs. (Maksudnya 500 Internal Server Error <img src="/images/misc/simple-smile.png" alt=":)" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /> )</p>
<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/htaccess/">htaccess</a> </div>										
									</div>
