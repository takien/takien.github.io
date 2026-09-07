---
title: "WordPress Plugin WP Sub Post"
date: "2010-01-28T21:08:08+00:00"
categories: ["Article"]
tags: ["PHP", "Plugins", "child post", "wordpress plugins", "wordpress sub post"]
slug: "2010/01/28/wordpress-plugin-wp-sub-post"
legacyUrl: "/2010/01/28/wordpress-plugin-wp-sub-post/"
comments: []
---

<div class="add">

</div>
<code><span style="color: #000000">
&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&amp;lt;/select&amp;gt;&amp;lt;/pre&amp;gt;&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&amp;lt;pre&amp;gt;function&nbsp;subpost_template($content)&nbsp;{&lt;/span&gt;<br/>&amp;nbsp;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;if(is_singular())&nbsp;{&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;remove_filter('&lt;/span&gt;posts_where&lt;span&nbsp;class="st_h"&gt;','&lt;/span&gt;where_no_parent&lt;span&nbsp;class="st_h"&gt;');&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;}&lt;/span&gt;<br/>&amp;nbsp;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;$parentID&nbsp;=&nbsp;get_the_ID();&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;$childposts&nbsp;=&nbsp;get_posts(array(&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;'&lt;/span&gt;post_type&lt;span&nbsp;class="st_h"&gt;'&nbsp;=&amp;gt;&nbsp;'&lt;/span&gt;post&lt;span&nbsp;class="st_h"&gt;',&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;'&lt;/span&gt;numberposts&lt;span&nbsp;class="st_h"&gt;'&nbsp;=&amp;gt;&nbsp;-1,&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;'&lt;/span&gt;post_status&lt;span&nbsp;class="st_h"&gt;'&nbsp;=&amp;gt;&nbsp;'&lt;/span&gt;publish&lt;span&nbsp;class="st_h"&gt;',&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;'&lt;/span&gt;post_parent&lt;span&nbsp;class="st_h"&gt;'&nbsp;=&amp;gt;&nbsp;$parentID&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;));&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;$subcontent&nbsp;=&nbsp;&amp;quot;&amp;quot;;&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;foreach($childposts&nbsp;as&nbsp;$childpost){&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;$subcontent&nbsp;.=&nbsp;&amp;quot;&amp;lt;/pre&amp;gt;&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&amp;lt;blockquote&amp;gt;&amp;quot;;&nbsp;$subcontent&nbsp;.=&nbsp;&amp;quot;&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&amp;lt;h3&amp;gt;&amp;quot;.$childpost-&amp;gt;post_title.&amp;quot;&amp;lt;/h3&amp;gt;&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&amp;quot;;&nbsp;$subcontent&nbsp;.=&nbsp;$childpost-&amp;gt;post_content;&nbsp;$subcontent&nbsp;.=&nbsp;'&lt;/span&gt;&nbsp;&lt;span&nbsp;class="sy0"&gt;&amp;lt;&lt;/span&gt;a&nbsp;href&lt;span&nbsp;class="sy0"&gt;=&lt;/span&gt;&lt;span&nbsp;class="st0"&gt;&amp;quot;'.get_edit_post_link(&lt;span&nbsp;class="es4"&gt;$childpost-&amp;gt;ID&lt;/span&gt;).'&amp;quot;&lt;/span&gt;&nbsp;rel&lt;span&nbsp;class="sy0"&gt;=&lt;/span&gt;&lt;span&nbsp;class="st0"&gt;&amp;quot;nofollow&amp;quot;&lt;/span&gt;&lt;span&nbsp;class="sy0"&gt;&amp;gt;&lt;/span&gt;Edit&lt;span&nbsp;class="sy0"&gt;&amp;lt;/&lt;/span&gt;a&lt;span&nbsp;class="sy0"&gt;&amp;gt;&lt;/span&gt;&nbsp;&lt;span&nbsp;class="st_h"&gt;';&nbsp;$subcontent&nbsp;.=&nbsp;&amp;quot;&amp;lt;/blockquote&amp;gt;&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&amp;lt;pre&amp;gt;&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&amp;quot;;&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;}&lt;/span&gt;<br/>&amp;nbsp;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;$content&nbsp;.=&nbsp;$subcontent;&lt;/span&gt;<br/>&amp;nbsp;<br/>&lt;span&nbsp;class="st_h"&gt;&nbsp;&amp;nbsp;&nbsp;&amp;nbsp;return&nbsp;$content;&lt;/span&gt;<br/>&lt;span&nbsp;class="st_h"&gt;}&lt;/span&gt;&lt;/pre&gt;<br/>&lt;/td&gt;<br/>&lt;/tr&gt;<br/>&lt;/tbody&gt;<br/>&lt;/table&gt;<br/>&lt;/div&gt;<br/>&lt;div&nbsp;class="bwp-syntax-source"&gt;<br/>&lt;pre&nbsp;class="no-parse"&gt;&amp;lt;&nbsp;?php
<br/>/*
<br/>Plugin&nbsp;Name:&nbsp;WP&nbsp;Sub&nbsp;Post
<br/>Plugin&nbsp;URI:&nbsp;http://wordpress.org/#
<br/>Description:&nbsp;You&nbsp;can&nbsp;make&nbsp;a&nbsp;post&nbsp;is&nbsp;a&nbsp;child&nbsp;of&nbsp;another&nbsp;post.
<br/>Author:&nbsp;Takien
<br/>Version:&nbsp;0.1&nbsp;Alpha
<br/>Author&nbsp;URI:&nbsp;/
<br/>*/
<br/>
<br/>////////////////////////////
<br/>
<br/>class&nbsp;Walker_PostDropdown&nbsp;extends&nbsp;Walker&nbsp;{
<br/>
<br/>var&nbsp;$tree_type&nbsp;=&nbsp;'post';
<br/>
<br/>var&nbsp;$db_fields&nbsp;=&nbsp;array&nbsp;('parent'&nbsp;=&amp;gt;&nbsp;'post_parent',&nbsp;'id'&nbsp;=&amp;gt;&nbsp;'ID');
<br/>
<br/>function&nbsp;start_el(&amp;amp;$output,&nbsp;$page,&nbsp;$depth,&nbsp;$args)&nbsp;{
<br/>$pad&nbsp;=&nbsp;str_repeat(' ',&nbsp;$depth&nbsp;*&nbsp;3);
<br/>
<br/>$output&nbsp;.=&nbsp;"\tID\"";
<br/>if&nbsp;(&nbsp;$page-&amp;gt;ID&nbsp;==&nbsp;$args['selected']&nbsp;)
<br/>$output&nbsp;.=&nbsp;'&nbsp;selected="selected"';
<br/>$output&nbsp;.=&nbsp;'&amp;gt;';
<br/>$title&nbsp;=&nbsp;esc_html($page-&amp;gt;post_title);
<br/>$output&nbsp;.=&nbsp;"$pad$title";
<br/>$output&nbsp;.=&nbsp;"\n";
<br/>}
<br/>}
<br/>/////////////
<br/>function&nbsp;&amp;amp;wp_get_posts($args&nbsp;=&nbsp;'')&nbsp;{
<br/>global&nbsp;$wpdb;
<br/>
<br/>$defaults&nbsp;=&nbsp;array(
<br/>'child_of'&nbsp;=&amp;gt;&nbsp;0,&nbsp;'sort_order'&nbsp;=&amp;gt;&nbsp;'ASC',
<br/>'sort_column'&nbsp;=&amp;gt;&nbsp;'post_title',&nbsp;'hierarchical'&nbsp;=&amp;gt;&nbsp;1,
<br/>'exclude'&nbsp;=&amp;gt;&nbsp;'',&nbsp;'include'&nbsp;=&amp;gt;&nbsp;'',
<br/>'meta_key'&nbsp;=&amp;gt;&nbsp;'',&nbsp;'meta_value'&nbsp;=&amp;gt;&nbsp;'',
<br/>'authors'&nbsp;=&amp;gt;&nbsp;'',&nbsp;'parent'&nbsp;=&amp;gt;&nbsp;-1,&nbsp;'exclude_tree'&nbsp;=&amp;gt;&nbsp;'',
<br/>'number'&nbsp;=&amp;gt;&nbsp;'',&nbsp;'offset'&nbsp;=&amp;gt;&nbsp;0
<br/>);
<br/>
<br/>$r&nbsp;=&nbsp;wp_parse_args(&nbsp;$args,&nbsp;$defaults&nbsp;);
<br/>extract(&nbsp;$r,&nbsp;EXTR_SKIP&nbsp;);
<br/>$number&nbsp;=&nbsp;(int)&nbsp;$number;
<br/>$offset&nbsp;=&nbsp;(int)&nbsp;$offset;
<br/>
<br/>$cache&nbsp;=&nbsp;array();
<br/>$key&nbsp;=&nbsp;md5(&nbsp;serialize(&nbsp;compact(array_keys($defaults))&nbsp;)&nbsp;);
<br/>if&nbsp;(&nbsp;$cache&nbsp;=&nbsp;wp_cache_get(&nbsp;'wp_get_posts',&nbsp;'posts'&nbsp;)&nbsp;)&nbsp;{
<br/>if&nbsp;(&nbsp;is_array($cache)&nbsp;&amp;amp;&amp;amp;&nbsp;isset(&nbsp;$cache[&nbsp;$key&nbsp;]&nbsp;)&nbsp;)&nbsp;{
<br/>$pages&nbsp;=&nbsp;apply_filters('wp_get_posts',&nbsp;$cache[&nbsp;$key&nbsp;],&nbsp;$r&nbsp;);
<br/>return&nbsp;$pages;
<br/>}
<br/>}
<br/>
<br/>if&nbsp;(&nbsp;!is_array($cache)&nbsp;)
<br/>$cache&nbsp;=&nbsp;array();
<br/>
<br/>$inclusions&nbsp;=&nbsp;'';
<br/>if&nbsp;(&nbsp;!empty($include)&nbsp;)&nbsp;{
<br/>$child_of&nbsp;=&nbsp;0;&nbsp;//ignore&nbsp;child_of,&nbsp;parent,&nbsp;exclude,&nbsp;meta_key,&nbsp;and&nbsp;meta_value&nbsp;params&nbsp;if&nbsp;using&nbsp;include
<br/>$parent&nbsp;=&nbsp;-1;
<br/>$exclude&nbsp;=&nbsp;'';
<br/>$meta_key&nbsp;=&nbsp;'';
<br/>$meta_value&nbsp;=&nbsp;'';
<br/>$hierarchical&nbsp;=&nbsp;false;
<br/>$incpages&nbsp;=&nbsp;preg_split('/[\s,]+/',$include);
<br/>if&nbsp;(&nbsp;count($incpages)&nbsp;)&nbsp;{
<br/>foreach&nbsp;(&nbsp;$incpages&nbsp;as&nbsp;$incpage&nbsp;)&nbsp;{
<br/>if&nbsp;(empty($inclusions))
<br/>$inclusions&nbsp;=&nbsp;$wpdb-&amp;gt;prepare('&nbsp;AND&nbsp;(&nbsp;ID&nbsp;=&nbsp;%d&nbsp;',&nbsp;$incpage);
<br/>else
<br/>$inclusions&nbsp;.=&nbsp;$wpdb-&amp;gt;prepare('&nbsp;OR&nbsp;ID&nbsp;=&nbsp;%d&nbsp;',&nbsp;$incpage);
<br/>}
<br/>}
<br/>}
<br/>if&nbsp;(!empty($inclusions))
<br/>$inclusions&nbsp;.=&nbsp;')';
<br/>
<br/>$exclusions&nbsp;=&nbsp;'';
<br/>if&nbsp;(&nbsp;!empty($exclude)&nbsp;)&nbsp;{
<br/>$expages&nbsp;=&nbsp;preg_split('/[\s,]+/',$exclude);
<br/>if&nbsp;(&nbsp;count($expages)&nbsp;)&nbsp;{
<br/>foreach&nbsp;(&nbsp;$expages&nbsp;as&nbsp;$expage&nbsp;)&nbsp;{
<br/>if&nbsp;(empty($exclusions))
<br/>$exclusions&nbsp;=&nbsp;$wpdb-&amp;gt;prepare('&nbsp;AND&nbsp;(&nbsp;ID&nbsp;&amp;lt;&amp;gt;&nbsp;%d&nbsp;',&nbsp;$expage);
<br/>else
<br/>$exclusions&nbsp;.=&nbsp;$wpdb-&amp;gt;prepare('&nbsp;AND&nbsp;ID&nbsp;&amp;lt;&amp;gt;&nbsp;%d&nbsp;',&nbsp;$expage);
<br/>}
<br/>}
<br/>}
<br/>if&nbsp;(!empty($exclusions))
<br/>$exclusions&nbsp;.=&nbsp;')';
<br/>
<br/>$author_query&nbsp;=&nbsp;'';
<br/>if&nbsp;(!empty($authors))&nbsp;{
<br/>$post_authors&nbsp;=&nbsp;preg_split('/[\s,]+/',$authors);
<br/>
<br/>if&nbsp;(&nbsp;count($post_authors)&nbsp;)&nbsp;{
<br/>foreach&nbsp;(&nbsp;$post_authors&nbsp;as&nbsp;$post_author&nbsp;)&nbsp;{
<br/>//Do&nbsp;we&nbsp;have&nbsp;an&nbsp;author&nbsp;id&nbsp;or&nbsp;an&nbsp;author&nbsp;login?
<br/>if&nbsp;(&nbsp;0&nbsp;==&nbsp;intval($post_author)&nbsp;)&nbsp;{
<br/>$post_author&nbsp;=&nbsp;get_userdatabylogin($post_author);
<br/>if&nbsp;(&nbsp;empty($post_author)&nbsp;)
<br/>continue;
<br/>if&nbsp;(&nbsp;empty($post_author-&amp;gt;ID)&nbsp;)
<br/>continue;
<br/>$post_author&nbsp;=&nbsp;$post_author-&amp;gt;ID;
<br/>}
<br/>
<br/>if&nbsp;(&nbsp;''&nbsp;==&nbsp;$author_query&nbsp;)
<br/>$author_query&nbsp;=&nbsp;$wpdb-&amp;gt;prepare('&nbsp;post_author&nbsp;=&nbsp;%d&nbsp;',&nbsp;$post_author);
<br/>else
<br/>$author_query&nbsp;.=&nbsp;$wpdb-&amp;gt;prepare('&nbsp;OR&nbsp;post_author&nbsp;=&nbsp;%d&nbsp;',&nbsp;$post_author);
<br/>}
<br/>if&nbsp;(&nbsp;''&nbsp;!=&nbsp;$author_query&nbsp;)
<br/>$author_query&nbsp;=&nbsp;"&nbsp;AND&nbsp;($author_query)";
<br/>}
<br/>}
<br/>
<br/>$join&nbsp;=&nbsp;'';
<br/>$where&nbsp;=&nbsp;"$exclusions&nbsp;$inclusions&nbsp;";
<br/>if&nbsp;(&nbsp;!&nbsp;empty(&nbsp;$meta_key&nbsp;)&nbsp;||&nbsp;!&nbsp;empty(&nbsp;$meta_value&nbsp;)&nbsp;)&nbsp;{
<br/>$join&nbsp;=&nbsp;"&nbsp;LEFT&nbsp;JOIN&nbsp;$wpdb-&amp;gt;postmeta&nbsp;ON&nbsp;(&nbsp;$wpdb-&amp;gt;posts.ID&nbsp;=&nbsp;$wpdb-&amp;gt;postmeta.post_id&nbsp;)";
<br/>
<br/>//&nbsp;meta_key&nbsp;and&nbsp;meta_value&nbsp;might&nbsp;be&nbsp;slashed
<br/>$meta_key&nbsp;=&nbsp;stripslashes($meta_key);
<br/>$meta_value&nbsp;=&nbsp;stripslashes($meta_value);
<br/>if&nbsp;(&nbsp;!&nbsp;empty(&nbsp;$meta_key&nbsp;)&nbsp;)
<br/>$where&nbsp;.=&nbsp;$wpdb-&amp;gt;prepare("&nbsp;AND&nbsp;$wpdb-&amp;gt;postmeta.meta_key&nbsp;=&nbsp;%s",&nbsp;$meta_key);
<br/>if&nbsp;(&nbsp;!&nbsp;empty(&nbsp;$meta_value&nbsp;)&nbsp;)
<br/>$where&nbsp;.=&nbsp;$wpdb-&amp;gt;prepare("&nbsp;AND&nbsp;$wpdb-&amp;gt;postmeta.meta_value&nbsp;=&nbsp;%s",&nbsp;$meta_value);
<br/>
<br/>}
<br/>
<br/>if&nbsp;(&nbsp;$parent&nbsp;&amp;gt;=&nbsp;0&nbsp;)
<br/>$where&nbsp;.=&nbsp;$wpdb-&amp;gt;prepare('&nbsp;AND&nbsp;post_parent&nbsp;=&nbsp;%d&nbsp;',&nbsp;$parent);
<br/>
<br/>$query&nbsp;=&nbsp;"SELECT&nbsp;*&nbsp;FROM&nbsp;$wpdb-&amp;gt;posts&nbsp;$join&nbsp;WHERE&nbsp;(post_type&nbsp;=&nbsp;'post'&nbsp;AND&nbsp;post_status&nbsp;=&nbsp;'publish')&nbsp;$where&nbsp;";
<br/>$query&nbsp;.=&nbsp;$author_query;
<br/>$query&nbsp;.=&nbsp;"&nbsp;ORDER&nbsp;BY&nbsp;"&nbsp;.&nbsp;$sort_column&nbsp;.&nbsp;"&nbsp;"&nbsp;.&nbsp;$sort_order&nbsp;;
<br/>
<br/>if&nbsp;(&nbsp;!empty($number)&nbsp;)
<br/>$query&nbsp;.=&nbsp;'&nbsp;LIMIT&nbsp;'&nbsp;.&nbsp;$offset&nbsp;.&nbsp;','&nbsp;.&nbsp;$number;
<br/>
<br/>$pages&nbsp;=&nbsp;$wpdb-&amp;gt;get_results($query);
<br/>
<br/>if&nbsp;(&nbsp;empty($pages)&nbsp;)&nbsp;{
<br/>$pages&nbsp;=&nbsp;apply_filters('wp_get_posts',&nbsp;array(),&nbsp;$r);
<br/>return&nbsp;$pages;
<br/>}
<br/>
<br/>//&nbsp;Sanitize&nbsp;before&nbsp;caching&nbsp;so&nbsp;it'll&nbsp;only&nbsp;get&nbsp;done&nbsp;once
<br/>$num_pages&nbsp;=&nbsp;count($pages);
<br/>for&nbsp;($i&nbsp;=&nbsp;0;&nbsp;$i&nbsp;&amp;lt;&nbsp;$num_pages;&nbsp;$i++)&nbsp;{
<br/>$pages[$i]&nbsp;=&nbsp;sanitize_post($pages[$i],&nbsp;'raw');
<br/>}
<br/>
<br/>//&nbsp;Update&nbsp;cache.
<br/>update_page_cache($pages);
<br/>
<br/>if&nbsp;(&nbsp;$child_of&nbsp;||&nbsp;$hierarchical&nbsp;)
<br/>$pages&nbsp;=&nbsp;&amp;amp;&nbsp;get_page_children($child_of,&nbsp;$pages);
<br/>
<br/>if&nbsp;(&nbsp;!empty($exclude_tree)&nbsp;)&nbsp;{
<br/>$exclude&nbsp;=&nbsp;(int)&nbsp;$exclude_tree;
<br/>$children&nbsp;=&nbsp;get_page_children($exclude,&nbsp;$pages);
<br/>$excludes&nbsp;=&nbsp;array();
<br/>foreach&nbsp;(&nbsp;$children&nbsp;as&nbsp;$child&nbsp;)
<br/>$excludes[]&nbsp;=&nbsp;$child-&amp;gt;ID;
<br/>$excludes[]&nbsp;=&nbsp;$exclude;
<br/>$num_pages&nbsp;=&nbsp;count($pages);
<br/>for&nbsp;(&nbsp;$i&nbsp;=&nbsp;0;&nbsp;$i&nbsp;&amp;lt;&nbsp;$num_pages;&nbsp;$i++&nbsp;)&nbsp;{
<br/>if&nbsp;(&nbsp;in_array($pages[$i]-&amp;gt;ID,&nbsp;$excludes)&nbsp;)
<br/>unset($pages[$i]);
<br/>}
<br/>}
<br/>
<br/>$cache[&nbsp;$key&nbsp;]&nbsp;=&nbsp;$pages;
<br/>wp_cache_set(&nbsp;'wp_get_posts',&nbsp;$cache,&nbsp;'posts'&nbsp;);
<br/>
<br/>$pages&nbsp;=&nbsp;apply_filters('wp_get_posts',&nbsp;$pages,&nbsp;$r);
<br/>
<br/>return&nbsp;$pages;
<br/>}
<br/>//////////////
<br/>
<br/>function&nbsp;walk_post_dropdown_tree()&nbsp;{
<br/>$args&nbsp;=&nbsp;func_get_args();
<br/>if&nbsp;(&nbsp;empty($args[2]['walker'])&nbsp;)&nbsp;//&nbsp;the&nbsp;user's&nbsp;options&nbsp;are&nbsp;the&nbsp;third&nbsp;parameter
<br/>$walker&nbsp;=&nbsp;new&nbsp;Walker_PostDropdown;
<br/>else
<br/>$walker&nbsp;=&nbsp;$args[2]['walker'];
<br/>
<br/>return&nbsp;call_user_func_array(array(&amp;amp;$walker,&nbsp;'walk'),&nbsp;$args);
<br/>}
<br/>
<br/>function&nbsp;wp_dropdown_posts($args&nbsp;=&nbsp;'')&nbsp;{
<br/>$defaults&nbsp;=&nbsp;array(
<br/>'depth'&nbsp;=&amp;gt;&nbsp;0,&nbsp;'child_of'&nbsp;=&amp;gt;&nbsp;0,
<br/>'selected'&nbsp;=&amp;gt;&nbsp;0,&nbsp;'echo'&nbsp;=&amp;gt;&nbsp;1,
<br/>'name'&nbsp;=&amp;gt;&nbsp;'page_id',&nbsp;'show_option_none'&nbsp;=&amp;gt;&nbsp;'',&nbsp;'show_option_no_change'&nbsp;=&amp;gt;&nbsp;'',
<br/>'option_none_value'&nbsp;=&amp;gt;&nbsp;''
<br/>);
<br/>
<br/>$r&nbsp;=&nbsp;wp_parse_args(&nbsp;$args,&nbsp;$defaults&nbsp;);
<br/>extract(&nbsp;$r,&nbsp;EXTR_SKIP&nbsp;);
<br/>
<br/>$pages&nbsp;=&nbsp;wp_get_posts($r);
<br/>$output&nbsp;=&nbsp;'';
<br/>$name&nbsp;=&nbsp;esc_attr($name);
<br/>
<br/>if&nbsp;(&nbsp;!&nbsp;empty($pages)&nbsp;)&nbsp;{
<br/>$output&nbsp;=&nbsp;"&amp;lt;select&nbsp;name="\"$name\""&amp;gt;
<br/>&amp;lt;option&nbsp;value="\"-1\""&amp;gt;$show_option_no_change&amp;lt;/option&amp;gt;
<br/>&amp;lt;option&nbsp;value="\"""&amp;gt;$show_option_none&amp;lt;/option&amp;gt;\n";
<br/>&amp;lt;/select&amp;gt;
<br/>&amp;lt;select&nbsp;name="\"$name\""&amp;gt;}
<br/>&amp;lt;/select&amp;gt;
<br/>
<br/>$output&nbsp;=&nbsp;apply_filters('wp_dropdown_pages',&nbsp;$output);
<br/>
<br/>if&nbsp;(&nbsp;$echo&nbsp;)
<br/>echo&nbsp;$output;
<br/>
<br/>return&nbsp;$output;
<br/>}
<br/>/////////////////////////////
<br/>
<br/>/*&nbsp;Use&nbsp;the&nbsp;admin_menu&nbsp;action&nbsp;to&nbsp;define&nbsp;the&nbsp;custom&nbsp;boxes&nbsp;*/
<br/>add_action('admin_menu',&nbsp;'myplugin_add_custom_box');
<br/>
<br/>/*&nbsp;Use&nbsp;the&nbsp;save_post&nbsp;action&nbsp;to&nbsp;do&nbsp;something&nbsp;with&nbsp;the&nbsp;data&nbsp;entered&nbsp;*/
<br/>add_action('save_post',&nbsp;'myplugin_save_postdata');
<br/>
<br/>/*&nbsp;Adds&nbsp;a&nbsp;custom&nbsp;section&nbsp;to&nbsp;the&nbsp;"advanced"&nbsp;Post&nbsp;and&nbsp;Page&nbsp;edit&nbsp;screens&nbsp;*/
<br/>function&nbsp;myplugin_add_custom_box()&nbsp;{
<br/>
<br/>if(&nbsp;function_exists(&nbsp;'add_meta_box'&nbsp;))&nbsp;{
<br/>add_meta_box(&nbsp;'myplugin_sectionid',&nbsp;__(&nbsp;'WP&nbsp;Sub&nbsp;Posts',&nbsp;'myplugin_textdomain'&nbsp;),&nbsp;'myplugin_inner_custom_box',&nbsp;'post',&nbsp;'side','high'&nbsp;);
<br/>//add_meta_box(&nbsp;$id,&nbsp;$title,&nbsp;$callback,&nbsp;$page,&nbsp;$context,&nbsp;$priority&nbsp;);
<br/>add_meta_box(&nbsp;'myplugin_sectionid',&nbsp;__(&nbsp;'WP&nbsp;Sub&nbsp;Posts',&nbsp;'myplugin_textdomain'&nbsp;),&nbsp;'myplugin_inner_custom_box',&nbsp;'page',&nbsp;'advanced'&nbsp;);
<br/>}&nbsp;else&nbsp;{
<br/>add_action('dbx_post_advanced',&nbsp;'myplugin_old_custom_box'&nbsp;);
<br/>add_action('dbx_page_advanced',&nbsp;'myplugin_old_custom_box'&nbsp;);
<br/>}
<br/>}
<br/>
<br/>function&nbsp;myplugin_inner_custom_box()&nbsp;{
<br/>echo&nbsp;'
<br/>&amp;lt;pre&amp;gt;&amp;lt;select&nbsp;name="\"$name\""&amp;gt;';&nbsp;echo&nbsp;'
<br/>&amp;lt;/select&amp;gt;&amp;lt;input&nbsp;id="myplugin_noncename"&nbsp;name="myplugin_noncename"&nbsp;type="hidden"&nbsp;value="'&nbsp;.
<br/>&nbsp;&nbsp;&nbsp;&nbsp;wp_create_nonce(&nbsp;plugin_basename(__FILE__)&nbsp;)&nbsp;.&nbsp;'"&nbsp;/&amp;gt;&amp;lt;select&nbsp;name="\"$name\""&amp;gt;';&nbsp;?&amp;gt;
<br/>&amp;lt;/select&amp;gt;&amp;lt;/pre&amp;gt;
<br/>&amp;lt;h5&amp;gt;&amp;lt;?php&nbsp;_e('Parent')&nbsp;?&amp;gt;&amp;lt;/h5&amp;gt;
<br/>&amp;lt;pre&amp;gt;&amp;lt;label&nbsp;for="post_parent"&amp;gt;Please&nbsp;select&nbsp;the&nbsp;parent&nbsp;of&nbsp;this&nbsp;post&amp;lt;/label&amp;gt;&amp;lt;select&nbsp;name="\"$name\""&amp;gt;&nbsp;&amp;lt;?php&nbsp;$currentid&nbsp;=&nbsp;$_GET['post'];&nbsp;wp_dropdown_posts(array('exclude_tree'&nbsp;=&amp;gt;&nbsp;$currentid,&nbsp;'selected'&nbsp;=&amp;gt;&nbsp;$post-&amp;gt;post_parent,&nbsp;'name'&nbsp;=&amp;gt;&nbsp;'parent_id',&nbsp;'show_option_none'&nbsp;=&amp;gt;&nbsp;__('Main&nbsp;Post&nbsp;(no&nbsp;parent)'),&nbsp;'sort_column'&nbsp;=&amp;gt;&nbsp;'menu_order,&nbsp;post_title'));&nbsp;}&nbsp;/*&nbsp;Prints&nbsp;the&nbsp;edit&nbsp;form&nbsp;for&nbsp;pre-WordPress&nbsp;2.5&nbsp;post/page&nbsp;*/&nbsp;function&nbsp;myplugin_old_custom_box()&nbsp;{&nbsp;echo&nbsp;'
<br/>&amp;lt;/select&amp;gt;&amp;lt;/pre&amp;gt;
<br/>&amp;lt;div&nbsp;class="dbx-b-ox-wrapper"&amp;gt;'&nbsp;.&nbsp;"\n";&nbsp;echo&nbsp;'
<br/>&amp;lt;fieldset&nbsp;id="myplugin_fieldsetid"&nbsp;class="dbx-box"&amp;gt;'&nbsp;.&nbsp;"\n";&nbsp;echo&nbsp;'
<br/>&amp;lt;div&nbsp;class="dbx-h-andle-wrapper"&amp;gt;
<br/>&amp;lt;h3&nbsp;class="dbx-handle"&amp;gt;'&nbsp;.&nbsp;__(&nbsp;'WP&nbsp;Sub&nbsp;Posts',&nbsp;'myplugin_textdomain'&nbsp;)&nbsp;.&nbsp;"&amp;lt;/h3&amp;gt;
<br/>&amp;lt;/div&amp;gt;
<br/>";&nbsp;echo&nbsp;'
<br/>&amp;lt;div&nbsp;class="dbx-c-ontent-wrapper"&amp;gt;
<br/>&amp;lt;div&nbsp;class="dbx-content"&amp;gt;';&nbsp;//&nbsp;output&nbsp;editing&nbsp;form&nbsp;myplugin_inner_custom_box();&nbsp;//&nbsp;end&nbsp;wrapper&nbsp;echo&nbsp;"&amp;lt;/div&amp;gt;
<br/>&amp;lt;/div&amp;gt;&amp;lt;/fieldset&amp;gt;
<br/>&amp;lt;/div&amp;gt;
<br/>&amp;lt;pre&amp;gt;&amp;lt;select&nbsp;name="\"$name\""&amp;gt;\n";&nbsp;}&nbsp;/*&nbsp;When&nbsp;the&nbsp;post&nbsp;is&nbsp;saved,&nbsp;saves&nbsp;our&nbsp;custom&nbsp;data&nbsp;*/&nbsp;function&nbsp;myplugin_save_postdata(&nbsp;$post_id&nbsp;)&nbsp;{&nbsp;//&nbsp;verify&nbsp;this&nbsp;came&nbsp;from&nbsp;the&nbsp;our&nbsp;screen&nbsp;and&nbsp;with&nbsp;proper&nbsp;authorization,&nbsp;//&nbsp;because&nbsp;save_post&nbsp;can&nbsp;be&nbsp;triggered&nbsp;at&nbsp;other&nbsp;times&nbsp;if&nbsp;(&nbsp;!wp_verify_nonce(&nbsp;$_POST['myplugin_noncename'],&nbsp;plugin_basename(__FILE__)&nbsp;))&nbsp;{&nbsp;return&nbsp;$post_id;&nbsp;}&nbsp;//&nbsp;verify&nbsp;if&nbsp;this&nbsp;is&nbsp;an&nbsp;auto&nbsp;save&nbsp;routine.&nbsp;If&nbsp;it&nbsp;is&nbsp;our&nbsp;form&nbsp;has&nbsp;not&nbsp;been&nbsp;submitted,&nbsp;so&nbsp;we&nbsp;dont&nbsp;want&nbsp;//&nbsp;to&nbsp;do&nbsp;anything&nbsp;if&nbsp;(&nbsp;defined('DOING_AUTOSAVE')&nbsp;&amp;amp;&amp;amp;&nbsp;DOING_AUTOSAVE&nbsp;)&nbsp;return&nbsp;$post_id;&nbsp;//&nbsp;Check&nbsp;permissions&nbsp;if&nbsp;(&nbsp;'page'&nbsp;==&nbsp;$_POST['post_type']&nbsp;)&nbsp;{&nbsp;if&nbsp;(&nbsp;!current_user_can(&nbsp;'edit_page',&nbsp;$post_id&nbsp;)&nbsp;)&nbsp;return&nbsp;$post_id;&nbsp;}&nbsp;else&nbsp;{&nbsp;if&nbsp;(&nbsp;!current_user_can(&nbsp;'edit_post',&nbsp;$post_id&nbsp;)&nbsp;)&nbsp;return&nbsp;$post_id;&nbsp;}&nbsp;//&nbsp;OK,&nbsp;we're&nbsp;authenticated:&nbsp;we&nbsp;need&nbsp;to&nbsp;find&nbsp;and&nbsp;save&nbsp;the&nbsp;data&nbsp;$mydata&nbsp;=&nbsp;$_POST['parent_id'];&nbsp;return&nbsp;$mydata;&nbsp;}&nbsp;add_filter('posts_where','where_no_parent');&nbsp;add_filter&nbsp;('the_content','subpost_template',&nbsp;1,&nbsp;2&nbsp;);&nbsp;function&nbsp;subpost_template($content)&nbsp;{&nbsp;if(is_singular)&nbsp;{&nbsp;remove_filter('posts_where','where_no_parent');&nbsp;}&nbsp;echo&nbsp;$content;&nbsp;$idnya&nbsp;=&nbsp;get_the_ID();&nbsp;$child&nbsp;=&nbsp;new&nbsp;WP_Query("post_type=post&amp;amp;post_parent=".$idnya."");&nbsp;while($child-&amp;gt;have_posts())&nbsp;:&nbsp;$child-&amp;gt;the_post();&nbsp;echo&nbsp;'
<br/>&amp;lt;/select&amp;gt;&amp;lt;/pre&amp;gt;
<br/>&amp;lt;blockquote&amp;gt;';&nbsp;echo&nbsp;'
<br/>&amp;lt;h3&amp;gt;';&nbsp;the_title();&nbsp;echo&nbsp;'&amp;lt;/h3&amp;gt;
<br/>';&nbsp;$childid&nbsp;=&nbsp;get_the_ID();&nbsp;the_content();&nbsp;edit_post_link('Edit','','',$childid);&nbsp;echo&nbsp;'&amp;lt;/blockquote&amp;gt;
<br/>&amp;lt;pre&amp;gt;&amp;lt;select&nbsp;name="\"$name\""&amp;gt;';&nbsp;endwhile;&nbsp;wp_reset_query();&nbsp;}&nbsp;function&nbsp;where_no_parent($where)&nbsp;{&nbsp;global&nbsp;$wpdb;&nbsp;$where&nbsp;.=&nbsp;"&nbsp;AND&nbsp;post_parent&nbsp;=&nbsp;0";&nbsp;return&nbsp;$where;&nbsp;}&nbsp;?&amp;gt;&nbsp;</span>
</code><code><span style="color: #000000">

<br/>&amp;lt;/select&amp;gt;&amp;lt;/pre&amp;gt;
<br/>&amp;lt;pre&amp;gt;function&nbsp;subpost_template($content)&nbsp;{
<br/>
<br/>&nbsp;&nbsp;&nbsp;&nbsp;if(is_singular())&nbsp;{
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_filter('posts_where','where_no_parent');
<br/>&nbsp;&nbsp;&nbsp;&nbsp;}
<br/>
<br/>&nbsp;&nbsp;&nbsp;&nbsp;$parentID&nbsp;=&nbsp;get_the_ID();
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$childposts&nbsp;=&nbsp;get_posts(array(
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'post_type'&nbsp;=&amp;gt;&nbsp;'post',
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'numberposts'&nbsp;=&amp;gt;&nbsp;-1,
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'post_status'&nbsp;=&amp;gt;&nbsp;'publish',
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'post_parent'&nbsp;=&amp;gt;&nbsp;$parentID
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;));
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$subcontent&nbsp;=&nbsp;"";
<br/>&nbsp;&nbsp;&nbsp;&nbsp;foreach($childposts&nbsp;as&nbsp;$childpost){
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$subcontent&nbsp;.=&nbsp;"&amp;lt;/pre&amp;gt;
<br/>&amp;lt;blockquote&amp;gt;";&nbsp;$subcontent&nbsp;.=&nbsp;"
<br/>&amp;lt;h3&amp;gt;".$childpost-&amp;gt;post_title."&amp;lt;/h3&amp;gt;
<br/>";&nbsp;$subcontent&nbsp;.=&nbsp;$childpost-&amp;gt;post_content;&nbsp;$subcontent&nbsp;.=&nbsp;'&nbsp;&amp;lt;a&nbsp;href="'.get_edit_post_link($childpost-&amp;gt;ID).'"&nbsp;rel="nofollow"&amp;gt;Edit&amp;lt;/a&amp;gt;&nbsp;';&nbsp;$subcontent&nbsp;.=&nbsp;"&amp;lt;/blockquote&amp;gt;
<br/>&amp;lt;pre&amp;gt;
<br/>";
<br/>&nbsp;&nbsp;&nbsp;&nbsp;}
<br/>
<br/>&nbsp;&nbsp;&nbsp;&nbsp;$content&nbsp;.=&nbsp;$subcontent;
<br/>
<br/>&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;$content;
<br/>}&lt;/pre&gt;<br/>&lt;/div&gt;<br/>&lt;/div&gt;<br/>[php&nbsp;title="wp_dropdown_posts()"&nbsp;block="WP&nbsp;Dropdown&nbsp;Post"]&lt;/p&gt;<br/>&lt;pre&gt;global&nbsp;$post;
<br/>$currentid&nbsp;=&nbsp;$_GET['post'];
<br/>wp_dropdown_posts(array('exclude_tree'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&amp;gt;&nbsp;$currentid,
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'selected'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&amp;gt;&nbsp;$post-&amp;gt;post_parent,
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'name'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&amp;gt;&nbsp;'parent_id',
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'show_option_none'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&amp;gt;&nbsp;__('Main&nbsp;Post&nbsp;(no&nbsp;parent)'),
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'sort_column'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&amp;gt;&nbsp;'menu_order,&nbsp;post_title'));&lt;/pre&gt;<br/>&lt;p&gt;</span>
</code><p>WP Sub Post is a wordpress plugin that allow you to make your wordpress post has a parent or child post.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>Child post is a real post that has a parent.</li>
<li>Child post only displayed on it&#8217;s parent post page or when parent page is displayed.</li>
<li>Child post can not be viewed individually.</li>
<li>Child post has all possibility <strong>like a normal post</strong>, such as attachment, custom fields etc.<strong><br/>
</strong></li>
</ul>
<p><strong>Features:</strong></p>
<ul>
<li>Add/edit parent post directly from your post area.</li>
<li>No need to edit theme file.</li>
</ul>
<p><strong>Limitations:</strong></p>
<ul>
<li>No setting page</li>
<li>I don&#8217;t know about it&#8217;s compatibility.</li>
</ul>
<p><strong>Bugs:</strong></p>
<ul>
<li>Not compatible with my syntax highlight plugin 😀</li>
</ul>
<p>[block title=&#8221;Screenshot&#8221;]</p>
<p>Plugin page:</p>
<p>New/Edit post page:</p>
<p>View Single Post:</p>
<p>RSS:</p>
<p>[/block]<br/>
<strong>Code:</strong></p>
<p>Here is the code of this plugins&#8230;  Hahaha.. little bit messy</p>

<div class="bwp-syntax-toolbar">
<div class="bwp-syntax-control"><a href="javascript:;" class="bwp-syntax-source-switch" title="View Source Code"></a></div>
</div>
<div class="bwp-syntax-wrapper clearfix bwp-syntax-simple">
<table class="php">
<tbody>
<tr class="li1">
<td class="ln">
<pre class="de1">1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
</pre>
</td>
<td class="de1">
<pre class="de1"><span class="sy0">&lt;</span> ?php
<span class="coMULTI">/*</span>
<span class="coMULTI">Plugin Name: WP Sub Post</span>
<span class="coMULTI">Plugin URI: http://wordpress.org/#</span>
<span class="coMULTI">Description: You can make a post is a child of another post.</span>
<span class="coMULTI">Author: Takien</span>
<span class="coMULTI">Version: 0.1 Alpha</span>
<span class="coMULTI">Author URI: /</span>
<span class="coMULTI">*/</span>
&nbsp;
<span class="co1">////////////////////////////</span>
&nbsp;
<span class="kw2">class</span> Walker_PostDropdown <span class="kw2">extends</span> Walker <span class="br0">&#123;</span>
&nbsp;
<span class="kw2">var</span> <span class="re0">$tree_type</span> <span class="sy0">=</span> <span class="st_h">'post'</span><span class="sy0">;</span>
&nbsp;
<span class="kw2">var</span> <span class="re0">$db_fields</span> <span class="sy0">=</span> <span class="kw3">array</span> <span class="br0">&#40;</span><span class="st_h">'parent'</span> <span class="sy0">=&gt;</span> <span class="st_h">'post_parent'</span><span class="sy0">,</span> <span class="st_h">'id'</span> <span class="sy0">=&gt;</span> <span class="st_h">'ID'</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="kw2">function</span> start_el<span class="br0">&#40;</span><span class="sy0">&amp;</span><span class="re0">$output</span><span class="sy0">,</span> <span class="re0">$page</span><span class="sy0">,</span> <span class="re0">$depth</span><span class="sy0">,</span> <span class="re0">$args</span><span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="re0">$pad</span> <span class="sy0">=</span> <span class="kw3">str_repeat</span><span class="br0">&#40;</span><span class="st_h">' '</span><span class="sy0">,</span> <span class="re0">$depth</span> <span class="sy0">*</span> <span class="nu0">3</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="re0">$output</span> <span class="sy0">.=</span> <span class="st0">&quot;<span class="es1">\t</span>ID<span class="es1">\&quot;</span>&quot;</span><span class="sy0">;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="re0">$page</span><span class="sy0">-&gt;</span><span class="me1">ID</span> <span class="sy0">==</span> <span class="re0">$args</span><span class="br0">[</span><span class="st_h">'selected'</span><span class="br0">]</span> <span class="br0">&#41;</span>
<span class="re0">$output</span> <span class="sy0">.=</span> <span class="st_h">' selected=&quot;selected&quot;'</span><span class="sy0">;</span>
<span class="re0">$output</span> <span class="sy0">.=</span> <span class="st_h">'&gt;'</span><span class="sy0">;</span>
<span class="re0">$title</span> <span class="sy0">=</span> esc_html<span class="br0">&#40;</span><span class="re0">$page</span><span class="sy0">-&gt;</span><span class="me1">post_title</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="re0">$output</span> <span class="sy0">.=</span> <span class="st0">&quot;<span class="es4">$pad</span><span class="es4">$title</span>&quot;</span><span class="sy0">;</span>
<span class="re0">$output</span> <span class="sy0">.=</span> <span class="st0">&quot;<span class="es1">\n</span>&quot;</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
<span class="br0">&#125;</span>
<span class="co1">/////////////</span>
<span class="kw2">function</span> <span class="sy0">&amp;</span>wp_get_posts<span class="br0">&#40;</span><span class="re0">$args</span> <span class="sy0">=</span> <span class="st_h">''</span><span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="kw2">global</span> <span class="re0">$wpdb</span><span class="sy0">;</span>
&nbsp;
<span class="re0">$defaults</span> <span class="sy0">=</span> <span class="kw3">array</span><span class="br0">&#40;</span>
<span class="st_h">'child_of'</span> <span class="sy0">=&gt;</span> <span class="nu0">0</span><span class="sy0">,</span> <span class="st_h">'sort_order'</span> <span class="sy0">=&gt;</span> <span class="st_h">'ASC'</span><span class="sy0">,</span>
<span class="st_h">'sort_column'</span> <span class="sy0">=&gt;</span> <span class="st_h">'post_title'</span><span class="sy0">,</span> <span class="st_h">'hierarchical'</span> <span class="sy0">=&gt;</span> <span class="nu0">1</span><span class="sy0">,</span>
<span class="st_h">'exclude'</span> <span class="sy0">=&gt;</span> <span class="st_h">''</span><span class="sy0">,</span> <span class="st_h">'include'</span> <span class="sy0">=&gt;</span> <span class="st_h">''</span><span class="sy0">,</span>
<span class="st_h">'meta_key'</span> <span class="sy0">=&gt;</span> <span class="st_h">''</span><span class="sy0">,</span> <span class="st_h">'meta_value'</span> <span class="sy0">=&gt;</span> <span class="st_h">''</span><span class="sy0">,</span>
<span class="st_h">'authors'</span> <span class="sy0">=&gt;</span> <span class="st_h">''</span><span class="sy0">,</span> <span class="st_h">'parent'</span> <span class="sy0">=&gt;</span> <span class="sy0">-</span><span class="nu0">1</span><span class="sy0">,</span> <span class="st_h">'exclude_tree'</span> <span class="sy0">=&gt;</span> <span class="st_h">''</span><span class="sy0">,</span>
<span class="st_h">'number'</span> <span class="sy0">=&gt;</span> <span class="st_h">''</span><span class="sy0">,</span> <span class="st_h">'offset'</span> <span class="sy0">=&gt;</span> <span class="nu0">0</span>
<span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="re0">$r</span> <span class="sy0">=</span> wp_parse_args<span class="br0">&#40;</span> <span class="re0">$args</span><span class="sy0">,</span> <span class="re0">$defaults</span> <span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw3">extract</span><span class="br0">&#40;</span> <span class="re0">$r</span><span class="sy0">,</span> EXTR_SKIP <span class="br0">&#41;</span><span class="sy0">;</span>
<span class="re0">$number</span> <span class="sy0">=</span> <span class="br0">&#40;</span>int<span class="br0">&#41;</span> <span class="re0">$number</span><span class="sy0">;</span>
<span class="re0">$offset</span> <span class="sy0">=</span> <span class="br0">&#40;</span>int<span class="br0">&#41;</span> <span class="re0">$offset</span><span class="sy0">;</span>
&nbsp;
<span class="re0">$cache</span> <span class="sy0">=</span> <span class="kw3">array</span><span class="br0">&#40;</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="re0">$key</span> <span class="sy0">=</span> <span class="kw3">md5</span><span class="br0">&#40;</span> <span class="kw3">serialize</span><span class="br0">&#40;</span> <span class="kw3">compact</span><span class="br0">&#40;</span><span class="kw3">array_keys</span><span class="br0">&#40;</span><span class="re0">$defaults</span><span class="br0">&#41;</span><span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="re0">$cache</span> <span class="sy0">=</span> wp_cache_get<span class="br0">&#40;</span> <span class="st_h">'wp_get_posts'</span><span class="sy0">,</span> <span class="st_h">'posts'</span> <span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="kw3">is_array</span><span class="br0">&#40;</span><span class="re0">$cache</span><span class="br0">&#41;</span> <span class="sy0">&amp;&amp;</span> <span class="kw3">isset</span><span class="br0">&#40;</span> <span class="re0">$cache</span><span class="br0">[</span> <span class="re0">$key</span> <span class="br0">]</span> <span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="re0">$pages</span> <span class="sy0">=</span> apply_filters<span class="br0">&#40;</span><span class="st_h">'wp_get_posts'</span><span class="sy0">,</span> <span class="re0">$cache</span><span class="br0">[</span> <span class="re0">$key</span> <span class="br0">]</span><span class="sy0">,</span> <span class="re0">$r</span> <span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">return</span> <span class="re0">$pages</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
<span class="br0">&#125;</span>
&nbsp;
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="sy0">!</span><span class="kw3">is_array</span><span class="br0">&#40;</span><span class="re0">$cache</span><span class="br0">&#41;</span> <span class="br0">&#41;</span>
<span class="re0">$cache</span> <span class="sy0">=</span> <span class="kw3">array</span><span class="br0">&#40;</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="re0">$inclusions</span> <span class="sy0">=</span> <span class="st_h">''</span><span class="sy0">;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="sy0">!</span><span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$include</span><span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="re0">$child_of</span> <span class="sy0">=</span> <span class="nu0">0</span><span class="sy0">;</span> <span class="co1">//ignore child_of, parent, exclude, meta_key, and meta_value params if using include</span>
<span class="re0">$parent</span> <span class="sy0">=</span> <span class="sy0">-</span><span class="nu0">1</span><span class="sy0">;</span>
<span class="re0">$exclude</span> <span class="sy0">=</span> <span class="st_h">''</span><span class="sy0">;</span>
<span class="re0">$meta_key</span> <span class="sy0">=</span> <span class="st_h">''</span><span class="sy0">;</span>
<span class="re0">$meta_value</span> <span class="sy0">=</span> <span class="st_h">''</span><span class="sy0">;</span>
<span class="re0">$hierarchical</span> <span class="sy0">=</span> <span class="kw4">false</span><span class="sy0">;</span>
<span class="re0">$incpages</span> <span class="sy0">=</span> <span class="kw3">preg_split</span><span class="br0">&#40;</span><span class="st_h">'/[\s,]+/'</span><span class="sy0">,</span><span class="re0">$include</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="kw3">count</span><span class="br0">&#40;</span><span class="re0">$incpages</span><span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="kw1">foreach</span> <span class="br0">&#40;</span> <span class="re0">$incpages</span> <span class="kw1">as</span> <span class="re0">$incpage</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span><span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$inclusions</span><span class="br0">&#41;</span><span class="br0">&#41;</span>
<span class="re0">$inclusions</span> <span class="sy0">=</span> <span class="re0">$wpdb</span><span class="sy0">-&gt;</span><span class="me1">prepare</span><span class="br0">&#40;</span><span class="st_h">' AND ( ID = %d '</span><span class="sy0">,</span> <span class="re0">$incpage</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">else</span>
<span class="re0">$inclusions</span> <span class="sy0">.=</span> <span class="re0">$wpdb</span><span class="sy0">-&gt;</span><span class="me1">prepare</span><span class="br0">&#40;</span><span class="st_h">' OR ID = %d '</span><span class="sy0">,</span> <span class="re0">$incpage</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
<span class="br0">&#125;</span>
<span class="br0">&#125;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span><span class="sy0">!</span><span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$inclusions</span><span class="br0">&#41;</span><span class="br0">&#41;</span>
<span class="re0">$inclusions</span> <span class="sy0">.=</span> <span class="st_h">')'</span><span class="sy0">;</span>
&nbsp;
<span class="re0">$exclusions</span> <span class="sy0">=</span> <span class="st_h">''</span><span class="sy0">;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="sy0">!</span><span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$exclude</span><span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="re0">$expages</span> <span class="sy0">=</span> <span class="kw3">preg_split</span><span class="br0">&#40;</span><span class="st_h">'/[\s,]+/'</span><span class="sy0">,</span><span class="re0">$exclude</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="kw3">count</span><span class="br0">&#40;</span><span class="re0">$expages</span><span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="kw1">foreach</span> <span class="br0">&#40;</span> <span class="re0">$expages</span> <span class="kw1">as</span> <span class="re0">$expage</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span><span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$exclusions</span><span class="br0">&#41;</span><span class="br0">&#41;</span>
<span class="re0">$exclusions</span> <span class="sy0">=</span> <span class="re0">$wpdb</span><span class="sy0">-&gt;</span><span class="me1">prepare</span><span class="br0">&#40;</span><span class="st_h">' AND ( ID &lt;&gt; %d '</span><span class="sy0">,</span> <span class="re0">$expage</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">else</span>
<span class="re0">$exclusions</span> <span class="sy0">.=</span> <span class="re0">$wpdb</span><span class="sy0">-&gt;</span><span class="me1">prepare</span><span class="br0">&#40;</span><span class="st_h">' AND ID &lt;&gt; %d '</span><span class="sy0">,</span> <span class="re0">$expage</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
<span class="br0">&#125;</span>
<span class="br0">&#125;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span><span class="sy0">!</span><span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$exclusions</span><span class="br0">&#41;</span><span class="br0">&#41;</span>
<span class="re0">$exclusions</span> <span class="sy0">.=</span> <span class="st_h">')'</span><span class="sy0">;</span>
&nbsp;
<span class="re0">$author_query</span> <span class="sy0">=</span> <span class="st_h">''</span><span class="sy0">;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span><span class="sy0">!</span><span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$authors</span><span class="br0">&#41;</span><span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="re0">$post_authors</span> <span class="sy0">=</span> <span class="kw3">preg_split</span><span class="br0">&#40;</span><span class="st_h">'/[\s,]+/'</span><span class="sy0">,</span><span class="re0">$authors</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="kw3">count</span><span class="br0">&#40;</span><span class="re0">$post_authors</span><span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="kw1">foreach</span> <span class="br0">&#40;</span> <span class="re0">$post_authors</span> <span class="kw1">as</span> <span class="re0">$post_author</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="co1">//Do we have an author id or an author login?</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="nu0">0</span> <span class="sy0">==</span> <span class="kw3">intval</span><span class="br0">&#40;</span><span class="re0">$post_author</span><span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="re0">$post_author</span> <span class="sy0">=</span> get_userdatabylogin<span class="br0">&#40;</span><span class="re0">$post_author</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$post_author</span><span class="br0">&#41;</span> <span class="br0">&#41;</span>
<span class="kw1">continue</span><span class="sy0">;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$post_author</span><span class="sy0">-&gt;</span><span class="me1">ID</span><span class="br0">&#41;</span> <span class="br0">&#41;</span>
<span class="kw1">continue</span><span class="sy0">;</span>
<span class="re0">$post_author</span> <span class="sy0">=</span> <span class="re0">$post_author</span><span class="sy0">-&gt;</span><span class="me1">ID</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
&nbsp;
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="st_h">''</span> <span class="sy0">==</span> <span class="re0">$author_query</span> <span class="br0">&#41;</span>
<span class="re0">$author_query</span> <span class="sy0">=</span> <span class="re0">$wpdb</span><span class="sy0">-&gt;</span><span class="me1">prepare</span><span class="br0">&#40;</span><span class="st_h">' post_author = %d '</span><span class="sy0">,</span> <span class="re0">$post_author</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">else</span>
<span class="re0">$author_query</span> <span class="sy0">.=</span> <span class="re0">$wpdb</span><span class="sy0">-&gt;</span><span class="me1">prepare</span><span class="br0">&#40;</span><span class="st_h">' OR post_author = %d '</span><span class="sy0">,</span> <span class="re0">$post_author</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="st_h">''</span> <span class="sy0">!=</span> <span class="re0">$author_query</span> <span class="br0">&#41;</span>
<span class="re0">$author_query</span> <span class="sy0">=</span> <span class="st0">&quot; AND (<span class="es4">$author_query</span>)&quot;</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
<span class="br0">&#125;</span>
&nbsp;
<span class="re0">$join</span> <span class="sy0">=</span> <span class="st_h">''</span><span class="sy0">;</span>
<span class="re0">$where</span> <span class="sy0">=</span> <span class="st0">&quot;<span class="es4">$exclusions</span> <span class="es4">$inclusions</span> &quot;</span><span class="sy0">;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="sy0">!</span> <span class="kw3">empty</span><span class="br0">&#40;</span> <span class="re0">$meta_key</span> <span class="br0">&#41;</span> <span class="sy0">||</span> <span class="sy0">!</span> <span class="kw3">empty</span><span class="br0">&#40;</span> <span class="re0">$meta_value</span> <span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="re0">$join</span> <span class="sy0">=</span> <span class="st0">&quot; LEFT JOIN <span class="es4">$wpdb-&gt;postmeta</span> ON ( <span class="es4">$wpdb-&gt;posts</span>.ID = <span class="es4">$wpdb-&gt;postmeta</span>.post_id )&quot;</span><span class="sy0">;</span>
&nbsp;
<span class="co1">// meta_key and meta_value might be slashed</span>
<span class="re0">$meta_key</span> <span class="sy0">=</span> <span class="kw3">stripslashes</span><span class="br0">&#40;</span><span class="re0">$meta_key</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="re0">$meta_value</span> <span class="sy0">=</span> <span class="kw3">stripslashes</span><span class="br0">&#40;</span><span class="re0">$meta_value</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="sy0">!</span> <span class="kw3">empty</span><span class="br0">&#40;</span> <span class="re0">$meta_key</span> <span class="br0">&#41;</span> <span class="br0">&#41;</span>
<span class="re0">$where</span> <span class="sy0">.=</span> <span class="re0">$wpdb</span><span class="sy0">-&gt;</span><span class="me1">prepare</span><span class="br0">&#40;</span><span class="st0">&quot; AND <span class="es4">$wpdb-&gt;postmeta</span>.meta_key = <span class="es6">%s</span>&quot;</span><span class="sy0">,</span> <span class="re0">$meta_key</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="sy0">!</span> <span class="kw3">empty</span><span class="br0">&#40;</span> <span class="re0">$meta_value</span> <span class="br0">&#41;</span> <span class="br0">&#41;</span>
<span class="re0">$where</span> <span class="sy0">.=</span> <span class="re0">$wpdb</span><span class="sy0">-&gt;</span><span class="me1">prepare</span><span class="br0">&#40;</span><span class="st0">&quot; AND <span class="es4">$wpdb-&gt;postmeta</span>.meta_value = <span class="es6">%s</span>&quot;</span><span class="sy0">,</span> <span class="re0">$meta_value</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="br0">&#125;</span>
&nbsp;
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="re0">$parent</span> <span class="sy0">&gt;=</span> <span class="nu0">0</span> <span class="br0">&#41;</span>
<span class="re0">$where</span> <span class="sy0">.=</span> <span class="re0">$wpdb</span><span class="sy0">-&gt;</span><span class="me1">prepare</span><span class="br0">&#40;</span><span class="st_h">' AND post_parent = %d '</span><span class="sy0">,</span> <span class="re0">$parent</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="re0">$query</span> <span class="sy0">=</span> <span class="st0">&quot;SELECT * FROM <span class="es4">$wpdb-&gt;posts</span> <span class="es4">$join</span> WHERE (post_type = 'post' AND post_status = 'publish') <span class="es4">$where</span> &quot;</span><span class="sy0">;</span>
<span class="re0">$query</span> <span class="sy0">.=</span> <span class="re0">$author_query</span><span class="sy0">;</span>
<span class="re0">$query</span> <span class="sy0">.=</span> <span class="st0">&quot; ORDER BY &quot;</span> <span class="sy0">.</span> <span class="re0">$sort_column</span> <span class="sy0">.</span> <span class="st0">&quot; &quot;</span> <span class="sy0">.</span> <span class="re0">$sort_order</span> <span class="sy0">;</span>
&nbsp;
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="sy0">!</span><span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$number</span><span class="br0">&#41;</span> <span class="br0">&#41;</span>
<span class="re0">$query</span> <span class="sy0">.=</span> <span class="st_h">' LIMIT '</span> <span class="sy0">.</span> <span class="re0">$offset</span> <span class="sy0">.</span> <span class="st_h">','</span> <span class="sy0">.</span> <span class="re0">$number</span><span class="sy0">;</span>
&nbsp;
<span class="re0">$pages</span> <span class="sy0">=</span> <span class="re0">$wpdb</span><span class="sy0">-&gt;</span><span class="me1">get_results</span><span class="br0">&#40;</span><span class="re0">$query</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$pages</span><span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="re0">$pages</span> <span class="sy0">=</span> apply_filters<span class="br0">&#40;</span><span class="st_h">'wp_get_posts'</span><span class="sy0">,</span> <span class="kw3">array</span><span class="br0">&#40;</span><span class="br0">&#41;</span><span class="sy0">,</span> <span class="re0">$r</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">return</span> <span class="re0">$pages</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
&nbsp;
<span class="co1">// Sanitize before caching so it'll only get done once</span>
<span class="re0">$num_pages</span> <span class="sy0">=</span> <span class="kw3">count</span><span class="br0">&#40;</span><span class="re0">$pages</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">for</span> <span class="br0">&#40;</span><span class="re0">$i</span> <span class="sy0">=</span> <span class="nu0">0</span><span class="sy0">;</span> <span class="re0">$i</span> <span class="sy0">&lt;</span> <span class="re0">$num_pages</span><span class="sy0">;</span> <span class="re0">$i</span><span class="sy0">++</span><span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="re0">$pages</span><span class="br0">[</span><span class="re0">$i</span><span class="br0">]</span> <span class="sy0">=</span> sanitize_post<span class="br0">&#40;</span><span class="re0">$pages</span><span class="br0">[</span><span class="re0">$i</span><span class="br0">]</span><span class="sy0">,</span> <span class="st_h">'raw'</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
&nbsp;
<span class="co1">// Update cache.</span>
update_page_cache<span class="br0">&#40;</span><span class="re0">$pages</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="re0">$child_of</span> <span class="sy0">||</span> <span class="re0">$hierarchical</span> <span class="br0">&#41;</span>
<span class="re0">$pages</span> <span class="sy0">=</span> <span class="sy0">&amp;</span> get_page_children<span class="br0">&#40;</span><span class="re0">$child_of</span><span class="sy0">,</span> <span class="re0">$pages</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="sy0">!</span><span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$exclude_tree</span><span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="re0">$exclude</span> <span class="sy0">=</span> <span class="br0">&#40;</span>int<span class="br0">&#41;</span> <span class="re0">$exclude_tree</span><span class="sy0">;</span>
<span class="re0">$children</span> <span class="sy0">=</span> get_page_children<span class="br0">&#40;</span><span class="re0">$exclude</span><span class="sy0">,</span> <span class="re0">$pages</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="re0">$excludes</span> <span class="sy0">=</span> <span class="kw3">array</span><span class="br0">&#40;</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">foreach</span> <span class="br0">&#40;</span> <span class="re0">$children</span> <span class="kw1">as</span> <span class="re0">$child</span> <span class="br0">&#41;</span>
<span class="re0">$excludes</span><span class="br0">[</span><span class="br0">]</span> <span class="sy0">=</span> <span class="re0">$child</span><span class="sy0">-&gt;</span><span class="me1">ID</span><span class="sy0">;</span>
<span class="re0">$excludes</span><span class="br0">[</span><span class="br0">]</span> <span class="sy0">=</span> <span class="re0">$exclude</span><span class="sy0">;</span>
<span class="re0">$num_pages</span> <span class="sy0">=</span> <span class="kw3">count</span><span class="br0">&#40;</span><span class="re0">$pages</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">for</span> <span class="br0">&#40;</span> <span class="re0">$i</span> <span class="sy0">=</span> <span class="nu0">0</span><span class="sy0">;</span> <span class="re0">$i</span> <span class="sy0">&lt;</span> <span class="re0">$num_pages</span><span class="sy0">;</span> <span class="re0">$i</span><span class="sy0">++</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="kw3">in_array</span><span class="br0">&#40;</span><span class="re0">$pages</span><span class="br0">[</span><span class="re0">$i</span><span class="br0">]</span><span class="sy0">-&gt;</span><span class="me1">ID</span><span class="sy0">,</span> <span class="re0">$excludes</span><span class="br0">&#41;</span> <span class="br0">&#41;</span>
<span class="kw3">unset</span><span class="br0">&#40;</span><span class="re0">$pages</span><span class="br0">[</span><span class="re0">$i</span><span class="br0">]</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
<span class="br0">&#125;</span>
&nbsp;
<span class="re0">$cache</span><span class="br0">[</span> <span class="re0">$key</span> <span class="br0">]</span> <span class="sy0">=</span> <span class="re0">$pages</span><span class="sy0">;</span>
wp_cache_set<span class="br0">&#40;</span> <span class="st_h">'wp_get_posts'</span><span class="sy0">,</span> <span class="re0">$cache</span><span class="sy0">,</span> <span class="st_h">'posts'</span> <span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="re0">$pages</span> <span class="sy0">=</span> apply_filters<span class="br0">&#40;</span><span class="st_h">'wp_get_posts'</span><span class="sy0">,</span> <span class="re0">$pages</span><span class="sy0">,</span> <span class="re0">$r</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="kw1">return</span> <span class="re0">$pages</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
<span class="co1">//////////////</span>
&nbsp;
<span class="kw2">function</span> walk_post_dropdown_tree<span class="br0">&#40;</span><span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="re0">$args</span> <span class="sy0">=</span> <span class="kw3">func_get_args</span><span class="br0">&#40;</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$args</span><span class="br0">[</span><span class="nu0">2</span><span class="br0">]</span><span class="br0">[</span><span class="st_h">'walker'</span><span class="br0">]</span><span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="co1">// the user's options are the third parameter</span>
<span class="re0">$walker</span> <span class="sy0">=</span> <span class="kw2">new</span> Walker_PostDropdown<span class="sy0">;</span>
<span class="kw1">else</span>
<span class="re0">$walker</span> <span class="sy0">=</span> <span class="re0">$args</span><span class="br0">[</span><span class="nu0">2</span><span class="br0">]</span><span class="br0">[</span><span class="st_h">'walker'</span><span class="br0">]</span><span class="sy0">;</span>
&nbsp;
<span class="kw1">return</span> <span class="kw3">call_user_func_array</span><span class="br0">&#40;</span><span class="kw3">array</span><span class="br0">&#40;</span><span class="sy0">&amp;</span><span class="re0">$walker</span><span class="sy0">,</span> <span class="st_h">'walk'</span><span class="br0">&#41;</span><span class="sy0">,</span> <span class="re0">$args</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
&nbsp;
<span class="kw2">function</span> wp_dropdown_posts<span class="br0">&#40;</span><span class="re0">$args</span> <span class="sy0">=</span> <span class="st_h">''</span><span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="re0">$defaults</span> <span class="sy0">=</span> <span class="kw3">array</span><span class="br0">&#40;</span>
<span class="st_h">'depth'</span> <span class="sy0">=&gt;</span> <span class="nu0">0</span><span class="sy0">,</span> <span class="st_h">'child_of'</span> <span class="sy0">=&gt;</span> <span class="nu0">0</span><span class="sy0">,</span>
<span class="st_h">'selected'</span> <span class="sy0">=&gt;</span> <span class="nu0">0</span><span class="sy0">,</span> <span class="st_h">'echo'</span> <span class="sy0">=&gt;</span> <span class="nu0">1</span><span class="sy0">,</span>
<span class="st_h">'name'</span> <span class="sy0">=&gt;</span> <span class="st_h">'page_id'</span><span class="sy0">,</span> <span class="st_h">'show_option_none'</span> <span class="sy0">=&gt;</span> <span class="st_h">''</span><span class="sy0">,</span> <span class="st_h">'show_option_no_change'</span> <span class="sy0">=&gt;</span> <span class="st_h">''</span><span class="sy0">,</span>
<span class="st_h">'option_none_value'</span> <span class="sy0">=&gt;</span> <span class="st_h">''</span>
<span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="re0">$r</span> <span class="sy0">=</span> wp_parse_args<span class="br0">&#40;</span> <span class="re0">$args</span><span class="sy0">,</span> <span class="re0">$defaults</span> <span class="br0">&#41;</span><span class="sy0">;</span>
<span class="kw3">extract</span><span class="br0">&#40;</span> <span class="re0">$r</span><span class="sy0">,</span> EXTR_SKIP <span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="re0">$pages</span> <span class="sy0">=</span> wp_get_posts<span class="br0">&#40;</span><span class="re0">$r</span><span class="br0">&#41;</span><span class="sy0">;</span>
<span class="re0">$output</span> <span class="sy0">=</span> <span class="st_h">''</span><span class="sy0">;</span>
<span class="re0">$name</span> <span class="sy0">=</span> esc_attr<span class="br0">&#40;</span><span class="re0">$name</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="sy0">!</span> <span class="kw3">empty</span><span class="br0">&#40;</span><span class="re0">$pages</span><span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="re0">$output</span> <span class="sy0">=</span> <span class="st0">&quot;&lt;select name=&quot;</span>\<span class="st0">&quot;<span class="es4">$name</span><span class="es1">\&quot;</span>&quot;</span><span class="sy0">&gt;</span>
<span class="sy0">&lt;</span>option value<span class="sy0">=</span><span class="st0">&quot;<span class="es1">\&quot;</span>-1<span class="es1">\&quot;</span>&quot;</span><span class="sy0">&gt;</span><span class="re0">$show_option_no_change</span><span class="sy0">&lt;/</span>option<span class="sy0">&gt;</span>
<span class="sy0">&lt;</span>option value<span class="sy0">=</span><span class="st0">&quot;<span class="es1">\&quot;</span>&quot;</span><span class="st0">&quot;&gt;<span class="es4">$show_option_none</span>&lt;/option&gt;<span class="es1">\n</span>&quot;</span><span class="sy0">;</span>
<span class="sy0">&lt;/</span>select<span class="sy0">&gt;</span>
<span class="sy0">&lt;</span>select name<span class="sy0">=</span><span class="st0">&quot;<span class="es1">\&quot;</span><span class="es4">$name</span><span class="es1">\&quot;</span>&quot;</span><span class="sy0">&gt;</span><span class="br0">&#125;</span>
<span class="sy0">&lt;/</span>select<span class="sy0">&gt;</span>
&nbsp;
<span class="re0">$output</span> <span class="sy0">=</span> apply_filters<span class="br0">&#40;</span><span class="st_h">'wp_dropdown_pages'</span><span class="sy0">,</span> <span class="re0">$output</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="kw1">if</span> <span class="br0">&#40;</span> <span class="re0">$echo</span> <span class="br0">&#41;</span>
<span class="kw1">echo</span> <span class="re0">$output</span><span class="sy0">;</span>
&nbsp;
<span class="kw1">return</span> <span class="re0">$output</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
<span class="co1">/////////////////////////////</span>
&nbsp;
<span class="coMULTI">/* Use the admin_menu action to define the custom boxes */</span>
add_action<span class="br0">&#40;</span><span class="st_h">'admin_menu'</span><span class="sy0">,</span> <span class="st_h">'myplugin_add_custom_box'</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="coMULTI">/* Use the save_post action to do something with the data entered */</span>
add_action<span class="br0">&#40;</span><span class="st_h">'save_post'</span><span class="sy0">,</span> <span class="st_h">'myplugin_save_postdata'</span><span class="br0">&#41;</span><span class="sy0">;</span>
&nbsp;
<span class="coMULTI">/* Adds a custom section to the &quot;advanced&quot; Post and Page edit screens */</span>
<span class="kw2">function</span> myplugin_add_custom_box<span class="br0">&#40;</span><span class="br0">&#41;</span> <span class="br0">&#123;</span>
&nbsp;
<span class="kw1">if</span><span class="br0">&#40;</span> <span class="kw3">function_exists</span><span class="br0">&#40;</span> <span class="st_h">'add_meta_box'</span> <span class="br0">&#41;</span><span class="br0">&#41;</span> <span class="br0">&#123;</span>
add_meta_box<span class="br0">&#40;</span> <span class="st_h">'myplugin_sectionid'</span><span class="sy0">,</span> __<span class="br0">&#40;</span> <span class="st_h">'WP Sub Posts'</span><span class="sy0">,</span> <span class="st_h">'myplugin_textdomain'</span> <span class="br0">&#41;</span><span class="sy0">,</span> <span class="st_h">'myplugin_inner_custom_box'</span><span class="sy0">,</span> <span class="st_h">'post'</span><span class="sy0">,</span> <span class="st_h">'side'</span><span class="sy0">,</span><span class="st_h">'high'</span> <span class="br0">&#41;</span><span class="sy0">;</span>
<span class="co1">//add_meta_box( $id, $title, $callback, $page, $context, $priority );</span>
add_meta_box<span class="br0">&#40;</span> <span class="st_h">'myplugin_sectionid'</span><span class="sy0">,</span> __<span class="br0">&#40;</span> <span class="st_h">'WP Sub Posts'</span><span class="sy0">,</span> <span class="st_h">'myplugin_textdomain'</span> <span class="br0">&#41;</span><span class="sy0">,</span> <span class="st_h">'myplugin_inner_custom_box'</span><span class="sy0">,</span> <span class="st_h">'page'</span><span class="sy0">,</span> <span class="st_h">'advanced'</span> <span class="br0">&#41;</span><span class="sy0">;</span>
<span class="br0">&#125;</span> <span class="kw1">else</span> <span class="br0">&#123;</span>
add_action<span class="br0">&#40;</span><span class="st_h">'dbx_post_advanced'</span><span class="sy0">,</span> <span class="st_h">'myplugin_old_custom_box'</span> <span class="br0">&#41;</span><span class="sy0">;</span>
add_action<span class="br0">&#40;</span><span class="st_h">'dbx_page_advanced'</span><span class="sy0">,</span> <span class="st_h">'myplugin_old_custom_box'</span> <span class="br0">&#41;</span><span class="sy0">;</span>
<span class="br0">&#125;</span>
<span class="br0">&#125;</span>
&nbsp;
<span class="kw2">function</span> myplugin_inner_custom_box<span class="br0">&#40;</span><span class="br0">&#41;</span> <span class="br0">&#123;</span>
<span class="kw1">echo</span> <span class="st_h">'</span>
<span class="st_h">&lt;pre&gt;&lt;select name=&quot;\&quot;$name\&quot;&quot;&gt;'</span><span class="sy0">;</span> <span class="kw1">echo</span> <span class="st_h">'</span>
<span class="st_h">&lt;/select&gt;&lt;input id=&quot;myplugin_noncename&quot; name=&quot;myplugin_noncename&quot; type=&quot;hidden&quot; value=&quot;'</span> <span class="sy0">.</span>
&nbsp; &nbsp; wp_create_nonce<span class="br0">&#40;</span> plugin_basename<span class="br0">&#40;</span><span class="kw4">__FILE__</span><span class="br0">&#41;</span> <span class="br0">&#41;</span> <span class="sy0">.</span> <span class="st_h">'&quot; /&gt;&lt;select name=&quot;\&quot;$name\&quot;&quot;&gt;'</span><span class="sy0">;</span> <span class="sy1">?&gt;</span>
<span class="sy0">&lt;/</span>select<span class="sy0">&gt;&lt;/</span>pre<span class="sy0">&gt;</span>
<span class="sy0">&lt;</span>h5<span class="sy0">&gt;</span><span class="kw2">&lt;?php</span> _e<span class="br0">&#40;</span><span class="st_h">'Parent'</span><span class="br0">&#41;</span> <span class="sy1">?&gt;</span><span class="sy0">&lt;/</span>h5<span class="sy0">&gt;</span>
<span class="sy0">&lt;</span>pre<span class="sy0">&gt;&lt;</span>label <span class="kw1">for</span><span class="sy0">=</span><span class="st0">&quot;post_parent&quot;</span><span class="sy0">&gt;</span>Please select the parent of this post<span class="sy0">&lt;/</span>label<span class="sy0">&gt;&lt;</span>select name<span class="sy0">=</span><span class="st0">&quot;<span class="es1">\&quot;</span><span class="es4">$name</span><span class="es1">\&quot;</span>&quot;</span><span class="sy0">&gt;</span> <span class="kw2">&lt;?php</span> <span class="re0">$currentid</span> <span class="sy0">=</span> <span class="re0">$_GET</span><span class="br0">[</span><span class="st_h">'post'</span><span class="br0">]</span><span class="sy0">;</span> wp_dropdown_posts<span class="br0">&#40;</span><span class="kw3">array</span><span class="br0">&#40;</span><span class="st_h">'exclude_tree'</span> <span class="sy0">=&gt;</span> <span class="re0">$currentid</span><span class="sy0">,</span> <span class="st_h">'selected'</span> <span class="sy0">=&gt;</span> <span class="re0">$post</span><span class="sy0">-&gt;</span><span class="me1">post_parent</span><span class="sy0">,</span> <span class="st_h">'name'</span> <span class="sy0">=&gt;</span> <span class="st_h">'parent_id'</span><span class="sy0">,</span> <span class="st_h">'show_option_none'</span> <span class="sy0">=&gt;</span> __<span class="br0">&#40;</span><span class="st_h">'Main Post (no parent)'</span><span class="br0">&#41;</span><span class="sy0">,</span> <span class="st_h">'sort_column'</span> <span class="sy0">=&gt;</span> <span class="st_h">'menu_order, post_title'</span><span class="br0">&#41;</span><span class="br0">&#41;</span><span class="sy0">;</span> <span class="br0">&#125;</span> <span class="coMULTI">/* Prints the edit form for pre-WordPress 2.5 post/page */</span> <span class="kw2">function</span> myplugin_old_custom_box<span class="br0">&#40;</span><span class="br0">&#41;</span> <span class="br0">&#123;</span> <span class="kw1">echo</span> <span class="st_h">'</span>
<span class="st_h">&lt;/select&gt;&lt;/pre&gt;</span>
<span class="st_h">&lt;div class=&quot;dbx-b-ox-wrapper&quot;&gt;'</span> <span class="sy0">.</span> <span class="st0">&quot;<span class="es1">\n</span>&quot;</span><span class="sy0">;</span> <span class="kw1">echo</span> <span class="st_h">'</span>
<span class="st_h">&lt;fieldset id=&quot;myplugin_fieldsetid&quot; class=&quot;dbx-box&quot;&gt;'</span> <span class="sy0">.</span> <span class="st0">&quot;<span class="es1">\n</span>&quot;</span><span class="sy0">;</span> <span class="kw1">echo</span> <span class="st_h">'</span>
<span class="st_h">&lt;div class=&quot;dbx-h-andle-wrapper&quot;&gt;</span>
<span class="st_h">&lt;h3 class=&quot;dbx-handle&quot;&gt;'</span> <span class="sy0">.</span> __<span class="br0">&#40;</span> <span class="st_h">'WP Sub Posts'</span><span class="sy0">,</span> <span class="st_h">'myplugin_textdomain'</span> <span class="br0">&#41;</span> <span class="sy0">.</span> <span class="st0">&quot;&lt;/h3&gt;</span>
<span class="st0">&lt;/div&gt;</span>
<span class="st0">&quot;</span><span class="sy0">;</span> <span class="kw1">echo</span> <span class="st_h">'</span>
<span class="st_h">&lt;div class=&quot;dbx-c-ontent-wrapper&quot;&gt;</span>
<span class="st_h">&lt;div class=&quot;dbx-content&quot;&gt;'</span><span class="sy0">;</span> <span class="co1">// output editing form myplugin_inner_custom_box(); // end wrapper echo &quot;&lt;/div&gt;</span>
<span class="sy0">&lt;/</span>div<span class="sy0">&gt;&lt;/</span>fieldset<span class="sy0">&gt;</span>
<span class="sy0">&lt;/</span>div<span class="sy0">&gt;</span>
<span class="sy0">&lt;</span>pre<span class="sy0">&gt;&lt;</span>select name<span class="sy0">=</span><span class="st0">&quot;<span class="es1">\&quot;</span><span class="es4">$name</span><span class="es1">\&quot;</span>&quot;</span><span class="sy0">&gt;</span>\n<span class="st0">&quot;; } /* When the post is saved, saves our custom data */ function myplugin_save_postdata( <span class="es4">$post_id</span> ) { // verify this came from the our screen and with proper authorization, // because save_post can be triggered at other times if ( !wp_verify_nonce( <span class="es4">$_POST</span>['myplugin_noncename'], plugin_basename(__FILE__) )) { return <span class="es4">$post_id</span>; } // verify if this is an auto save routine. If it is our form has not been submitted, so we dont want // to do anything if ( defined('DOING_AUTOSAVE') &amp;&amp; DOING_AUTOSAVE ) return <span class="es4">$post_id</span>; // Check permissions if ( 'page' == <span class="es4">$_POST</span>['post_type'] ) { if ( !current_user_can( 'edit_page', <span class="es4">$post_id</span> ) ) return <span class="es4">$post_id</span>; } else { if ( !current_user_can( 'edit_post', <span class="es4">$post_id</span> ) ) return <span class="es4">$post_id</span>; } // OK, we're authenticated: we need to find and save the data <span class="es4">$mydata</span> = <span class="es4">$_POST</span>['parent_id']; return <span class="es4">$mydata</span>; } add_filter('posts_where','where_no_parent'); add_filter ('the_content','subpost_template', 1, 2 ); function subpost_template(<span class="es4">$content</span>) { if(is_singular) { remove_filter('posts_where','where_no_parent'); } echo <span class="es4">$content</span>; <span class="es4">$idnya</span> = get_the_ID(); <span class="es4">$child</span> = new WP_Query(&quot;</span>post_type<span class="sy0">=</span>post<span class="sy0">&amp;</span>post_parent<span class="sy0">=</span><span class="st0">&quot;.<span class="es4">$idnya</span>.&quot;</span><span class="st0">&quot;); while(<span class="es4">$child-&gt;have_posts</span>()) : <span class="es4">$child-&gt;the_post</span>(); echo '</span>
<span class="st0">&lt;/select&gt;&lt;/pre&gt;</span>
<span class="st0">&lt;blockquote&gt;'; echo '</span>
<span class="st0">&lt;h3&gt;'; the_title(); echo '&lt;/h3&gt;</span>
<span class="st0">'; <span class="es4">$childid</span> = get_the_ID(); the_content(); edit_post_link('Edit','','',<span class="es4">$childid</span>); echo '&lt;/blockquote&gt;</span>
<span class="st0">&lt;pre&gt;&lt;select name=&quot;</span>\<span class="st0">&quot;<span class="es4">$name</span><span class="es1">\&quot;</span>&quot;</span><span class="sy0">&gt;</span><span class="st_h">'; endwhile; wp_reset_query(); } function where_no_parent($where) { global $wpdb; $where .= &quot; AND post_parent = 0&quot;; return $where; } ?&gt; [/php]</span>
<span class="st_h">&lt;/select&gt;&lt;strong&gt; Revision by &lt;a href=&quot;http://www.kaskus.us/member.php?u=1202930&quot;&gt;polvocdo&lt;/a&gt;&lt;/strong&gt;&lt;select id=&quot;\&quot;$name\&quot;&quot; name=&quot;\&quot;$name\&quot;&quot;&gt; 1
&lt;/select&gt;&lt;strong&gt; Revision by &lt;a href="http://www.kaskus.us/member.php?u=1202930"&gt;polvocdo&lt;/a&gt;&lt;/strong&gt;&lt;select id="\"$name\"" name="\"$name\""&gt; 1
<div class="panel panel-warning"><div class="panel-heading"><h3 class="panel-title">Download</h3></div><div class="panel-content" style="padding:5px 10px">You can download alpha version of this plugin here <a href="/wp-content/plugins/wp-sub-post.zip">Click here </a></div></div>
<div class="panel panel-warning">This plugin is Alpha version, use it for testing purpose only. Any problem caused by this plugin is not my responsibility.<br/>
</div>
<p><strong>Demo: </strong></p>
<p>See below:</p>
<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/child-post/">child post</a> <a class="label label-default" href="/tag/php/">PHP</a> <a class="label label-default" href="/tag/wp-plugins/">Plugins</a> <a class="label label-default" href="/tag/wordpress-plugins/">wordpress plugins</a> <a class="label label-default" href="/tag/wordpress-sub-post/">wordpress sub post</a> </div>										
									</div>
