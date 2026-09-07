---
title: "How to Fix WordPress database error Table ‘wp_termmeta’ doesn’t exist"
date: "2016-02-08T22:40:05+00:00"
categories: ["Tips & Tutorial"]
tags: ["WordPress", "database", "error"]
slug: "2016/02/08/how-to-fix-wordpress-database-error-table-wp_termmeta-doesnt-exist"
legacyUrl: "/2016/02/08/how-to-fix-wordpress-database-error-table-wp_termmeta-doesnt-exist/"
comments: [{"author": "Anonymous", "date": "2016-02-08", "text": "Ferri Sutanto says:"}]
---

<div class="content-wrap">
					<figure class="image-missing-placeholder" role="img" aria-label="WordPress database error">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">WordPress database error</span>
  </div>
</figure><div class="add">

</div>
<p>Recently I got so many errors log contains <em>WordPress database error Table &#8216;wpdb.wp_termmeta&#8217; doesn&#8217;t exist for query SELECT term_id &#8230; </em>. I don&#8217;t know why it happened but it says that the table wp_termmeta does not exists.</p>
<figure class="image-missing-placeholder" role="img" aria-label="WordPress Error Database Term Meta Does Not Exists">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">WordPress Error Database Term Meta Does Not Exists</span>
  </div>
</figure>
<h3>Error log</h3>



```javascript
[08-Feb-2016 15:19:13 UTC] WordPress database error Table 'wpdb.wp_termmeta' doesn't exist for query SELECT term_id, meta_key, meta_value FROM wp_termmeta WHERE term_id IN (20,55,36,3,8,41,113,117,200,12,14,15,112,6,22,78,7,13,16,17,31,34,61,64,75,93,96,103,107,108,109,110,144,155,202,19,23,4,47,48,49,51,52,40,42) ORDER BY meta_id ASC made by require('wp-blog-header.php'), require_once('wp-includes/template-loader.php'), include('/themes/mythemes/single.php'), get_sidebar, locate_template, load_template, require_once('/themes/mythemes/sidebar.php'), wp_tag_cloud, get_terms, update_termmeta_cache, update_meta_cache
[08-Feb-2016 15:19:23 UTC] WordPress database error Table 'wpdb.wp_termmeta' doesn't exist for query SELECT term_id, meta_key, meta_value FROM wp_termmeta WHERE term_id IN (1,28) ORDER BY meta_id ASC made by require('wp-blog-header.php'), require_once('wp-includes/template-loader.php'), include('/themes/mythemes/single.php'), get_header, locate_template, load_template, require_once('/themes/mythemes/header.php'), wp_nav_menu, wp_get_nav_menu_items, get_terms, update_termmeta_cache, update_meta_cache
```


<h3>Solution</h3>
<p>To solve this problem, I created table <code>wp_termmeta</code></p>
<pre>CREATE TABLE IF NOT EXISTS `wp_termmeta` (
  `meta_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `term_id` bigint(20) unsigned NOT NULL DEFAULT '0',
  `meta_key` varchar(255) DEFAULT NULL,
  `meta_value` longtext,
  PRIMARY KEY (`meta_id`),
  KEY `term_id` (`term_id`),
  KEY `meta_key` (`meta_key`(191))
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;</pre>
</p><div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/database/">database</a> <a class="label label-default" href="/tag/error/">error</a> <a class="label label-default" href="/tag/wordpress/">WordPress</a> </div>										
									</div>
