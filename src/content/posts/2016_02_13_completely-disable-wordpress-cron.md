---
title: "How to Completely Disable WordPress Cron?"
date: "2016-02-13T18:20:08+00:00"
categories: ["Tips & Tutorial"]
tags: ["WordPress"]
slug: "2016/02/13/completely-disable-wordpress-cron"
legacyUrl: "/2016/02/13/completely-disable-wordpress-cron/"
comments: []
---

<div class="content-wrap">
					<figure class="image-missing-placeholder" role="img" aria-label="clock time">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">clock time</span>
  </div>
</figure><div class="add">

</div>
<p>WordPress has ability to schedule posts, so our posts can be published in the future. This feature uses WordPress cron system, not a real cron, but something like virtual cron. Yes, because it use a file called `wp-cron.php` to do this task.  This is useful of course. But, if you don&#8217;t need this, you can completely disable it.</p>
<p>All you need to do is add a line of code on your `wp-config.php` that prevent cron to run. Open wp-config.php using your favourite code editor. Find a line contain <code>define('WP_DEBUG', false);</code> and add <code>define('DISABLE_WP_CRON', true);</code> after it and save the file.</p>



```php
define('DISABLE_WP_CRON', true);
```


<p>Or see the figure below:</p>
<figure class="image-missing-placeholder" role="img" aria-label="wordpress disable cron">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">wordpress disable cron</span>
  </div>
</figure>
<p>So, what happened after you add the code? You can still scheduled post, it it won&#8217;t be published. It said <em>missed schedule</em></p>
<figure class="image-missing-placeholder" role="img" aria-label="missed schedule">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">missed schedule</span>
  </div>
</figure>
<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/wordpress/">WordPress</a> </div>										
									</div>
