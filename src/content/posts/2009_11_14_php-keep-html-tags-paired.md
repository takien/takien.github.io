---
title: "PHP: Keep HTML Tags Paired"
date: "2009-11-14T01:50:40+00:00"
categories: ["Tips & Tutorial"]
tags: ["PHP", "html"]
slug: "2009/11/14/php-keep-html-tags-paired"
legacyUrl: "/2009/11/14/php-keep-html-tags-paired/"
comments: []
---

<div class="content-wrap">
					<div class="add">

</div>
<p>After applying <a href="https://web.archive.org/web/20160405100713/http://id2.php.net/manual/en/function.substr.php">substr </a>to a string that contains HTML tags, usually I found that the result is broken because the closing tags are truncated.</p>
<p>To prevent this, I have made a function that keep the closing tags remains and will not break the appearance of my website.</p>
<p><strong>Here is the function:</strong></p>



```php
function pair_tag($string) {
$tags = Array('em','i','b','strong','div','span','p'); 
//array of tags we will keep paired, you may add another
foreach($tags as $tag) {

$opentag 	= substr_count($string, '<'.$tag); 
// I don't put > in the opentag in case they may have an attribute
$closetag 	= substr_count($string, '</'.$tag.'>');

if($opentag !== $closetag) {
$return .= str_repeat('</'.$tag.'>', ($opentag-$closetag));
}
}
return $return;
}
```


<p><strong>Usage/Example:</strong></p>



```php
$fullcontent = '<p>This is my first post blah blah blah...</p>';
$excerpt = substr($string, 0, 20);  //only display first 20 character
$excerpt .= pair_tag($excerpt); // this will count any unclosed tags then close it.
echo $excerpt; // returns <p>This is my first pos</p>
```


<p>Feedback and comment are welcome. Thanks</p>
<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/html/">html</a> <a class="label label-default" href="/tag/php/">PHP</a> </div>										
									</div>
