---
title: "WordPress Spry Menu Plugins"
date: "2009-07-01T00:00:00Z"
categories: ["Uncategorized"]
tags: []
slug: "2009/07/01/wordpress-spry-menu-plugins"
legacyUrl: "/2009/07/01/wordpress-spry-menu-plugins/"
comments: [{"author": "Anonymous", "date": "2010-05-09", "text": "Morpie says:"}, {"author": "Anonymous", "date": "2010-06-09", "text": "takien says:"}, {"author": "Anonymous", "date": "2010-06-07", "text": "Ling says:"}, {"author": "Anonymous", "date": "2010-06-09", "text": "takien says:"}, {"author": "Anonymous", "date": "2010-06-18", "text": "Shari says:"}, {"author": "Anonymous", "date": "2010-06-26", "text": "takien says:"}, {"author": "Anonymous", "date": "2010-09-05", "text": "Shezz says:"}, {"author": "Anonymous", "date": "2010-09-10", "text": "phillip gosper says:"}, {"author": "Anonymous", "date": "2010-11-15", "text": "bnther says:"}, {"author": "Anonymous", "date": "2010-11-15", "text": "bnther says:"}, {"author": "Anonymous", "date": "2010-11-21", "text": "Flourian says:"}, {"author": "Anonymous", "date": "2010-12-17", "text": "Matt says:"}, {"author": "Anonymous", "date": "2011-01-09", "text": "Brad Strong says:"}, {"author": "Anonymous", "date": "2011-01-09", "text": "Brad Strong says:"}, {"author": "Anonymous", "date": "2011-01-09", "text": "Brad Strong says:"}, {"author": "Anonymous", "date": "2011-01-18", "text": "julien says:"}, {"author": "Anonymous", "date": "2011-06-08", "text": "Lyuben says:"}, {"author": "Anonymous", "date": "2011-06-08", "text": "Lyuben says:"}, {"author": "Anonymous", "date": "2011-06-20", "text": "Henrik says:"}, {"author": "Anonymous", "date": "2011-08-02", "text": "Dave says:"}, {"author": "Anonymous", "date": "2013-01-04", "text": "Riversatile says:"}, {"author": "Anonymous", "date": "2013-02-14", "text": "takien says:"}, {"author": "Anonymous", "date": "2013-04-12", "text": "Bootjesgek says:"}]
---

<div class="content-wrap">
					<div class="add">

</div>
<p>Hi, this is my first plugin I write. WP Spry Menu that automatically creating Spry Drop Down Menu for wordpress category include configuration page with configurable &#8220;Home&#8221; link. This plugin using Spry (Copyright (c) 2006. Adobe Systems Incorporated) javascript library from www.adobe.com. The Spry library is FREE and redistributable with some condition (see license on the js file).</p>
<p><strong>Feature:</strong><br/>
* Displaying WordPress Category in dropdown css menu.<br/>
* No template arguments are needed to configure menu behavior, all settings are place on the Admin.<br/>
* Live preview as soon as you change the settings. No need to refresh your homepage to see changes.<br/>
* Configurable direction, your menu should appears horizontal, vertical drop left, or vertical drop right.<br/>
* Changeable Home text link, you can leave it blank for no home link.<br/>
* Depth setting, how many child you want to display.<br/>
* Exclue setting, you can select which category should not appears on the menu.<br/>
* Order setting, order by name or ID.<br/>
* Hide/Hide emtpy category. By default WordPress won&#8217;t display an empty category, now you can configure.<br/>
* Child of setting, only display menu from selected parent category.</p>
<p><strong>How to install?</strong></p>
<p>The installation is very easy.</p>
<p>1. Upload `wp-spry-menu` folder to the `/wp-content/plugins/` directory. Make sure wp-spry-menu contains all included files.<br/>
2. Activate the plugin through the &#8216;Plugins&#8217; menu in WordPress<br/>
3. Place `&lt; ?php if ( function_exists('wp_spry_menu') ) wp_spry_menu();?&gt;` in your templates<br/>
4. Configure from WP Spry Menu options in your WordPress Admin.</p>
<p>Note: Since WordPress 2.7.1 you can easy upload zipped plugin from admin.</p>
<p><strong>Frequently Asked Questions</strong></p>
<p>Is it support to display page menu?<br/>
<em>Currently not, may be in the next release.</em></p>
<p>Can I edit my own css from the settings page?<br/>
<em>I&#8217;m sorry you can&#8217;t, wait for the next release <img src="/images/misc/simple-smile.png" alt=":)" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><br/>
</em></p>
<p><strong>Screenshots</strong></p>
<p>1. Setting page and Vertical Drop Right preview.<br/>
<figure class="image-missing-placeholder" role="img" aria-label="screenshot-1-300x213.png">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">screenshot-1-300x213.png</span>
  </div>
</figure></p>
<p>2. Setting page and Vertical Drop Left preview.<br/>
<figure class="image-missing-placeholder" role="img" aria-label="screenshot-2-300x215.png">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">screenshot-2-300x215.png</span>
  </div>
</figure></p>
<p>3. Setting page and Horizontal preview.<br/>
<figure class="image-missing-placeholder" role="img" aria-label="screenshot-3-300x179.PNG">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">screenshot-3-300x179.PNG</span>
  </div>
</figure></p>
<p><strong>Changelog</strong></p>
<p>July 01, 2009 version 1.0.1<br/>
* Add Child of as dropdown select.<br/>
* Live preview from plugin setting page.<br/>
* Code improvement</p>
<p>June, 2009 version 1.0.0</p>
<p>* Add admin settings<br/>
* No need to add template argument, all go to setting area.<br/>
* Add Vertical Drop Left and Vertical Drop Right</p>
<p>January, 2009 version 0.0.1</p>
<p>* Only display Horizontal style<br/>
* First release </p>
<p><strong>Download</strong></p>
<p><a href="https://web.archive.org/web/20160211011603/http://wordpress.org/extend/plugins/wp-spry-menu/">Download from WordPress.org</a></p>
<p>Question and feedback are welcome <img src="/images/misc/simple-smile.png" alt=":)" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><br/>
<em><br/>
Post updated: August 13, 2009</em><br/>
<strong>Next Release&#8217;s Features:</strong><br/>
1. Added menu for page<br/>
2. Added ability to select theme for menu<br/>
3. Added ability to change the category title (&#8220;View all posts filed under &#8230;&#8221;)<br/>
4. User friendly help, using tooltips.<br/>
5. Cleaner output.<br/>
6. Fixed some IE problems <img src="/images/misc/simple-smile.png" alt=":)" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>
<p><em>Still in my head:</em><br/>
1. Add menu for blogroll.<br/>
2. Add ability to edit CSS directly.<br/>
3. Add ability to create custom menu.</p>
<div id="bawah-artikel" style="clear:both"> 

</div>										
									</div>
