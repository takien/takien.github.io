---
title: "WordPress Spry Menu Plugins"
date: "2009-07-01T00:00:00.000Z"
categories: ["WordPress Plugins"]
tags: []
slug: "2009/07/01/wordpress-spry-menu-plugins"
legacyUrl: "/2009/07/01/wordpress-spry-menu-plugins/"
source: "takien.com"
author: "takien"
comments: [{"author":"Morpie","date":"","text":"Hello\n\nI can’t find the menu options in wordpress admin?\nI use wp 2.9.2\n\nthx alot"},{"author":"takien","date":"","text":"See under settings, Wp Spry Menu should be there"},{"author":"Ling","date":"","text":"Hi takien,\n\nCan you please take a look at the menu at my site?\nhttp://teresaling.com/blog\n\nI tweaked everything and it’s turning out to be exactly like how I want it but the background color seems to end where the last letter is and I can’t get it to span across properly.\n\nAppreciate if you can help me"},{"author":"takien","date":"","text":"Hi Link,\nit’s look great.. do you combine with another css/plugins or tweak the code manually?\nso which is the problem? i can see the white border is not placed properly when sub menu is hovered. but I am not sure can help you."},{"author":"Shari","date":"","text":"I can’t figure out why I have the large gaps in the verticle menu bar on IE8. Looks fine in Firefox and Safari\n\nhttp://themessyartist.com/wp/"},{"author":"takien","date":"","text":"you have to hack some css since IE always has different behavior handling css"},{"author":"Shezz","date":"","text":"Hi,\n\nI added the menu, its working fine in admin panel and but after integration in header.php, I am unable to see dropdown sub-categories in header at http://www.wallpapersall.com\n\nPlease help."},{"author":"phillip gosper","date":"","text":"Hello Takien,\nyour wp spry menu looks just like the sort of program I have been searching for, but I am having difficulty moving to the next button.\nI am using\nwordpress 3..0.1\natahualpa 3.5.3\nwp spry menu 1.0.3\ncan you suggest an answer"},{"author":"bnther","date":"","text":"sorry the code is[php] [/php]"},{"author":"bnther","date":"","text":"wp_list_pages(‘title_li=’);"},{"author":"Flourian","date":"","text":"Your plugin is perfect, exactly what I need.\nBut but but… It’s so small! The menu is really tiny, is there any possibility to make it bigger?"},{"author":"Matt","date":"","text":"I’m wondering if there’s any relatively simple workaround to have the menu show the Pages instead of the Categories? Is this possible?"},{"author":"Brad Strong","date":"","text":"@flourian – just add this code to your style.css file. You can make other changes but this gets you the idea:\n#access a {\nfont-size: 18px;\n}\n\n@Matt – If you want your menu to work for pages, you are in luck, that is the default behavior of WordPress menus. Try the twentyten theme. I guarantee it would be no simple workaround to get Takien’s menu to work with Pages, that’s the whole point, his menu works with categories.\n\n@Takien – This is a great plugin! Thanks for making it! Menus driven by categories makes great sense. I do have a question though. You can sort the menus by ID – but there are no IDs by default. How might a person go about adding an ID to the menu items?"},{"author":"Brad Strong","date":"","text":"Okay, I figured out how to access a category ID – go to your category page in the Admin panel, hover over any given category, you will see the ID at the end of the address in your browsers status bar. It seems to increment the ID’s based on the order they were created. This means you better be content with your menu items being shown in the order you create them, or ordered by name.\n\nTakien, if you decide to develop this menu further, please add a method to order the menu items with a unique identifier; this will give us more complete flexibility in ordering menu items. Thanks for considering."},{"author":"Brad Strong","date":"","text":"Takien, I’m sorry to make a pest of myself. Just had a thought, that you could add the capability to order by category description, since that is a hook that WordPress provides, which would allow all us users to reorder our menus just by making sure our description starts with 1 or 2 or whatever. Just a thought!"},{"author":"julien","date":"","text":"Hello,\n\nI have install wp_spry_menu on my local computer.\nEverything is OK.\n\nI have also install my website on the http.\nBut when I consult my http website the spry menu do not respect the saved colors.\nI have change settings, chmod 777 for files. But nothing.\n\nCould you please help me ?\n\nI do the trial with Safari (osX) Firefox (Linux) and IE (XP). The same problem for all.\n\nThanks by advance"},{"author":"Lyuben","date":"","text":"Hi, I’ve got a problem – installed your plugin just to try it and when deactivated it the main menu dissapeared. Actually all the tabs are on the left side and in black, so not visible…how can I resolve this?"},{"author":"Lyuben","date":"","text":"Actually it is completely gone. I switched to different themes and there is still no menu?"},{"author":"Henrik","date":"","text":"I want to change the name of the “Home” button on my theme. Or maybe delete it from the menu. Is one of those possible? I don’t know how to do that?"},{"author":"Dave","date":"","text":"Hi. Works great thanks. One question, my drop down menu has no background colour so users are unable to see it. Any ideas? thanks"}]
---

