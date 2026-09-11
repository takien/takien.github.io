---
title: "The Way I Deal with Spam Comments"
date: "2010-11-05T00:00:00.000Z"
categories: ["WordPress Plugins"]
tags: ["spam"]
slug: "2010/11/05/the-way-i-deal-with-spam-comments"
legacyUrl: "/2010/11/05/the-way-i-deal-with-spam-comments/"
source: "takien.com"
author: "takien"
comments: [{"author":"jejen","date":"","text":"pertamax………."},{"author":"Brian Gottier","date":"","text":"I’ve been using Defensio, but I just don’t want to deal with the spam comments que, and most spams are easily targeted. I’m going to try your plugin. It looks like it will work perfectly. Thanks!"},{"author":"Presiden IDIOTNESIA","date":"","text":"Lhah, sama aja Mastah, make plugins juga, cuman Plugins punya Mastah Takien gak pake capcay ama api..\n\nI will try this at home.. 😀\n\n\n*ada list backlist keyword gak Mastah?"},{"author":"David","date":"","text":"I want to thank you for your little plugin. I discovered that over 80% of my spam was from yahoo.com and gmail.com. I blacklisted both domains and presto – huge drop in spam comments BUT huge spam folder. Your plugin lets me check my site every week or so now instead of daily.  One question – how could I change the plugin to delete spam daily? \n\nWith gratitude\n\nDavid"}]
---

<div id="attachment_728" style="width: 254px" class="wp-caption alignleft"><a href="/wp-content/uploads/2010/11/spammer.gif"><img src="/images/2010/11/spammer.gif" alt="Spammer" title="spammer" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">Spammer</p></div>
<p>There are so many WordPress plugins tagged <em>spam </em>published in <a href="https://web.archive.org/web/20150509174609/http://wordpress.org/extend/plugins/tags/spam" target="_blank">WordPress plugins directory</a>. Most of the plugins is to combat spam comment in WordPress blog. However, I am not use one of those plugins, because of several reasons:  they are captcha based (eg. re-Captcha) and they are using API (eg. Akismet). In my experience, using both type of anti spam could decrease my blog performance.</p>
<p><div style="float:right;width:300px;height:250px;margin-left:20px">

</div></p>
<p>For that reason I have a few tips for you to combat spam without sacrificing your web performance:</p>
<p>1. Never install any anti spam plugins that come with captcha, API, or remote database access.</p>
<p>2. Some plugins will count your spam, haha&#8230; it&#8217;s funny. Do not install such plugins.</p>
<p>3. Ensure you have these setting in <em>wp-admin/options-discussion.php</em></p>
<p><em>&#8211; An administrator must always approve the comment </em>( This should be ON)<br/>
<em> &#8211; Comment author must  have a previously approved comment </em>(This should be OFF)</p>
<p>4.  Use built in WordPress feature, blacklist comment. See figure below:</p>
<div id="attachment_727" style="width: 310px" class="wp-caption alignnone"><a href="/wp-content/uploads/2010/11/comment-blacklist.gif"><img src="/images/2010/11/comment-blacklist-300x89.gif" alt="Comment blacklist" title="comment-blacklist" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">Comment blacklist</p></div>
<p>6. Delete spam comment automatically. To do this I have written a little plugin named <strong>Delete Spam Hourly.</strong></p>
<p>Here is the code:</p>
<p>[php title=Delete Spam Hourly]</p>
<pre>
/*
Plugin Name: Delete Spam Hourly
Plugin URI: /
Description: Automatically delete blacklisted comment/spam every hour.
Author: takien
Version: 0.1
Author URI: /
*/

register_activation_hook(__FILE__, 'activate_delete_spam_hourly');
add_action('delete_spam_hourly_event', 'delete_spam_hourly');

function activate_delete_spam_hourly() {
	wp_schedule_event(time(), 'hourly', 'delete_spam_hourly_event');
}

function delete_spam_hourly() {
$pending = '0';
$spam	 = 'spam';

global $wpdb;
$comment_ids = $wpdb-&gt;get_col( "SELECT comment_ID FROM $wpdb-&gt;comments WHERE comment_approved = '$pending' OR comment_approved = '$spam'" );

foreach ($comment_ids as $comment_id){
	$comment = get_comment($comment_id, 'ARRAY_A');
	if(wp_blacklist_check($comment['comment_author'],$comment['comment_author_email'],$comment['comment_author_url'],$comment['comment_content'], $comment['comment_author_IP'],$comment['comment_agent'])){
		wp_delete_comment($comment_id);
	}
}
}
</pre>
<p>[/php]</p>
<div class="panel panel-info"><div class="panel-heading"><h3 class="panel-title">Download</h3></div><div class="panel-content" style="padding:5px 10px"><br/>
<a href="/project/plugins/delete-spam-hourly.zip">/project/plugins/delete-spam-hourly.zip</a><br/>
</div></div>

<div id="jp-relatedposts" class="jp-relatedposts">
	<h3 class="jp-relatedposts-headline"><em>Related</em></h3>
</div>
