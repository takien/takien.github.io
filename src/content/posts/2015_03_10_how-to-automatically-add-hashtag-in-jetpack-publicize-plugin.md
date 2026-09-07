---
title: "How to Automatically Add Hashtag In Jetpack Publicize Plugin"
date: "2015-03-10T00:00:00Z"
categories: ["Wordpress"]
tags: []
slug: "2015/03/10/how-to-automatically-add-hashtag-in-jetpack-publicize-plugin"
legacyUrl: "/2015/03/10/how-to-automatically-add-hashtag-in-jetpack-publicize-plugin/"
comments: []
---

<div style="float:left;margin-right:10px;margin-bottom:10px;">

</div>
						<p>JetPack has lot of great functions, one of my favourite is <em>publicize</em> that will auto post published WordPress posts into selected social media like Twitter, Facebook, Google+ etc.<br/>
You can modify the content of social post before publishing a post. But if you want to do it automatically, just add the following code somewhere in your plugin or functions.php file.</p>



```php
add_filter( 'wpas_default_message', 'auto_add_publicize_hashtag', 10, 4 );

function auto_add_publicize_hashtag($title) {
	$title = $title.' #hashtag1 #hashtag2';
	return $title;
}
```


<p>Once it saved, you publicize screen will be like this:</p>
<p><img src="/images/2015/03/WordPress-Jetpack-Automatic-hashtag-Twitter-Facebook-Google-Plus-Publicize.png" alt="WordPress Jetpack Automatic hashtag Twitter Facebook Google Plus Publicize" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>

<div id="jp-relatedposts" class="jp-relatedposts">
	<h3 class="jp-relatedposts-headline"><em>Related</em></h3>
</div>
