---
title: "How To Disable Native WordPress Comment If You’re Using Disqus?"
date: "2016-03-01T11:12:07+00:00"
categories: ["Tips & Tutorial"]
tags: ["WordPress", "WordPress comment", "disqus"]
slug: "2016/03/01/disable-native-wordpress-comment-using-disqus"
legacyUrl: "/2016/03/01/disable-native-wordpress-comment-using-disqus/"
comments: []
---

<div class="content-wrap">
					<figure class="image-missing-placeholder" role="img" aria-label="WordPress comment">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">WordPress comment</span>
  </div>
</figure><div class="add">

</div>
<p>I have been using Disqus since <a href="/2011/09/12/cara-memasang-komentar-disqus-di-wordpress/" target="_blank">years ago</a> to replace default comment system on this WordPress blog. Previously I was using Disqus Comment System plugin (https://wordpress.org/plugins/disqus-comment-system/) , the official Disqus plugin for WordPress.  But now I&#8217;m using <strong>Disqus Conditional Load</strong>, the unofficial Disqus plugin, because it&#8217;s promised to be faster than the official one. The only problem is, although you have enabled Disqus on your blog, the spammer still can insert comment directly. I think, this should be disabled.</p>
<p>So, how to disable WordPress comment? There&#8217;s a filter named <code>preprocess_comment</code> in WordPress. This filter located inside <code>wp_new_comment()</code> function in <code>wp-includes/comment.php</code>. No, you no need to go there. Just add this one line code on your <code>functions.php</code> of your theme.</p>



```php
add_filter('preprocess_comment','__return_false');
```


<p>Wanna spam? Please fight with Disqus. 🙂</p>
<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/disqus/">disqus</a> <a class="label label-default" href="/tag/wordpress/">WordPress</a> <a class="label label-default" href="/tag/wordpress-comment/">WordPress comment</a> </div>										
									</div>
