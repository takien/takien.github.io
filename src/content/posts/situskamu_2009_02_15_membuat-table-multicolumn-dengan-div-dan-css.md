---
title: "Membuat table multicolumn dengan div dan css"
date: "2009-02-15T12:00:00Z"
categories: ["Internet", "Webdesign", "html"]
tags: ["2007", "2008", "blog", "blogger", "Browser", "cara menginstall wordpress", "cari duit", "city", "css", "custom block", "custom region", "div", "domain", "domain parking", "Drupal", "drupal theme", "forum", "Google", "htaccess", "html", "integration", "Internet", "Internet Explorer", "kaleidoskop", "kilas balik", "layout", "mini city", "mod rewrite", "parked domain", "review", "security", "SEO", "SMF", "Spyware", "table", "tutorial wordpress", "upgrade wordpress", "Web 2.0", "Webdesign", "website", "WordPress", "wordpress plugin", "Wordpress theme", "wordpress upgrade", "xampp"]
slug: "2009/02/15/membuat-table-multicolumn-dengan-div-dan-css"
legacyUrl: "/membuat-table-multicolumn-dengan-div-dan-css/"
source: "blog.situskamu.com"
comments: [
  {
    "author": "Anonymous",
    "date": "May 7, 08 at 3:52 pm",
    "text": "kalau salah satu kolomnya ada yg di merge cell nya gmana bro ngakalinnya ?\n\nmisal kolom 2 di merge ama kolom 3 tapi cuma di baris ke 2…ngerti kan ?  \n\nklau table yg di atas kan table umum\n\nmohon penjelasan suhu…\n\nnamakamu reply on May 7th, 2008:\n\nBisa aja, itu namanya colspan.\n\nKita ambil contoh baris pertama, colom ke satu dan kedua mau di merge (span).\n\naslinya:\n\n<div class=“baris”>\n\n<div class=“kolom”>1</div>\n\n<div class=“kolom”>2</div>\n\ndirubah menjadi:\n\n <div class=“baris”>\n\n<div class=“kolomspan”>1</div>\n\nkolom2 harus dihapus, karena kita anggap sudah merged dengan kolom 1  \n\ndi cssnya kita tambahkan..\n\n\n\n.kolomspan {\n\nwidth: 24.4px; /* jumlah width kol 1 dengan kol 2 */\n\nfloat:left\n\n}"
  },
  {
    "author": "Anonymous",
    "date": "May 7, 08 at 5:53 pm",
    "text": "What the hell about DIV CSS\n\ni dont understand what are you talking about  ….\n\nGreat Tutorial Bro\n\ni Love you\n\nnamakamu reply on May 7th, 2008:\n\n      \n\nchika-mela-santi.3gp reply on May 7th, 2008:\n\ni love you to\n\nwakakakakak\n\npotoseleb reply on May 9th, 2008:\n\nme too\n\nwakakaka"
  },
  {
    "author": "Anonymous",
    "date": "May 8, 08 at 4:03 pm",
    "text": "wah lengkap tutorialnya… thanks brooo"
  },
  {
    "author": "Anonymous",
    "date": "May 8, 08 at 6:46 pm",
    "text": "Kayaknya malah lebih banyak tag nya deh, alasan menggunakan div sbg pengganti layout table ditujukan untuk mengurangi jumlah tag, sehingga diharapkan dokumen di donlot bisa lbh cepat.\n\nkayak gitu deh, maaf klo salah he he\n\nnamakamu reply on May 9th, 2008:\n\nhaha.. untuk contoh ini mungkin ya.., tapi kan masih div,  gak ada table, tr, td.  \n\ntapi entarnya kalau ada yang table di dalam table gitu pasti lebih enak pake div kan  \n\neh, link segera dipasang, tengkyu.\n\nbimoweb.com reply on May 10th, 2008:\n\nsudah saya pasang bos, silahkan di cek di blogrollnya\n\nnama link nya blog situs kamu\n\nbtw tolong label situsku diganti jadi\n\nbimoweb[dot]com\n\nhe he tenkyu bos"
  },
  {
    "author": "Anonymous",
    "date": "Jun 6, 08 at 8:06 pm",
    "text": "waw infonya keren nih, mau coba ah  \n\nnamakamu reply on June 11th, 2008:\n\nhehe"
  },
  {
    "author": "Anonymous",
    "date": "Jan 26, 09 at 9:34 pm",
    "text": "mas menurut saya klo untuk buat table di dalam kontent website lebih pas n mudah pake tag table dech… soalnya khan emang itu fungsi utama dari tag table, dan sepertinya lebih mudah.\n\nklo layout baru pake div+CSS\n\nnamakamu reply on January 27th, 2009:\n\niya sih bener juga  \n\nlagian sebenernya belakangan jadi tahu klu ada yang lebih simple dari contoh diatas..\n\nheh"
  },
  {
    "author": "Anonymous",
    "date": "Mar 30, 09 at 11:00 am",
    "text": "Kalau ada background-nya gimana caranya????"
  }
]
---

