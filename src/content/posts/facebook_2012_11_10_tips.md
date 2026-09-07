---
title: "Bagaimana cara menggunakan fungsi2 WordPress di luar WordPress?"
date: "2012-11-10T22:51:00.000Z"
categories: ["WordPress"]
tags: ["facebook","Belajar WordPress","wordpress"]
slug: "2012/11/10/tips"
legacyUrl: "/2012/11/10/tips/"
source: "facebook.com"
author: "Wak Jek"
group: "Belajar WordPress"
comments: [{"author":"Wak Jek","date":"Saturday 10 November 2012 at 22:51","text":"blablabla itu absolute path ke direktori root wp nya"},{"author":"Prast Rahastu","date":"Saturday 10 November 2012 at 22:51","text":"itu autoload nya ya"},{"author":"Wak Jek","date":"Saturday 10 November 2012 at 22:54","text":"ya begitu mungkin"},{"author":"Jeni Gemintang","date":"Sunday 11 November 2012 at 08:21","text":"ini seperti menjadikan wordpress sebagai framework gitu ?"},{"author":"Wak Jek","date":"Sunday 11 November 2012 at 09:09","text":"bukan"}]
---

<p>ask: Bagaimana cara menggunakan fungsi2 WordPress di luar WordPress?<br/>
answer:<br/>

**include wp-load.php**

```
<?php
require_once('blablabla/wp-load.php');

/*
selamat, semua fungsi WordPress berjalan disini. heheh<br/>
*/
```
