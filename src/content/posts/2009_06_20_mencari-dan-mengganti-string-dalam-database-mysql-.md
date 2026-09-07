---
title: "Mencari dan Mengganti String dalam Database MySQL dengan phpMyAdmin"
date: "2009-06-20T15:47:00.000Z"
categories: ["MySQL"]
tags: []
slug: "2009/06/20/mencari-dan-mengganti-string-dalam-database-mysql"
legacyUrl: "/2009/06/20/mencari-dan-mengganti-string-dalam-database-mysql/"
source: "takien.com"
author: "takien"
nowNote: "Setelah baca lagi blog ini ternyata masukan dari bro Ian Bali itu salah dan membahayakan, itu malah mengganti keseluruhan konten. Padahal maksud aku cuma mengganti sub-string-nya saja. Wakkwwk. Namanya dulu aku masih cupu jadi nggih-nggih aja."
nowDate: "7 September 2026"
comments: []
---

Kadangkala kita perlu mengganti suatu teks langsung dari database mySQL menggunakan phpMyAdmin. Hal ini tentu mudah saja dilakukan jika teks yang akan diganti jumlahnya cuma sedikit.

Nah, bagaimana cara merubah teks yang berjumlah banyak dalam database tersebut dengan cepat tanpa mengekspor database?

Hal itu bisa dilakukan menggunakan perintah SQL, caranya bukalah phpMyAdmin, kemudian buka tab SQL dan ketikkan perintah berikut:

```
UPDATE namatabel SET namakolom = replace(namakolom,"teksyangdicari","tekspengganti");
```

Contoh berikut akan mengganti semua teks **google.com** dalam posting wordpress menjadi **yahoo.com**.

```
UPDATE wp_posts SET post_content = replace(post_content,"google.com","yahoo.com");
```

**Update: (22 Juni 2009)**

 Malu aku, posting ini dibaca oleh [sang master](http://ianbali.wordpress.com/) juga ternyata.

Tapi gak apa-apa, itu menandakan masih punya kemaluan.

 Si master tadi ngasih solusi yang *lebih cepat lebih baik* (bukan kampanye, red).

Kata dia cukup pakai ini aja:

```
"UPDATE wp_posts SET `post_content` = 'google.com' WHERE `post_content` = 'yahoo.com'" ;
```

Standard MySQL tuh, katanya menambahkan.

Weleh-weleh, yo wis lah, makasih oom, ntar tak hadiahin chika versi manohara deh sekalian [tak gendong kemana-mana.](http://blog.rizkyonline.com/)

*NB: google.com dan yahoo.com diatas hanyalah sebagai contoh saja, bukan bermaksud mempromosikan kedua situs tersebut apalagi menyemarakkan nama baik.*
