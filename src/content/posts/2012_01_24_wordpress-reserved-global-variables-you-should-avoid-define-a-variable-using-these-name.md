---
title: "WordPress Reserved Global Variables, You Should Avoid Define A Variable Using These Name"
date: "2012-01-24T00:00:00Z"
categories: ["Wordpress"]
tags: []
slug: "2012/01/24/wordpress-reserved-global-variables-you-should-avoid-define-a-variable-using-these-name"
legacyUrl: "/blog/2012/01/24/wordpress-reserved-global-variables-you-should-avoid-define-a-variable-using-these-name/"
comments: [{"author": "www.ozgurhaber.org", "date": "", "text": "Good systeem! I like it much"}]
---

<div style="float:left;margin-right:10px;margin-bottom:10px;">

</div>
						<div id="attachment_1054" style="width: 310px" class="wp-caption alignleft"><a href="https://web.archive.org/web/20151020022805/http://img.takien.com/2012/01/wordpress-logos.jpg"><img src="/images/2012/01/wordpress-logos-300x218.jpg" alt="" title="wordpress-logos" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">Wordpress Logos</p></div>
<p><em>Global variable</em> is a variable that is accessible in <em>every scope</em>, in PHP it works ONLY for the same page and the file that are included after. However, some predefined variables, known as <em>superglobals</em> are always accessible in whole site. Both of global and superglobal variable can be redefined or overwrite it&#8217;s value.</p>
<p>When developing a WordPress Plugin and or Theme, sometimes you use the PHP global variable. That&#8217;s okay, but it&#8217;s HIGHLY RECOMMENDED that you not use variable name that are already defined by WordPress. Why?  Because it may break your other code that may intended to use WordPress variable.</p>

<h2>Example</h2>
<p>Example case:</p>
<p><strong>1. You have this code somewhere in your theme:</strong><br/>

```php
$cat = 5; /*define cat global variable */

$paged = 2; /*define paged global variable */

/* Those variable are intended to this custom query */

query_posts("cat=$cat&posts_per_page=10&paged=$paged");

if (have_posts()) while (have_posts()) : the_post();

	echo get_the_title().'<br />';

endwhile;
```

<p>The result is you will get the list of 10 post title from category 5, paged 2. That way as what you expected.</p>
<p><strong>2. On the other hand, you (or other developer) also have this code:</strong></p>

```php
query_posts("cat=$cat&posts_per_page=10&paged=$paged");
if (have_posts()) while (have_posts()) : the_post();
	echo get_the_title().'<br />';
endwhile;
```

<p>Here, you are not define $cat and $paged variable. For the reason that your purpose is to get post in current category ($cat) and current page ($paged) <em>since $cat</em> and <em>$paged</em> variable is always available as global variable in WordPress depending on which page you&#8217;re accessed. But what happened is unexpected, because those global variable was already previously redefined (in example #1).</p>
<p>So, do not redefine a reserved WordPress global variable unless you are know what are you doing.</p>
<h2>The lists of WordPress Reserved Variable</h2>
<p>Anyway, what is the variables that reserved WordPress? Here is the list, the left side is variable name, and the right side is the type:</p>

```php
$_template_file = string
$require_once = boolean
$posts = array
$post = object
$wp_did_header = boolean
$wp_did_template_redirect = NULL
$wp_query = object
$wp_rewrite = object
$wpdb = object
$wp_version = string
$wp = object
$id = integer
$comment = NULL
$user_ID = integer
$cat = string
$paged = integer
$error = string
$m = integer
$p = integer
$post_parent = string
$subpost = string
$subpost_id = string
$attachment = string
$attachment_id = integer
$name = string
$static = string
$pagename = string
$page_id = integer
$second = string
$minute = string
$hour = string
$day = integer
$monthnum = integer
$year = integer
$w = integer
$category_name = string
$tag = string
$tag_id = string
$author_name = string
$feed = string
$tb = string
$comments_popup = string
$meta_key = string
$meta_value = string
$preview = string
$s = string
$sentence = string
$fields = string
$category__in = array
$category__not_in = array
$category__and = array
$post__in = array
$post__not_in = array
$tag__in = array
$tag__not_in = array
$tag__and = array
$tag_slug__in = array
$tag_slug__and = array
$ignore_sticky_posts = boolean
$suppress_filters = boolean
$cache_results = boolean
$update_post_term_cache = boolean
$update_post_meta_cache = boolean
$post_type = string
$posts_per_page = integer
$nopaging = boolean
$comments_per_page = string
$no_found_rows = boolean
$order = string
```

<p><img src="/images/misc/simple-smile.png" alt=":)" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>
