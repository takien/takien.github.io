---
title: "[Photoshop] Tutorial Menyeleksi Rambut (Hair Selection Tutorial)"
date: "2007-10-10T05:10:00.000Z"
categories: ["Design","Tutorial"]
tags: ["design","photoshop"]
slug: "2007/10/10/photoshop-tutorial-menyeleksi-rambut-hair-selection-tutorial"
legacyUrl: "/2007/10/10/photoshop-tutorial-menyeleksi-rambut-hair-selection-tutorial/"
source: "designkillers.com"
author: "takien"
nowNote: "Kalau lihat tutorial ini sekarang aku nggak habis fikir, gimana dulu aku membuatnya dan kapan waktunya, padahal di saat itu juga ngurusin 2 forum, banyak blog, dan tetap rajin posting di KasKus dan ikut forum-forum luar negeri, sambil jaga warnet. Jualan hosting, menerima proyek orderan website dan benerin komputer. Ya, semua ini aku kerjakan di warnet, karena aku nggak punya PC sendiri. Dan aku ngekos, bolak-balik ke warnet naik angkot. Jaraknya cukup jauh."
nowDate: "7 September 2026"
comments: []
---

<figure class="text-center">
<img src="/images/designkillers/seleksi/-0-foto-miyabi-depan.webp"></figure>

<img src="/images/designkillers/ym/grin.gif" alt="Grin"> Hayaw ngeliatin apa? kenal gak sama foto ini? ah masa gak kenal.. <img src="/images/designkillers/ym/shocked.gif" alt="Shocked">

Karena ini bukan kuis tebak gambar, lanjut deh! Dalam tutorial Photoshop kali ini kita akan melakukan seleksi rambut menggunakan fasilitas Channel dan Masking. Apa itu channel dan apa itu masking tidak usah dijelaskan yah, yang penting gunakan aja, heheh.... Juga gak usah dibahas kenapa memilih foto tersebut sebagai objeknya.. huehueheuehee..

Apa itu seleksi rambut, singkatnya memisahkan objek dengan backgroundnya untuk dimana objeknya tersebut berambut.. <img src="/images/designkillers/ym/cool.gif" alt="Cool"> Kenapa dipisahkan? yah biasanya bertujuan untuk penggantian background dengan latar yang lain.

Sebelumnya tentu saja sediakan fotonya dulu, bagi yang belum punya koleksinya (ah masa sih... ) klik link di bawah ini:

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-00-foto-asli-miyabi-pho.webp" />
<Figcaption>Foto Miyabi (Asli)</figcaption>

</figure>
**1. Buka gambar tersebut menggunakan Photoshop (Gambar A)**

Otomatis gambar akan menjadi layer Background yang terkunci (tidak bisa di-edit).

Untuk membukanya cukup klik dua kali pada Layer Background tersebut dan klik OK, maka layer Background sudah editable dan berubah namanya menjadi Layer 0 (Gambar B).

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-01-buka-file-miyabi-pho.webp">

<figcaption>Gambar A</figcaption>

</figure> <figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-02-buat-layer-editable-.webp">

<figcaption>Gambar B</figcaption>

</figure>

**2. Terangkan bagian muka**

Perhatikan foto tersebut sejenak terutama di bagian muka (husshh.. jangan lama-lama <img src="/images/designkillers/ym/tongue.gif" alt="Tongue">). Nah bagian tersebut terlihat agak gelap dibandingkan bagian tubuh yang lain.

Sekarang kita terangkan warnanya menggunakan Dodge Tool (O) dengan memberinya Midtones (karena kalau pake Highlight akan terlalu terang).

a. Pilih Dodge Tool

Pilih Dodge Tool atau tekan huruf O (Gambar C), kemudian tentukan nilainya:

Brush: 500
Range: Midtones
Exposure: 100%

(Gambar D)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-03-dodge-tool-miyabi-ph.webp">

<figcaption>Gambar C</figcaption>

</figure> <figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-04-nilai-nilai-dodge-to.webp">

<figcaption>Gambar D</figcaption>

</figure>
b. Klik bagian kepala

Kemudian klik bagian kepala menggunakan Dodge tadi (berbentuk bulat seperti brush).

Klik satu kali aja yah, udah terlihat terang kan? (Gambar E)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-05-sebelum-dan-sesudah-.webp">

