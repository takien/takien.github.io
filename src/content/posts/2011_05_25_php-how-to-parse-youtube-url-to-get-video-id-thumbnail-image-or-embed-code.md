---
title: "How To Parse Youtube using PHP to Get Video ID, Thumbnail Image, or Embed Code"
date: "2011-05-25T00:00:00Z"
categories: ["Uncategorized"]
tags: ["youtube"]
slug: "2011/05/25/php-how-to-parse-youtube-url-to-get-video-id-thumbnail-image-or-embed-code"
legacyUrl: "/blog/2011/05/25/php-how-to-parse-youtube-url-to-get-video-id-thumbnail-image-or-embed-code/"
comments: [{"author": "Bodoh", "date": "", "text": "Mantap, bisa dipake utk snippet PHP laen"}, {"author": "eMr*", "date": "", "text": "Thanks For this codes…."}, {"author": "Vladimir Gilevich", "date": "", "text": "Thank you for code. That help me a lot."}, {"author": "Irineu", "date": "", "text": "Thanks… really easy to use."}, {"author": "How to register a website", "date": "", "text": "Well, that’s great and i wanted to know the samething. \n\nI loved this post most, as i found it most useful one."}, {"author": "Thiago Machado", "date": "", "text": "You need to close the  to work well"}, {"author": "Amri MF", "date": "", "text": "Siip, makasih gan"}, {"author": "Priyanksharmajpr", "date": "", "text": "nice one"}, {"author": "Mango Africano", "date": "", "text": "Great share, thanks for this code. You help me a lot."}, {"author": "None", "date": "", "text": "amazing, thanks"}, {"author": "Amaal Zohny", "date": "", "text": "greaaaaaaaaaaaaaaaaat , thans"}, {"author": "Nssss", "date": "", "text": "thank you man. Helped a lot."}, {"author": "qwewqqwe", "date": "", "text": "bullshit"}, {"author": "K Williams", "date": "", "text": "May I suggest a\n\n\nreturn false;\n\n\nAt the end if no match was found?"}, {"author": "Nizzzy", "date": "", "text": "40 some lines for something that should take 5 at most.\n\n\npublic static function extractYoutubeID($url){\n\n if($parsed_url = parse_url($url)){\n\n  if(isset($parsed_url[‘query’])){\n\n   parse_str($parsed_url[‘query’],$param);\n\n   return @$param[‘v’];\n\n  }\n\n }\n\n return false;\n\n}"}, {"author": "loadforfun", "date": "", "text": "It isn’t working way if yt url is like: \n\nhttp://www.youtube.com/watch?v=CYxw78Fhaug&feature=g-logo\n\nIt contains more url params here, and your function returns CYxw78Fhaug&feature=g-logo.\n\n\nHere the code to fix:\n\n\nReplace Line 41                $id = reset(explode(‘&’, end(explode(‘v=’,$urls[‘query’]))));"}, {"author": "Aleix", "date": "", "text": "It does not work if it doesn’t have http:// or https://"}, {"author": "TylerB24890", "date": "", "text": "How can I get the thumbnail URL into a variable from the array?"}, {"author": "admien", "date": "", "text": "how to get the title of the video?"}]
---

<div id="attachment_866" style="width: 160px" class="wp-caption alignleft"><a href="/wp-content/uploads/2011/05/youtube-screenshot.jpg"><img src="/images/2011/05/youtube-screenshot-150x150.jpg" alt="Youtube Screenshot" title="youtube-screenshot" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">Youtube Screenshot</p></div>
<p>Hello, sometime we need to parse Youtube URL to get video ID, thumbnail image, or embed code automatically with PHP. To do so, I have created a function <strong>parse_youtube_url();</strong></p>
<p>With this function we can:</p>
<p>&#8211; Get video ID<br/>
&#8211; Get Embed code<br/>
&#8211; Get Thumbnail or HQ Thumbnail URL</p>
<p>Check this out:<br/>
<span id="more-864"></span></p>

```php
/*
* parse_youtube_url() PHP function
* Author: takien
* URL: /
*
* @param string $url URL to be parsed, eg:
* http://youtu.be/zc0s358b3Ys,
* http://www.youtube.com/embed/zc0s358b3Ys
* http://www.youtube.com/watch?v=zc0s358b3Ys
* @param string $return what to return
* - embed, return embed code
* - thumb, return URL to thumbnail image
* - hqthumb, return URL to high quality thumbnail image.
* @param string $width width of embeded video, default 560
* @param string $height height of embeded video, default 349
* @param string $rel whether embeded video to show related video after play or not.

*/

function parse_youtube_url($url,$return='embed',$width='',$height='',$rel=0){
	$urls = parse_url($url);

	//url is http://youtu.be/xxxx
	if($urls['host'] == 'youtu.be'){ 
		$id = ltrim($urls['path'],'/');
	}
	//url is http://www.youtube.com/embed/xxxx
	else if(strpos($urls['path'],'embed') == 1){ 
		$id = end(explode('/',$urls['path']));
	}
	 //url is xxxx only
	else if(strpos($url,'/')===false){
		$id = $url;
	}
	//http://www.youtube.com/watch?feature=player_embedded&v=m-t4pcO99gI
	//url is http://www.youtube.com/watch?v=xxxx
	else{
		parse_str($urls['query']);
		$id = $v;
		if(!empty($feature)){
			$id = end(explode('v=',$urls['query']));
		}
	}
	//return embed iframe
	if($return == 'embed'){
		return '
```

