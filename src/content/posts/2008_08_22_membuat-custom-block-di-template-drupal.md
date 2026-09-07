---
title: "Membuat Custom Block di Template Drupal"
date: "2008-08-22T04:39:00.000Z"
categories: ["Drupal"]
tags: []
slug: "2008/08/22/membuat-custom-block-di-template-drupal"
legacyUrl: "/2008/08/22/membuat-custom-block-di-template-drupal/"
source: "indowebmasters.com"
author: "takien"
comments: []
---

Block region adalah area di Drupal yang bisa digunakan untuk menampilkan content tertentu misalnya text ataupun modul seperti chatbox, banner, link dan sebagainya. Konfigurasi Block ini bisa diakses melaui panel administer `( /admin/build/block)`. Meskipun jumlah block yang dapat kita tambahkan dalam sebuah region block tidak terbatas, tapi jumlah regionnya sendiri adalah terbatas. Banyaknya region block tergantung dengan template yang digunakan misalnya header, sidebar, content top/bottom, dan footer. Beberapa template mempunyai jumlah block region yang terbatas, untuk itu kita perlu membuat block region baru.

Untuk membuat block region baru, yang perlu kita lakukan adalah mengedit beberapa file template yang kita gunakan. Langkah-langkahnya:

Buka file template.php di folder themes, temukan baris-baris berikut (buat file baru bernama `template.php` jika tidak ada) :

```
// regions for nama_template
function nama_template_regions() {
    return array(
    'left' => t('left sidebar'),
    'content_top' => t('content top'),
    'content_top_right' => t('content top right'),
    'content_bottom' => t('content bottom'),
    'content_header' => t('header'),
    );
}
```

Sisipkan nama region baru yang akan ditambahkan diantara tanda kurung return aray di atas. Pastikan format penulisannya sama dengan region yang sudah ada, contoh:

`'region_baru' => t('region baru'),`

Nama di sebelah kiri tanda => adalah teks yang akan dibaca oleh drupal, tidak boleh menggunakan spasi dan karakter khusus, sedankan di sebelah kanan tanda => adalah nama yang akan ditampilkan di panel Administer, boleh menggunakan spasi.

Langkah berikutnya adalah memanggil region tersebut ke template. Sebelum ini dilakukan region baru tersebut tidak akan muncul di panel administer dan tidak bisa digunakan.Buka file page.tpl.php di folder themes, tentukan tempat dimana block akan kita tampilkan nantinya. Sisipkan baris berikut di tempat tersebut.

`<div><?php print $region_baru; ?></div>`

Gunakan CSS untuk memanipulasi ukuran region baru yang kita buat.

Selamat mencoba
