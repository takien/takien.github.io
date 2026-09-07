---
title: "Cara Membuat Spoiler"
date: "2008-11-10T06:49:00.000Z"
categories: ["Tutorial", "JavaScript", "HTML"]
tags: ["spoiler", "javascript", "html", "vbulletin", "web development"]
slug: "2008/11/10/cara-membuat-spoiler"
legacyUrl: "/2008/11/10/cara-membuat-spoiler/"
source: "indowebmasters.com"
author: "takien"
comments:
  - author: "ripiyuku"
    date: "2008-11-28 18:32:00"
    text: "udah nyoba boss … seeppppp"
  - author: "iBNuX"
    date: "2008-12-01 04:29:00"
    text: "thx for sharing…"
  - author: "iBNuX"
    date: "2009-01-27 03:42:00"
    text: "tapi klo multi spoiler ga jalan yang keduanya"
  - author: "Administrator"
    date: "2009-01-27 16:04:00"
    text: "@ibnux, bisa, untuk multi spoiler cukup tambahkan div lagi di masing2 spoilernya… jadinya begini… spoiler 1: <div>... kode spoiler</div> spoiler 2: <div>... kode spoiler</div> boleh dicoba :)"
  - author: "dago7"
    date: "2009-01-29 10:38:00"
    text: "bikin yang kaya di kaskus douung"
  - author: "Administrator"
    date: "2009-01-29 17:08:00"
    text: "tinggal ganti aja Tampilkan/Sembunyikan menjadi Show/Hide :-j"
---

Menyembunyikan konten tertentu dari sebuah halaman website terkadang diperlukan untuk menghemat space. Ketika visitor ingin melihatnya mereka dapat dengan mudah menampilkannya. Dalam software forum semacam vBulletin, hal ini disebut dengan Spoiler.

Berikut adalah contoh penggunaan spoiler:

<div style="margin: 1rem 0;">
  <div>
    <input style="margin: 0; padding: 0.35rem 0.75rem; cursor: pointer; border-radius: 4px; border: 1px solid #ccc; background: #eee; font-weight: 500;" onclick="if (this.parentNode.parentNode.getElementsByTagName('div')[1].getElementsByTagName('div')[0].style.display != '') { this.parentNode.parentNode.getElementsByTagName('div')[1].getElementsByTagName('div')[0].style.display = ''; this.value = 'Sembunyikan'; } else { this.parentNode.parentNode.getElementsByTagName('div')[1].getElementsByTagName('div')[0].style.display = 'none'; this.value = 'Tampilkan'; }" type="button" value="Sembunyikan" />
  </div>
  <div style="margin: 10px auto; background: #c9d2ed; padding: 10px 14px; border: 1px solid #a3b2db; border-radius: 4px; color: #1e293b;">
    <div>Ini adalah konten yang disembunyikan, klik tombol Sembunyikan/Tampilkan untuk membuka atau menutup konten ini.</div>
  </div>
</div>

Bagaimana cara membuatnya? Hanya diperlukan sedikit kode javascript yang langsung diembed di kode html.

```html
<div>
<input style="margin:0px;padding:0px;" onclick="if (this.parentNode.parentNode.getElementsByTagName('div')[1].getElementsByTagName('div')[0].style.display != '') { this.parentNode.parentNode.getElementsByTagName('div')[1].getElementsByTagName('div')[0].style.display = '';this.innerText = ''; this.value = 'Sembunyikan'; } else { this.parentNode.parentNode.getElementsByTagName('div')[1].getElementsByTagName('div')[0].style.display = 'none'; this.innerText = ''; this.value = 'Tampilkan'; }" type="button" value="Tampilkan" /></div>
<div style="border: 1px solid #000000; margin: 10px auto; padding: 5px; background: #c9d2ed none repeat scroll 0% 0%; width: 500px;">
<div style="display: none;">
Ini adalah konten yang disembunyikan, klik tombol Sembunyikan/Tampilkan untuk membuka atau menutup konten ini.</div>
</div>
```
