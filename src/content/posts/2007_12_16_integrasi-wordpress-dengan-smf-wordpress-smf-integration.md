---
title: "Integrasi WordPress dengan SMF (WordPress + SMF Integration)"
date: "2007-12-16T00:00:00.000Z"
categories: ["SMF","Wordpress"]
tags: ["SMF","Wordpress","blog","forum","integration"]
slug: "2007/12/16/integrasi-wordpress-dengan-smf-wordpress-smf-integration"
legacyUrl: "/2007/12/16/integrasi-wordpress-dengan-smf-wordpress-smf-integration/"
source: "takien.com"
author: "takien"
comments: [{"author":"rie","date":"","text":"iseng2 coba ah…"},{"author":"Loki Dan","date":"","text":"asli bro, bagus infonya, sayang mo UAN uda ga bisa ngebikin2 website lagi."},{"author":"rizkyonline","date":"","text":"asli bro\n\nmumet bacanya  he he\n\n\nmending tut intgerasi chika ama blogspot ada gak   \n\n\n:kaborrr…:"},{"author":"Leon","date":"","text":"wah sori ga minta ijin dulu.. blognya ga buat dipublish koq.. \n\n\nko bisa ya ada komentarnya disini?"},{"author":"arie","date":"","text":"bro SMF ama PhpBB bagusan mane? Bingung pilih antara itu…"},{"author":"takien.com","date":"","text":"bagusan SMF dong.."},{"author":"supernando","date":"","text":"bro ada plugin buat smileynya buat smf n wp jd otomatis bisa dipake 2 2nya , thx ya bro infonya  nice blog .."},{"author":"takien.com","date":"","text":"#supernando\n\nwah.. lom tau bro.. hehueh\n\nlom pernah coba seh.. cuba aja browsing,.. ntar sharing"},{"author":"grand","date":"","text":"wah malah rusak bro jadi hilang semua"},{"author":"takien.com","date":"","text":"masa sih, apanya yang ilang bro"},{"author":"toto","date":"","text":"Seep!… keren brow!…"},{"author":"takien.com","date":"","text":"Ingat, baca-baik urutannya.\n\njangan keburu ngeklik Integrate Previous Users setelah aktifasi plugin di WordPress sebelum menginstal plugin bridgenya di SMF…\n\n\nPengalamanku baru-baru ini plugin jadi gak jalan / member tidak terintegrasi dengan benar.\n\n\nmakasih"},{"author":"yudi","date":"","text":"mas link ini http://www.earthorbit.com/opensource/SMF_Wordpress_1.09.zip error mas. dimana saya dapet download filenya ato tolong donk kirim ke saya lewat email aja.\n\n\nthanks ya mas"},{"author":"Review Squad","date":"","text":"mangstabs boss tipsnya!! ini yg gw cari2… hehe\n\n(Y) (Y) (Y)"},{"author":"javanesse","date":"","text":"boz….ketika sy c0ba konfig plugin wp_smf,terjadi eror dan minta l0gin ulang pada admin wp….tapi saya coba l0gin katanya user n0t f0und…gimana s0lusinya b0z??wp yg saya gunakan versi 2.8 . Dan satu lagi…plugin buat smfnya mana ni b0z…linknya er0r"},{"author":"vincent87","date":"","text":"walah tambah rusak forumku g bisa login sama sekali malahan"},{"author":"Fonsms","date":"","text":"Very nice http://www.turkarama.de/"},{"author":"takien.com","date":"","text":"o iya..\n\nsepertinya situsnya down…\n\n\ncoba ini\n\nhttp://downloads.wordpress.org/plugin/wp-smf-a-simplemachines-bridge.1.09.zip"},{"author":"yudi","date":"","text":"kalo yang itu (plugin utk WP) dah dapat mas. yg utk diinstal di smf-nya yg belum dapat (mod-nya). bisa didapat dimana ya? kalo mas punya email ke saya donk\n\n\nthanks"}]
---

<img src="/images/2007/12/wp-smf.png" alt="Wordpress SMF Integration" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" />

