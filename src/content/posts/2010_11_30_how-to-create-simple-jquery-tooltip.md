---
title: "How to Create Simple jQuery Tooltip"
date: "2010-11-30T00:00:00Z"
categories: ["Web Design"]
tags: ["jQuery"]
slug: "2010/11/30/how-to-create-simple-jquery-tooltip"
legacyUrl: "/blog/2010/11/30/how-to-create-simple-jquery-tooltip/"
comments: [{"author": "Anonymous", "date": "", "text": "buset ini post jadul gak ada yang komen"}]
---

<p><div id="attachment_754" style="width: 267px" class="wp-caption alignleft"><a href="/wp-content/uploads/2010/11/tooltip.gif"><img src="/images/2010/11/tooltip.gif" alt="" title="tooltip" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">Tooltip on desktop application</p></div>There are so many jQuery Tooltip we can find on Google.  However, sometimes we just need something simple. So, why don&#8217;t you create your own?</p>
<p><strong>Basic</strong></p>
<ul>
<li>This tooltip would replace title attribute of an HTML element.</li>
<li>This tooltip text is extracted from the title attribute.</li>
<li>This tooltip is compatible with common modern browser.</li>
<li>This is not a jQuery plugin.</li>
</ul>
<p><strong>Logic</strong></p>
<p><div style="float:right;width:300px;height:250px;margin-left:20px">

</div></p>
<p>When cursor over on an element with title attribute, normally it will display a tooltip. Extract that title attribute, save it to a variable and remove original title attribute (to prevent original title being displayed).<br/>
Create a div element next to current element with position absolute, hidden, and fill it up with extracted title text. Finally, display that div when mouse over on it.</p>
<p>Then what happen when mouse cursor leaves the element? Simply, restore title attribute, and hide or remove tooltip.</p>
<p><strong>Do it your self</strong></p>
<p>Below is the code with explanation comment.</p>
<p><strong>Mouse Enter</strong></p>


```javascript
$('.poptip').mouseenter(function(){
var text = $(this).attr('title'); //extract title, save to "text" variable
var posi = $(this).position();
var top  = posi.top; //top position
var left = posi.left+5; //left position
var wid	 = $(this).width(); //element width
$(this).attr('title',''); //remove original title
$(this).parent().append(''+text.replace('|','')+''); //create div element with class .poptext, and fill with extracted title.

//some css styling
	$('.poptext').css({'left':(left+wid)+'px',
				'top':(top-$('.poptext').height())+'px',
				'background':'#fffeee',
				'border':'1px solid #f7a229',
				'display':'none',
				'position':'absolute',
				'z-index':'1000',
				'padding':'5px',
				'font-size':'0.8em'
	});

//show tooltip, slowly 
	$('.poptext').fadeIn('slow');
});
```


<p><strong>Mouse Leave</strong></p>


```javascript
$('.poptip').mouseleave(function(){
	var title = $(this).parent().find('.poptext').html(); //restore title text from tooltip
	$(this).attr('title',title.replace('','|')); //place it back to title attribute
	$(this).parent().find('.poptext').fadeOut('slow'); //hide tooltip
	$(this).parent().find('.poptext').remove(); //remove element.
});
```


<p><strong>Usage/Example</strong></p>


```html

```


<p>You&#8217;re done.</p>
<div class="panel panel-info"><div class="panel-heading"><h3 class="panel-title">Demo</h3></div><div class="panel-content" style="padding:5px 10px"><br/>
See a live demo here  <a target="_blank" href="https://web.archive.org/web/20140719042607/http://cektkp.com/test/jquerytooltip">http://cektkp.com/test/jquerytooltip</a><br/>
</div></div>
<div class="panel panel-info"><div class="panel-heading"><h3 class="panel-title">Download</h3></div><div class="panel-content" style="padding:5px 10px"><br/>
Download full code here <a target="_blank" href="https://web.archive.org/web/20140719042607/http://ngoding.com/74cac">http://ngoding.com/74cac</a><br/>
</div></div>
