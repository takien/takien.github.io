---
title: "Membuat Elemen Halaman Transparan Menggunakan CSS"
date: "2008-11-03T04:42:00.000Z"
categories: ["HTML","CSS"]
tags: []
slug: "2008/11/03/membuat-elemen-halaman-transparan-menggunakan-css"
legacyUrl: "/2008/11/03/membuat-elemen-halaman-transparan-menggunakan-css/"
source: "indowebmasters.com"
author: "takien"
comments: []
---

Barangkali kita pernah berfikir bagaimana caranya membuat elemen halaman website kelihatan transparan (tembus pandang) terhadap elemen dibelakangnya. Ini biasanya digunakan pada menu dropdown ataupun elemen div untuk mempercantik halaman website.

Melanjutkan trick css sebelumnya, berikut ini adalah tips untuk membuat elemen transparan tersebut, yang tentu saja bersifat crossbrowser alias dilihat dari browser manapun akan menghasilkan tampilan yang sama.

Misalkan kita akan membuat sebuah elemen div bernama `#kotak (div id=”kotak”)` menjadi transparan, hal yang perlu dilakukan adalah dengan menambahkan properti berikut pada CSS.

```
div#kotak {
filter:alpha(opacity=70);
-moz-opacity: 0.7;
opacity: 0.7;
}
```

Nilai yang dapat diberikan antara 0 s/d 1 untuk `-moz-opacity` dan `opacity`, sedangkan untuk `filter:alpha(opacity)` adalah 0 s/d 100. Semakin tinggi nilai opacity maka elemen akan semakin jelas terlihat, sementara semakin rendah nilainya, sebuah elemen akan nampak makin transparan.

Selamat mencoba :)
