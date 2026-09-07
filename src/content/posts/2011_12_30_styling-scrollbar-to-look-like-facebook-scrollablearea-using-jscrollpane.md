---
title: "Styling Scrollbar to Look Like Facebook ScrollableArea Using jScrollPane"
date: "2011-12-30T12:15:00.000Z"
categories: ["Tips & Tutorial"]
tags: ["Web Design"]
slug: "2011/12/30/styling-scrollbar-to-look-like-facebook-scrollablearea-using-jscrollpane"
legacyUrl: "/2011/12/30/styling-scrollbar-to-look-like-facebook-scrollablearea-using-jscrollpane/"
source: "takien.com"
author: "takien"
comments: [{"author":"Rodolfo Jorge Nemer Nogueira","date":"","text":"Very good post. I recently used this technique to compose the scroll effect.\n\nRodolfo Nogueira Curitiba Paraná UFPR Música"},{"author":"Anonymous","date":"","text":"yeah, every stuff in famous sites like facebook, google, or twtitter is great to be imitated and applied  since they have mature programmer and or web designer, xD"},{"author":"Guest","date":"","text":"i think it does not work in ie."},{"author":"Anonymous","date":"","text":"That doesn’t matter"},{"author":"Guest","date":"","text":"and you call yourself a web developer?"},{"author":"Anonymous","date":"","text":"yes, Not IE developer. problem?"},{"author":"Pedox","date":"","text":"and im called who ??"},{"author":"Anonymous","date":"","text":"troll"},{"author":"keaglez","date":"","text":"There is no reason it doesn’t work on IE 7 and up. It does work by the way, you lost border-radius but that’s pretty much it.\n\n@takien:disqus The mouseover event seems to be not reliable, if you hover in and out fast, the scrollbar will repeat fade in/out. CSS3 might help in this case. Or do some checking if animation is playing before calling fadein/out."},{"author":"Fauzie","date":"","text":"for the animation problem, you could use the stop() event.\n\nhttp://api.jquery.com/stop/"},{"author":"Anonymous","date":"","text":"for those who use IE, I confirmed it does work in IE 6 and above.\n\n@2413c800e6b3406b83ae7f720b62fd8d:disqus fixed missed vendor prefix’s border radius in CSS.\n\nmultiple queued animations problem in fadein/out it also has been fixed, thanks to @fauzie811:disqus . use stop(true, true) since .stop() doesn’t work.\n\nThe article updated, as well as the demo page.\nthanks."},{"author":"Pedox","date":"","text":"it’s great takien… don’t forget for give me Good reputation !!\nim still waiting"}]
---

<div class="content-wrap">
					<img src="/images/2011/12/facebook-scrollable-area.png" alt="Facebook Scrollable Area" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><div class="add">

