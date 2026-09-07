---
title: "Menampilkan Recent Post pada Blog Multisite"
date: "2013-05-09T11:50:00Z"
categories: ["WordPress"]
tags: ["facebook", "wordpress"]
slug: "2013/05/09/menampilkan-recent-post-pada-blog-multisite"
legacyUrl: "/2013/05/09/menampilkan-recent-post-pada-blog-multisite/"
source: "facebook.com"
author: "Wak Jek"
comments: [{"author": "Hasyim Asyari", "date": "Thursday 9 May 2013 at 12:10", "text": "terima kasih.. saya coba dulu mastah,,,"}, {"author": "Hasyim Asyari", "date": "Tuesday 21 May 2013 at 10:46", "text": "oiya mastah, kalo ditampilkan di recent post gimana ya mastah,, terima kasih."}, {"author": "Hasyim Asyari", "date": "Tuesday 21 May 2013 at 18:35", "text": "maaf ni master wp, bingung ni.. mksdnya di tampilkan di template home gimana ya, di file apa pada template y master, page.php atau dimana ya? :("}, {"author": "Wak Jek", "date": "Wednesday 22 May 2013 at 07:51", "text": "tergantung template nya,\njadi template home itu bisa macem2, kalau gk front-page.php, home.php\nkalau kedua file tsb nggka ada berarti index.php\n\nlihat selengkapnya tentang template hierarchy http://codex.wordpress.org/.../1/18/Template_Hierarchy.png"}, {"author": "Hasyim Asyari", "date": "Wednesday 22 May 2013 at 09:33", "text": "terima kasih master.."}]
---

<p>Menampilkan Recent Post pada Blog Multisite</p>

<p>1. Bikin fungsi ini di functions.php</p>

<p>/**<br/>
* List recent posts across a Multisite network<br/>
*<br/>
* @uses get_blog_list(), get_blog_permalink()<br/>
*<br/>
* @param int $size The number of results to retrieve<br/>
* @param int $expires Seconds until the transient cache expires<br/>
* @return object Contains the blog_id, post_id, post_date and post_title<br/>
*/<br/>
function wp_recent_across_network( $size = 10, $expires = 7200 ) {<br/>
if( !is_multisite() ) return false;</p>

<p>// Cache the results with the WordPress Transients API<br/>
// Get any existing copy of our transient data<br/>
if ( ( $recent_across_network = get_site_transient( 'recent_across_network' ) ) === false ) {</p>

<p>// No transient found, regenerate the data and save a new transient<br/>
// Prepare the SQL query with $wpdb<br/>
global $wpdb;</p>

<p>$base_prefix = $wpdb->get_blog_prefix(0);<br/>
$base_prefix = str_replace( '1_', '' , $base_prefix );</p>

<p>// Because the get_blog_list() function is currently flagged as deprecated<br/>
// due to the potential for high consumption of resources, we'll use<br/>
// $wpdb to roll out our own SQL query instead. Because the query can be<br/>
// memory-intensive, we'll store the results using the Transients API<br/>
if ( false === ( $site_list = get_site_transient( 'multisite_site_list' ) ) ) {<br/>
global $wpdb;<br/>
$site_list = $wpdb->get_results( $wpdb->prepare('SELECT * FROM wp_blogs ORDER BY blog_id') );<br/>
set_site_transient( 'multisite_site_list', $site_list, $expires );<br/>
}</p>

<p>$limit = absint($size);</p>

<p>// Merge the wp_posts results from all Multisite websites into a single result with MySQL "UNION"<br/>
foreach ( $site_list as $site ) {<br/>
if( $site == $site_list[0] ) {<br/>
$posts_table = $base_prefix . "posts";<br/>
} else {<br/>
$posts_table = $base_prefix . $site->blog_id . "_posts";<br/>
}</p>

<p>$posts_table = esc_sql( $posts_table );<br/>
$blogs_table = esc_sql( $base_prefix . 'blogs' );</p>

<p>$query .= "(SELECT $posts_table.ID, $posts_table.post_title, $posts_table.post_date, $blogs_table.blog_id FROM $posts_table, $blogs_table\n";<br/>
$query .= "\tWHERE $posts_table.post_type = 'post'\n";<br/>
$query .= "\tAND $posts_table.post_status = 'publish'\n";<br/>
$query .= "\tAND $blogs_table.blog_id = {$site->blog_id})\n";</p>

<p>if( $site !== end($site_list) )<br/>
$query .= "UNION\n";<br/>
else<br/>
$query .= "ORDER BY post_date DESC LIMIT 0, $limit";<br/>
}</p>

<p>// Sanitize and run the query<br/>
$query = $wpdb->prepare($query);<br/>
$recent_across_network = $wpdb->get_results( $query );</p>

<p>// Set the Transients cache to expire every two hours<br/>
set_site_transient( 'recent_across_network', $recent_across_network, 60*60*2 );<br/>
}</p>

<p>return $recent_across_network;<br/>
}</p>

<p>2. Tampiklan di template home</p>

<p><?php</p>

<p>$recent_blog_posts = wp_recent_across_network(5);<br/>
foreach($recent_blog_posts as $recent) { ?><br/>
<?php<br/>
echo '<li><a href="'.get_blog_permalink($recent->blog_id, $recent->ID).'">'.$recent->post_title.'</a></li>';<br/>
?><br/>
<?php<br/>
}<br/>
?></p>

<p>Kode ini berasal dari smashingmagazine, saya modifikasi sedikit.</p>
