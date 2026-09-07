---
title: "Status Facebook 25 June 2012"
date: "2012-06-25T18:33:00Z"
categories: ["Programming"]
tags: ["facebook", "W3 kaskus", "programming"]
slug: "2012/06/25/status-facebook-25-june-2012"
legacyUrl: "/2012/06/25/status-facebook-25-june-2012/"
source: "facebook.com"
author: "Wak Jek"
group: "W3 kaskus"
comments: [{"author": "Wak Jek", "date": "Monday 25 June 2012 at 18:33", "text": "kebetulan ane perlu hahahah"}, {"author": "Mohammad Naufal Fadil", "date": "Monday 25 June 2012 at 18:34", "text": "anonmous itu heker kan ya?"}, {"author": "Wak Jek", "date": "Monday 25 June 2012 at 18:35", "text": "diganti pake apa, klu dulu kan cuma ngandalkan create_function() untuk anonymous, klo create_function yang mbingungi krn quote qutoe nya harus bener supaya gk eror (kyk eval());"}, {"author": "Wak Jek", "date": "Monday 25 June 2012 at 18:35", "text": "anonymous function berguna untuk fungsi yang argumennya callback, jadi gk perlu bikin fungsi lagi secara terpisah."}, {"author": "Jeffri Tjin", "date": "Monday 25 June 2012 at 18:42", "text": "asik nih... :))\n\nadd_filter('blabla', function($maho){ return 'bukan'.$maho; });"}, {"author": "Teguh Oktian", "date": "Monday 25 June 2012 at 18:50", "text": "'hehe' ama 'blabla' itu fungsi apa string?"}, {"author": "Wak Jek", "date": "Monday 25 June 2012 at 18:51", "text": "itu string,"}]
---

<p>.<br/>
baru tau ternyata di php >= 5.3.0  udah ada anonymous function</p>

<p>echo some_function('hehe',function($hammer){<br/>
return $hammer;<br/>
});</p>

<p>jadi kyk javascrpt</p>
