---
title: "Sering bikin form di WordPress kadang bikin hehe. Aku dah ada bikin Class..."
date: "2012-11-26T01:57:00Z"
categories: ["WordPress"]
tags: ["facebook", "Belajar WordPress", "wordpress", "plugin"]
slug: "2012/11/26/sering-bikin-form-di-wordpress-kadang-bikin-hehe-aku-dah-ada"
legacyUrl: "/2012/11/26/sering-bikin-form-di-wordpress-kadang-bikin-hehe-aku-dah-ada/"
source: "facebook.com"
author: "Wak Jek"
group: "Belajar WordPress"
comments: [{"author": "Wak Jek", "date": "Monday 26 November 2012 at 01:57", "text": "Helmi Aditya, jah cuma di like"}, {"author": "Wak Jek", "date": "Monday 26 November 2012 at 13:12", "text": "Helmi Aditya, bisa dijelaskan gimana? siapa tau bisa diimplementasikan"}, {"author": "Sabihul Anwary", "date": "Monday 26 November 2012 at 14:51", "text": "kalo bisa plugin form by wak"}]
---

<p>Sering bikin form di WordPress kadang bikin hehe. Aku dah ada bikin Class form sih, tapi masih hardcoded, harus ngedit PHP nya. Mau nya sih via admin aja.</p>

<p>Jadi terpikir bikin Plugin shortcode untuk form.<br/>
Kira-kira seperti ini.</p>

<p>[form type="mailform" sendto="wakjek@google.com"]<br/>
Name/name*[type=text&default=&placeholder=Enter name&class=field]<br/>
Email/email*[type=email&default=&placeholder=Enter email&class=field]<br/>
Birthdate/birtdate[type=date&range=1980-Now&class=field]<br/>
Gender/gender[type=select&data=male/female&class=field]<br/>
Subject/subject*[type=text&default=&placeholder=Enter subject&class=field]<br/>
Message/message*[type=textarea&default=&class=field]<br/>
Submit/submit_form[type=submit]<br/>
[/form]</p>

<p>Oh ya, nantinya form ini bukan hanya untuk Contact form, tapi bisa apa aja, termasuk submit ke Post/Page atau Custom Post Type.</p>

<p>Emang udah ada plugin Contact Form 7, menurutku masih terlalu ribet (walau masih banyak yang lebih ribet) dan hanya untuk Contact form saja.</p>

<p>Kira-kira efektif gak ya? Kalau ada masukan/ide lain boleh di share</p>
