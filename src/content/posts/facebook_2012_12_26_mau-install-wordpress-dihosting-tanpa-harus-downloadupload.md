---
title: "Mau install WordPress dihosting tanpa harus download/upload?"
date: "2012-12-26T14:30:00.000Z"
categories: ["WordPress"]
tags: ["facebook","Belajar WordPress","wordpress"]
slug: "2012/12/26/mau-install-wordpress-dihosting-tanpa-harus-downloadupload"
legacyUrl: "/2012/12/26/mau-install-wordpress-dihosting-tanpa-harus-downloadupload/"
source: "facebook.com"
author: "Wak Jek"
group: "Belajar WordPress"
comments: [{"author":"Bang Ate","date":"Wednesday 26 December 2012 at 14:30","text":"tinggal copy script and save? taruh dimna nih om?"},{"author":"Kecoa Ngamuk Kecoa","date":"Wednesday 26 December 2012 at 14:30","text":"klo di cpanel yg shared host ane biasa pake cron aja satu2nya akses shell   wget http://urldownload   dah lama gak download upload kecuali kerjaan dari kompie lokal"},{"author":"Kecoa Ngamuk Kecoa","date":"Wednesday 26 December 2012 at 14:31","text":"oiya php ini juga bisa dieksekusi di cron jadi gak usah nunggu loading"},{"author":"Wak Jek","date":"Wednesday 26 December 2012 at 14:32","text":"Rizky , save as aja script tsb ke, misalnya copy.php, kemudian jalankan dari browser webagan.com/copy.php"},{"author":"Kecoa Ngamuk Kecoa","date":"Wednesday 26 December 2012 at 14:32","text":"GET  http://url/scriptwakjek.php\natau\nphp -q /path/ke/scriptwakjek.php"},{"author":"Wak Jek","date":"Wednesday 26 December 2012 at 14:32","text":"Kecoa itu sekalian extract"},{"author":"Kecoa Ngamuk Kecoa","date":"Wednesday 26 December 2012 at 14:33","text":"nah iya maksudnya pakein cron biar gak pake loading"},{"author":"Wak Jek","date":"Wednesday 26 December 2012 at 14:34","text":"oh, gk pake loading, tapi nunggu sampe waktu nya baru jalan\nbtw loadingnya cpt kok, cuma bbrp detik."},{"author":"Kecoa Ngamuk Kecoa","date":"Wednesday 26 December 2012 at 14:35","text":"waktunya 1 menit aja    oo wp terbaru berapa emang ukurannya? klo file 100 mb aja pake exec(wget) kadang setengah menitan :hammer:"},{"author":"Wak Jek","date":"Wednesday 26 December 2012 at 14:37","text":"5Mb an"},{"author":"Agus Triyono","date":"Wednesday 26 December 2012 at 15:00","text":"alasan nya tidak aman kenapa gan jika\ninstal pake fatastico atau softacolus ..?\napakah ada secrip yang di susupi atau bagemana..?"},{"author":"Wak Jek","date":"Wednesday 26 December 2012 at 15:08","text":"sbrnya itu dulu gan, bnyk yang di hack klo instalan dari fantastico, gk tau skrg, krn script2 installer itu pake username/db nya biasanya default seperti wp1 wp2 dsb."},{"author":"Sabihul Anwary","date":"Wednesday 26 December 2012 at 15:39","text":"bukannya bisa di set ya sebelum install nama dbnya apaan?\nCMIIW gak pernah install lewat situ soalnya, bisa diterapkan ini nih kalo pindah rumah"},{"author":"Wak Jek","date":"Wednesday 26 December 2012 at 15:41","text":"Sabihul Anwary, pake fantastico bisa diset?"},{"author":"Sabihul Anwary","date":"Wednesday 26 December 2012 at 15:42","text":"eh tapi ini fresh install ya?\nkalo pindah rumahkan ada dbnya om, bijimana tuh?"},{"author":"Wak Jek","date":"Wednesday 26 December 2012 at 15:45","text":"nah itu gak tau"},{"author":"Kecoa Ngamuk Kecoa","date":"Wednesday 26 December 2012 at 15:53","text":"klo pindah rumah, terus shared host ane biasa pake wget aja dari cron, sayang untuk db gak bisa otomatis karena user biasa cpanel gak bisa create user dan nama db via shell (mesti u root) , untuk db mesti create manual dari cpanel, baru klo untuk dumpnya bisa lwt shell (cronjob).\n\nTapi klo fresh install kayanya ane hampir gak pernah lsg install di hosting, biasa di utak atik dulu di lokal kompie. utak atik di live hosting sayang BW lagian editornya kurang yahud"},{"author":"Yanuar Arifianto","date":"Wednesday 26 December 2012 at 18:30","text":"Ane selalu upload manual, apalagi karena sekarang pake Contorl Panel Webuzo, mau copast file dari browser susah beudh."},{"author":"Sabihul Anwary","date":"Wednesday 26 December 2012 at 18:31","text":"^ paham kemanualan"},{"author":"Mohamad Rafi","date":"Thursday 27 December 2012 at 16:56","text":"wah,nice inpoh kk,"},{"author":"Argado Simarmata","date":"Monday 31 December 2012 at 23:46","text":"Akhirnya nemu lagi, kemarin smpt liat sekilas, tp mlm tahun baru dibutuhin. Thanks mastah"},{"author":"Argado Simarmata","date":"Monday 31 December 2012 at 23:48","text":"Om, hasilnya kaya gini\n\nCopy ok\nFatal error: Class 'ZipArchive' not found in /home/ftpname/public_html/wp.php on line 6\n\nitu knp ya?\nTp hasil kopiannya ada .."},{"author":"Kecoa Ngamuk Kecoa","date":"Tuesday 1 January 2013 at 02:28","text":"^ cek pake phpinfo modul zip ada apa nggak di phpnyam biasanya ada keterangannya zip active atau enabled atau zip installed"}]
---

<p>Mau install WordPress dihosting tanpa harus download/upload?</p>

<p>Script ini jika dijalankan otomatis akan mencopy Wordpress versi terbaru dan mengextract nya ke folder /wordpress.</p>

```
<?php
if(copy('http://wordpress.org/latest.zip','wp.zip')) {

echo 'Copy ok';
//extract 
$zip = new ZipArchive;
if ($zip->open('wp.zip') === TRUE) {
$zip->extractTo('/');
$zip->close();
echo 'extract OK';
} else {
echo 'Extract failed';
}
}
else {
echo 'copy failed';
}
?>
```

<p>sbrnya di cpanel ada juga fasilitas installer fantastico atau srciptaculous. tapi ktnya sih tidak aman, makanya saya tidak pernah pake</p>
