---
title: "[Solved] WordPress Custom Taxonomy Slug Using Forward Slash"
date: "2014-09-27T12:33:22+00:00"
categories: ["Tips & Tutorial"]
tags: ["WordPress", "custom post type", "custom taxonomy", "rewrite"]
slug: "2014/09/27/solved-wordpress-custom-taxonomy-slug-using-forward-slash"
legacyUrl: "/2014/09/27/solved-wordpress-custom-taxonomy-slug-using-forward-slash/"
comments: []
---

<div class="content-wrap">
					<div class="add">

</div>
<p>I have custom post type <code>product</code> and want to attach custom taxonomy for that post type named <code>Product Category</code>. By default that custom taxonomy slug is <code>product-category</code>. What I want is to use custom slug <code>product/category</code>. But, unfortunately, WordPress just ignore that slug and return 404.</p>
<p><strong>Debugging</strong><br/>
I looked on the <code>$wp_rewrite</code> variable and found that custom taxonomy rewrite comes after custom post type slug. That was caused the problem.</p>
<p><strong>Solution 1, Using Rewrite Plugin</strong></p>
<p>Surprisingly, my own plugin, <strong><a href="https://web.archive.org/web/20160305194419/https://wordpress.org/plugins/rewrite/">Rewrite</a></strong> solves this problem.<br/>
All you need to do is <em>reorder</em> the rules so that custom taxonomy rewrite rules placed before custom post type rewrite rules.</p>
<p>See figure below.</p>
<figure id="attachment_1408" style="width: 1024px" class="wp-caption aligncenter"><img src="/images/2014/09/rewrite-rules-wordpress-custom-taxonomy-1024x492.png" alt="WordPress custom taxonomy slug using forward slash " title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><figcaption class="wp-caption-text">WordPress custom taxonomy slug using forward slas</figcaption></figure>
<p><strong>Solution 2, Using Code Snippet</strong></p>


```php
add_filter('rewrite_rules_array', 'takien_custom_tax_slug_forward_slash',100);

function takien_custom_tax_slug_forward_slash( $rules ) {
	$slug = 'product/category';
	
	$rule = Array();
	$rule = array($slug.'/([^/]+)/?$' => $rules[$slug.'/([^/]+)/?$']) + $rule;
	$rule = array($slug.'/([^/]+)/page/?([0-9]{1,})/?$' => $rules[$slug.'/([^/]+)/page/?([0-9]{1,})/?$']) + $rule;
	$rule = array($slug.'/([^/]+)/(feed|rdf|rss|rss2|atom)/?$' => $rules[$slug.'/([^/]+)/(feed|rdf|rss|rss2|atom)/?$']) + $rule;
	$rule = array($slug.'/([^/]+)/feed/(feed|rdf|rss|rss2|atom)/?$' => $rules[$slug.'/([^/]+)/feed/(feed|rdf|rss|rss2|atom)/?$']) + $rule;
	
	$rules = $rule + $rules;
	return $rules;
}
```


</p><div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/custom-post-type/">custom post type</a> <a class="label label-default" href="/tag/custom-taxonomy/">custom taxonomy</a> <a class="label label-default" href="/tag/rewrite/">rewrite</a> <a class="label label-default" href="/tag/wordpress/">WordPress</a> </div>										
									</div>
