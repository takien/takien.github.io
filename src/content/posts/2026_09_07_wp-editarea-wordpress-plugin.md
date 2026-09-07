---
title: "WP Editarea WordPress Plugin"
date: "2010-02-11T13:54:00.000Z"
categories: ["Plugins"]
tags: ["WordPress"]
slug: "2010/02/11/wp-editarea-wordpress-plugin"
legacyUrl: "/2010/02/11/wp-editarea-wordpress-plugin/"
source: "takien.com"
author: "takien"
comments: [{"author":"patrick","date":"","text":"Hi!\nThis is the best advanced editor for WordPress but:\ntoggle WordWrap doesn’t work using Firefox 3.5.7 and WordPress 2.9.1???"},{"author":"takien","date":"","text":"You’re right Pattrick,\nI’m sorry, that’s my mistake.\nI missed typing in this line (line 179, wp-editarea.php)\n\n[php]\n,word_wrap: < ?php echo get_option('wp_editarea_allow_toggle'); ?>\n[/php]\n\ninstead of :\n\n[php]\n,word_wrap: < ?php echo get_option('wp_editarea_word_wrap'); ?>\n[/php]"},{"author":"takien","date":"","text":"Thanks to Pattrick,\nPlugin is now updated to version 0.2 please check your dasboard."},{"author":"patrick","date":"","text":"great! thank you so much – now it’s PERFECT. Using it right now"},{"author":"Gale","date":"","text":"The best plugin for wordpress admins!!"},{"author":"takien","date":"","text":"Thanks Gale,"},{"author":"ortixia","date":"","text":"i am no longer getting edit area capabilities after the most recent update of wordpress (3.1). i love this plugin, and am wondering if anyone else has experienced this difficulty, and how they have dealt with this?"},{"author":"ortixia","date":"","text":"i am sorry, it seems edit area is working fine in my other wordpress site that i run it in (with same theme as well), so it must be a plug-in issue. (you can delete my above comment..)"},{"author":"Eben","date":"","text":"I love this plug in,but could you extend it so it could be used when editing the HTML in pages and posts, It extends the code editing area but with no syntax highlighting."},{"author":"takien","date":"","text":"Hello Eben, thank you for using my plugin.\nunfortunately, the WordPress editing page is still confusing me in many ways"},{"author":"domain registration","date":"","text":"Nice blog. I will keep visiting this blog very often."}]
---

Wordpress used to embed Codepress syntax highlighting at [Version 2.8](http://codex.wordpress.org/Version_2.8#New_Features) and immediately disabled it at [Version 2.8.1](http://wordpress.org/development/2009/07/wordpress-2-8-1/) due to browser incompatibilities. However I found another free Javascript code editor called [Editarea](http://www.cdolivet.com/index.php?page=editArea) which has more features than [Codepress](http://sourceforge.net/projects/codepress/). Now you can simply integrate Editarea functionality to your WordPress by using **WP Editarea Plugins**.

**WP Editarea**

- Contributors: takien
- Requires at least: 2.9
- Tested up to: 2.9.1
- Stable tag: 0.1

**Description**

WP Editarea turns your Oldschool textarea code editor in WordPress Dashboard (plugin/theme editor) into a fancy realtime highlighted code editor using [Editarea](http://www.cdolivet.com/index.php?page=editArea).

**Plugin Feature**

* Automatically detect syntax language
 * Live preview in plugin option page
 * Better than codepress (for me)
 * Easy integration, no file to edit
 * Easy to use configuration page

**Editarea Feature**
 * Multi language interface
 * Bracket matching highlight
 * Support many syntax
 * Line numbers
 * Search/replace with regex
 * More at [Editarea homepage](http://www.cdolivet.com/index.php?page=editArea).

**Browser Compatibility**
 * IE 6 & 7 & 8, Firefox 1.5 & 2 & 3, Safari 3.x & 4, Opera 9, 9.5, 9.6 and Chrome 1 & 2[2]

**Installation**

The installation process.

1. Upload `wp-editarea` folder to the `/wp-content/plugins/` directory. Make sure directory structures are not changed. Or Directly upload from your Plugin management page.
 2. Activate the plugin through the ‘Plugins’ menu in WordPress
 3. Go to Settings menu and set options you need.

**Screenshots**

1. Setting page and live preview.

[![wordpress editarea, wordpress syntax highlight](/images/uploads/1788794702264_editarea-screenshot-11.png)](http://takien.com/wp-content/uploads/2010/02/screenshot-11.png)

WP Editarea setting page.

2. Your new theme editor :D

[![ editarea, wordpress code editor, wordpress syntax highlight](/images/uploads/1788794710019_editarea-screenshot-2.png)](http://takien.com/wp-content/uploads/2010/02/screenshot-2.png)

Wordpress Editarea

Download [Download from WordPress.org](http://wordpress.org/extend/plugins/wp-editarea/)
