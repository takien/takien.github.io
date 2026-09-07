---
title: "Reserved socket.io event"
date: "2012-05-13T01:04:00Z"
categories: ["Pribadi"]
tags: ["facebook", "Node.js Indonesia", "pribadi"]
slug: "2012/05/13/reserved-socketio-event"
legacyUrl: "/2012/05/13/reserved-socketio-event/"
source: "facebook.com"
author: "Wak Jek"
group: "Node.js Indonesia"
comments: [{"author": "Mohammad Naufal Fadil", "date": "Sunday 13 May 2012 at 01:04", "text": "untuk di server side apa client side ??"}, {"author": "Wak Jek", "date": "Sunday 13 May 2012 at 01:06", "text": ".\nclient, kalau server cuma ini yang reserved:\n'connection'\n'message'\n'disconnect'"}]
---

<p>reserved socket.io event:</p>

<p>'message'<br/>
'connect'<br/>
'disconnect'<br/>
'connect_failed'<br/>
'open'<br/>
'close'<br/>
'error'<br/>
'retry'<br/>
'reconnect'<br/>
'reconnect_failed'</p>

<p>pastikan kalau bikin custom event jangan pake nama2 tersebut krn udah mempunyai fungsi2nya sendiri.</p>
