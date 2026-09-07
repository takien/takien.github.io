---
title: "Halaman yang pake ajax itu kan bisa cepet load, dengan meload bagian2..."
date: "2011-09-23T11:47:00Z"
categories: ["Internet"]
tags: ["facebook", "W3 kaskus", "internet"]
slug: "2011/09/23/halaman-yang-pake-ajax-itu-kan-bisa-cepet-load-dengan-meload"
legacyUrl: "/2011/09/23/halaman-yang-pake-ajax-itu-kan-bisa-cepet-load-dengan-meload/"
source: "facebook.com"
author: "Wak Jek"
group: "W3 kaskus"
comments: [{"author": "Mohammad Naufal Fadil", "date": "Friday 23 September 2011 at 11:47", "text": "facebook itu pake infrastruktur Bigpipe om."}, {"author": "Wak Jek", "date": "Friday 23 September 2011 at 12:06", "text": "ck ck ck keren tuh bigpipe.\nizin baca dulu\nhttp://www.facebook.com/note.php?note_id=389414033919"}, {"author": "Wak Jek", "date": "Friday 23 September 2011 at 12:10", "text": "In BigPipe, the life cycle of a user request is the following: The browser sends an HTTP request to web server. After receiving the HTTP request and performing some sanity check on it, web server immediately sends back an unclosed HTML document that includes an HTML tag and the first part of the tag. The tag includes BigPipe’s JavaScript library to interpret pagelet responses to be received later. In the tag, there is a template that specifies the logical structure of page and the placeholders for pagelets.\n\nhmmmmmmmm.."}, {"author": "Asep Bagja", "date": "Friday 23 September 2011 at 13:05", "text": "^ pokoknya bagus deh #halah"}, {"author": "Prast Rahastu", "date": "Friday 23 September 2011 at 13:07", "text": "kadang harus pake fb versi mobile kalo gambar loader muncul terus"}, {"author": "Mohammad Naufal Fadil", "date": "Friday 23 September 2011 at 13:07", "text": "jadi kesimpulanya Bigpipe itu semacam infrastruktur untuk mempercepat loading page. dengan HTTP request semacam ajax. seperti HTML Javascript CSS dll."}, {"author": "Wak Jek", "date": "Friday 23 September 2011 at 14:17", "text": "dimana download bigpie"}, {"author": "Heri Hehe Setiawan", "date": "Friday 23 September 2011 at 14:59", "text": "teknologi bigboob memang keren. perlu didalami nih."}, {"author": "Jeffri Tjin", "date": "Saturday 24 September 2011 at 06:54", "text": "Like dulu gan"}, {"author": "Franky Kolondam", "date": "Saturday 24 September 2011 at 16:44", "text": "i like bigboob"}, {"author": "Wak Jek", "date": "Sunday 25 September 2011 at 00:20", "text": "http://www.juhonkoti.net/.../open-bigpipe-javascript..."}]
---

<p>Halaman yang pake ajax itu kan bisa cepet load, dengan meload bagian2 tertentu ketika diperlukan saja atau ketika event2 tertentu seperti klik, hover, scroll ataupun otomatis dengan setTimeout.</p>

<p>Masalahnya adalah ketika halaman tersebut sudah 'berumur lama', maka elemen2 hasil generate dari ajax tersebut sudah sangat banyak dan ini memenuhi pemakaian memori browser cleint.</p>

<p>Bagaimana mengatasi hal ini, kenapa fb tidak begitu</p>
