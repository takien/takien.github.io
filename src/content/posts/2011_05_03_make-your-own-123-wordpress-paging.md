---
title: "Make Your Own 123 WordPress Paging"
date: "2011-05-03T00:00:00Z"
categories: ["Wordpress"]
tags: ["Wordpress"]
slug: "2011/05/03/make-your-own-123-wordpress-paging"
legacyUrl: "/blog/2011/05/03/make-your-own-123-wordpress-paging/"
comments: [{"author": "ian lubis", "date": "", "text": "brader. scriptsnya kepotong tuh.. ketutup sidebar kanan."}, {"author": "Xrvel", "date": "", "text": "2. Call the funciton in theme file\n\n\ntypo bro 😀"}, {"author": "The-Di-Lab", "date": "", "text": "I have a similar function, but it offers an additional function of range, so you can specify how many numbers to appear around the current page.\n\nYou can check it out if you are interested:\n\nhttp://www.the-di-lab.com/?p=517"}, {"author": "Aiammee", "date": "", "text": "thanks ! i’m looking for it \n\nhttp://www.fshop14.com"}]
---

<div style="float:left;margin-right:10px;margin-bottom:10px;">

</div>
						<div id="attachment_826" style="width: 310px" class="wp-caption alignleft"><a href="/wp-content/uploads/2011/05/paging.jpg"><img src="/images/2011/05/paging-300x203.jpg" alt="Wordpress Paging" title="paging" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">WordPress Paging</p></div>
<p>Hello, In this tutorial I will show you how to make your WordPress paging looks eye-catching without using plugins. But hey, there are many plugins out there could do it automatically without any programming skills required. Yes I know, at least, I assume that you want to do it yourself by using PHP. Yes you can do it with easy.</p>
<p>Basically, WordPress has its own built in functions to create paging. So do not have to think about how to write database query or other complex  coding. All we need to do is create a function to generate paging, and call in the theme where you want to paging should appear.</p>
<h2>1. Create a my_wordpress_paging() function in your functions.php under theme directory.</h2>

```php
<?php
//PAGING
function my_wordpress_paging($prev='<< Previous', $next='Next >>', $currentclass='currentpage', $pagingclass='navigation', $echo=true){
	global $wp_query,$paged;
$paging_maxpage = $wp_query->max_num_pages;
$paging_current  = $paged ? $paged : 1;
$paging_prev 	= get_pagenum_link($paging_current-1);
$paging_next 	= get_pagenum_link($paging_current+1);
if($paging_current == $paging_maxpage){
	$paging_next = '';
}
if($paging_current == 1){
	$paging_prev = '';
}
$pre_output = '
```

<h2>2. Call the function in theme file.</h2>
<p>Then in your template (example: index.php, archive.php, category.php etc) paste this code outside the loop:</p>

```php
< ?php my_wordpress_paging();?>
```

<p>If you using <a title="WordPress 3.0 with Twenty Ten Default Theme" href="/599/wordpress-3-0-with-twenty-ten-default-theme.php" target="_blank">TwentyTen</a> theme, open each files named loop-xxx.php and find these lines and replace with code above:</p>

```html
<div id="nav-below" class="navigation">
    <div class="nav-previous"><?php next_posts_link( __( '<span class="meta-nav">&larr;</span> Older posts', 'twentyten' ) ); ?></div>
    <div class="nav-next"><?php previous_posts_link( __( 'Newer posts <span class="meta-nav">&rarr;</span>', 'twentyten' ) ); ?></div>
</div>
```

<h2>3. Styling</h2>
<p>Here is the basic style css for the paging links, please customize to fit your needs.</p>

```css
.navigation{
	text-align:center;
	padding:10px;
	font-size:20px;
}
 .navigation ul li{
	display:inline;
}
.navigation ul li a{
	text-decoration:none;
}
.navigation ul li a:hover{
	text-decoration:underline;
}
```

<h2>4. Parameters</h2>
<p>The <em>my_wordpress_paging() </em>above accepts some parameters.</p>
<ul>
<li><strong>$prev</strong>, previous link text, default value &#8216;&lt;&lt; Previous&#8217;,</li>
<li><strong>$next</strong>, next link text, default value &#8216;Next &gt;&gt;&#8217;,</li>
<li><strong>$currentclass</strong>, class for current page, default &#8221;currentpage&#8217;,</li>
<li><strong>$pagingclass</strong>, class for wrapper div, default value &#8216;navigation&#8217;,</li>
<li><strong>$echo</strong>, whether paging will be echoed or not, if you want to store it in a variable set it to false, default &#8216;true&#8217;</li>
</ul>
<p>That&#8217;s all, any bug report or feedback are welcome. Thank you.</p>
<h2>5. Demo?</h2>
<p>Ah, I forget it, see this blog homepage. I already use it in this blog.</p>