<figure class="image-missing-placeholder" role="img" aria-label="table-css.gif">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">table-css.gif</span>
  </div>
</figure>Perlahan namun pasti, penggunaan tag table dalam sebuah website sudah mulai ditinggalkan baik itu dalam membuat layout maupun kontent website itu sendiri. Bahkan pembuatan layout tanpa table sudah sangat lumrah kita jumpai dan menjadi suatu keharusan saat dengan alasan file size menjadi lebih kecil dan tentu saja mempengaruhi waktu load. Apalagi dengan diluncurkannya standard <a href="https://web.archive.org/web/20090421000646/http://code.google.com/p/blueprintcss/">Blueprint CSS Framework</a> oleh google code yang jelas membantu para web designer untuk membuat multicolumn div, div column span dan masih banyak lagi yang dulunya hanya bisa dilakukan jika menggunakan tabel. <span id="more-133"></span>Namun yang akan aku bahas adalah membuat table untuk isi website menggunakan div. <em>(Untuk membuat tableless layout, lihat referensi di akhir post ini)</em></p>
<p><span style="color: #ffffff;">.</span></p>
<p>Beralih ke table dalam kontent website, sebenarnya ada toolsnya yakni <a href="/table-to-css-converter-convert-table-to-div-in-seconds/">&#8220;table2css converter&#8221;</a> yang bisa langsung mengkonvert table menjadi div hanya dengan beberapa klik. Namun sayangnya  tool ini hanya bisa membuat tabel statik dengan ukuran-ukuran absolut. Bagaimana jika table tersebut merupakan table dinamis, multicolumn, multirow seperti daftar harga barang, statistik atau member, dimana data diambil secara loop dari database?</p>
<p><span style="color: #ffffff;">.</span></p>
<p>Berikut contoh membuat tabel div yang mempunyai 8 kolom (columns) dan 2 baris (rows).</p>
<p><span style="color: #ffffff;">.</span></p>
<p><em>Pertama,</em> buat kontainer yang bertidak sebagai &lt;table&gt; &lt;/table&gt;.</p>
<pre style="padding-left: 30px;"><span style="color: #0000ff;">&lt;div class=</span><span style="color: #3366ff;">"kontainer"</span><span style="color: #0000ff;">&gt;&lt;/div&gt;</span></pre>
<p>Properti css nya adalah:</p>
<pre style="padding-left: 30px;"><span style="color: #ff00ff;">.kontainer {</span>
<span style="color: #0000ff;">width</span><span style="color: #ff00ff;">:</span><span style="color: #3366ff;">100%</span><span style="color: #ff00ff;">;</span> <span style="color: #808080;">   /* penuh layar atau fluid/flexible, gunakan ukuran px untuk fixed width */</span>
<span style="color: #0000ff;">margin</span><span style="color: #ff00ff;">:</span><span style="color: #3366ff;">0 auto</span><span style="color: #ff00ff;">;</span> <span style="color: #808080;">/* opsional, supaya table berada di tengah jika dalam mode fixed,*/
               /* bertindak seperti &lt;table align="center"&gt;*/</span>
<span style="color: #0000ff;">border</span><span style="color: #ff00ff;">:</span> <span style="color: #3366ff;">1px solid #000</span> <span style="color: #808080;">/* border, opsional */</span>
<span style="color: #ff00ff;">}</span></pre>
<p><em>Kedua, </em>tambahkan row/baris di dalam div kontainer tadi, yang bertindak sebagai &lt;tr&gt;&lt;/tr&gt;.</p>
<pre style="padding-left: 30px;"><span style="color: #0000ff;">&lt;div class=<span style="color: #3366ff;">"</span></span><span style="color: #3366ff;">kontainer"</span><span style="color: #0000ff;">&gt;
   &lt;div class=</span><span style="color: #3366ff;">"baris"</span><span style="color: #0000ff;">&gt;&lt;/div&gt;</span>
