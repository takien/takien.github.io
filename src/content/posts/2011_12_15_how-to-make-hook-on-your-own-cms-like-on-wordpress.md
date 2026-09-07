---
title: "How To Create a Wordpress-Alike Hook For Your Own CMS?"
date: "2011-12-15T00:00:00Z"
categories: ["Uncategorized"]
tags: []
slug: "2011/12/15/how-to-make-hook-on-your-own-cms-like-on-wordpress"
legacyUrl: "/blog/2011/12/15/how-to-make-hook-on-your-own-cms-like-on-wordpress/"
comments: [{"author": "Heri Setiawan", "date": "", "text": "Dude, this is awesome. !"}, {"author": "Nilesh Parate", "date": "", "text": "thanks for nice and functional"}]
---

<div id="attachment_972" style="width: 310px" class="wp-caption alignleft"><a href="https://web.archive.org/web/20160103044025/http://img.takien.com/2011/12/hooks.jpg"><img src="/images/2011/12/hooks-300x300.jpg" alt="" title="hooks" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">Hooks ilustration, image courtesy of lookingglassoutfitters.com</p></div>
<p>Probably you have known this, WordPress code is pretty good, especially when compared with other CMS or what we ever found on PHP tutorials. The one I like is how WordPress uses <a href="https://web.archive.org/web/20160103044025/http://codex.wordpress.org/Plugin_API/Hooks" target="_blank">hooks.</a>   If you ever created WordPress <a href="/category/cms/wordpress/wp-plugins" target="_blank">plugins</a>, you may experienced that you don&#8217;t need to modify any of core code just to add something in the header and footer. Or even for more complex task, add additional menu and page on WordPress admin.</p>
<p>Things you need to do is to know what hook related to that, and add actions or filter with your own callback function. WordPress hooks divided in to two sections; <em>Action hook</em> and <em>Filter hook</em>. What is the difference? In simple, actions is to add functionality or output, where filter is to manipulate existing output. WordPress hook code stored in <em>wp-includes/plugins.php</em></p>
<p>Err, I am not going to deeply explain about WordPress hook. But, in case you&#8217;re wondering how it works or may be you want implement it in your own CMS or PHP script, here is the step by step .</p>
<p>If WordPress uses global variable <strong>$wp_filter</strong> to store all of the filters, we use <strong>$cms_filter</strong> instead, or name it whatever you like .  This variable contains array of filters where we could modify later. To start, fill it with empty array.</p>

```php
$cms_filter = array();
```

<p>Declare <strong>do_action()</strong> function, the task of this function is to call custom functions stored in $cms_filter, uses  <a href="https://web.archive.org/web/20160103044025/http://php.net/manual/en/function.call-user-func-array.php" target="_blank"><em>call_user_func_array()</em></a>;</p>

```php
function do_action($tag){
  global $cms_filter;
  if(isset($cms_filter[$tag]) AND function_exists($cms_filter[$tag])){
    call_user_func_array($cms_filter[$tag], array());
  }
}
```

<p>Declare <strong>add_action()</strong> function, the task of this function is to store custom function to $cms_filter global variable.</p>

```php
function add_action($tag,$callback){

global $cms_filter;

$cms_filter[$tag] = $callback;

}
```

<p>And&#8230;&#8230;&#8230;. you&#8217;re done. What..? Yes, that code is already to use.</p>
<p>Ok, let&#8217;s go. Place this code in wherever you like, for example in your core CMS file, or in your header&#8217;s template file between &lt;head&gt; and &lt;/head&gt;</p>

```php
do_action('cms_head');
```

<p>Whenever you want to add something to the location, just call this function:</p>

```php
add_action('cms_head','script_in_my_head');
```

<p><em>cms_head</em> is hook name, and<em> script_in_my_head</em> is must exists callback function that refer to your custom code. See example below:</p>

```php
function script_in_my_head(){

echo '<script>alert('Hello world!')</script>';

}
```

<p><strong>Note</strong>: This is only a simple working code, not a replacement nor has same capability as actual WordPress hooks. You may edit or improve it to meet your need.</p>
