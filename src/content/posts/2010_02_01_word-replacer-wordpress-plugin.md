---
title: "Word Replacer WordPress Plugin"
date: "2010-02-01T00:00:00Z"
categories: ["Plugins"]
tags: ["Plugins", "Wordpress", "comment replace", "content replace", "str_replace", "text replace", "word replace", "wordpress plugins"]
slug: "2010/02/01/word-replacer-wordpress-plugin"
legacyUrl: "/2010/02/01/word-replacer-wordpress-plugin/"
comments: [{"author": "Jan Ik", "date": "2012-03-15", "text": "BUG REPORT (v0.2.3)\n\n\n1) Line $action_url = $_SERVER[PHP_SELF] . ‘?page=’ . $word_replacer[‘base_name’];  should be$action_url = site_url().$_SERVER[PHP_SELF] . ‘?page=’ . $word_replacer[‘base_name’];so that the plugin works with subdomain blogs.\n\n2) The regex is pretty useless because it doesn’t match newlines. Now, I understand that the plugin started as a _WORD_ replacer, but nevertheless you should add /s (either hardcoded or as an option like “case insensitive”)\n\n\n3) backslashes are prepended everytime one clicks “update”. \n\n\nHence “foo” becomes “foo” becomes \\”foo\\” becomes \\\\\\”foo\\\\\\”\n\n\n\t\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t \n\t\t\t\t\t\tReply ↓"}]
---

<div style="float:left;margin-right:10px;margin-bottom:10px;">

</div>
						<p><div class="panel panel-info"><div class="panel-heading"><h3 class="panel-title">Update</h3></div><div class="panel-content" style="padding:5px 10px"><br/>
Version 0.2.3 is available at WordPress.org<br/>
Please install/upgrade from your wp-admin or <a href="https://web.archive.org/web/20150101194337/http://wordpress.org/extend/plugins/word-replacer/" target="_blank">download from WordPress.org</a><br/>
Thank you.</p>
<p><em>Oct 23, 2011</em><br/>
</div></div><br/>
Word Replacer is a WordPress plugins to replace any desired text/word with your choice. You can filter which content to be replaced, eg. only in page, comment, or post. With very userfriendly administration page you can manage list of word eaasily. It&#8217;s also can be used to censor any bad/vulgar words in your comment your your guest posting. It&#8217;s simple but useful.<br/>
<div style="float:right;width:300px;height:250px;margin-left:20px">

</div><br/>
<strong>Features<br/>
</strong></p>
<ol>
<li>With regex support.</li>
<li>Userfriendly administration page.</li>
<li>Define yourself what word to replace in where. (e.g. a word shoud be replaced in comment but not in post etc)</li>
</ol>
<p><strong>Changelog:</strong></p>
<div>
<h4>version 0.2.1</h4>
<ul>
<li>Changed: original and replacement field in database is now TEXT type instead of VARCHAR</li>
<li>Fixed: plugins will analyze first whether original value in databse  is base64 encoded (bug in version 0.2, when upgrade from version 0.1)</li>
</ul>
<h4>version 0.2</h4>
<ul>
<li>Regex support</li>
<li>Some bug fixes</li>
<li>Changed: Now using preg_replace PHP functions, instead of str_replace</li>
<li>Added: Replace title and page title</li>
<li>Added: Search whole word only</li>
<li>Added: Search case insensitive</li>
<li>Added: Contextual help</li>
<li>Changed: Original words saved to the database is now base64 encoded, to keep character consistency.</li>
<li>Added: Expand/collapse options page</li>
<li>Removed: initial word value (badword/good word)</li>
</ul>
<h4>version 0.1</h4>
<ul>
<li>First release</li>
</ul>
</div>
<p><strong>Screenshot:</strong></p>
<p>Options page:<br/>
<figure class="image-missing-placeholder" role="img" aria-label="screenshot-1-300x113.png">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">screenshot-1-300x113.png</span>
  </div>
</figure></p>
<p>Help:<br/>
<figure class="image-missing-placeholder" role="img" aria-label="screenshot-2-300x175.png">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">screenshot-2-300x175.png</span>
  </div>
</figure></p>
<p>Options page (expanded):<br/>
<figure class="image-missing-placeholder" role="img" aria-label="screenshot-3-300x108.png">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">screenshot-3-300x108.png</span>
  </div>
</figure></p>
<div class="panel panel-info"><div class="panel-content" style="padding:5px 10px"></p>
<p><a href="https://web.archive.org/web/20150101194337/http://wordpress.org/extend/plugins/word-replacer/" target="_blank">Download from WordPress.org</a></p>
<p></div></div>