<span style="color: #0000ff;">&lt;/div&gt;</span></pre>
<p>Properti cssnya:</p>
<pre style="padding-left: 30px;"><span style="color: #ff00ff;">.baris {</span>
<span style="color: #0000ff;">width</span><span style="color: #ff00ff;">:</span> <span style="color: #3366ff;">100% </span><span style="color: #808080;">   /* harus 100% supaya penuh ke area table */</span>
}</pre>
<p><em>Ketiga, </em>tambahkan beberapa kolom (contoh ini 8 kolom) diantara div baris tadi, yang bertindak sebagai &lt;td&gt;&lt;/td&gt;.</p>
<pre style="padding-left: 30px;"><span style="color: #0000ff;">&lt;div class=<span style="color: #3366ff;">"</span></span><span style="color: #3366ff;">kontainer"</span><span style="color: #0000ff;">&gt;
   &lt;div class=</span><span style="color: #3366ff;">"baris"</span><span style="color: #0000ff;">&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>1<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>2<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>3<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>4<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>5<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>6<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>7<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>8<span style="color: #0000ff;">&lt;/div&gt;
   &lt;/div&gt;
   &lt;div style="clear</span><span style="color: #ff00ff;">:</span> <span style="color: #3366ff;">both</span><span style="color: #ff00ff;">;</span><span style="color: #0000ff;">" /&gt;</span><span style="color: #808080;"> &lt;!-- tambahkan ini, supaya div kontainer
                                melingkupi semua div yang ada di dalamnya --&gt;</span>
<span style="color: #0000ff;">&lt;/div&gt;</span></pre>
<p>Properti css nya:</p>
<pre style="padding-left: 30px;"><span style="color: #ff00ff;">.kolom {</span>
<span style="color: #0000ff;">width</span><span style="color: #ff00ff;">:</span> <span style="color: #3366ff;">12.2%</span><span style="color: #ff00ff;">;</span> <span style="color: #808080;">/* pembagian 100% dengan 8 kolom, seharusnya 12.5%, */
              /* diberikan kompensasi seperlunya karena penggunaan margin,*/</span>
              <span style="color: #808080;">/* padding maupun border nantinya akan mempengaruhi lebar kolom */</span>
<span style="color: #0000ff;">float</span><span style="color: #ff00ff;">:</span> <span style="color: #3366ff;">left</span><span style="color: #ff00ff;">;</span>  <span style="color: #808080;">/* kolom yang lebih duluan akan ditempatkan di kiri, begitu seterusnya */</span>
}</pre>
<p><span style="color: #ffffff;">.</span></p>
<p><em>Berikut screenshot hasil sementara:</em></p>
<p><em></em><span style="color: #ffffff;">.</span><br/>
<figure class="image-missing-placeholder" role="img" aria-label="dbmnuw.gif">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">dbmnuw.gif</span>
  </div>