<figcaption>Gambar E</figcaption>

</figure>

**3. Buat Path**

Nah, sekarang kita menggunakan path untuk menyeleksi bagian badan, kenapa pake ini? Yah inilah tools yang paling fleksibel dan mudah digunakan untuk menyeleksi di Photoshop, terutama untuk objek-objek yang tajam / sharp).

a. Gunakan Pen Tool

Untuk membuat path, kita menggunakan Pen Tool (Gambar F), tapi jangan lupa pilih Path di toolbar (Gambar G), kalau tidak maka sapuan Pen Tool akan menjadi Shape (Objek).

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-06-pen-tool-miyabi-phot.webp">

<figcaption>Gambar F</figcaption>

<img src="/images/designkillers/seleksi/foto-miyabi-07-pilih-path-miyabi-ph.webp">

<figcaption>Gambar G</figcaption>

</figure>

b. Buat path mengelilingi badan

Tariklah Pen Tool (tapi bukan drag), Pen Tool digunakan dengan cara mengeklik pada suatu titik kemudian menariknya ke arah titik selanjutnya, begitu seterusnya.

Tarik sampai titik akhir bertemu dengan titik awal melalui sekeliling badan foto. (Gambar H)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-08-buat-path-miyabi-pho.webp">

<figcaption>Gambar H</figcaption>

</figure>
c. Perhatikan bagian rambut

Namun ada yang perlu diperhatikan (dan tidak boleh diabaikan tentu saja), ketika melewati bagian kepala (rambut), path tidak dibuat di tepi rambut, melainkan lebih ke dalam lagi. (Gambar I)

Kenapa begitu? Karena area ini nantinya akan kita seleksi menggunakan Channel.

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-09-bagian-rambut-jangan.webp">

<figcaption>Gambar I</figcaption>

</figure>
d. Tutup path

Nah, pastikan ujung path bertemu dengan titik awal tadi sehingga terbentuklah path tertutup (Gambar J).

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-10-path-di-tutup-miyabi.webp">

<figcaption>Gambar J</figcaption>

</figure>
e. Buat path tambahan

Lalu bagaimana dengan area ini?

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-11-trus-bagian-ini-gima.webp">

<figcaption>Gambar K</figcaption>

</figure>

Hueheuheueheeue, tenang... kita buat lagi path baru di area tersebut. Caranya sama, pake Pen Tools (P) juga.. jangan pake pen beneran <img src="/images/designkillers/ym/grin.gif" alt="Grin">

Pastikan juga path tertutup (Gambar L).

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-12-buat-path-di-area-ta.webp">
<figcaption>Gambar L</figcaption>

</figure>

Nah.. sekarang baru kita gabungkan kedua path tersebut menjadi satu kesatuan yang solid, adil dan makmur.... bagi seluruh rakyat Indonesia.. heuehueeheue ngacaw... <img src="/images/designkillers/ym/grin.gif" alt="Grin">

Kita satukan menggunakan Path Selection Tool (A) (Gambar M).

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-13a-gunakan-path-select.webp">

<figcaption>Gambar M</figcaption>

</figure>

Caranya:

Klik path pertama (badan) menggunakan Path Selection Tool (A), tekan tombol Shift (jangan dilepas) kemudian klik path kedua (lengan). Path yang terpilih akan ditandai dengan kotak-kotak di sekelilingnya. (Gambar N)

Lihat di bagian toolbar, di situ ada beberapa pilihan penggabungan (combine) path. Kita pilih yang Exclude Overlapping Shape Areas, kemudian klik Combine (Gambar N).

<div style="border:1px dashed red;text-align:center;padding:10px">IMAGE MISSING</div>

**4. Simpan Path**

Path yang udah cape-cape kita buat sekarang disimpan, biar gak nyesal di kemudian hari. heheh.

Caranya, klik tab Paths yang ada di pallete Layer.

Nah, di situ akan terlihat sebuah layer path dengan nama Work Path, kita klik 2 kali untuk menyimpannya dan beri nama misalnya Body. (Gambar O)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-14-simpan-path-miyabi-p.webp">

<figcaption>Gambar O</figcaption>

</figure>

**5. Pilih Channel**

Nah, sekarang kita menuju pallete Channel, dimana? Ah.. deket-deket pallete Path juga kok. Tepatnya di antara pallete Layer dan pallete Paths.