</div>
<h2>What Is Scrollbar?</h2>
<p>According to Wikipedia, A <strong>scrollbar</strong> is an object in a graphical user interface (GUI) with which continuous text, pictures or anything else can be scrolled including time in video applications, i.e., viewed even if it does not fit into the space in a computer display, window, or viewport. It was also known as a <strong>handle</strong> in the very first GUIs.</p>
<h2>What Is jScrollPane?</h2>
<p>jScrollPane is a cross-browser <a href="https://web.archive.org/web/20160220110315/http://jquery.com/" target="_blank">jQuery</a> plugin by <a href="https://web.archive.org/web/20160220110315/http://www.kelvinluck.com/" target="_blank">Kelvin Luck</a> which converts a browser&#8217;s default scrollbars (on elements with a relevant overflow property) into an HTML structure which can be easily skinned with CSS.</p>
<p>jScrollPane is designed to be flexible but very easy to use. After you have downloaded and included the relevant files in the head of your document all you need to to is call one javascript function to initialise the scrollpane. You can style the resultant scrollbars easily with CSS or choose from the existing themes. There are a number of different examples showcasing different features of jScrollPane and a number of ways for you to get support.</p>
<h2>What Is Facebook ScrollableArea?</h2>
<figure id="attachment_983" style="width: 300px" class="wp-caption aligncenter"><a href="https://web.archive.org/web/20160220110315/http://img.takien.com/2011/12/facebook-scrollable-area.png"><img src="/images/2011/12/facebook-scrollable-area-300x261.png" alt="Facebook Scrollable Area" title="facebook-scrollable-area" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><figcaption class="wp-caption-text">Facebook Scrollable Area</figcaption></figure>
<p>Recently, Facebook ScrollableArea can be found in many part of Facebook user interface to handle overflow content. One is in the activity feed in the top right area with a cute scrollbar that can be scrolled by dragging and mouse scroll.</p>
<p>Yes, it can be done nicely &#8212; with little CSS and JavaScript customization &#8212; using jScrollPane I mentioned above</p>
<h2>jScrollPane + (JavaScript + CSS) = Facebook ScrollableArea</h2>
<p>Don&#8217;t worry, there is no pain coding needed to do this, just follow this steps:</p>
<p><strong>1. Include jScrollPane library and jQuery (if not yet) to your page</strong></p>



```html
<!-- styles needed by jScrollPane -->
<link type="text/css" href="style/jquery.jscrollpane.css" rel="stylesheet" media="all" />

<!-- latest jQuery direct from google's CDN -->
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js">
</script>

<!-- the mousewheel plugin - optional to provide mousewheel support -->
<script type="text/javascript" src="script/jquery.mousewheel.js"></script>

<!-- the jScrollPane script -->
<script type="text/javascript" src="script/jquery.jscrollpane.min.js"></script>
```


<p><strong>2.Initialize jScrollPane to your selector.</strong></p>
<p>By default, the following code is ready to convert your scrollbar to  jScrollPane.</p>



```javascript
$(function() {
	$('.content-area').jScrollPane();
});
```


<p>But here, we need more settings. It&#8217;s should look like this:</p>



```javascript
$('.content-area').jScrollPane({
	horizontalGutter:5,
	verticalGutter:5,
	'showArrows': false
});
```


<p><strong>3. Scrollbar should be hidden if no mouse over on it.</strong></p>
<p>So, we use .fadeIn() and .fadeOut() jQuery effects:</p>



```javascript
$('.jspDrag').hide();
$('.jspScrollable').mouseenter(function(){
    $(this).find('.jspDrag').stop(true, true).fadeIn('slow');
});
$('.jspScrollable').mouseleave(function(){
    $(this).find('.jspDrag').stop(true, true).fadeOut('slow');
});
```


<p><strong>4. Last but not least, add custom CSS</strong><br/>
&#8211;</p>



```css
/*scrollpane custom CSS*/
.jspVerticalBar {
	width: 8px;
	background: transparent;
	right:10px;
}

.jspHorizontalBar {
	bottom: 5px;
	width: 100%;
	height: 8px;
	background: transparent;
}
.jspTrack {
	background: transparent;
}

.jspDrag {
	background: url(images/transparent-black.png) repeat;
	-webkit-border-radius:4px;
	-moz-border-radius:4px;
	border-radius:4px;
}

.jspHorizontalBar .jspTrack,
.jspHorizontalBar .jspDrag {
	float: left;
	height: 100%;
}

.jspCorner {
	display:none
}
```


<p>We use a 1&#215;1 pixel PNG transparent image for jspDrag background, <a href="https://web.archive.org/web/20160220110315/http://img.takien.com/2011/12/transparent-black.png">Download it here</a> (right click, save link/target)</p>
<h2> Live Demo</h2>
<p><a href="https://web.archive.org/web/20160220110315/http://demo.takien.com/index.php?page=scrollable_area" target="_blank">Click Here to See Live Demo</a></p>
<p><em><br/>
</em></p>
<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/web-design/">Web Design</a> </div>										
									</div>
