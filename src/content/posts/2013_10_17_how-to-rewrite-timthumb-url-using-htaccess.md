---
title: "How To Rewrite TimThumb URL Using .htaccess"
date: "2013-10-17T00:00:00Z"
categories: ["Uncategorized"]
tags: []
slug: "2013/10/17/how-to-rewrite-timthumb-url-using-htaccess"
legacyUrl: "/blog/2013/10/17/how-to-rewrite-timthumb-url-using-htaccess/"
comments: [{"author": "Jay", "date": "", "text": "Not working for me. My website is http://forexminute.es/ but i still see the string queried image by timthumb…"}]
---

<div id="attachment_1356" style="width: 229px" class="wp-caption aligncenter"><img src="/images/2013/10/thumb-nail-219x300.jpg" alt="Thumbnail" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><p class="wp-caption-text">Thumbnail (pixabay.com)</p></div>
<p><strong>TimThumb </strong>is PHP script to generate and resize image via URL query. To resize image on the fly, you can access <code>timthumb.php</code> and pass some query in the URL.</p>
<p>For example to resize <code>http://example.com/wp-content/uploads/2013/10/your-image-name.jpg</code> to 150px width and 100px height, you can access <code>http://example.com/timthumb.php?src=http://example.com/wp-content/uploads/2013/10/your-image-name.jpg&amp;w=150&amp;h=100.</code> It&#8217;s quite easy isn&#8217;t it?</p>
<p>It&#8217;s easy and some people no problem with it. But if you want more fancy URL to your image path, you can done it using <code>.htaccess</code> rewrite. Note that this trick only works if your website run on Apache webserver and <code>mod_rewrite</code> is loaded.</p>
<p><strong>Before:</strong></p>
<pre>http://yoursite.com/timthumb.php?src=http://example.com/wp-content/uploads/2013/10/your-image-name.jpg&amp;w=150&amp;h=100</pre>
<p><strong>After:</strong></p>
<pre>http://example.com/uploads/2013/10/your-image-name_150_100.jpg</pre>
<p>The image link looks nice and shorter.</p>
<p><strong>How to do that?</strong></p>
<p>1. Place timthumb.php on your web root (usually under public_html)<br/>
2. Edit .htaccess and put this code</p>

```bash
RewriteRule ^(.*)_([0-9]+)_([0-9]+)\.(jpg|jpeg|png|gif)$ timthumb.php?src=http://example.com/wp-content/uploads/$1.$4&w=$2&h=$3 [NC,L]
```

<p>Replace example.com with your domain.</p>