<p>Istilah WordPress dan SMF barangkali sudah tidak asing lagi di telinga kita, terutama bagi orang yang  pernah membuat blog dan maupun forum. Selain gratis, opensource, populer, keduanya juga mudah digunakan pastinya. Tapi yang mau saya tulis di sini bukanlah pengertian maupun perbedaan kedua CMS tersebut, melainkan bagaimana keduanya bisa &#8216;disatukan&#8217; atau istilah kerennya diintegrasikan.</p>
<p>Hasil apakah yang akan didapat setelah proses penggabungan? Akankah melahirkan sebuah spesies baru di dunia per-CMS-an?  He he, tidak lucu kalau dibilang  spesies  baru. Yang jelas kedua cms tersebut bisa saling &#8216;berkomunikasi&#8217; satu sama lainnya, seperti pengunjung yang mendaftar/login di blog wordpress otomatis akan terdaftar/login juga di forum SMF, begitu juga sebaliknya. Selain itu statistik forum (posting terakhir, jumlah member dsb) bisa ditampilkan di blog.</p>
<p><span id="more-199"></span></p>
<p>Untuk penggabungan keduanya pastikan wordpress maupun SMF sudah terinstall dengan baik. Sebaiknya install wordpress di root directory  dan SMF install di subfoldernya (misalnya /forum).</p>
<ol>
<li>Install plugin <a href="https://web.archive.org/web/20140915081622/http://www.earthorbit.com/opensource/WP_SMF_1.09.zip" title="Install di WordPress">WP_SMF Bridge</a> di wordpress. Extract dan upload plugin ke folder wp-content/plugins/kemudian aktifkan dari plugins panel.<br/>
<a href="/wp-content/uploads/2007/12/wp-smf-plugin.png" title="Wordpress SMF Integration"><img src="/images/2007/12/wp-smf-plugin-150x150.png" alt="Wordpress SMF Integration" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><br/>
</a>Masih di plugins panel, akan terdapat menu baru bernama SMF, klik untuk melakukan konfigurasi.<br/>
<a href="/wp-content/uploads/2007/12/smf-wp-plugin3.png" title="Wordpress SMF Integration"><img src="/images/2007/12/smf-wp-plugin3-150x150.png" alt="Wordpress SMF Integration" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><br/>
</a>Tentukan folder dimana kita menginstall SMF yaitu folder /forum, kemudian klik <span style="font-style: italic">Update SMF Integration Options </span>(lihat gambar di atas). Pastikan muncul tulisan <span style="font-style: italic">WP_SMF Bridge is Connected</span>.<br/>
Sampai di sini dulu, sekarang kita ke admin page nya SMF.<br/>
<a href="/wp-content/uploads/2007/12/wp-smf-plugin.png" title="Wordpress SMF Integration"><br/>
</a></li>
<li>Login ke admin SMF,   install plugin <a href="https://web.archive.org/web/20140915081622/http://www.earthorbit.com/opensource/SMF_Wordpress_1.09.zip" title="Install di SMF" target="_blank">SMF_Wordpress</a> kemudian aktifkan.<br/>
<a href="/wp-content/uploads/2007/12/smf-wp-plugin.png" title="SMF wordpress integration"><img src="/images/2007/12/smf-wp-plugin-150x150.png" alt="SMF wordpress integration" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><a href="/wp-content/uploads/2007/12/smf-wp-plugin2.png" title="SMF wordpress integration"><img src="/images/2007/12/smf-wp-plugin2-150x150.png" alt="SMF wordpress integration" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><br/>
</a>Selesai untuk SMF, tidak ada konfigurasi yang perlu diset disini, kemudian kembali lagi ke admin WordPress. (bolak-balik, cape deh <img src="/images/misc/icon_smile.gif" alt=":)" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /> )<a href="/wp-content/uploads/2007/12/smf-wp-plugin2.png" title="SMF wordpress integration"><br/>
</a></li>
<li>Mengintegrasikan user wordpress dengan user SMF.<br/>
Kembali ke halaman di langkah no 1, klik <span style="font-style: italic">Integrate Previous Users, </span>penggabungan user berhasil ditandai dengan tulisan <span style="font-style: italic">Previous Users Are Integrated.<br/>
</span><a href="/wp-content/uploads/2007/12/smf-wp-plugin4.png" title="SMF wordpress integration"><img src="/images/2007/12/smf-wp-plugin4-150x150.png" alt="SMF wordpress integration" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /> </a><a href="/wp-content/uploads/2007/12/smf-wp-plugin5.PNG" title="SMF wordpress integration"><img src="/images/2007/12/smf-wp-plugin5-150x150.PNG" alt="SMF wordpress integration" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><a href="/wp-content/uploads/2007/12/smf-wp-plugin4.png" title="SMF wordpress integration"><br/>
</a><span style="font-style: italic"><br/>
</span></li>
<li>Menampilkan statistik forum SMF di blog WordPress.<br/>
Ini adalah langkah terakhir dalam proses integrasi ini.  Masih di halaman yang sama klik <span style="font-style: italic">Theme Integration </span>yang akan menampilkan kode variabel-variabel php untuk memanggil beberapa informasi statistik forum untuk ditampilkan ke blog.<br/>
Yang perlu dilakukan adalah menyalin baris-baris kode tersebut ke theme blog dimana statistik akan ditampilkan, sebaiknya di sidebar.<br/>
&#8211; Menampilkan pesan terbaru</p>
<pre>    &lt;?php

    echo SMF_EnSonBasliklar<span style="color: #006600; font-weight: bold">

    (</span><span style="color: #0000ff">$limit</span>=<span style="color: #800000">10</span>,<span style="color: #800000">'&lt;ul&gt;'</span>,<span style="color: #800000">'&lt;li&gt;'</span>,<span style="color: #800000">'&lt;/li&gt;'</span>,<span style="color: #800000">'&lt;/ul&gt;'</span><span style="color: #006600; font-weight: bold">) </span>

    ?&gt;</pre>
