---
title: "Mengambil dan Mengirim Data Menggunakan Curl"
date: "2011-02-04T18:02:19+00:00"
categories: ["PHP"]
tags: []
slug: "2011/02/04/mengambil-dan-mengirim-data-menggunakan-curl"
legacyUrls: ["468/mengambil-dan-mengirim-data-menggunakan-curl.html", "468/mengambil-dan-mengirim-data-menggunakan-curl", "w3magz/468/mengambil-dan-mengirim-data-menggunakan-curl.html", "w3magz/468/mengambil-dan-mengirim-data-menggunakan-curl"]
source: "w3magz.com"
author: "Wak Jek"
comments: [{"author": "Hardi Kristawan", "date": "", "text": "sangat membatu"}, {"author": "Gea Bianlala", "date": "", "text": "sebelum loading situs lain tentukan dulu ukuran web page nya. loading web page dengan ukuran besar dapat memboroskan bandwidth web server."}]
---

<p><strong>Penggunaan cURL di PHP </strong>(bagian 2, habis)</p>
<p>Pada edisi lalu (w3magz edisi #1) telah saya bahas dasar-dasar penggunaan cURL untuk mengambil data dari URL lain di localhost.<br/>

```php
<?php

$ch = curl_init();

curl_setopt($ch,CURLOPT_URL,'http://localhost/test/curl/data.php');

curl_exec($ch);

curl_close($ch);

?>
```

<p>Kali ini akan saya lanjutkan pembahasan tentang pengambilan data dari website lain dengan domain yang berbeda. Pada dasarnya teknik yang digunakan adalah sama seperti sebelumnya, hanya saja di bagian CURLOPT_URL kita isikan alamat URL website yang kita tuju, dalam contoh ini adalah website http://w3magz.com, seperti di bawah ini:</p>

```php
<?php

$ch = curl_init();

curl_setopt($ch,CURLOPT_URL,'http://w3magz.com');

curl_exec($ch);

curl_close($ch);

?>
```

<p>Simpan file tersebut sebagai curl-latihan-2.php dan jalankan di browser. Hasilnya akan terlihat seperti ini:</p>
<figure class="image-missing-placeholder" role="img" aria-label="curl-2-1">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">curl-2-1</span>
  </div>
</figure>
<p><strong>Opsi Curl</strong></p>
<p>Opsi curl adalah parameter-parameter yang dapat kita tambahkan untuk menentukan bagaimana curl dijalankan. Opsi dapat ditentukan dengan memanggil fungsi curl_setopt, dan menambahkan konstan dan nilai ke dalamnya. Konstan opsi curl biasanya diawali dengan CURLOPT_</p>
<p>Di contoh sebelumnya, kita telah menggunakan opsi curl:</p>

```php
<?php

curl_setopt($ch,CURLOPT_URL,'http://w3magz.com');

?>
```

<p>curl_setopt 	= fungsi untuk memanggil opsi curl.<br/>
$ch			= resource sesi curl.<br/>
CURLOPT_URL	= konstan opsi curl yang nilainya kita isi dengan url http://w3magz.com</p>
<p>Ada banyak konstan dalam opsi curl ini, namun yang paling umum digunakan adalah sebagai berikut:</p>
<p><strong>CURLOPT_HEADER</strong>, jika nilai TRUE, menyertakan info <em>response header</em> dalam outputnya.<br/>
<strong>CURLOPT_NOBODY</strong>, jika nilai TRUE, tidak menyertakan body ke dalam outputnya.<br/>
<strong>CURLOPT_FOLLOWLOCATION</strong>, jika nilai TRUE, akan mengikuti semua location recdirect.<br/>
<strong>CURLOPT_MAXREDIRS</strong>, menentukan jumlah redirek yang akan diikuti.<br/>
<strong>CURLOPT_RETURNTRANSFER</strong>, jika nilai TRUE, maka output dari curl_exec() dapat disimpan di dalam variabel, tidak langsung ditampilkan ke browser.<br/>
<strong>CURLOPT_POST</strong>, jika nilai TRUE, untuk melakukan pengiriman data, contohnya mengisi dan mengeksekusi form.<br/>
<strong>CURLOPT_POSTFIELDS</strong>, dapat diisi dengan data yang akan di POST, data dapat berbentuk Array atau string dengan format urlencode seperti field1=value1&#038;field2=value2</p>
<p>Berikut contoh curl dengan opsi menampilkan header response, tanpa body, dan menyimpan output ke dalam variabel $result kemudian menampilkannya.</p>

```php
<?php

$ch = curl_init();

curl_setopt($ch,CURLOPT_URL,'http://w3magz.com');

curl_setopt($ch,CURLOPT_HEADER,TRUE);

curl_setopt($ch,CURLOPT_NOBODY,true);

curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);

$result = curl_exec($ch);

echo $result;

curl_close($ch);

?>
```

<p>Simpan file dengan nama<em>  curl-latihan-3.php</em> dan lihat hasilnya di browser, seperti gambar berikut:</p>
<figure class="image-missing-placeholder" role="img" aria-label="curl-2-2">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">curl-2-2</span>
  </div>
</figure>
<p><strong>Mengirim Data (POST) dengan CURL</strong></p>
<p>Untuk mengepost data dengan curl, kita harus memberi opsi CURLOPT_POST dengan TRUE atau 1, dan mengisi opsi CURLOPT_POSTFIELDS dengan data yang akan dipost.</p>
<p>Contoh:<br/>
1. Buatlah sebuah form sederhana, simpan sebagai form.php</p>

```php
<?php

if(isset($_POST['submit'])){

	echo '

```php
';

	print_r($_POST);

	echo '
```

';

}

?>

<form action="" method="post">

Nama: <input type="text" name="nama" value="" /><br />

Email: <input type="text" name="email" value="" /><br />

<input type="submit" name="submit" value="submit" />

</form>
```

<p>Ketika form diisi dan disubmit, maka akan terlihat seperti gambar berikut:</p>
<figure class="image-missing-placeholder" role="img" aria-label="curl-2-3">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">curl-2-3</span>
  </div>
</figure>
<p>2. Pada gambar form diatas terlihat field nama dengan value john dan field email dengan value john@test.com berhasil di submit. Mari kita coba melakukan hal yang sama, tapi melalui CURL, untuk itu buatlah file  curl-latihan-4.php dengan isi sebagai berikut:</p>

```php
<?php

$ch = curl_init();

curl_setopt($ch,CURLOPT_URL,'http://localhost/test/curl/form.php');

curl_setopt($ch,CURLOPT_POST,TRUE);

curl_setopt($ch,CURLOPT_POSTFIELDS,'nama=john&email=john@test.com&submit=submit');

curl_setopt($ch,CURLOPT_RETURNTRANSFER,TRUE);

$result = curl_exec($ch);

echo $result;

curl_close($ch);

?>
```

<p>Maka ketika file curl-latihan-4.php dijalankan, hasilnya adalah seperti gambar berikut:</p>
<figure class="image-missing-placeholder" role="img" aria-label="curl-2-4">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">curl-2-4</span>
  </div>
</figure>
<p>Dapat kita lihat bahwa hasilnya adalah sama dengan ketika kita melakukan pengsian form secara manual.</p>
<p>Demikianlah pembahasan tentang dasar-dasar penggunaan curl di PHP, semoga bermanfaat.</p>
<p><em>Note:<br/>
response header = Reponse header adalah jawaban dari server atas permintaan dari client/browser, biasanya berisi beberapa informasi server, cache, type maupun status dokumen. Response header tidak  ditampilkan di browser.</em></p>

