---
title: "Tips dan Trick CSS (Bagian I)"
date: "2008-09-10T06:29:00.000Z"
categories: ["Web Design","CSS"]
tags: ["web design","css"]
slug: "2008/09/10/tips-dan-trick-css-bagian-i"
legacyUrl: "/2008/09/10/tips-dan-trick-css-bagian-i/"
source: "indowebmasters.com"
author: "takien"
comments: []
---

Penggunaan CSS (Cascading Style Sheets) sudahlah mutlak dalam mendesain sebuah website. Dengan CSS hampir semua format tampilan dapat kita deklarasikan hanya melalui sebuah file, sehingga halaman lebih cepat di load, selain dapat dengan mudah jika suatu saat ingin menggantinya. Namun terkadang masih banyak terdapat kesalahan dimana terjadi banyak pengulangan-pengulangan yang tidak penting. Juga penggunaan ID dan class yang salah tempat. Sehingga tujuan penggunaan CSS untuk mempercepat loading halaman jadi tidak tercapai.

Berikut beberapa tips dalam menuliskan CSS:

**1. Hindari penggunaan ID ganda.**

ID adalah sebuah penanda unik untuk sebuah elemen halaman, artinya dalam sebuah halaman tidak ada dua ID dengan nama yang sama. Jadi, gunakanlah ID hanya untuk elemen-elemen utama yang tidak ada duanya, seperti header, menu, container, sidebar, footer dsb.

Contoh1:

[IMAGE MISSING]

Contoh2:

[IMAGE MISSING]

Contoh2 di atas adalah salah, karena kemungkinan besar elemen title dan post adalah lebih dari satu dalam sebuah halaman.

Solusinya gunakanlah class daripada ID.

**2. Buang nilai-nilai yang mubazir**

Kita lihat contoh CSS berikut:

Contoh3


```

#container {
padding-top: 5px;
padding-right: 0px;
padding-bottom: 5px;
padding-right: 0px;
}
```



Contoh4



```
#container {
padding: 5px 0px 5px 0px;
}
```



Contoh3 dan Contoh4 di atas akan menghasilkan tampilan yang sama, tentu saja contoh4 lebih sederhana daripada contoh3. Namun demikian, contoh4 tersebut masih terdapat perulangan nilai 5 dan 0. Mari kita perbaiki menjadi sebagai berikut:

Contoh5



```
#container {
padding: 5px 0;
}
```



Wow, sederhana bukan? Ya, karena nilai pertama sudah dapat mewakili top dan bottom, dan nilai kedua sudah mewakili left dan right. Sementara untuk zero value (0) tidak perlu menambahkan satuan px, jadi boleh dihilangkan.

**3. Bijak dalam memberikan nilai warna**

Asumsikan kita akan memberi latar warna biru untuk div container, css nya adalah sebagai berikut.

Contoh6



```
#container {
background: #0000FF;
}
```



Contoh6 akan menghasilkan warna background dari div container menjadi berwarna biru. Kode tersebut bisa dipersingkat lagi menjadi sebagai berikut:

Contoh7



```
#container {
background: blue;
}
```



Ya, karena nilai #0000FF sama artinya dengan blue. Lebih singkat bukan?

Beberapa alternatif lain dalam memberikan warna seperti tertera dalam table berikut:


```

alternatif1        alternatif2          alternatif3            hasil warna
#000000           #000                  black                  hitam
#FFFFFF           #FFF                  white                  putih
#FFFF00           #FF0                  yellow                 kuning
#FF0000           #F00                  red                    merah

```



Di sinilah kebijakan kita dituntut, dimana kita harus bisa memilih mana yang paling sedikit karakternya. Misalnya untuk memberi warna kuning, maka lebih baik menggunakan #FF0 dari pada yellow, sementara untuk memberi warna merah, lebih baik menggunakan red, daripada #F00. Pemberian nama warna langsung kemungkinan tidak terbaca oleh semua browser, tapi untuk warna2 dasar hal ini masih bisa ditolelir.

Untuk lebih jelasnya dalam menentukan kode warna, bisa dilihat color chart di sini.

**4. Semicolons, hanya untuk pemisah**

Kita lihat contoh berikut

Contoh8



```
#container {
background: blue;  /*terdapat semicolon (titik koma) setelah nilai blue.*/
}
```



Jika hanya ada sebuah properties, kita tidak perlu mengakhirinya dengan titik koma (;) atau semicolon.

Jadi CSS yang baik adalah.

Contoh9



```
#container {
background: blue
}
```



Demikian juga jika sebuah nilai tidak diikuti oleh nilai lainnya, maka semicolon bisa dihilangkan.

Contoh10



```
#container {
background: blue;
padding: 5px 0;
margin: 0
}
```



Setelah nilai margin: 0 kita tidak perlu lagi menambahkan semicolon, karena properties untuk container sudah berakhir.

**6. Kelompokkan nilai yang sama.**

Misalkan div header, div sidebar, dan div footer mempunyai beberapa nilai yang sama, kita bisa mengelompokkannya dengan memisahkannya dengan koma.

Contoh11



```
#header, #sidebar, #footer {
background: red;
font-family: Arial, Helvetica;
padding: 5px
```



**5. Kurangi spasi yang berlebihan**

Sedapat mungkin kurangi penggunaan spasi kosong yang berlebihan.
Untuk contoh10 di atas, bisa kita padatkan lagi menjadi

Contoh12



```
#container {
background:blue;
padding:5px 0;
margin:0
}
```



Atau bahkan

Contoh13



```
#container {background:blue;padding:5px 0;margin:0}
```



Namun contoh13 tidak dianjurkan, karena akan merepotkan kita sendiri sewaktu-waktu ingin merubah tampilan nantinya.

Demikian beberapa tips yang mungkin berguna, sebenarnya masih ada beberapa tips lagi yang mungkin lain kali bisa disambung lagi. :)
