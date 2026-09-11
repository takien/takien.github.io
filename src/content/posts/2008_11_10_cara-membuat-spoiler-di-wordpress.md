---
title: "Cara Membuat Spoiler di Wordpress | Wordpress Spoiler Plugins"
date: "2008-11-10T02:41:00.000Z"
categories: ["WordPress Plugins"]
tags: ["wordpress","plugim"]
slug: "2008/11/10/cara-membuat-spoiler-di-wordpress"
legacyUrl: "/2008/11/10/cara-membuat-spoiler-di-wordpress/"
source: "takien.com"
author: "takien"
comments: []
---

![spoiler](/images/uploads/1788662585082_spoiler.gif)

Menyembunyikan konten tertentu dari sebuah halaman website terkadang diperlukan untuk menghemat space. Ketika visitor ingin melihat konten yang tersembunyi tersebut mereka dapat dengan mudah menampilkannya. Dalam software forum semacam vBulletin, hal ini disebut dengan Spoiler.

Bagaimana cara membuatnya? Hanya diperlukan sedikit kode javascript yang langsung diembed di kode html. Kode ini saya colonk save as dari kaskus :D

```
[spoiler title="Test"]
Hello ini adalah text yang disembunyikan
[/spoiler]
```

Contoh diatas ditulis tanpa menggunakan spasi setelah tanda kurung buka [ dan sebelum tanda kurung tutup ]



## Plugin Spoiler



```
<?php
/*
Plugin Name: WP Kaskus Spoiler
Plugin URI: http://takien.com/99/cara-membuat-spoiler.php
Description: This plugin to insert spoiler (like vBulletin) in wordpress. Usage: [spoiler title="Hello"]Your text here[/spoiler]
Author: Takien
Version: 1.0
Author URI: http://takien.com/
*/
add_shortcode('spoiler', 'spoiler_shortcode'); 
function spoiler_shortcode( $atts, $contents = null ) {
		extract( shortcode_atts( array(
		'title' => '',
		), $atts ) );

	$return = '
	<div style="margin: 5px 20px 20px;">
	<div class="smallfont" style="margin-bottom: 2px;"><b>Spoiler</b> for <i>'.esc_attr($title).'</i>: <input value="Show" style="width: 60px; font-size: 10px; margin: 0px; padding: 0px;" onclick="if (this.parentNode.parentNode.getElementsByTagName(\'div\')[1].getElementsByTagName(\'div\')[0].style.display != \'\') { this.parentNode.parentNode.getElementsByTagName(\'div\')[1].getElementsByTagName(\'div\')[0].style.display = \'\';        this.innerText = \'\'; this.value = \'Hide\'; } else { this.parentNode.parentNode.getElementsByTagName(\'div\')[1].getElementsByTagName(\'div\')[0].style.display = \'none\'; this.innerText = \'\'; this.value = \'Show\'; }" type="button">
	</div>
	<div style="background:#e1e4f2;margin: 0px; padding: 6px; border: 1px inset;"><div style="display:none">'.$contents.'</div></div>
	</div>';
	return $return;
}
?>
```
