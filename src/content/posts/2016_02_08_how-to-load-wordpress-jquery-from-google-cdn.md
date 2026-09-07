---
title: "How to Load WordPress jQuery from Google CDN?"
date: "2016-02-08T17:27:47+00:00"
categories: ["Tips & Tutorial"]
tags: ["WordPres", "jQuery"]
slug: "2016/02/08/how-to-load-wordpress-jquery-from-google-cdn"
legacyUrl: "/2016/02/08/how-to-load-wordpress-jquery-from-google-cdn/"
comments: []
---

<div class="content-wrap">
					<figure class="image-missing-placeholder" role="img" aria-label="internet illustration">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">internet illustration</span>
  </div>
</figure><div class="add">

</div>
<p>By default, WordPress would load jQuery script from it&#8217;s own wp-includes directory. But, if you want, you can change it to jQuery which hosted by Google CDN. Why you should do this? It will load faster, because Google has server with better performance, and it might has been loaded by your visitor already. Yeah, they may have visited another website with the same jQuery URL. That&#8217;s mean the script already cached on their browser.</p>
<p>So, how to do that? Place this script somewhere in your <code>functions.php</code> of your theme:</p>



```php
function use_jquery_cdn() {
	if (!is_admin()) {
		wp_deregister_script('jquery');
		wp_register_script('jquery', 'http://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js', Array(), '1.11.3', true);
		wp_enqueue_script('jquery');
	}
}
add_action('init', 'use_jquery_cdn');
```

<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/jquery/">jQuery</a> <a class="label label-default" href="/tag/wordpres/">WordPres</a> </div>										
									</div>
