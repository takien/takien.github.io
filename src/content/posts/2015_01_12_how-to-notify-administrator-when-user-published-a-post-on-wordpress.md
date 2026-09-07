---
title: "How to Notify Administrator When User Published a Post on WordPress?"
date: "2015-01-12T11:45:32+00:00"
categories: ["Tips & Tutorial"]
tags: ["WordPress"]
slug: "2015/01/12/how-to-notify-administrator-when-user-published-a-post-on-wordpress"
legacyUrl: "/2015/01/12/how-to-notify-administrator-when-user-published-a-post-on-wordpress/"
comments: []
---

<div class="content-wrap">
					<div class="add">

</div>
<figure class="image-missing-placeholder" role="img" aria-label="Email">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">Email</span>
  </div>
</figure>
<p>Do you have multi-author WordPress site and you want to get notification when an user published a post? Here is the solution:</p>



```php
<?php 
/**
 *  Notify admin when user published post
 *  @author: takien
 */
function notify_admin_published_post( $ID, $post ) {
	$emailed_to       = 'admin@example.com';//edit this, your email here.
	
    $author_id        = $post->post_author; 
    $author_name      = get_the_author_meta( 'display_name', $author_id );
    $author_email     = get_the_author_meta( 'user_email', $author_id );
    $title     = $post->post_title;
    $permalink = get_permalink( $ID );
    $edit      = get_edit_post_link( $ID, '' );
    $to[]      = $emailed_to;
    $subject   = $author_name.' published an article "'. $title .'"';
    $message   = 'Dear Admin, '.$author_name.' has publised an article';
	$message   .= '<br />Title: '. $title ;
	$message   .= '<br />Link: '. $permalink ;
	$message   .= '<br />Edit Link: '. $edit ;
	
    $headers = "From: " . $author_email . "\r\n";
	$headers .= "Content-Type: text/html; charset=ISO-8859-1\r\n";
	
    wp_mail( $to, $subject, $message, $headers );
}
add_action( 'publish_post', 'notify_admin_published_post', 10, 2 );
```

<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/wordpress/">WordPress</a> </div>										
									</div>
