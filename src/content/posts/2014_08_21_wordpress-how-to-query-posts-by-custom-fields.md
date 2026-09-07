---
title: "WordPress: How to Query Posts by Custom Fields?"
date: "2014-08-21T00:00:00Z"
categories: ["Wordpress"]
tags: []
slug: "2014/08/21/wordpress-how-to-query-posts-by-custom-fields"
legacyUrl: "/2014/08/21/wordpress-how-to-query-posts-by-custom-fields/"
comments: []
---

<div style="float:left;margin-right:10px;margin-bottom:10px;">

</div>
						<p>One of my friends asked me how to make WordPress query by custom fields. Let&#8217;s say he has a <code>date</code> custom fields in <code>event</code> post type and want to filter posts based on the date.</p>
<p>By default, WordPress has this capability. That&#8217;s why I loved WordPress <img src="/images/misc/icon_wink.gif" alt=";)" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /> And of course, WordPress codex done the job very well.</p>
<div class="table-responsive"><table style="width:500px; " class="easy-table easy-table-default tablesorter  table-striped">
<tbody>
<tr><td>Post type</td>
<td> event</td>
</tr>

<tr><td>Custom field name </td>
<td> date</td>
</tr>

<tr><td>Custom field value</td>
<td> August 20, 2014</td>
</tr>
</tbody></table></div>
<p><strong>Build query parameter</strong></p>



```php
$args = array(
	'post_type'  => 'event', /* If you leave it empty it would be 'post' by default */
	'meta_query' => array(
		array(
			'key'     => 'date', /* Custom field name */
			'value'   => 'August 20, 2014',  /* Custom field value */
		),
	),
);
$query = new WP_Query( $args );
if ( $query->have_posts() ) :
	while ( $query->have_posts() ) :
		$query->the_post();
		echo get_the_title().'<br />';
	endwhile;
endif;
```


<p>That&#8217;s it. For more complex custom fields parameter, please refers to: <a href="https://web.archive.org/web/20141220095906/http://codex.wordpress.org/Function_Reference/WP_Query#Custom_Field_Parameters" target="_blank">http://codex.wordpress.org/Function_Reference/WP_Query#Custom_Field_Parameters</a></p>
