---
title: "WordPress Media Browser CSS Fix"
date: "2013-11-18T00:00:00Z"
categories: ["Wordpress"]
tags: []
slug: "2013/11/18/wordpress-media-browser-css-fix"
legacyUrl: "/blog/2013/11/18/wordpress-media-browser-css-fix/"
comments: [{"author": "Nicholas Sihotang", "date": "", "text": "Solusi yang menawan, bang.\n\nIjin pakai yaah"}]
---

<div style="float:left;margin-right:10px;margin-bottom:10px;">

</div>
						<p>Hi there, since 3.5 WordPress use new version of WordPress media library (uploader and browser). It&#8217;s faster and more convenient than older version which was using iframe.  But I found some issue with layout, I think it should be better in user experience. The current media browser is focus on multiple images on the left,  it has more space, whereas the media sidebar only have 267px in width. This is ineficient especially when you want to add long text on the picture caption or description. At least it&#8217;s my experience.</p>
<p>So, I made some CSS fix on it. See figures below:</p>
<p><strong>Before:</strong></p>
<div id="attachment_1368" style="width: 1010px" class="wp-caption alignnone"><img src="/images/2013/11/wordpress-media-browser-library-before.jpg" alt="WordPress media library" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><p class="wp-caption-text">WordPress media library</p></div>
<p><strong>After:</strong></p>
<div id="attachment_1367" style="width: 1010px" class="wp-caption alignnone"><img src="/images/2013/11/wordpress-media-browser-after.jpg" alt="WordPress media library after fix" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><p class="wp-caption-text">WordPress media library after fix</p></div>

<p><strong>Changes:</strong></p>
<ul>
<li>Media sidebar is now 450px, previously 267px</li>
<li>Textarea, input, on sidebar is now 100% width</li>
<li>Label is now block</li>
<li>Removed float on search textbox, it&#8217;s now on the left, next to media filter dropdown</li>
<li>Insert into post button remains on the right</li>
</ul>
<p><strong>Code:</strong></p>
<p>Here is the code, put it somewhere in your <code>functions.php</code> file of your current theme.</p>



```php
add_action('admin_head','takien_media_browser_fix');
function takien_media_browser_fix () {
global $pagenow;
//if( 'post.php' !== $pagenow ) return;
if( !in_array( $pagenow, Array( 'post.php','post-new.php')) ) return;

	?>
	<style type="text/css">
	.media-sidebar {
		width:450px !important;
	}

	.attachments-browser .attachments, 
	.attachments-browser .uploader-inline {
		right: 500px !important
	}

	.media-sidebar .setting input, .media-sidebar .setting textarea {
		float:none !important;
		width:95% !important
	}
	.media-sidebar .setting span, .compat-item label span,
	.media-toolbar-primary {
		float:none !important
	}
	.media-toolbar-primary {
		float:none !important
	}

	.media-toolbar-primary .button-primary {
		float:right !important
	}
	</style>
<?php
}
```



<div id="jp-relatedposts" class="jp-relatedposts">
	<h3 class="jp-relatedposts-headline"><em>Related</em></h3>
</div>
