---
title: "Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18"
date: "2017-07-10T07:58:00Z"
categories: ["Programming"]
tags: ["facebook", "PHP Indonesia", "programming"]
slug: "2017/07/10/gimana-cara-benerin-eror-di-ubuntu-16041-gara2-error-di-mysq"
legacyUrl: "/2017/07/10/gimana-cara-benerin-eror-di-ubuntu-16041-gara2-error-di-mysq/"
source: "facebook.com"
author: "Wak Jek"
group: "PHP Indonesia"
comments: [{"author": "Handy Rusydi", "date": "Monday 10 July 2017 at 07:58", "text": "sepertinya ubuntu 16.0.1 belum ready untuk mysql nya. saya juga mentok pas install mysql jadi balik lagi ke ubuntu 14"}, {"author": "Shu", "date": "Monday 10 July 2017 at 00:22", "text": "apt-get purge mysql"}, {"author": "Ronald Sipatuhar", "date": "Sunday 9 July 2017 at 20:19", "text": "error nya di package, bukan di os  eh koneksi inet nya pakai apa ?"}, {"author": "Newbiee Last", "date": "Sunday 9 July 2017 at 13:06", "text": "Apt-get install -f"}, {"author": "Ian Hehe Lubis", "date": "Sunday 9 July 2017 at 12:19", "text": "Install ulang OS nya gimana ?"}, {"author": "Wak Jek", "date": "Sunday 9 July 2017 at 11:57", "text": "https://askubuntu.com/.../cannot-reinstall-mysql-server...\ngk bisa juga, ahhhhh"}, {"author": "Aprilia Awaludin", "date": "Sunday 9 July 2017 at 11:34", "text": "Wak Jek gimana udah bisa?"}, {"author": "Wak Jek", "date": "Sunday 9 July 2017 at 01:25", "text": "tidur aja lah dlu,\nmakasih ya Ronald Sipatuhar Ian Hehe Lubis Novrian Yf, dan semua yang komen di sini"}, {"author": "Agus Setia Putra", "date": "Sunday 9 July 2017 at 01:20", "text": "klo buntu dibawa ngopi beres wak biasanya wkwkwk"}, {"author": "Wak Jek", "date": "Sunday 9 July 2017 at 01:10", "text": "lama di sini Ronald Sipatuhar\ntapi gpp lah, tunggu aja"}, {"author": "Ronald Sipatuhar", "date": "Sunday 9 July 2017 at 00:59", "text": "nah itu bagus, baru di purge"}, {"author": "Wak Jek", "date": "Sunday 9 July 2017 at 00:58", "text": "Ronald Sipatuhar, setelah dihapsu /var/lib/dpkg/info/mysql*\n\njadi eror gini\nlist file for package 'mysql-server-core-5.7' missing; assuming package has no files currently installed"}, {"author": "Wak Jek", "date": "Sunday 9 July 2017 at 00:18", "text": "gmn cara hapus manual, tanpa hilang data bro?"}, {"author": "Ronald Sipatuhar", "date": "Sunday 9 July 2017 at 00:07", "text": "apt install --reinstall mysql-common\napt purge mysql-common\n\natau\n\nmv /etc/mysql/my.cnf.fallback /etc/mysql/my.cnf"}, {"author": "Novrian Yf", "date": "Saturday 8 July 2017 at 23:38", "text": "Kalo ini om??\n\nhttps://askubuntu.com/.../e-dpkg-was-interrupted-run-sudo..."}, {"author": "Wak Jek", "date": "Saturday 8 July 2017 at 23:37", "text": "Rifqi Habibi, sama aja bro, nih hasilnya"}, {"author": "Rifqi Habibi", "date": "Saturday 8 July 2017 at 23:27", "text": "Yg ini udh d coba um?"}, {"author": "Wak Jek", "date": "Saturday 8 July 2017 at 23:15", "text": "sampe tua"}, {"author": "Wak Jek", "date": "Saturday 8 July 2017 at 23:15", "text": "mau di purge juga gk bisa"}, {"author": "Wak Jek", "date": "Saturday 8 July 2017 at 23:15", "text": "dpkg --configure -a"}, {"author": "Wak Jek", "date": "Saturday 8 July 2017 at 23:14", "text": "misal mau instal apapun, jadi gak bisa"}]
---

<p>Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18</p>

<p>Jadi Gak bisa instal paket apapun, ketika mysql mau di reinstal juga gk bisa,</p>

<p>stuck di error seperti ini:</p>

<p>Renaming removed key_buffer and myisam-recover options (if present)</p>

<p>Kata google,askubuntu dll, disuru sudo apt-get -f install<br/>
Tetep aja gk bisa, balik lagi ke situ</p>

<p>dpkg --configure -a, gak bisa juga.</p>

<p>Thanks buat yang mau bantui</p>

<p><img src="/images/facebook/fb_new_0_0_d00193098b.jpg" alt="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" title="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>

<p><img src="/images/facebook/fb_new_0_1_83d7a3df2f.jpg" alt="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" title="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>

<p><img src="/images/facebook/fb_new_0_2_95bfca010e.jpg" alt="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" title="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>

<p><img src="/images/facebook/fb_new_0_3_56d736892d.jpg" alt="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" title="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>

<p><img src="/images/facebook/fb_new_0_4_9cf9074d72.jpg" alt="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" title="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>

<p><img src="/images/facebook/fb_new_0_5_80e394ec55.jpg" alt="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" title="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>

<p><img src="/images/facebook/fb_new_0_6_0b15c5ebd4.jpg" alt="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" title="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>

<p><img src="/images/facebook/fb_new_0_7_eb83f066d6.jpg" alt="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" title="Gimana cara benerin eror di Ubuntu 16.04.1, gara2 error di MySQL 5.7.18" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>