Di situ terlihat ada beberapa channel warna, di antaranya RGB, Red, Green, dan Blue.

Sekarang coba klik salah satu channel tersebut? Apa yang terjadi dengan gambar? heheh berubah warna yah..

Di sini kita pilih channel yang memberikan perbedaan warna paling kontras antara rambut dan background. In this case, Red Channel does. <img src="/images/designkillers/ym/grin.gif" alt="Grin">

Maka kita pilih Red. (Gambar P)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-15-pilih-channel-red-mi.webp">
 <figcaption>Gambar P</figcaption>

</figure>

**6. Duplikasi Channel**

Karena channel Red merupakan channel utama dalam gambar, maksudnya perubahan di channel ini juga akan mempengaruhi keseluruhan gambar. Hal ini tentu saja tidak diperbolehkan.

Maka kita perlu melakukan penggandaan channel (duplikasi, red) <img src="/images/designkillers/ym/smiley.gif" alt="Smiley">

Untuk melakukannya klik kanan channel Red kemudian klik Duplicate Channel, sehingga terbentuklah channel baru bernama Red Copy. (Gambar Q)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-16-duplikat-channel-miy.webp">
<figcaption>Gambar Q</figcaption>

</figure>

**7. Highlight Menggunakan Dodge Tool**

Untuk apa? Kita menegaskan perbedaan warna latar (background putih) dengan warna rambut (hitam).

a. Atur Dodge Tool

Untuk melakukannya kita pake Dodge Tool (R) dengan memilih:

Range: Highlights
Exposure: 30–50%

(Gambar R)

<div style="border:1px dashed red;text-align:center;padding:10px">IMAGE MISSING</div>
b. Sapukan Dodge Tool

Sapukan Dodge Tool di area luar rambut sedemikian rupa sehingga area tersebut menjadi lebih putih. (Dengan konsekuensi tidak menghapus rambutnya loh)...

Sesuaikan exposure dan besar brush sesuai kebutuhan. (Gambar S)

<div style="border:1px dashed red;text-align:center;padding:10px">IMAGE MISSING</div>

**8. Pilih/Seleksi Area Rambut**

Sekarang kita lakukan seleksi terhadap area sekeliling rambut yang telah di-highlight tadi menggunakan Polygonal Lasso Tool. (Gambar T)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-19-polygonal-lasso-tool.webp">
<figcaption>
Gambar T</figcaption></figure>

Yang dipilih adalah area yang berwarna putih (jangan kena rambut dan jangan kena bagian luar lainnya), dan seleksi hanya dilakukan di kepala saja. (Gambar U)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-20-lakukan-seleksi-di-s.webp">
<figcaption>
Gambar U</figcaption></figure>

Kita balikkan seleksi (inverse) dengan memilih menu Select → Select Inverse atau menekan tombol Ctrl + Shift + I, sehingga bagian kepala jadi tidak terseleksi sementara bagian lain terseleksi. (Gambar V)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-21-balikkan-seleksi-sel.webp">
<figcaption>
Gambar V</figcaption></figure>

**9. Isi seleksi dengan warna putih**

Setelah kita melakukan pembalikan seleksi, sekarang kita isi (Fill) dengan warna putih.

Caranya klik menu Edit → Fill dan pilih White di kotak dialog yang muncul. (Gambar W)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-22-diisi-dg-warna-putih.webp">
<figcaption>
Gambar W</figcaption></figure>

Nah, beginilah penampakannya setelah area tersebut diisi dengan warna putih. (Gambar X)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-23-setelah-diisi-warna-.webp">
<figcaption>
Gambar X</figcaption></figure>

Jangan lupa tekan tombol Ctrl + D untuk menghilangkan seleksi, atau menu Select → Deselect.

**10. Membuat Path menjadi seleksi**

Kembali ke pallete Paths, klik path Body (tadi disimpan dengan nama Body soalnya heheh).

Kemudian klik Load Path as Selection di bagian bawah pallete Path. (Gambar Y)

<div style="border:1px dashed red;text-align:center;padding:10px">IMAGE MISSING</div>
11. Balikkan seleksi, isi dengan warna hitam
a. Balikkan seleksi

