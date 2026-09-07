---
title: "WordPress 3.0.2 is available! Please update now"
date: "2010-12-01T14:43:32+00:00"
categories: ["Article"]
tags: ["WordPress"]
slug: "2010/12/01/wordpress-3-0-2-is-available-please-update-now"
legacyUrl: "/2010/12/01/wordpress-3-0-2-is-available-please-update-now/"
comments: []
---

<div class="content-wrap">
					<div class="add">

</div>
<figure id="attachment_760" style="width: 300px" class="wp-caption alignleft"><a href="/wp-content/uploads/2010/12/wp-update.jpg"><img src="/images/2010/12/wp-update-300x215.jpg" alt="Wordpress 3.0.2" title="wp-update" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><figcaption class="wp-caption-text">Wordpress 3.0.2</figcaption></figure>
<p>On November 30, 2010, WordPress 3.0.2 was released to the public. This is a mandatory security update for all previous WordPress versions.</p>
<p>For version 3.0.2, the database version (db_version in wp_options) remained at 15477.<br/>
<strong><br/>
Installation/Update Information</strong></p>
<p>To download WordPress 3.0.2, update automatically from the Dashboard &gt; Updates menu in your site&#8217;s admin area or visit <a href="https://web.archive.org/web/20160404154845/http://wordpress.org/download/release-archive/" target="_blank">http://wordpress.org/download/release-archive/</a>.</p>
<p><strong>Summary</strong></p>
<ul>
<li>Fix moderate security issue where a malicious Author-level user could gain further access to the site. (r16625)</li>
</ul>

<p><strong>Other bugs and security hardening:</strong></p>
<ul>
<li>Remove pingback/trackback blogroll whitelisting feature as it can easily be abused. (#13887)</li>
<li>Fix canonical redirection for permalinks containing %category% with nested categories and paging. (#13471)</li>
<li>Fix occasional irrelevant error messages on plugin activation. (#15062)</li>
<li>Minor XSS fixes in request_filesystem_credentials() and when deleting a plugin. (r16367, r16373)</li>
<li>Clarify the license in the readme (r15534)</li>
<li> Multisite: Fix the delete_user meta capability (r15562)</li>
<li> Multisite: Force current_user_can_for_blog() to run map_meta_cap() even for super admins (#15122)</li>
<li> Multisite: Fix ms-files.php content type headers when requesting a URL with a query string (#14450)</li>
<li> Multisite: Fix the usage of the SUBDOMAIN_INSTALL constant for upgraded WordPress MU installs (#14536)</li>
</ul>
<p><strong>List of Files Revised<br/>
</strong></p>
<pre>wp-includes/ms-files.php
wp-includes/version.php
wp-includes/comment.php
wp-includes/functions.php
wp-includes/load.php
wp-includes/canonical.php
wp-includes/capabilities.php
readme.html
wp-admin/includes/plugin.php
wp-admin/includes/file.php
wp-admin/includes/update-core.php
wp-admin/plugins.php</pre>
<p>Source: WordPress.org</p>
<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/wordpress/">WordPress</a> </div>										
									</div>
