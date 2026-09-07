---
title: "Cara Membuat Spoiler"
date: "2008-11-10T06:49:00.000Z"
categories: ["Tutorial","JavaScript","HTML"]
tags: ["spoiler","javascript","html","vbulletin","web development"]
slug: "2008/11/10/cara-membuat-spoiler"
legacyUrl: "/2008/11/10/cara-membuat-spoiler/"
source: "indowebmasters.com"
author: "takien"
comments: [{"author":"ripiyuku","date":"","text":"udah nyoba boss … seeppppp"},{"author":"iBNuX","date":"","text":"thx for sharing…"},{"author":"iBNuX","date":"","text":"tapi klo multi spoiler ga jalan yang keduanya"},{"author":"takien","date":"","text":"@ibnux,\nbisa, untuk multi spoiler cukup tambahkan div lagi di masing2 spoilernya…\n\njadinya begini…\n\nspoiler 1\n\n\n.... disini kode spoiler seperti contoh di atas\n\n\n\n\nspoiler 2\n\n\n.... disini kode spoiler untuk contoh diatas...\n\n\n\n\nboleh dicoba"},{"author":"dago7","date":"","text":"bikin yang kaya di kaskus douung"},{"author":"takien","date":"","text":"tinggal ganti aja Tampilkan/Sembunyikan menjadi Show/Hide :-j"},{"author":"Misz","date":"","text":"Bisa dipakai di WP ngga ya?\nTerus kalo bisa naruhnya di bagaian mana?"},{"author":"Cyber Search","date":"","text":"ane coba di theme ane kok ngga bisa ya mas..apa themenya yang ngga support ya..?"},{"author":"takien","date":"","text":"hmmmm…\nntar ane cek lagi gan"},{"author":"Xrvel","date":"","text":"udah saya cek gan. makasih gan.. bisa gan :p"},{"author":"takien","date":"","text":"Hello all,\nsudah saya buatkan pluginnya untuk WordPress, tinggal upload instal.\nCek link di atas.\nThank you"},{"author":"Cyber Search","date":"","text":"walah…mantaff..ijin sedot gan..pertamaxxx"},{"author":"Crist_erick","date":"","text":"ijin sedot gan, thx"},{"author":"Anonymous","date":"","text":"silahkan gan"},{"author":"Anonymous","date":"","text":"work gan… bisa di wp ane"}]
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

**Versi plugin WordPress**

[Di sini](/2008/11/10/cara-membuat-spoiler-di-wordpress/)