</figure>
<p><span style="color: #ffffff;">.</span></p>
<p>Untuk menambahkan baris lainnya, baris kedua, ketiga dan seterusnya, cukup ulangi div baris beserta div kolom sebanyak baris yang diperlukan. Berikut contoh setelah diatambahkan baris (baris ke 2):</p>
<pre style="padding-left: 30px;"><span style="color: #0000ff;">&lt;div class=<span style="color: #3366ff;">"</span></span><span style="color: #3366ff;">kontainer"</span><span style="color: #0000ff;">&gt;
   &lt;div class=</span><span style="color: #3366ff;">"baris"</span><span style="color: #0000ff;">&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>1<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>2<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>3<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>4<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>5<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>6<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>7<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>8<span style="color: #0000ff;">&lt;/div&gt;
   &lt;/div&gt;</span>
   <span style="color: #0000ff;">&lt;div class=</span><span style="color: #3366ff;">"baris"</span><span style="color: #0000ff;">&gt;</span> <span style="color: #808080;">&lt;!-- baris ke dua --&gt;</span>
<span style="color: #0000ff;">      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>1<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>2<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>3<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>4<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>5<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>6<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>7<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>8<span style="color: #0000ff;">&lt;/div&gt;
   &lt;/div&gt;</span>
<span style="color: #0000ff;">&lt;div style="clear</span><span style="color: #ff00ff;">:</span> <span style="color: #3366ff;">both</span><span style="color: #ff00ff;">;</span><span style="color: #0000ff;">" /&gt;</span><span style="color: #808080;"> &lt;!-- jangan lupa untuk selalu menempatkan tag ini
                             sebelum penutup div kontainer --&gt;</span>
<span style="color: #0000ff;">&lt;/div&gt;</span></pre>
<p><span style="color: #ffffff;">.</span></p>
<p>Kode lengkapnya adalah:</p>
<p><span style="color: #ffffff;">.</span></p>
<pre style="padding-left: 30px;"><span style="color: #0000ff;">&lt;!DOCTYPE HTML PUBLIC <span style="color: #3366ff;">"</span></span><span style="color: #3366ff;">-//W3C//DTD HTML 4.01 Transitional//EN"</span>
<span style="color: #3366ff;">"http://www.w3.org/TR/html4/loose.dtd"</span><span style="color: #0000ff;">&gt;</span>
<span style="color: #0000ff;">&lt;html&gt;
&lt;head&gt;
&lt;meta http-equiv=<span style="color: #3366ff;">"</span></span><span style="color: #3366ff;">Content-Type"</span> <span style="color: #0000ff;">content=</span><span style="color: #3366ff;">"text/html; charset=iso-8859-1"</span><span style="color: #0000ff;">&gt;</span>
<span style="color: #0000ff;">&lt;title&gt;</span>Contoh Table menggunakan div<span style="color: #0000ff;">&lt;/title&gt;</span>
<span style="color: #800000;">&lt;style type=</span><span style="color: #008000;">"text/css"</span><span style="color: #800000;">&gt;</span>
<span style="color: #ff00ff;">.kontainer {</span>
<span style="color: #0000ff;">width</span><span style="color: #ff00ff;">:</span><span style="color: #3366ff;">100%</span><span style="color: #ff00ff;">;</span> <span style="color: #808080;">   /* penuh layar atau fluid/flexible, gunakan ukuran px untuk fixed width */</span>
<span style="color: #0000ff;">margin</span><span style="color: #ff00ff;">:</span><span style="color: #3366ff;">0 auto</span><span style="color: #ff00ff;">;</span> <span style="color: #808080;">/* opsional, supaya table berada di tengah jika dalam mode fixed,*/
               /* bertindak seperti &lt;table align="center"&gt;*/</span>
<span style="color: #0000ff;">border</span><span style="color: #ff00ff;">:</span> <span style="color: #3366ff;">1px solid #000</span> <span style="color: #808080;">/* border, opsional */</span>
<span style="color: #ff00ff;">}</span>
<span style="color: #ff00ff;">.baris {</span>
<span style="color: #0000ff;">width</span><span style="color: #ff00ff;">:</span> <span style="color: #3366ff;">100% </span><span style="color: #808080;">   /* harus 100% supaya penuh ke area table */</span>
<span style="color: #ff00ff;">}</span>
<span style="color: #ff00ff;">.kolom {</span>
<span style="color: #0000ff;">width</span><span style="color: #ff00ff;">:</span> <span style="color: #3366ff;">12.2%</span><span style="color: #ff00ff;">;</span> <span style="color: #808080;">/* pembagian 100% dengan 8 kolom, seharusnya 12.5%, */
              /* diberikan kompensasi seperlunya karena penggunaan margin,*/</span>
              <span style="color: #808080;">/* padding maupun border nantinya akan mempengaruhi lebar kolom */</span>
<span style="color: #0000ff;">float</span><span style="color: #ff00ff;">:</span> <span style="color: #3366ff;">left</span><span style="color: #ff00ff;">;</span>  <span style="color: #808080;">/* kolom yang lebih duluan akan ditempatkan di kiri, begitu seterusnya */</span>
<span style="color: #ff00ff;">}</span>
<span style="color: #800000;">&lt;/style&gt;</span>
<span style="color: #0000ff;">&lt;/head&gt;</span>

