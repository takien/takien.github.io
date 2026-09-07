---
title: "Membuat Custom URL untuk Attachments Image di WordPress"
date: "2011-09-10T00:00:00Z"
categories: ["Uncategorized"]
tags: []
slug: "2011/09/10/membuat-custom-url-untuk-attachments-image-di-wordpress"
legacyUrl: "/blog/2011/09/10/membuat-custom-url-untuk-attachments-image-di-wordpress/"
comments: [{"author": "ian lubis", "date": "", "text": "wew.. di upload juga gan… ahahahaha, aye kopas dulu. tutor yang laennya di tunggu."}, {"author": "pedox", "date": "", "text": "anu itu, biar kliatan pamer pake cdn diblakang nya #cool #nyindir"}, {"author": "rizky", "date": "", "text": "hahaha\n\nmanteb nih baru tau bisa di pake alias gitu sub domainnya"}, {"author": "zaqy", "date": "", "text": "oh .. ada cara seperti itu yah ..  nubie mode on 😀"}, {"author": "rainer", "date": "", "text": "baru tau ane bisa gitu, hehe…\n\n\ntips mantap nih, biar gaya kayak forum yg #sesuatu banget.."}, {"author": "Jeffri", "date": "", "text": "Ada filternya ga ya biar otomatis gitu…"}, {"author": "Prast Rahastu", "date": "", "text": "wah keren deh"}, {"author": "Prast Rahastu", "date": "", "text": "wah keren deh"}, {"author": "home-garden", "date": "", "text": "klo mau ngedit atau ngoprek file attachment di wordpress letaknya di file apa ya mas.."}]
---

<p>Pada umumnya URL image/attachment di WordPress adalah <strong>http://example.com/wp-content/uploads/</strong>, supaya lebih keren kita dapat menggantinya menjadi <strong>http://img.example.com/. </strong>Mari kita ikuti caranya:</p>
<p>1. Buatlah sebuah sub-domain di cpanel, document Root nya diisi dengan /public_html/wp-content/uploads (lihat gambar 1)</p>

<div id="attachment_890" style="width: 310px" class="wp-caption aligncenter"><a href="https://web.archive.org/web/20151225032910/http://img.takien.com/2011/09/subdomain-image.jpg"><img src="/images/2011/09/subdomain-image-300x118.jpg" alt="Create sub domain" title="subdomain-image" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">Gambar 1. Create sub domain</p></div>

<p>2. Di wp-admin, buka menu Settings-&gt;Media</p>
<p>3. Pada field <em>Full URL path to files, </em> isikan<strong>http://img.example.com/</strong> (lihat gambar 2) kemudian klik Save Changes untuk menyimpan setting tersebut.<strong></strong></p>
<div id="attachment_891" style="width: 310px" class="wp-caption aligncenter"><a href="https://web.archive.org/web/20151225032910/http://img.takien.com/2011/09/file-url.jpg"><img src="/images/2011/09/file-url-300x86.jpg" alt="Wordpress Full URL path to files" title="file-url" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">Gambar 2: Full URL path to files</p></div>
<p>4. Sekarang coba bikin post baru, upload image dan insert ke post, secara otomatis URL image nya sekarang adalah http://img.example.com/tahun/bulan/nama-file.jpg  (demo: lihat path URL gambar2 attachments diatas).</p>
<p>Sekian, semoga bermanfaat <img src="/images/misc/simple-smile.png" alt=":)" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>
