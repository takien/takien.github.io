---
title: "jQuery PHP: Facebook Friend Selector Without FBML"
date: "2010-08-16T00:00:00Z"
categories: ["PHP"]
tags: ["facebook", "html", "jQuery", "javascript", "json"]
slug: "2010/08/16/jquery-php-facebook-friend-selector-without-fbml"
legacyUrl: "/blog/2010/08/16/jquery-php-facebook-friend-selector-without-fbml/"
comments: [{"author": "budakoyot", "date": "", "text": "pertamax diamankan 😀\n\n\nane dongdot yah om :malus\n\nakhirnya ada tutorialnya juga, jadi semangat nih\n\ntinggal diakalin dikit2, mudah2an bisa :hammer:"}, {"author": "bhcrew", "date": "", "text": "wah template webnya keren 😀\n\nntar deh ane pake scriptnya, kalo lagi iseng lagi nerusin yang kemaren"}, {"author": "dieka", "date": "", "text": "ane juga pngen ah…. 😀"}, {"author": "budakoyot", "date": "", "text": "ane lagi2 bermasalah dengan konak facebook :mewek"}, {"author": "BandenX", "date": "", "text": "Gan, ada yg pake framework prototype nggak. Tuh kan nggak jauh beda sama ajax autocompleter/suggest. Gw biasanya pake duet prototype+scriptaculous (ajax autocompleter). Tapi nggak ada highlight dari keyword yg diinputkan di list suggestnya."}, {"author": "Kristjan", "date": "", "text": "How to put this on tab? If i put this to tab it gives me errors and will not work."}, {"author": "kuratha", "date": "", "text": "can’t display  [target_id]  with big length\n\neg: 100000211240977"}, {"author": "Bruno", "date": "", "text": "Hi, problem with [target_id] too.. it returns -1 when the selected friend had relationship status"}, {"author": "Mike", "date": "", "text": "all i get is the circle spinning but no drop down containing a name? please help!"}, {"author": "philip", "date": "", "text": "thanks a lot for this,\n\ni just noticedthat if you use this code in  a tab application it’s not working.\n\n\nanyone can help fix it?\n\nthanks a lot!!!"}, {"author": "Joey", "date": "", "text": "Can’t display  big [target_id]. How fix this bug? Please!"}]
---

<div style="float:left;margin-right:10px;margin-bottom:10px;">

</div>
						<div id="attachment_719" style="width: 160px" class="wp-caption alignleft"><a href="/wp-content/uploads/2010/08/friend-selector.png"><img src="/images/2010/08/friend-selector-300x223.png" alt="Facebook Friend Selector, PHP + jQuery without FBML/iframe" title="friend-selector" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">Facebook Friend Selector</p></div>
<p>Facebook friends selector is one of important thing when you develop a Facebook application. It will simplify the way your visitor select their Facebook friend&#8217;s instead of manually find friend&#8217;s user ID.</p>
<p>Just type part of the friend&#8217;s name, the matches name will appears below the field and select one you want.</p>
<p>This is not just another Facebook friend selector you might found somewhere, because it&#8217;s not using FBML or iframe, there&#8217;s only JavaScript and PHP.<br/>
<div style="float:right;width:300px;height:250px;margin-left:20px">

</div><br/>
<strong>How it works?</strong></p>
<ol>
<li>Once you logged in, the script will ask your permission to access your account (friends list etc).</li>
<li>If you choose allow, then the script fetchs your friend data from https://graph.facebook.com/me/friends and get your friend lists in JSON format.</li>
<li>Some PHP function convert it into PHP array and simplify it, do some filtering based on user input, then encode back to JSON format so it will compatible with the jQuery autocomplete plugin.</li>
</ol>
<p><strong>Can&#8217;t wait to see it in action? </strong><br/>
Just follow the links below:</p>
<p><div class="panel panel-info"><div class="panel-heading"><h3 class="panel-title">Demo</h3></div><div class="panel-content" style="padding:5px 10px"><a href="https://web.archive.org/web/20150510010014/http://cektkp.com/test/friend/" target="_blank">Demo and Download</a><br/>
</div></div><br/>
Credit: <a target="_blank" href="https://web.archive.org/web/20150510010014/http://www.codeassembly.com/Unobtrusive-jQuery-autocomplete-plugin-with-json-key-value-support/">jQuery Autocomplete Plugins</a></p>

<div id="jp-relatedposts" class="jp-relatedposts">
	<h3 class="jp-relatedposts-headline"><em>Related</em></h3>
</div>