Setelah path menjadi seleksi kemudian kita balikkan seleksi tersebut (inverse), dengan menekan Ctrl + Shift + I atau dari menu Select → Select Inverse. (Gambar Z)

b. Isi dengan warna hitam

Setelah seleksi berbalik, kemudian kita isi dengan warna hitam, klik menu Edit → Fill dan pilih Black pada pilihan kotak dialog Fill yang muncul. (Gambar Z)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-25-balikkan-seleksi-isi.webp">
<figcaption>
Gambar Z</figcaption></figure>

Setelah itu jangan lupa menghilangkan seleksi dengan menekan Ctrl + D.

**12. Padukan bagian rambut dengan Burn Tool**

Setelah terisi dengan warna hitam, maka keseluruhan body termasuk rambut akan berwarna hitam dengan latar putih.

Hanya saja biasanya terdapat semacam garis pemisah (gap) di area sebelah dalam rambut. Ini terjadi karena area tersebut diseleksi menggunakan dua cara yang berbeda, yaitu path dan yang satunya lagi dengan channel.

Maka dari itu kita perlu memadukan / blur daerah tersebut menggunakan Burn Tool (O).

Pilih:

Range: Shadows
Exposure: 30–50%

Sapukan Burn Tool di sepanjang gap tersebut secara merata sehingga warna hitam di area kepala akan terlihat solid. Tapi Burn Tool jangan sampe keluar area rambut. (Gambar AA)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-26-rapikan-menggunakan-.webp">

<figcaption>Gambar AA</figcaption>

</figure>

**13. Seleksi Channel**

Sekarang kita lakukan seleksi terhadap channel Red Copy yang telah dimodifikasi tersebut dengan cara mengeklik icon Load Channel As Selection di bagian bawah pallete Channel. (Gambar AB)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-27-klik-load-channel-as.webp">

<figcaption>Gambar AB</figcaption>

</figure>

Seperti biasa kita lakukan pembalikan seleksi (Select Inverse) dengan menekan tombol Ctrl + Shift + I. (Gambar AC)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-28-balikkkan-seleksi-mi.webp">

<figcaption>Gambar AC</figcaption>

</figure>

**14. Tambahkan Masking di Layer 0**

Dengan keadaan masih terseleksi, kita kembali ke pallete Layer. Di sini kita akan menambahkan Masking pada Layer 0.

Caranya klik Layer 0 di pallete Layer untuk mengaktifkannya, kemudian klik icon Add Layer Mask yang ada di bagian bawah pallete Layer. (Gambar AD)

<figure class="text-center">
 <img src="/images/designkillers/seleksi/foto-miyabi-29-klik-add-layer-mask-.webp">

<figcaption>Gambar AD</figcaption>

</figure>

**15. Hehehe... Background sudah jadi transparan**

Apa yang terjadi selanjutnya ternyata background dari foto tadi menjadi transparan..

wow... <img src="/images/designkillers/ym/shocked.gif" alt="Shocked"> heheh....

Don't Panic, lagunya Coldplay <img src="/images/designkillers/ym/grin.gif" alt="Grin">

Memang itu kok tujuan dari perjalanan panjang tadi... heheheh (gak ada icon cape deh.. <img src="/images/designkillers/ym/sad.gif" alt="Sad"> )

**16. Tambahkan background baru sesukanya**

Hehhee..

Untuk menambah background baru tinggal membuat layer baru yang diletakkan di bawah Layer 0. (buat ndiri yah.. cape neh.. hehehhe..)

Nih contohnya.. klik untuk melihat versi besarnya...

<di class="md:flex">
<img src="/images/designkillers/seleksi/hasil_03.webp"> 

<img src="/images/designkillers/seleksi/hasil_02.webp"> 

<img src="/images/designkillers/seleksi/hasil_01.webp"> 

</div>

Oke.. sekian dulu deh, bagi yang mao coba-coba jangan segan-segan postingkan disini hasilnya, bagi yang kuran jelas silakan di tanya, kalau belum ngerti juga entarnya dibuat lagi tutorial yang lebih spesifik tentang rambut. Bagi yang mao rekues foto-fotonya yang lain PM aja. <img src="/images/designkillers/ym/cheesy.gif" alt="Cheesy">

Trus bagi yang udah tau, kritik dan sarannya dipersilahkan.

Selamat bekerja, yang udah siap kumpulkan! wkwkkakawkwa
