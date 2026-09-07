---
title: "Cara Mempercepat Loading Website, Asyncronous JavaScript, YepnopeJS HeadJS, Chain JS"
date: "2013-09-05T00:00:00Z"
categories: ["Uncategorized"]
tags: []
slug: "2013/09/05/cara-mempercepat-loading-website-menggunakan-asyncronous-javascript"
legacyUrl: "/blog/2013/09/05/cara-mempercepat-loading-website-menggunakan-asyncronous-javascript/"
comments: [{"author": "Abonk Farouk", "date": "", "text": "karna saiya ga bisa apa-apa nanti minta tolong wak aja yang bikinin :v"}, {"author": "Fauzie", "date": "", "text": "nice info"}, {"author": "Coki Widodo", "date": "", "text": "Mantab gan"}, {"author": "ruidi", "date": "", "text": "gan tulung detail create filenya dimana2 aja… bingung realisasinya… hehhe"}, {"author": "Diki Satrio Budi", "date": "", "text": "wah ini penting, jarang nih artikel kayak gini. trimakasih bro"}, {"author": "opikini", "date": "", "text": "saya coba dulu mas moga ga lemot lagi blog sy"}]
---

<div id="attachment_1261" style="width: 310px" class="wp-caption alignleft"><a href="https://web.archive.org/web/20160120194548/http://img.takien.com/2013/09/page-speed-performance.jpg"><img src="/images/2013/09/page-speed-performance-300x185.jpg" alt="Page Speed Performance test" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">Page Speed Performance test</p></div>
<p>Semakin bagus sebuah design membutuhkan banyak resource CSS dan JavaScript plugin yang perlu dimuat. Tapi konsekuensinya pageload jadi berat. Seperti kebanyakan Theme Premium yang beraaaaaaaaaaat hehe.<br/>
Selain design, sudah saatnya kita perhatikan juga pageload, semakin cepat halaman dibuka akan semakin banyaklah pengunjung, page yang ringan juga bagus buat SEO.<br/>
Solusinya, muatlah CSS dan atau JavaScript seperlunya saja, atau sesuaikan dengan kondisi.</p>
<p>Misalnya, kita nggak perlu memuat atau meload JavaScript untuk slider, jika di halaman tersebut tidak ada slider/carousel, atau kita nggak perlu load Touch API jika device client tidak touchscreen (misalnya untuk PC desktop). Begitu juga kita nggak perlu memuat jQuery Mousewheel jika client menggunakan mobile phone. Selain itu kita juga bisa membuat kondisi berdasarkan ukuran layar / viewport.<br/>
Jika hal itu dilakukan dengan benar, maka halaman akan merequest file-file yang diperlukan saja, sesuai dengan kondisi yang kita tentukan.</p>
<p>Selain itu kiga juga bisa merequest file JavaScript dan CSS secara diam-diam dibelakang layar setelah halaman selesai diload (asynchronous). Hal ini akan mencegah sebuah halaman yang macet (stuck) dan gagal menampilkan sebagian halaman karena menunggu suatu file yang ternyata terlalu berat di load, misalnya file di luar domain kita yang bisa jadi kecepatan aksesnya berbeda.<br/>
Solusi:</p>
<h2>1. Menggunakan Pure JavaScript</h2>
<p>Script ini saya temukan dari diskusi di StackOverflow (<a href="https://web.archive.org/web/20160120194548/http://stackoverflow.com/questions/3973441/conditionally-load-javascript-external-and-internal-and-keep-execution-order" target="_blank">http://stackoverflow.com/questions/3973441/conditionally-load-javascript-external-and-internal-and-keep-execution-order</a>).<br/>
Buatlah fungsi berikut ini:</p>

```javascript
// Load the script designated by `src`, poll for the appearance
// of the symbol `name` on the `window` object. When it shows
// up, call `callback`. Timeout if the timeout is reached.
function loadAndWait(src, name, timeout, callback) {
    var stop, script;

    // Do nothing if the symbol is already defined
    if (window[name]) {
        setTimeout(function() {
            callback("preexisting");
        }, 10);
    }
    else {
        // Load the script
        script = document.createElement('script');
        script.type = "text/javascript";
        script.src = src;
        document.body.appendChild(script);

        // Remember when we should stop
        stop = new Date().getTime() + timeout;

        // Start polling, long-ish initial interval
        setTimeout(poll, 150);
    }

    function poll() {
         if (window[name]) {
             // Got it
             callback("loaded");
         }
         else if (new Date().getTime() > stop) {
             // Time out
             callback("timeout");
         }
         else {
             // Keep waiting, shorter interval if desired
             setTimeout(poll, 75);
         }
    }
}
```

<p>Dan ketika kita akan meload jQuery secara asyncronous, gunakan fungsi loadAndWait tadi<br/>

```javascript
loadAndWait(
    "http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js",
    "jQuery",
    10000, // ten seconds or whatever
    function(result) {
        //fungsi jQuery Anda ketik di sini
    }
 );
```

<p>Jika Anda merasa script tersebut terlalu ribet, masih ada alternatif lain yaitu dengan mengunakan library terentu, seperti di bawah ini.</p>
<h2>2. Menggunakan Head.js</h2>
<p><a href="https://web.archive.org/web/20160120194548/http://img.takien.com/2013/09/head-js.jpg"><img src="/images/2013/09/head-js-1024x228.jpg" alt="head-js" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a></p>
<p>Head JS adalah JavaScript library yang dapat digunakan untuk meload JavaScript secara dinamis. Cara menggunakannya cukup mudah. Misalnya kita akan membuat carousel menggunakan library CarouFredSel, dimana membutuhkan jQuery. Kita akan meloadnya seperti berikut</p>

```javascript
head.js("/js/jquery.js", "/js/caroufredsel.js",function() {

   //panggil fungsi plugin jQuery di sini
   jQuery(document).ready(function($) {
   $('#mydiv').carouFredSel({
   });
  });

})
```

<p>HeadJs berukuran sangat kecil sekitar 4KB dan dapat didownload di situs resminya http://head.js.com</p>
<h2>3. Menggunakan Yepnope.JS</h2>
<div id="attachment_1265" style="width: 1029px" class="wp-caption aligncenter"><a href="https://web.archive.org/web/20160120194548/http://img.takien.com/2013/09/yepnope-js.jpg"><img src="/images/2013/09/yepnope-js.jpg" alt="YepnopeJS" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">YepnopeJS</p></div>
<p>Nah, Yepnope ini favorit saya, karena fiturnya cukup lengkap dan mudah digunakan. Yepnope mendukung callback dan kondisional. YepnopeJS dapat didownload di http://yepnopejs.com<br/>
Contoh cara meload jQuery secara asyncronous menggunakan Yepnope</p>

```javascript
yepnope([{
  // mencoba mendownload jQuery dari Google CDN
  load: 'http:/¬/ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js',
  complete: function () {
    if (!window.jQuery) { //Cek, jikta Google CDN gagal, maka kita load jQuery di lokal.
      yepnope('local/jquery.min.js');
    }
  }
}, {
  load: 'jquery.plugin.js', //load plugin tertentu
  complete: function () {
    jQuery(function () {     //panggil fungsi plugin di sini
      jQuery('div').plugin();
    });
  }
}]);
```

<p>Object Yepnope selengkapnya seperti ini<br/>

```javascript
yepnope([{
  test : /* kondisional test, boolean true atau false    */,
  yep  : /* array, jika test bernilai true, maka yep akan diload  */,
  nope : /* array, jika test bernilai false, maka nope akan diload */,
  both : /* array, akan selalu diload, meskipun test bernilau true atau false*/,
  load : /* array, akan selalu diload*/,
  callback : /* function ( testResult, key ) | object { key : fn }            */,
  complete : /* function                                                      */
}, ... ]);
```

<p>Contoh lainnya: Saya akan meload script dan CSS tertentu hanya ketika viewport lebih besar dari 320 piksel.</p>

```javascript
yepnope([{
	test: 320 < document.documentElement.clientWidth //test jika viewport lebih dari 320pixel
  , yep: [ "js/jquery.js","js/bootstrap.js","css/largescreen.css" ]
  , complete:function () {
	jQuery(document).ready(function($) {
		//kode plugin jquery di sini.
	})
	}
}
```

<br/>
Selain yang saya sebutkan di atas, sebenarnya masih banyak lagi library JavaScript yang dapat digunakan untuk meload file JavaScript/CSS secara dinamis, diantaranya</p>
<ul>
<li>Lazyload https://github.com/rgrove/lazyload/</li>
<li>ChainJS https://github.com/chriso/chain.js</li>
<li>LoadJS https://github.com/chriso/load.js</li>
<li>RequireJS http://requirejs.org</li>
<li>Conditionizr http://conditionizr.com/</li>
<li>AMDJS https://github.com/amdjs/amdjs-api/wiki/AMD</li>
<li>Modernizr http://modernizr.com</li>
</ul>
