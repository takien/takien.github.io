---
title: "How to Display WordPress Post Only from Current User"
date: "2015-01-05T00:00:00Z"
categories: ["Tips & Tutorial"]
tags: []
slug: "2015/01/05/how-to-display-wordpress-post-only-from-current-user"
legacyUrl: "/2015/01/05/how-to-display-wordpress-post-only-from-current-user/"
comments: []
---

<div class="content-wrap">
					<div class="add">

</div>
<p>Do you want to display your users&#8217; posts only for posts they own when they logged in? By using the following code, you can do that.</p>
<p>Here is the code, place it on your <code>funtions.php</code> file on your current theme.</p>



```php
function display_post_only_current_user( $query ) {
    if ( is_admin() ) {
        $query->set( 'author', get_current_user_id() );
    }
}
add_action( 'pre_get_posts', 'display_post_only_current_user' );
```

<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/wordpress/">WordPress</a> </div>										
									</div>
