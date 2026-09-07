---
title: "Tips mencegah klonengan pake Gmail dot dan Gmail plus"
date: "2011-09-02T10:52:00Z"
categories: ["Programming"]
tags: ["facebook", "programming"]
slug: "2011/09/02/tips-mencegah-klonengan-pake-gmail-dot-dan-gmail-plus"
legacyUrl: "/2011/09/02/tips-mencegah-klonengan-pake-gmail-dot-dan-gmail-plus/"
source: "facebook.com"
author: "Wak Jek"
comments: [{"author": "Argado Simarmata", "date": "Saturday 3 September 2011 at 00:43", "text": "manteb om, lebih2 dari nice inpo ..\nane baru tau klo yg + ...\nmkn banyak dah nih akun ternak :D"}, {"author": "Job Media Sekata", "date": "Saturday 3 September 2011 at 01:47", "text": "wuidiiihh cadas om jek jek . saya baru tau bisa bijitu :thumbup"}, {"author": "Mohammad Naufal Fadil", "date": "Saturday 3 September 2011 at 06:16", "text": "brarti tanda dot dot ( . )( . ) masih bisa ditambahkan username nya di setiap email. baru tau ane"}, {"author": "Kecoa Ngamuk Kecoa", "date": "Saturday 3 September 2011 at 09:37", "text": "ini keren, saya baru tau bisa ++"}, {"author": "Mokhamad Oky", "date": "Saturday 3 September 2011 at 12:56", "text": "wah, jungker malah seneng dapet trik baru ++ :D"}, {"author": "Prast Rahastu", "date": "Saturday 3 September 2011 at 22:19", "text": "ok nih,"}, {"author": "Prast Rahastu", "date": "Saturday 3 September 2011 at 22:22", "text": "yang ok justru info ++ nya"}]
---

<p>Tips mencegah klonengan pake Gmail dot dan Gmail plus</p>

<p>Simpan sini dlu ya, barusan bikin fungsi mencegah klonengan pake account gmail.</p>

<p>Seperti diketahui, 1 account gmail bisa digunakan untuk mendaftarkan banyak account dalam sebuah website. (seperti di trit alm. oom idi). yaitu dengan menambahkan dot ( . )( . ) di antara username. misal, email asli = alamatemailsaya@gmail.com, bisa diduplikat jadi a.l.amatemailsaya@gmail.com (letakkan titik dimana aja sebelum @gmail.com), jadi semakin panjang username, semakin banyaklah kemungkinan klonengan yang bisa dibuat dengan 1 account.</p>

<p>Bahkan domain bisa diganti dengan @goooglemail.com (tetep masuk ke inbox yang sama).</p>

<p>tidak cuma itu, gmail sangat mendukung program perkembanngbiakan klonengan, selain trik dot (.) dan doman googlemail, gmail juga menyediakan fasilitas ++ yaitu tambahkan kata apapun setelah username anda diawali dengan tanda +, misalnya: alamatemailsaya+satu@gmail.com, alamatemailsaya+dua@gmail.com, alamatemailsaya+apasaja@gmail.com, alamatemailsaya+danseterusnya@gmail.com (semua akan masuk ke inbox yang sama yaitu, alamatemailsaya@gmail.com)</p>

<p>Bayangkan berapa banyak alamat email yang dapat diciptakan dengan kombinasi dot (.), domain, dan + diatas? wow, nearly uncountable bahkan UNLIMITED.</p>

<p>Nah, fasilitas ini tentu sangat berguna untuk filtering, misal mendaftar di web A, pake domain email alamatemailsaya+web.a@gmail.com, dan beri label yang sesuai.</p>

<p>Namun bagi pemilik web tentu sangat merugikan, apalagi fasilitas ini biasanya digunakan oleh spammer untuk nyepam dengan multiple account (1 alamat email dengan kombinasi yang berbeda). Ini sangat menguntungkan spammer karena mereka cukup mendaftar 1x account gmail, so, verifikasi no HP, bukan masalah berarti bagi mereka. heheh.</p>

<p>Nah, untuk mencegahnya, mari kita cegah dengan fungsi berikut:</p>

<p>[php]</p>

<p>function cleanup_gmail_email($email){</p>

<p>$emailbody = explode('@',strtolower($email));</p>

<p>$part1 = $emailbody[0];</p>

<p>$part2 = $emailbody[1];</p>

<p>if($part2 == 'gmail.com' OR $part2 == 'googlemail.com'){</p>

<p>$part1 = preg_replace('/([\.]+)|((\+)+([\+\.\-_a-z0-9]+))/i','',$part1);</p>

<p>$email = $part1.'@'.$part2;</p>

<p>}</p>

<p>return $email;</p>

<p>}</p>

<p>[/php]</p>

<p>Tempatkan fungsi tersebut, pada saat registrasi atau login (jika login menggunakan email). Jadi kombinasi apapun yang mereka pake, maka yang terecord ke database adalah email asli alamatemailsaya@gmail.com (tanpa dot, tanpa +, dan bukan domain googlemail.com), kalau alamat asli udah terecord, otomatis, kombinasi apapun akan dianggap duplicate (already registered). Heheh.</p>
