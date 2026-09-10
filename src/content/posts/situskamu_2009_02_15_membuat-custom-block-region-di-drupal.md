---
title: "Membuat Custom Block Region di Drupal"
date: "2009-02-15T12:00:00.000Z"
categories: ["Drupal"]
tags: ["2007","2008","blog","blogger","Browser","cara menginstall wordpress","cari duit","city","css","custom block","custom region","div","domain","domain parking","Drupal","drupal theme","forum","Google","htaccess","html","integration","Internet","Internet Explorer","kaleidoskop","kilas balik","layout","mini city","mod rewrite","parked domain","review","security","SEO","SMF","Spyware","table","tutorial wordpress","upgrade wordpress","Web 2.0","Webdesign","website","WordPress","wordpress plugin","Wordpress theme","wordpress upgrade","xampp"]
slug: "2009/02/15/membuat-custom-block-region-di-drupal"
legacyUrl: "/2009/02/15/membuat-custom-block-region-di-drupal/"
source: "blog.situskamu.com"
author: "takien"
comments: [{"author":"Anonymous","date":"Jan 9, 08 at 9:58 pm","text":"makasih ya, backlink nya,,sering2 mampir blog gw,,bravo indonesia"},{"author":"Anonymous","date":"Jan 12, 08 at 2:50 am","text":"maknyuss"},{"author":"Anonymous","date":"Jan 18, 08 at 9:08 pm","text":"hehehe drupal yah…… mau dong……  ntar buat ah….."},{"author":"Anonymous","date":"Jan 19, 08 at 11:15 am","text":"kapok main2 drupal…hehe"},{"author":"Anonymous","date":"Mar 31, 08 at 12:20 am","text":"[...] lama nggak ngomongin Drupal, kangen euy. Setelah beberapa waktu lalu release Drupal 5.7 baru kali ini aku sempat mengupdate ke [...]"},{"author":"Anonymous","date":"Jun 10, 08 at 9:57 am","text":"thanks banget ilmunya… blognya sudah pasti saya bookmark coz’ ini blog sangat bermanfaat sekali  \n\nnamakamu reply on June 11th, 2008:\n\nHehe tengkyu.."},{"author":"Anonymous","date":"Aug 13, 08 at 11:41 am","text":"menarik sekali contentnya, semakin menambah wawasan sy di drupal, thanks yah.  \n\nnamakamu reply on August 15th, 2008:\n\nhehe.. main drupal juga ya"}]
---

<p><figure class="image-missing-placeholder" role="img" aria-label="Drupal logo, drupal">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Drupal logo, drupal</span>
  </div>
</figure>Block region adalah area di Drupal yang bisa digunakan untuk menampilkan content tertentu misalnya text ataupun modul seperti chatbox, banner, link dan sebagainya. Konfigurasi Block ini bisa diakses melaui panel administer ( situskamu.com/admin/build/block). Meskipun jumlah block yang dapat kita tambahkan dalam sebuah region block tidak terbatas, tapi jumlah regionnya sendiri adalah terbatas. Banyaknya region block tergantung dengan template yang digunakan misalnya header, sidebar, content top/bottom, dan footer. Dalam kasus tertentu jumlah block region ini sangat terbatas, untuk itu kita perlu membuat block region baru.  <span id="more-57"></span></p>
<p>Untuk membuat block region baru, yang perlu kita lakukan adalah mengedit beberapa file template yang kita gunakan. Langkah-langkahnya:</p>
<ol>
<li>Buka file template.php di folder themes, temukan baris-baris berikut:


```
// regions for nama_template
function nama_template_regions() {
    return array(
    'left' =&gt; t('left sidebar'),
    'content_top' =&gt; t('content top'),
    'content_top_right' =&gt; t('content top right'),
    'content_bottom' =&gt; t('content bottom'),
    'content_header' =&gt; t('header'),
    );
}
```

<p>Sisipkan nama region baru yang akan ditambahkan diantara tanda kurung <em>return aray</em> di atas. Pastikan format penulisannya sama dengan region yang sudah ada, contoh:</p>
<pre> 'region_baru' =&gt; t('region baru'),</pre>
<p>Nama di sebelah kiri tanda =&gt; adalah teks yang akan dibaca oleh drupal, tidak boleh menggunakan spasi dan karakter khusus, sedankan di sebelah kanan tanda =&gt; adalah nama yang akan ditampilkan di panel Administer, boleh menggunakan spasi.</li>
<li>Langkah berikutnya adalah memanggil region tersebut ke template. Sebelum ini dilakukan region baru tersebut tidak akan muncul di panel administer dan tidak bisa digunakan.Buka file <em>page.tpl.php</em> di folder themes, tentukan tempat dimana block akan kita tampilkan nantinya. Sisipkan baris berikut di tempat tersebut.
<pre>&lt;div&gt;&lt;?php print $region_baru; ?&gt;&lt;/div&gt;</pre>
<p>Gunakan CSS untuk memanipulasi ukuran region baru yang kita buat.</li>
<li>Selamat mencoba 🙂 </li>
</ol>
