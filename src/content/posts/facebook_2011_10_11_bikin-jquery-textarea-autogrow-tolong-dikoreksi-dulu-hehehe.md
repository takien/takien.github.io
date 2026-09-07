---
title: "Bikin jQuery textarea autogrow, tolong dikoreksi dulu hehehe"
date: "2011-10-11T15:06:00Z"
categories: ["Programming"]
tags: ["facebook", "programming"]
slug: "2011/10/11/bikin-jquery-textarea-autogrow-tolong-dikoreksi-dulu-hehehe"
legacyUrl: "/2011/10/11/bikin-jquery-textarea-autogrow-tolong-dikoreksi-dulu-hehehe/"
source: "facebook.com"
author: "Wak Jek"
comments: [{"author": "Heri Hehe Setiawan", "date": "Tuesday 11 October 2011 at 15:14", "text": "ada demonya?"}, {"author": "Kecoa Ngamuk Kecoa", "date": "Tuesday 11 October 2011 at 15:18", "text": "^ kok ilang komennya?"}, {"author": "Heri Hehe Setiawan", "date": "Tuesday 11 October 2011 at 15:27", "text": "konspirasi"}, {"author": "Prast Rahastu", "date": "Tuesday 11 October 2011 at 15:50", "text": "kalo nulis pake tag code dong gan. biar rapi"}, {"author": "Wak Jek", "date": "Tuesday 11 October 2011 at 15:54", "text": "wait demo :D"}, {"author": "Heri Hehe Setiawan", "date": "Tuesday 11 October 2011 at 16:26", "text": "Wak Hehe Jek can i see it yet?"}, {"author": "Mohammad Naufal Fadil", "date": "Tuesday 11 October 2011 at 16:26", "text": "bukan nya itu namanya jQuery Texarea Elastic ya ?"}, {"author": "Heri Hehe Setiawan", "date": "Tuesday 11 October 2011 at 16:26", "text": "Muhammad Naufal Fadil where can i get it?"}, {"author": "Mohammad Naufal Fadil", "date": "Tuesday 11 October 2011 at 16:27", "text": "Google it n00b's !"}, {"author": "Heri Hehe Setiawan", "date": "Tuesday 11 October 2011 at 16:28", "text": "what the f*ck dude"}, {"author": "Mohammad Naufal Fadil", "date": "Tuesday 11 October 2011 at 16:28", "text": "dude? dude harlino"}, {"author": "Heri Hehe Setiawan", "date": "Tuesday 11 October 2011 at 16:28", "text": "Dude Jande"}, {"author": "Kecoa Ngamuk Kecoa", "date": "Tuesday 11 October 2011 at 16:28", "text": "go fuck dude herlino"}, {"author": "Heri Hehe Setiawan", "date": "Tuesday 11 October 2011 at 16:32", "text": "fuck me"}, {"author": "Wak Jek", "date": "Tuesday 11 October 2011 at 16:35", "text": "emang diguugel banyak kok yk gitu,\ntapi bwt sendiri lebih maknyos.\nini mau setup demo pake bilerplate malah kelamaan asem"}, {"author": "Mohammad Naufal Fadil", "date": "Tuesday 11 October 2011 at 16:36", "text": "Wak Hehe Jek : Wow wak jeek ikut2an om her maho wwowowo"}, {"author": "Heri Hehe Setiawan", "date": "Tuesday 11 October 2011 at 16:37", "text": "hehe"}, {"author": "Wak Jek", "date": "Tuesday 11 October 2011 at 17:02", "text": ":D"}, {"author": "Prast Rahastu", "date": "Tuesday 11 October 2011 at 17:31", "text": "About the author\n\nWak, 28 years old, not gay."}, {"author": "Wak Jek", "date": "Tuesday 11 October 2011 at 17:43", "text": "http://cektkp.com/demo/index.php?page=textarea_autogrow"}, {"author": "Heri Hehe Setiawan", "date": "Tuesday 11 October 2011 at 18:32", "text": "di webkit ada delay dikit om"}, {"author": "Prast Rahastu", "date": "Tuesday 11 October 2011 at 18:46", "text": "di ie7 juga #abaikan"}, {"author": "Wak Jek", "date": "Tuesday 11 October 2011 at 19:26", "text": "apa mungkin karena pake animate, 70, :D\nwait ane coba di ie9, siap2 ngakak"}, {"author": "Wak Jek", "date": "Tuesday 11 October 2011 at 19:31", "text": "diie delai jg :D"}, {"author": "Mohammad Naufal Fadil", "date": "Tuesday 11 October 2011 at 19:36", "text": "di opera mobile sama skali gag work om...."}]
---

<p>Bikin jQuery textarea autogrow, tolong dikoreksi dulu hehehe.</p>

<p><script></p>

<p>$(document).ready(function(){</p>

<p>function cektkp_growtextarea(textarea){</p>

<p>textarea.each(function(){</p>

<p>textarea = $(this);</p>

<p>textarea.css('overflow','hidden');</p>

<p>var pos = textarea.position();</p>

<p>var growerid = 'textarea_grower_'+textarea.attr('id');</p>

<p>textarea.after('<div style="position:absolute;z-index:-1000;visibility:hidden;top:'+pos.top+';height:'+textarea.height()+'" id="'+growerid+'"></div>');</p>

<p>var growerdiv = $('#'+growerid);</p>

<p>growerdiv.css({'font-size':textarea.css('font-size'),'width':textarea.width()});</p>

<p>growerdiv.html(textarea.val().replace(/\n/g, "<br />."));</p>

<p>if(textarea.val() == ''){</p>

<p>growerdiv.html('.');</p>

<p>}</p>

<p>textarea.height(growerdiv.height());</p>

<p>textarea.keyup(function(){</p>

<p>growerdiv.html($(this).val().replace(/\n/g, "<br />."));</p>

<p>if($(this).val() == ''){</p>

<p>growerdiv.html('.');</p>

<p>}</p>

<p>$(this).animate({height:growerdiv.height()}, 70);</p>

<p>});</p>

<p>});</p>

<p>}</p>

<p>cektkp_growtextarea($('textarea.autogrow'));</p>

<p>});</p>

<p></script></p>

<p>demo:</p>

<p>http://cektkp.com/demo/index.php?page=textarea_autogrow</p>
