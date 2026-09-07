---
title: "How to Login into WordPress Without User and Password?"
date: "2014-07-15T01:57:28+00:00"
categories: ["Tips & Tutorial"]
tags: ["WordPress"]
slug: "2014/07/15/how-to-login-into-wordpress-without-user-and-password"
legacyUrl: "/2014/07/15/how-to-login-into-wordpress-without-user-and-password/"
comments: []
---

<div class="content-wrap">
					<div class="add">

</div>
<p>Sometime we need to login to WordPress system without knowing username and password. Using these sort of functions you can bypass all authentication process and directly logged in into speficif user id.</p>
<p>Change <code>$user_id</code> value to desired user id, eg. 1 for admin.</p>



```php
if(!is_user_logged_in()) {
$user_id = 1;
wp_clear_auth_cookie();
wp_set_current_user( $user_id );
wp_set_auth_cookie( $user_id );
}
```


<p>Place it somewhere in your theme or plugin, and, voila&#8230;.. You&#8217;re logged in.</p>
<figure id="attachment_1025" style="width: 285px" class="wp-caption aligncenter"><img src="/images/2012/01/wordpress-logo.jpg" alt="wordpress logo" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><figcaption class="wp-caption-text">wordpress logo</figcaption></figure>
<p>So what the heck this thing useful for?</p>
<ul>
<li>To login into WordPress without using username and password. You don&#8217;t say.</li>
<li>To know site behavior for spesific user.</li>
<li>To make connection with social networking site like Facebook or Google Plus.</li>
</ul>
</p><div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/wordpress/">WordPress</a> </div>										
									</div>