<span style="color: #0000ff;">&lt;body&gt;</span>
<span style="color: #0000ff;">&lt;div class=<span style="color: #3366ff;">"</span></span><span style="color: #3366ff;">kontainer"</span><span style="color: #0000ff;">&gt;
   &lt;div class=</span><span style="color: #3366ff;">"baris"</span><span style="color: #0000ff;">&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>1<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>2<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>3<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>4<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>5<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>6<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>7<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>8<span style="color: #0000ff;">&lt;/div&gt;
   &lt;/div&gt;</span>
   <span style="color: #0000ff;">&lt;div class=</span><span style="color: #3366ff;">"baris"</span><span style="color: #0000ff;">&gt;</span> <span style="color: #808080;">&lt;!-- baris ke dua --&gt;</span>
<span style="color: #0000ff;">      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>1<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>2<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>3<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>4<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>5<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>6<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>7<span style="color: #0000ff;">&lt;/div&gt;
      &lt;div class=</span><span style="color: #3366ff;">"kolom"</span><span style="color: #0000ff;">&gt;</span>8<span style="color: #0000ff;">&lt;/div&gt;
   &lt;/div&gt;</span>
<span style="color: #0000ff;">&lt;div style="clear</span><span style="color: #ff00ff;">:</span> <span style="color: #3366ff;">both</span><span style="color: #ff00ff;">;</span><span style="color: #0000ff;">" /&gt;</span><span style="color: #808080;"> &lt;!-- jangan lupa untuk selalu menempatkan tag ini
                             sebelum penutup div kontainer --&gt;</span>
<span style="color: #0000ff;">&lt;/div&gt;</span>
<span style="color: #0000ff;">&lt;/body&gt;
&lt;/html&gt;</span></pre>
<p><span style="color: #ffffff;">.</span></p>
<p>Sesuaikan style tambahan seperti warna background, border, text dan sabagainya. Selanjutnya, untuk pengisian data bisa menggunakan parameter-parameter php sesuai dengan kebutuhan.</p>
<p><span style="color: #ffffff;">.</span></p>
<p>Dalam contoh ini sengaja menggunakan<em> </em>atribut <em>class </em>bukan <em>id </em>dalam mengidentifikasi css properties karena sesuai dengan standard <a href="https://web.archive.org/web/20090421000646/http://www.w3.org/TR/REC-html40/struct/global.html#h-7.5.2">W3C </a>bahwa id adalah harus unik untuk menamai suatu elemen dalam sebuah halaman web.</p>
<p><span style="color: #ffffff;">.</span></p>
<p>Demo: <a href="/wp-content/uploads/8kolom.htm" target="_blank">Klik di sini</a><br/>
Download: <a href="/wp-content/uploads/8kolom.zip" target="_blank">Klik di sini</a></p>
<p><span style="color: #ffffff;">.</span></p>
<p>Sementara untuk tutorial membuat layout menggunakan css lihat referensi ini:</p>
<p><a href="https://web.archive.org/web/20090421000646/http://kusaeni.com/blog/blueprint-css">http://kusaeni.com/blog/blueprint-css</a><br/>
<a href="https://web.archive.org/web/20090421000646/http://bimoweb.com/layout-web-tanpa-tabel-untuk-ajax.html">http://bimoweb.com/layout-web-tanpa-tabel-untuk-ajax.html</a></p>
