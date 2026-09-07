---
title: "Alasan saya jarang \"Update status\" adalah karena frase itu menyalahi..."
date: "2011-12-16T15:03:00Z"
categories: ["Internet"]
tags: ["facebook", "internet"]
slug: "2011/12/16/alasan-saya-jarang-update-status-adalah-karena-frase-itu-men"
legacyUrl: "/2011/12/16/alasan-saya-jarang-update-status-adalah-karena-frase-itu-men/"
source: "facebook.com"
author: "Wak Jek"
comments: [{"author": "Aprilia Awaludin", "date": "Friday 16 December 2011 at 15:03", "text": ":hammer:"}, {"author": "Mohammad Naufal Fadil", "date": "Friday 16 December 2011 at 15:46", "text": "saya jarang update status karena kasian facebook nya yang harus menampung ribuan status tidak penting yang mengakibatkan pembekakan Bandwidth dan Space Database sehingga membuat kinerja menjadi menurun akibat bommber like yang menyebabkan para alay meraja lela"}, {"author": "Kris Suprapto", "date": "Friday 16 December 2011 at 16:19", "text": "sudah jelas sekarang"}, {"author": "Prast Rahastu", "date": "Friday 16 December 2011 at 17:00", "text": "emang nosql gitu?"}, {"author": "Tegar Muhammad Aji", "date": "Friday 16 December 2011 at 17:01", "text": "querynya 2x gan\n\nINSERT INTO statuses(status, id_user) VALUES id('mandi dulu ah', 'wakjek')\n\nUPDATE actual_status ac SET ac.id_status=(SELECT id_status FROM statuses st WHERE st.id_user='wakjek' LIMIT 1)"}]
---

<p>Alasan saya jarang "Update status" adalah karena frase itu menyalahi aturan berbahasa, baik bahasa Inggris maupun bahasa SQL. Harusnya yang benar adalah "Add status" atau "Insert Status".</p>

<p>Update = edit = mengubah sesuatu yang udah ada, padahal Facebook tidak mengizinkan kita untuk mengedit status yang sudah ditulis.</p>

<p>Contoh statemen SQL UPDATE untuk merubah value yang udah ada ke value baru:</p>

<p>UPDATE table_status SET status='new status' WHERE userid=1 AND statusid=2;</p>

<p>Padahal ketika kita melakukan 'update status' di Facebook, kira-kira SQL nya adalah sebagai berikut:</p>

<p>INSERT INTO table_status (status) VALUES ('new status');</p>

<p>So, janganlah pernah lagi melakukan update status, jika anda sebenarnya hanya bisa Insert status.</p>
