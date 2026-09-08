---
title: "Membuat Private NS Sendiri"
date: "2008-08-28T16:25:00.000Z"
categories: ["Web Hosting"]
tags: []
slug: "2008/08/28/membuat-private-ns-sendiri"
legacyUrl: "/2008/08/28/membuat-private-ns-sendiri/"
source: "takien.com"
author: "takien"
comments: [{"author":"aagun2006","date":"","text":"wah mantebs gan …\nsip … sip …"},{"author":"angga","date":"","text":"kalo domain nya beli yahoo small business bisa gak?caranya gimna?"},{"author":"Belajar Ngeblog","date":"","text":"kemarin saya cb buat di godaddy ama namecheap koq gagal semua ya gan?\nerrot nya pas diping malah couldn’t locate remote address :-s\npls help me, cendol menunggu gan :-s"},{"author":"takien","date":"","text":"masa sih, biasanya lancar jaya tuh"},{"author":"satub","date":"","text":"thank banget informasinya"},{"author":"takien","date":"","text":"sama-sama"},{"author":"punya info","date":"","text":"tank boss ternyata di godaddy bisa pakai ip sendiri"},{"author":"Kfai","date":"","text":"Thanks bro atas sharenya, sangat membantu sekali."},{"author":"Anonymous","date":"","text":"sama2 bro ehehe"}]
---

Ketika menyewa sebuah webhosting, kita biasanya diberi informasi account dan informasi nameserver dengan format NS1.NAMAHOSTING.COM dan NS2.NAMAHOSTING.COM. Nama server tersebut nantinya akan bisa dilihat publik ketika melakukan Whois ke domain kita sehingga orang lain akan tahu dimana kita menyewa hosting.

Sebenarnya kita bisa membuat nameserver sendiri dengan format NS1.DOMAINKITA.COM dan NS2.DOMAINKITA.COM. Untuk dapat membuat nameserver sendiri syaratnya adalah kita harus punya akses ke control panel domain yang memungkinkan mengedit DNS Zone. Beberapa registrar domain yang memungkinkan kita membuat nameserver sendiri (tanpa biaya tambahan) diantaranya Godaddy.com, Name.com, Dynadot.com

Berikut tutorial untuk membuat nameserver di Godaddy.com

- Login ke account di **Godaddy.com**
- Masuk ke domain management dengan mengklik menu **My Domain**

[![image](/images/uploads/1788799451805_ns-001.png)](/images/uploads/1788799451805_ns-001.png)

- Klik salah satu domain yang akan dibuat nameservernya

[![image](/images/uploads/1788799455396_ns-002.png)](/images/uploads/1788799455396_ns-002.png)

- Scroll ke bawah, di situ tertera tertera **Host Summary (add)**, klik pada link (add)

[![image](/images/uploads/1788799458587_ns-003.png)](/images/uploads/1788799458587_ns-003.png)

- Pada kotak **hostname**isikan NS1, pada kotak **Host IP1** isikan no IP untuk NS1

[![image](/images/uploads/1788799462584_ns-004.png)](/images/uploads/1788799462584_ns-004.png)

- Ulangi sekali lagi untuk NS2, pada kotak **Host IP1** isikan no IP untuk NS2
- Klik OK jika sudah selesai. Nameserver akan aktif dalam waktu paling lama 48 jam.

NB:

Untuk mendapatkan no IP. lakukan ping ke NS1.NAMAHOSTING.COM dan NS2.NAMAHOSTING.COM (sesuai yang diberikan pihak webhosting), caranya ketikkan di Start -> Run *ping ns1.namahosting.com -t* dan tekan Enter, demikian juga untuk NS2-nya*.*

Trik ini hanya untuk merubah nameserver, dimana orang lain masih tetap dapat melihat dimana kita menyewa hosting dengan melakukan trace-route. :D