```php
<?php 
echo parse_youtube_url('http://youtu.be/zc0s358b3Ys','hqthumb'); //return http://i1.ytimg.com/vi/zc0s358b3Ys/hqdefault.jpg 
echo parse_youtube_url('http://www.youtube.com/watch?v=zc0s358b3Ys','embed'); //return embed code (iframe) 
?>
```

<p>Note:<br/>
Please report if there any error in the code you copied from here, because it might has changed by WordPress during saved/published.<br/>
Thank you.</p>
<p>Update: June 16, 2012</p>
<h2>Youtube Parser Class</h2>
<p>Helo all, I have created the new version of Youtube parser, now use class. This version allow you to parse or extract Youtube ID, Thumbnails and Embed Code from a page or long content (not only single link)</p>
<p>Here is the code:</p>

```php
<?php
/*
* YoutubeParser() PHP class
* @author: takien
* @version: 1.0
* @date: June 16, 2012
* URL: /864/php-how-to-parse-youtube-url-to-get-video-id-thumbnail-image-or-embed-code.php
*
* @param string $source content source to be parsed, eg: a string or page contains youtube links or videos.
* @param boolean $unique whether the return should be unique (duplicate result will be removed)
* @param boolean $suggested whether show suggested video after finished playing
* @param boolean $https whether use https or http, default false ( http )
* @param string $width width of embeded video, default 420
* @param string $height height of embeded video, default 315
* @param boolean $privacy whether to use 'privacy enhanced mode or not', 
* if true then the returned Youtube domain would be youtube-nocookie.com
*/
class YoutubeParser{
	var $source    = '';
	var $unique    = false;
	var $suggested = false;
	var $https     = false;
	var $privacy   = false;
	var $width     = 420;
	var $height    = 315;

	function __construct(){
	}

	function set($key,$val){
		return $this->$key = $val;
	}
	function getall(){
		$return = Array();
		$domain = 'http'.($this->https?'s':'').'://www.youtube'.($this->privacy?'-nocookie':'').'.com';
		$size   = 'width="'.$this->width.'" height="'.$this->height.'"';

		preg_match_all('/(youtu.be\/|\/watch\?v=|\/embed\/)([a-z0-9\-_]+)/i',$this->source,$matches);
		if(isset($matches[2])){
			if($this->unique){
				$matches[2] = array_values(array_unique($matches[2]));
			}
			foreach($matches[2] as $key=>$id) {
				$return[$key]['id']       = $id;
				$return[$key]['embed']    = '<iframe '.$size.' src="'.$domain.'/embed/'.$id.($this->suggested?'':'?rel=0&wmode;=transparent').'" frameborder="0" allowfullscreen></iframe>';
				$return[$key]['embedold'] = '<object '.$size.'>
				<param name="movie" value="'.$domain.'/v/'.$id.'?version=3'.($this->suggested?'':'&rel=0').'"></param>
				<param name="allowFullScreen" value="true"></param>
				<param name="allowscriptaccess" value="always"></param>
				<embed src="'.$domain.'/v/'.$id.'?version=3'.($this->suggested?'':'&rel=0').'" type="application/x-shockwave-flash" '.$size.' allowscriptaccess="always" allowfullscreen="true"></embed>
				</object>';
				$return[$key]['thumb']    = 'http://i4.ytimg.com/vi/'.$id.'/default.jpg';
				$return[$key]['hqthumb']  = 'http://i4.ytimg.com/vi/'.$id.'/hqdefault.jpg';
			}
		}
		return $return;
	}
}
```

<p><strong>Example usage:</strong></p>
<p>Parse long content:</p>

```php
$content = 'This is the example content contains various Youtube URLS http://www.youtube.com/watch?v=R55e-uHQna0&feature=topvideos http://www.youtube.com/watch?v=iP526fG_M0Y <p><iframe title="YouTube video player" width="480" height="390" src="http://www.youtube.com/embed/26YwnQijaOg" frameborder="0" allowfullscreen></iframe></p> <p>Lorem ipsum dolor sit amet</p>
http://www.youtube.com/embed/26YwnQijaOg Lorem ipsum dolor sit amet http://youtu.be/1u7a5otGnFc Lorem ipsum dolor sit amet http://www.youtube.com/watch?v=CYxw78Fhaug&feature=g-logo';

$youtube = new YoutubeParser;
$youtube->set('source',$content);
$youtube->set('unique',true);

echo'<pre>';
print_r($youtube->getall());
echo'</pre>';
```

<p>Parse single link:</p>

```php
$youtube = new YoutubeParser;
$youtube->set('source','http://www.youtube.com/watch?v=R55e-uHQna0&feature=topvideos');

echo'<pre>';
print_r($youtube->getall());
echo'</pre>';
```

<h2>Update Nov 17, 2012: Get YouTube ID using JavaScript:</h2>
<p>Hello, I write another snippet, Get YouTube ID from various YouTube URL using <strong>JavaScript</strong><br/>
<br/>
Or check out the gist here: https://gist.github.com/4077195</p>
