---
title: "How To Insert Image In WordPress via Context Menu?"
date: "2016-02-29T16:48:48+00:00"
categories: ["Tips & Tutorial"]
tags: ["Plugins", "WordPress", "tinymce"]
slug: "2016/02/29/insert-image-wordpress-via-context-menu"
legacyUrl: "/2016/02/29/insert-image-wordpress-via-context-menu/"
comments: []
---

<div class="content-wrap">
					<figure class="image-missing-placeholder" role="img" aria-label="Blogging using WordPress">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Blogging using WordPress</span>
  </div>
</figure><div class="add">

</div>
<p>In WordPress, you can add or insert image easily using Add Media button above the WordPress editor toolbar. Yes, there&#8217;s no problem with it, except you have to move your mouse cursor there. If you think it&#8217;s too much efforts to do it, now you can simplify the access to <em>Add Media </em>button via context menu on your WordPress editor using <strong>Insert Image Context Menu</strong> plugin.</p>
<p>Thank God, WordPress uses TinyMCE, the most popular WYSIWYG editor which is very customizable and supports many plugins. For this purpose, I use <strong>contextmenu</strong> plugin (https://www.tinymce.com/docs/plugins/contextmenu/). This plugin, if added to TinyMCE will replace native browser context menu to our own custom menus.</p>
<p>Here is the plugin code:</p>
<p>File: <strong>insert-image-contextmenu.php</strong></p>
<p>This is the main file, add WordPress action and filter to load TinyMCE plugin.</p>



```php
<?php
/*
Plugin Name: Insert Image Context Menu
Plugin URI: /
Description: Add context menu on WordPress editor contains link to insert image.
Author: Takien
Version: 1.0
*/

add_action( 'admin_init', 'insert_imagecontextmenu_tinymce_button' );
add_filter( 'tiny_mce_before_init', 'insert_imagecontextmenu_context_menu' );

function insert_imagecontextmenu_tinymce_button() {
     if ( current_user_can( 'edit_posts' ) && current_user_can( 'edit_pages' ) ) {
          add_filter( 'mce_external_plugins', 'insert_imagecontextmenu_add_tinymce_button' );
     }
}

function insert_imagecontextmenu_add_tinymce_button( $plugin_array ) {
     $plugin_array['contextmenu'] = plugins_url( '/tinymce/plugins/contextmenu/plugin.min.js', __FILE__ ) ;
     $plugin_array['image_contextmenu'] = plugins_url( '/tinymce/plugins/image-contextmenu/image-contextmenu.js', __FILE__ ) ;
     return $plugin_array;
}

function insert_imagecontextmenu_context_menu( $in ) {
	$in['contextmenu'] = 'image_contextmenu';
	return $in;
}
```


<p>File: <strong>image-contextmenu.js</strong></p>
<p>This is the TinyMCE plugin to add menu item in context menu, when clicked, it simply trigger to click Insert Media button.</p>



```javascript
tinymce.PluginManager.add('image_contextmenu', function(editor) {
	editor.addMenuItem('image_contextmenu', {
		icon: 'image',
		text: 'Insert image',
		onclick: function() {
			document.getElementById('insert-media-button').click();
		},
		context: 'insert',
		prependToContext: true
	});
});
```


<p><strong>Note</strong></p>
<p>This plugin will replace native browser context menu. But you can still access native menu (cut, copy etc) by holding <kbd>CTRL</kbd> key when right click on the editor.</p>
<p><strong>Plugin in action </strong></p>
<div style="width: 968px; " class="wp-video">
<video class="wp-video-shortcode" id="video-1510-1" width="968" height="482" loop="1" autoplay="1" preload="metadata" controls="controls"><source type="video/mp4" src="https://web.archive.org/web/20160504040736im_/http://img.takien.com/2016/02/Insert-image-context-menu-wordpress-plugin-1.mp4?_=1"/><a href="https://web.archive.org/web/20160504040736/http://img.takien.com/2016/02/Insert-image-context-menu-wordpress-plugin-1.mp4">http://img.takien.com/2016/02/Insert-image-context-menu-wordpress-plugin-1.mp4</a></video></div>

<p>Wanna this plugin? Download it from Github using the following link:</p>
<div style="text-align: center;">
<div class="btn-group"><a class="btn btn-primary" href="https://web.archive.org/web/20160504040736/https://github.com/takien/Insert-Image-Context-Menu" target="_blank"><i class="glyphicon glyphicon-arrow-down"></i> Download Insert Image Context Menu plugin</a></div>
</div>
</p><div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/wp-plugins/">Plugins</a> <a class="label label-default" href="/tag/tinymce/">tinymce</a> <a class="label label-default" href="/tag/wordpress/">WordPress</a> </div>										
									</div>
