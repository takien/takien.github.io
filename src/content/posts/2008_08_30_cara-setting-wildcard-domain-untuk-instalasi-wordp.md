---
title: "Cara Setting Wildcard Domain untuk Instalasi WordPress MU"
date: "2008-08-30T04:34:00.000Z"
categories: ["WordPress"]
tags: []
slug: "2008/08/30/cara-setting-wildcard-domain-untuk-instalasi-wordpress-mu"
legacyUrl: "/2008/08/30/cara-setting-wildcard-domain-untuk-instalasi-wordpress-mu/"
source: "indowebmasters.com"
author: "takien"
comments: []
---

Pernah bikin blog di Wordpress.com? Tentu sudah dong! Nah, setiap user melakukan signup ke situs tersebut, secara otomatis akan dibuatkan sebuah akun blog dengan alamat `username.wordpress.com.` Blog ini bisa bertindak selayaknya blog standalone dimana kita bisa melakukan posting, memanage, mengganti template dan sebagainya.

Sebenarnya kita bisa membuat sendiri website seperti Wordpress.com yang menawarkan akun blog kepada setiap penggunanya. Apakah kita perlu menginstalkan wordpress ke setiap akun yang mendaftar? Tentu tidak. Karena Wordpress telah menyediakan apa yang dinamakan dengan Wordpress MU (Multi User) yang dapat di download di `http://mu.wordpress.org`

Secara umum tidak banyak perbedaan instalasi Wordpress MU dengan Wordpress biasa, karena sebenarnya Wordpress MU juga bisa dipakai selayaknya wordpress biasa. Namum ada satu hal yang perlu diperhatikan di sini, yakni Wordpress MU memerlukan settingan di DNS Zone dan server yaitu WildCard Domain. Wildcard domain sangat penting supaya server secara otomatis membuatkan “subdomain” (tepatnya, virtual subdomain)  sesuai dengan username waktu registrasi. Tanpa setting Wildcard domain ini alamat akun `username.wordpress` nya tidak dapat diakses.

Berikut langkah-langkah dalam membuat Wildcard Domain:


**1. Login ke cPanel atau WHM dan pilih Edit DNS Zone.**


Jika tidak ada akses ke lokasi tersebut bisa minta bantuan ke admin server hosting yang bersangkutan. Alternatif lainnya belilah domain yang sudah mendukung Edit DNS seperti di name.com

Pada form isian DNS Zone tambahkan record berikut

`Domain : *
Record Type : A`

Di sebelah kanannya isikan alamat IP hostingnya, misalnya : `123.45.67.89`

Screenshoot:

[IMAGE MISSING]

**2. Langkah kedua**

Sepertinya memang harus mengontak admin server, kecuali anda memiliki hak akses root.

Buka file `httpd.conf` di folder Apache dan tambahkan baris-baris berikut:

```
DocumentRoot /home/username/public_html
BytesLog domlogs/domainkamu.com-bytes_log
User username
Group username
ServerAlias domainkamu.com *.domainkamu.com
ServerName www.domainkamu.com
CustomLog domlogs/domainkamu.com combined
```

Yang berwarna biru dan merah sesuaikan dengan username dan domainnya.

Selanjutnya cobalah membuat account baru di Wordpress MU yang sudah anda instal.