Hi, this is my first plugin I write. WP Spry Menu that automatically creating Spry Drop Down Menu for wordpress category include configuration page with configurable “Home” link. This plugin using Spry (Copyright (c) 2006. Adobe Systems Incorporated) javascript library from www.adobe.com. The Spry library is FREE and redistributable with some condition (see license on the js file).

**Feature:**
 * Displaying WordPress Category in dropdown css menu.
 * No template arguments are needed to configure menu behavior, all settings are place on the Admin.
 * Live preview as soon as you change the settings. No need to refresh your homepage to see changes.
 * Configurable direction, your menu should appears horizontal, vertical drop left, or vertical drop right.
 * Changeable Home text link, you can leave it blank for no home link.
 * Depth setting, how many child you want to display.
 * Exclue setting, you can select which category should not appears on the menu.
 * Order setting, order by name or ID.
 * Hide/Hide emtpy category. By default WordPress won’t display an empty category, now you can configure.
 * Child of setting, only display menu from selected parent category.

**How to install?**

The installation is very easy.

1. Upload `wp-spry-menu` folder to the `/wp-content/plugins/` directory. Make sure wp-spry-menu contains all included files.
 2. Activate the plugin through the ‘Plugins’ menu in WordPress
 3. Place `< ?php if ( function_exists('wp_spry_menu') ) wp_spry_menu();?>` in your templates
 4. Configure from WP Spry Menu options in your WordPress Admin.

Note: Since WordPress 2.7.1 you can easy upload zipped plugin from admin.

**Frequently Asked Questions**

Is it support to display page menu?
 *Currently not, may be in the next release.*

Can I edit my own css from the settings page?
 *I’m sorry you can’t, wait for the next release :)*

**Screenshots**

1. Setting page and Vertical Drop Right preview.
 [![screenshot-1](/images/uploads/1788794396792_spry-screenshot-1.png)](http://takien.com/wp-content/uploads/2009/07/screenshot-1.png)

2. Setting page and Vertical Drop Left preview.
 [![screenshot-2](/images/uploads/1788794390322_spry-screenshot-2.png)](http://takien.com/wp-content/uploads/2009/07/screenshot-2.png)

3. Setting page and Horizontal preview.
 [![screenshot-3](/images/uploads/1788794383515_spry-screenshot-3.png)](http://takien.com/wp-content/uploads/2009/07/screenshot-3.PNG)

**Changelog**

July 01, 2009 version 1.0.1
 * Add Child of as dropdown select.
 * Live preview from plugin setting page.
 * Code improvement

June, 2009 version 1.0.0

* Add admin settings
 * No need to add template argument, all go to setting area.
 * Add Vertical Drop Left and Vertical Drop Right

January, 2009 version 0.0.1

* Only display Horizontal style
 * First release

**Download**

[Download from WordPress.org](http://wordpress.org/extend/plugins/wp-spry-menu/)

Question and feedback are welcome :) 

 *Post updated: August 13, 2009*

 **Next Release’s Features:**
 1. Added menu for page
 2. Added ability to select theme for menu
 3. Added ability to change the category title (“View all posts filed under …”)
 4. User friendly help, using tooltips.
 5. Cleaner output.
 6. Fixed some IE problems !;)

*Still in my head:*
 1. Add menu for blogroll.
 2. Add ability to edit CSS directly.
 3. Add ability to create custom menu.