<p>&#8211; Menampilkan topik terbaru</p>
<pre>   &lt;?php

   echo SMF_EnSonMesajlar<span style="color: #006600; font-weight: bold">

   (</span><span style="color: #0000ff">$limit</span>=<span style="color: #800000">10</span>,<span style="color: #800000">'&lt;ul&gt;'</span>,<span style="color: #800000">'&lt;li&gt;'</span>,<span style="color: #800000">'&lt;/li&gt;'</span>,<span style="color: #800000">'&lt;/ul&gt;'</span><span style="color: #006600; font-weight: bold">)

</span>   ?&gt;</pre>
<p>&#8211; Menampilkan member terbaru</p>
<pre>   &lt;?php echo SMF_EnSonUyeler

<span style="color: #006600; font-weight: bold">   (</span><span style="color: #0000ff">$limit</span>=<span style="color: #800000">10</span>,<span style="color: #800000">'&lt;ul&gt;'</span>,<span style="color: #800000">'&lt;li&gt;'</span>,<span style="color: #800000">'&lt;/li&gt;'</span>,<span style="color: #800000">'&lt;/ul&gt;'</span><span style="color: #006600; font-weight: bold">)

</span>   ?&gt;</pre>
<p>&#8211; Menampilkan statistik forum</p>
<pre>   &lt;?php

   echo SMF_ForumIstatistik<span style="color: #006600; font-weight: bold">

   (</span><span style="color: #800000">'&lt;ul&gt;'</span>,<span style="color: #800000">'&lt;li&gt;'</span>,<span style="color: #800000">'&lt;/li&gt;'</span>,<span style="color: #800000">'&lt;/ul&gt;'</span><span style="color: #006600; font-weight: bold">) </span>

   ?&gt;</pre>
</li>
<li>Sekarang mesin wordpress dan SMF sudah terintegrasi, supaya lebih &#8216;nyatu&#8217; sesuaikan juga penampilan template/theme nya.</li>
</ol>
