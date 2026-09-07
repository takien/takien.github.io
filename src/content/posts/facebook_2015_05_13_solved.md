---
title: "HTACCESS +FollowSymlinks"
date: "2015-05-13T13:18:00.000Z"
categories: ["Programming"]
tags: ["facebook","Forum PHP Indonesia","programming"]
slug: "2015/05/13/solved"
legacyUrl: "/2015/05/13/solved/"
source: "facebook.com"
author: "Wak Jek"
group: "Forum PHP Indonesia"
comments: [{"author":"Wak Jek","date":"Wednesday 13 May 2015 at 13:18","text":"solved,\ndengan nambahin ini di htaccess\nOptions +FollowSymlinks -MultiViews"}]
---

<p>[SOLVED]</p>

solved,
dengan nambahin ini di htaccess

```Options +FollowSymlinks -MultiViews```

<p>Bantuin dong, bingung nih.</p>

<p>HTACCESS rewrite.</p>

```
RewriteRule ^lirik/([a-z]+)(/([a-z]{1}))?(/page([0-9]+))?/?$   lirik.php?lang=$1&letter=$3&page=$5  [NC,L,QSA]
```

<p>dengan harapan URL ini<br/>
lirik/indonesia/a/9</p>

<p>akan dibaca oleh system sebagai</p>

```lirik.php?lang=indonesia&letter=a&page=9```

<p>itu semua udah berhasil di localhost.<br/>
tapi pas di online, query variable nya semua tidak kebaca.</p>

<p>artinya server hanya membaca sampai translate.php selebihnya tidak.<br/>
sehingga ketika ane `print_r($_REQUEST)` tidak ada query apa-apa.</p>
