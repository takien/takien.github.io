---
title: "Wampserver 2.5 Error: The configuration file contains a syntax error on line 326"
date: "2014-08-21T22:22:36+00:00"
categories: ["Tips & Tutorial"]
tags: ["Website"]
slug: "2014/08/21/wampserver-2-5-error-the-configuration-file-contains-a-syntax-error-on-line-326"
legacyUrl: "/2014/08/21/wampserver-2-5-error-the-configuration-file-contains-a-syntax-error-on-line-326/"
comments: []
---

<div class="content-wrap">
					<div class="add">

</div>
<p>Wampserver is my favourite package for web development in Windows. It contains PHP, MySQL and Apache. Wampserver 2.5 is the newest version, comes with Apache 2.4.9, MySQL 5.6.17 and PHP 5.5.12 PHPMyAdmin 4.1.14 SqlBuddy 1.3.3 and XDebug 2.2.5.</p>
<p>Bad thing happened when I trying to upgrade my Wampserver from version 2.2 to 2.5 on Windows 7 32 bit. The installation was successfull but it can&#8217;t start and showing the following error.</p>
<figure id="attachment_1406" style="width: 449px" class="wp-caption aligncenter"><img src="/images/2014/08/wampserver-2.5-the-configuration-file-contains-a-syntax-error-on-line-326.jpg" alt="wampserver 2.5 the configuration file contains a syntax error on line 326" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><figcaption class="wp-caption-text">wampserver 2.5 the configuration file contains a syntax error on line 326</figcaption></figure>
<pre>
Aestan Tray Menu
The configuration file contains a syntax error on line 326:
[EParseError] Parameter "Service" specifies an unknown service
</pre>
<p><strike>Not sure what happened. I will update this post once I found the solution. </strike></p>
<p>It has been 2 hours since I had this problem. 😀<br/>
Found a solution? Not actually.</p>
<p>First time I tought that was problem in the <code>wampmanager.ini</code> that is not compatible with new version of Wampserver. </p>
<p>Asked Google and found this <a href="https://web.archive.org/web/20160322130539/http://forum.wampserver.com/read.php?2,123685" target="_blank">WAMPServer 2.5 release notes and corrections </a>. Doh, <strike>they blame me</strike>. That was my mistake, as everyone do, I hate reading the f_cking manual :'(</p>
<p>As you can see on the link above, hundred lines of text contains tutorial and warning how to upgrade to Wampserver 2.5. Not read all of them, of course. For the brief: <strong>DO NOT INSTALL NEW WAMPSERVER OVER THE OLD ONE.</strong> 😀</p>
<p>I had my own decision, UNINSTALL the broken-Wampserver, and hope magic happen.</p>
<p>And.. voila. Wampserver 2.5 successfully installed with green icon on the systray smiling to me. <img src="/images/misc/simple-smile.png" alt=":)" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /> Click on the icon and see what&#8217;s version of PHP and Apache installed, PHP 5.5.12 and Apache 2.4.9. Looks good. Open my project on the browser. Tada&#8230;. too many deprecated notice showing up.  <img src="/images/misc/frownie.png" alt=":(" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>
<p>Hmmm. I thought I need lower PHP version, so I downloaded PHP 5.3 from here <a href="https://web.archive.org/web/20160322130539/http://sourceforge.net/projects/wampserver/files/WampServer%202%20-%20Extensions/PHP/" target="_blank">http://sourceforge.net/projects/wampserver/files/WampServer%202%20-%20Extensions/PHP/</a>. Solving the problem? No. The PHP version does not compatible with current Apache version. Download lower Apache version from here <a href="https://web.archive.org/web/20160322130539/http://sourceforge.net/projects/wampserver/files/WampServer%202%20-%20Extensions/Apache/" target="_blank">http://sourceforge.net/projects/wampserver/files/WampServer%202%20-%20Extensions/Apache/</a>. Still not solving the problem. Service wont start.</p>
<p>At the end of my frustation, found <a href="https://web.archive.org/web/20160322130539/http://sourceforge.net/projects/wampserver/files/WampServer%202%20-%20Extensions/Apache/readme.txt/download" target="_blank">readme.txt </a>. It says:</p>
<pre>
Don't Use previous WampServer Extensions/Addons. 
There are no more compatible with the new wampserver version's (VC11)</pre>
<p>Doh!</p>
<p><strong>Solved?</strong><br/>
NO.</p>
<p><strong>So, what next?</strong><br/>
Uninstall Wampserver 2.5 and re-instal Wampserver 2.2 😀</p>
<p><strong>CONCLUSION:</strong><br/>
Do not ever upgrade to Wampserver 2.5 unless you want to use PHP 5.5.12 and Apache 2.4.9. period.</p>
<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/website/">Website</a> </div>										
									</div>
