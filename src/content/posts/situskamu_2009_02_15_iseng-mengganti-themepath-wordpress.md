---
title: "Iseng Mengganti ThemePath Wordpress"
date: "2009-02-15T12:00:00Z"
categories: ["CMS", "Internet", "Template", "Theme", "WordPress", "website"]
tags: ["2007", "2008", "blog", "blogger", "Browser", "cara menginstall wordpress", "cari duit", "city", "css", "custom block", "custom region", "div", "domain", "domain parking", "Drupal", "drupal theme", "forum", "Google", "htaccess", "html", "integration", "Internet", "Internet Explorer", "kaleidoskop", "kilas balik", "layout", "mini city", "mod rewrite", "parked domain", "review", "security", "SEO", "SMF", "Spyware", "table", "tutorial wordpress", "upgrade wordpress", "Web 2.0", "Webdesign", "website", "WordPress", "wordpress plugin", "Wordpress theme", "wordpress upgrade", "xampp"]
slug: "2009/02/15/iseng-mengganti-themepath-wordpress"
legacyUrl: "/iseng-mengganti-themepath-wordpress/"
source: "blog.situskamu.com"
comments: [
  {
    "author": "Anonymous",
    "date": "Apr 28, 08 at 2:23 pm",
    "text": "mantap juragan,….\n\ndi tunggu tut…tut… yg lain      \n\nbrb"
  },
  {
    "author": "Anonymous",
    "date": "Aug 28, 08 at 2:14 pm",
    "text": "Pak…Bisa tidak step2nya di jelaskan lebih detail..saya kok gak bisa yach…\n\nnamakamu reply on September 3rd, 2008:\n\nsebaiknya coba dulu di localhost, supaya aman..\n\nsepertinya udah jelas tuh.. kalau ada yang kurang jelas tanyakan aja…\n\nsesuai dengan judulnya “iseng..” disini penulis juga tidak pertanggung jawab terhadap dampak negatif yang mungkin ditimbulkan akibat pengeditan tersebut…"
  }
]
---

<p><img src="/images/2008/04/wordpress-25-logo.jpg" alt="Wordpress Theme Free" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" />Wordpress yang secara default meletakkan file-file theme atau template nya di folder <span style="text-decoration: underline;">wp-content/themes/namatheme</span> sebenarnya bisa diganti loh, sesuai dengan <a href="https://web.archive.org/web/20090415193218/http://bb17.net/">selera nusantara</a>. Informasi mengenai path theme wordpress tersebut disimpan dalam beberapa file yang bisa diedit menggunakan editor file manager maupun dreamweaver, dengan catatan harus terlebih dahulu memindahkan file-file theme ke folder baru yang diinginkan, misalnya <span style="text-decoration: underline;">theme</span>/. <span id="more-126"></span><br/>
<span style="color: #ffffff;">/</span><br/>
Setelah folder theme dipindahkan ke tempat yang baru, selanjutnya adalah mengedit file yang meyimpan informasi path tadi. File yang harus diedit diantaranya: wp-admin/themes.php, wp-admin/includes/upgrade.php, wp-includes/comment-template.php, wp-includes/general-template.php, wp-includes/theme.php. Buka file tersebut satu persatu menggunakan text editor, dan cari teks <em>wp-content/themes</em>, kemudian diganti/replace dengan nama folder baru tempat meletakkan theme misalnya <em>theme</em>. SImpan kembali file-file yang telah diedit tersebut.</p>
<p><span style="color: #ffffff;">/</span></p>
<p>Karena perubahan path ini biasanya theme yang dipakai akan kembali ke default theme, untuk mengembalikannya, masuk ke <em>Dashboard -&gt; Design</em>, dan kembali aktifkan theme yang sebelumnya digunakan. 🙂 </p>
<p><span style="color: #ffffff;">/</span></p>
<p>Selain path theme yang bisa dirubah, <em>path admin wordpress</em> juga bisa diganti dari <span style="text-decoration: underline;">wp-admin</span> menjadi folder lainnya sesuai keinginan. Tapi aku sendiri belum mengetesnya apakah mempengaruhi kinerja wordpress, seperti plugins-plugins maupun proses <a href="/wordpress-automatic-upgrade-otomatis-jadi-version-25/">upgrade </a>nantinya. Eh, sekarang <a href="https://web.archive.org/web/20090415193218/http://andri.cisco.or.id/blogs/index.php/2008/04/26/wordpress-251-upgrade-lagi/">Wordpress udah versi 2.5.1</a> loh, untung udah pakai Wordpress automatic upgrade. 🙂 </p>
