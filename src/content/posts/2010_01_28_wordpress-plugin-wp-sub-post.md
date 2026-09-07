---
title: "WordPress Plugin WP Sub Post"
date: "2010-01-28T21:08:00.000Z"
categories: ["Plugins"]
tags: ["PHP","Plugins","child post","wordpress plugins","wordpress sub post"]
slug: "2010/01/28/wordpress-plugin-wp-sub-post"
legacyUrl: "/2010/01/28/wordpress-plugin-wp-sub-post/"
source: "takien.com"
author: "takien"
comments: [{"author":"aagun2006","date":"","text":"bagus bang nih,cocok buat situs berita.\nLanjutkan, walau sudah 100 hari berlalu …\nLAnjutkan …"},{"author":"uwiuw","date":"","text":"wah, keren euy. ide plugin yg keren dan kalau udah stabil bakal killer. Pasti banyak yang akan butuh untuk mindahkan ke kanan dan kekiri post child mereka."},{"author":"takien","date":"","text":"hehe maskasih mas uwiuw,\nmudah2an ada waktu untuk ngutak-atik lagi :)"},{"author":"bugtracker","date":"","text":"Child post can not be viewed individually.?? I still can see it individually. A bug maybe."},{"author":"takien","date":"","text":"sorry.. the code is still confusing me.. :D"},{"author":"uwiuw","date":"","text":"udah di tes untuk 3.0 ?"},{"author":"takien","date":"","text":"udah bro, no problemo :)"},{"author":"Shelly","date":"","text":"This is a great idea – however, I have it installed on WordPress 3.0. When you give a post a “parent,” the post itself disappears from the list of posts (in the admin area, under “Posts>Posts”) to be edited or deleted in the future. So far, the only way I’ve found to get to a child post to be edited is to view the source code of the parent post editing screen, find the child page in the dropdown (the value is the post ID) and change the post ID in the “edit” screen to the child’s value that I found by viewing the source code.\n\nI’ve managed ot mess with the plugin a bit to add a secondary section in the parent page to show a list of that posts’ children, but that’s all it does. So far, I can’t get it to *ink* to the actual child page so if you select it, it’ll move to that child page’s edit screen.\n\nI know this is in alpha, but I thought I’d let you know."},{"author":"Neyah","date":"","text":"Hi,\nhave you found any solution for displaying sub posts in the admin area?"},{"author":"Morten","date":"","text":"I just installed the plugin on a new pages, plugin seam to work with out any problem, i although have the following questions.\n\n1. is there any way to awoid that pictures overlap the next sub post, this seams to happen if you dont have enoug text in the sub post. (like with your monkey picture above)\n\nMorten"},{"author":"takien","date":"","text":"Thanks Morten,\nI think your problem is only about CSS."},{"author":"Morten","date":"","text":"Ok, then i will see if i can find some help solving that issue (:"},{"author":"takien","date":"","text":"please give me your links here"},{"author":"Morten","date":"","text":"Hi Takien,\n\ni solved it by making sure i have enought text which is ok solution for me now, i am quite happy with the result here http://www.medulin-croatia.com/apartments-accommodation-for-4-6-persons-medulin/\n\nOne improvment could be not having to forward the subpost to the main post, the sub post occur in related post and gives a 404 if you havent redirected them.\n\nMorten"},{"author":"takien","date":"","text":"Actually i have fix this problem and updated my code.\n\nPlease refer to my sub post above Code Update WP Sub Post\n\nto to make sub post redirected to the parent post, please edit this line\n\nThis post is a child post of ‘.get_the_title($post->post_parent).’. To view the parent post, please click here.\n\nand replace with your own Redirection code (e.g. HTML redirection)"},{"author":"takien","date":"","text":"BTW, your site is nice :)"},{"author":"Morten","date":"","text":"Thanks, i will try to fix it\n\nMorten"},{"author":"Morten","date":"","text":"Takien, i discovered another bug, when i have the plugin activated like on this page http://www.pula-croatia.com/usefull-stuff/croatias-top-holiday-destinations/ the subpages gives a 404, do you know why that happens?\n\nMorten"},{"author":"takien","date":"","text":"Have you patched the code?"},{"author":"Morten","date":"","text":"yes i patched the code on my page http://www.medulin-croatia.com/ but the SUBPAGES still get 404, any idea how to fix?\n\nYou mention i should replace some code with my redirection code, could you specify that with an exsample?\n\nMorten"},{"author":"Shelly","date":"","text":"I can verify this – when I activate the plugin on WordPress 3.0.1, in my backend Pages section, any subpages that I have are gone from the list. The parent page is fine, but child pages do not show at all. On the front end of the site, trying to access child pages sends me to a 404 page. I cannot query them either (to create a menu list – the query returns as empty.) If I deactivate the plugin, the child pages show up on the front end, and in the list on the back end, and I can query just fine."},{"author":"Shelly","date":"","text":"If it helps, I’ve managed to find *here* the problem is, but I haven’t found a solution yet. It’s in the where_no_parent() function."},{"author":"mervandi","date":"","text":"hi, i got the same problem when trying to implement this sub post plugin..\ni could not open the sub-post directly, it returns to 404..\n\nany body fix this..?\n\nbtw: really nice plugin..\n\ntetep semangat Bro..!!"},{"author":"Fabian","date":"","text":"Hi,\n\nthanks a lot for the great plugin! I can confirm the same error as the posters before me.\n\nIndependently of that, I was wondering how to change your code in order to get the following results (I’m not very firm with php or WP):\n\n1. The child inherits the categories (and perhaps also the title) from the parent, at least as a preset in the edit form.\n2. The output of potential parents in the drop down menu is limited to top-level parents (i.e., all without parents themselves), or to some other level.\n\nAny suggestions?\n\nThanks!\n\nFabian"},{"author":"Marina","date":"","text":"Wow, very nice work..\nI’ve installed it and it’s working smoothly (haven’t found any bug).\n\nBut just a question:\nI’ve chosen a category for a child post, but somehow when I clicked the category from the homepage, the child post isn’t there on the list of posts of that category. Do you know how to solve this problem?\n\nThanks a lot!\nKeep up the good work\n\nM"},{"author":"takien","date":"","text":"the idea of this plugin is not as you expected.\nof course it can’t be viewed on it’s own category because there’s no parents there. but if you want to do, just look at where_no_parent functions, and edit as you need.\n\nas this plugin is still experimental, all your comments are very appreciated for the future stable release."},{"author":"Marina","date":"","text":"Another thing is that I hope to have the actual child post on the bottom, and the older child post on top of it…. Do you know how to change this?"},{"author":"takien","date":"","text":"You want to reorder the child post? yes you can.\n\nGo to this this code.\n$childposts = get_posts(array(\n'post_type' => 'post',\n'numberposts' => -1,\n'post_status' => 'publish',\n'post_parent' => $parentID\n));\n\nthen add order parameter, like this:\n$childposts = get_posts(array(\n'post_type' => 'post',\n'numberposts' => -1,\n'post_status' => 'publish',\n'orderby' => 'post_date',\n'order' => 'ASC',\n'post_parent' => $parentID\n));"},{"author":"Marina","date":"","text":"Oh.. wonderful!!\n\nI edit it as you wrote and it works perfectly! :) It’s really a superb plugin.\n\nBy the way, since i’m really a beginner in php (or lets say, dont know anything about it), do you know what to paste in the where_no_parent post for category? since every child post has its own URL, it should all generally possible isn’t it?\n\nThank you very much again!!"},{"author":"tom","date":"","text":"Hi, i installed the plugin and it works great, except the fact that its harder to edit your sub posts and they dont show up in the admin panel … …. i really like how morten styled his subposts and was wondering if you can tell me how to style …… i have no php background so i cant really find where to insert the style codes (background color, border, etc) in this plugin\n\nalso, how can you make the title of the subpost a link to the subpost (so you can view it individually)\n\nThanks"},{"author":"takien","date":"","text":"Hello tom,\nthank you for using my plugin and give a feedback.\nI’m so sorry I’m not have much time to maintenance this plugin, I’m not promising but i will try keep the plugin is useful to everyone."},{"author":"Arnon Rodrigues","date":"","text":"Hello, isn’t it possible to make posts like this:\n\nhttp://www.example.com/post/subpost\n\nIn this case, the subpost can be viewed like a singular post, changing only the url.\n\nThanks a lot!\n\n;)"},{"author":"takien","date":"","text":"I don’t think that is possible because i did not explore the wordpress rewrite function yet. thank you"},{"author":"Pearl","date":"","text":"I can’t seem to install this. Is there any update to this?"},{"author":"Anonymous","date":"","text":"sorry there’s currently no update for this plugins.\nbtw is there any error message or something break/ blank etc?\nthanks."},{"author":"Pearl","date":"","text":"Managed to upload it manually. Thanks."},{"author":"Pearl","date":"","text":"May I know what’s the block quote class for the sub-post?"},{"author":"Anonymous","date":"","text":"it has class .sub_post"},{"author":"Pearl","date":"","text":"Thank you. I really do appreciate this plugin. Can I also ask if it is possible to put a user photo per post or custom fields per post?"},{"author":"Pearl","date":"","text":"Okay. I figured the last one out. Query again: Is it possible to include the user/author in the child post and put the user’s photo with it?"},{"author":"Anonymous","date":"","text":"try this to retrieve user/author avatar.\necho get_avatar( get_the_author_meta(‘user_email’), 80 );"},{"author":"Pearl","date":"","text":"where shall i put the echo get_avatar ?"},{"author":"Anonymous","date":"","text":"See my next comment"},{"author":"Pearl","date":"","text":"I’m confused now. because when i placed it in side the code it just got the avatar of the parent author and not the child author. it was also above the “block quoted sub post.” i wanted it to be inside the block quote post and the sub post user author’s photo."},{"author":"Anonymous","date":"","text":"hello Pearl,\ndid you read this comment?\nhttp://takien.com/550/wordpress-plugin-wp-sub-post.php#comment-395530357"},{"author":"Anonymous","date":"","text":"To do, you must edit the plugins at this line:\n$content = $parent_info.$content;\n\nshould be replaced with:\n$avatar = ”;\n$content = $parent_info.$content.$avatar;\n\nreference about the_author_meta can be found here:\nhttp://codex.wordpress.org/Template_Tags/the_author_meta"},{"author":"Pearl","date":"","text":"Hi, Yes. I read this. But it doesn’t seem to work still. I replaced it already. Really sorry for the hassle. I appreciate the support."},{"author":"Anonymous","date":"","text":"After discovering the documentation of get_the_author_meta, it seems to pass the child author ID, otherwise it shows the info of the current loop (parent post)\n\nWorth to try:\n$avatar = ‘post_author), 80 ).’”>’;\n$content = $parent_info.$content.$avatar;\n\nNo problem, I’m glad I could help :)\n\nOops, replace & gt; with > ( ‘greater than’ sign)"},{"author":"Pearl","date":"","text":"Where will I put this: try this to retrieve user/author avatar.\necho get_avatar( get_the_author_meta(‘user_email’), 80 ); ?"},{"author":"Anonymous","date":"","text":"this one shouldn’t be used"},{"author":"Pearl","date":"","text":"Does that mean it will look like: get_the_author_meta(‘user_email’,$post->post_author), 80 ).’”>’;"},{"author":"Pearl","date":"","text":"Sigh. It’s still not working. :("}]
---

<p>WP Sub Post is a wordpress plugin that allow you to make your wordpress post has a parent or child post.</p>

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

Screenshots:

<p>Plugin page:</p>



![wp-sub-post](/images/uploads/1788782462022_wp-sub-post.png)




<p>New/Edit post page:</p>
<p>View Single Post:</p>
<p>RSS:</p>



<strong>Code:</strong></p>
<p>Here is the code of this plugins&#8230;  Hahaha.. little bit messy</p>

```
<?php 
/*
Plugin Name: WP Sub Post
Plugin URI: http://wordpress.org/#
Description: You can make a post is a child of another post.
Author: Takien
Version: 0.1 Alpha
Author URI: http://takien.com
*/

////////////////////////////

class Walker_PostDropdown extends Walker {
	/**
	 * @see Walker::$tree_type
	 * @since 2.1.0
	 * @var string
	 */
	var $tree_type = 'post';

	/**
	 * @see Walker::$db_fields
	 * @since 2.1.0
	 * @todo Decouple this
	 * @var array
	 */
	var $db_fields = array ('parent' => 'post_parent', 'id' => 'ID');

	/**
	 * @see Walker::start_el()
	 * @since 2.1.0
	 *
	 * @param string $output Passed by reference. Used to append additional content.
	 * @param object $page Page data object.
	 * @param int $depth Depth of page in reference to parent pages. Used for padding.
	 * @param array $args Uses 'selected' argument for selected page to set selected HTML attribute for option element.
	 */
	function start_el(&$output, $page, $depth, $args) {
		$pad = str_repeat('&nbsp;', $depth * 3);

		$output .= "\t<option class=\"level-$depth\" value=\"$page->ID\"";
		if ( $page->ID == $args['selected'] )
			$output .= ' selected="selected"';
		$output .= '>';
		$title = esc_html($page->post_title);
		$output .= "$pad$title";
		$output .= "</option>\n";
	}
}
/////////////
function &wp_get_posts($args = '') {
	global $wpdb;

	$defaults = array(
		'child_of' => 0, 'sort_order' => 'ASC',
		'sort_column' => 'post_title', 'hierarchical' => 1,
		'exclude' => '', 'include' => '',
		'meta_key' => '', 'meta_value' => '',
		'authors' => '', 'parent' => -1, 'exclude_tree' => '',
		'number' => '', 'offset' => 0,
		'cat' => ''
	);

	$r = wp_parse_args( $args, $defaults );
	extract( $r, EXTR_SKIP );
	$number = (int) $number;
	$offset = (int) $offset;

	$cache = array();
	$key = md5( serialize( compact(array_keys($defaults)) ) );
	if ( $cache = wp_cache_get( 'wp_get_posts', 'posts' ) ) {
		if ( is_array($cache) && isset( $cache[ $key ] ) ) {
			$pages = apply_filters('wp_get_posts', $cache[ $key ], $r );
			return $pages;
		}
	}

	if ( !is_array($cache) )
		$cache = array();

	$inclusions = '';
	if ( !empty($include) ) {
		$child_of = 0; //ignore child_of, parent, exclude, meta_key, and meta_value params if using include
		$parent = -1;
		$exclude = '';
		$meta_key = '';
		$meta_value = '';
		$hierarchical = false;
		$incpages = preg_split('/[\s,]+/',$include);
		if ( count($incpages) ) {
			foreach ( $incpages as $incpage ) {
				if (empty($inclusions))
					$inclusions = $wpdb->prepare(' AND ( ID = %d ', $incpage);
				else
					$inclusions .= $wpdb->prepare(' OR ID = %d ', $incpage);
			}
		}
	}
	if (!empty($inclusions))
		$inclusions .= ')';

	$exclusions = '';
	if ( !empty($exclude) ) {
		$expages = preg_split('/[\s,]+/',$exclude);
		if ( count($expages) ) {
			foreach ( $expages as $expage ) {
				if (empty($exclusions))
					$exclusions = $wpdb->prepare(' AND ( ID <> %d ', $expage);
				else
					$exclusions .= $wpdb->prepare(' AND ID <> %d ', $expage);
			}
		}
	}
	if (!empty($exclusions))
		$exclusions .= ')';

	$author_query = '';
	if (!empty($authors)) {
		$post_authors = preg_split('/[\s,]+/',$authors);

		if ( count($post_authors) ) {
			foreach ( $post_authors as $post_author ) {
				//Do we have an author id or an author login?
				if ( 0 == intval($post_author) ) {
					$post_author = get_userdatabylogin($post_author);
					if ( empty($post_author) )
						continue;
					if ( empty($post_author->ID) )
						continue;
					$post_author = $post_author->ID;
				}

				if ( '' == $author_query )
					$author_query = $wpdb->prepare(' post_author = %d ', $post_author);
				else
					$author_query .= $wpdb->prepare(' OR post_author = %d ', $post_author);
			}
			if ( '' != $author_query )
				$author_query = " AND ($author_query)";
		}
	}

	$join = '';
	$where = "$exclusions $inclusions ";
	if ( ! empty( $meta_key ) || ! empty( $meta_value ) ) {
		$join = " LEFT JOIN $wpdb->postmeta ON ( $wpdb->posts.ID = $wpdb->postmeta.post_id )";

		// meta_key and meta_value might be slashed
		$meta_key = stripslashes($meta_key);
		$meta_value = stripslashes($meta_value);
		if ( ! empty( $meta_key ) )
			$where .= $wpdb->prepare(" AND $wpdb->postmeta.meta_key = %s", $meta_key);
		if ( ! empty( $meta_value ) )
			$where .= $wpdb->prepare(" AND $wpdb->postmeta.meta_value = %s", $meta_value);

	}

	if ( $parent >= 0 )
		$where .= $wpdb->prepare(' AND post_parent = %d ', $parent);

	$query = "SELECT * FROM $wpdb->posts $join WHERE (post_type = 'post' AND post_status = 'publish') $where ";
	$query .= $author_query;
	$query .= " ORDER BY " . $sort_column . " " . $sort_order ;

	if ( !empty($number) )
		$query .= ' LIMIT ' . $offset . ',' . $number;

	$pages = $wpdb->get_results($query);

	if ( empty($pages) ) {
		$pages = apply_filters('wp_get_posts', array(), $r);
		return $pages;
	}

	// Sanitize before caching so it'll only get done once
	$num_pages = count($pages);
	for ($i = 0; $i < $num_pages; $i++) {
		$pages[$i] = sanitize_post($pages[$i], 'raw');
	}

	// Update cache.
	update_page_cache($pages);

	if ( $child_of || $hierarchical )
		$pages = & get_page_children($child_of, $pages);

	if ( !empty($exclude_tree) ) {
		$exclude = (int) $exclude_tree;
		$children = get_page_children($exclude, $pages);
		$excludes = array();
		foreach ( $children as $child )
			$excludes[] = $child->ID;
		$excludes[] = $exclude;
		$num_pages = count($pages);
		for ( $i = 0; $i < $num_pages; $i++ ) {
			if ( in_array($pages[$i]->ID, $excludes) )
				unset($pages[$i]);
		}
	}

	$cache[ $key ] = $pages;
	wp_cache_set( 'wp_get_posts', $cache, 'posts' );

	$pages = apply_filters('wp_get_posts', $pages, $r);

	return $pages;
}
//////////////

function walk_post_dropdown_tree() {
	$args = func_get_args();
	if ( empty($args[2]['walker']) ) // the user's options are the third parameter
		$walker = new Walker_PostDropdown;
	else
		$walker = $args[2]['walker'];

	return call_user_func_array(array(&$walker, 'walk'), $args);
}

function wp_dropdown_posts($args = '') {
	$defaults = array(
		'depth' => 0, 'child_of' => 0,
		'selected' => 0, 'echo' => 1,
		'name' => 'page_id', 'show_option_none' => '', 'show_option_no_change' => '',
		'option_none_value' => ''
	);

	$r = wp_parse_args( $args, $defaults );
	extract( $r, EXTR_SKIP );

	$pages = wp_get_posts($r);
	$output = '';
	$name = esc_attr($name);

	if ( ! empty($pages) ) {
		$output = "<select name=\"$name\" id=\"$name\">\n";
		if ( $show_option_no_change )
			$output .= "\t<option value=\"-1\">$show_option_no_change</option>";
		if ( $show_option_none )
			$output .= "\t<option value=\"" . esc_attr($option_none_value) . "\">$show_option_none</option>\n";
		$output .= walk_post_dropdown_tree($pages, $depth, $r);
		$output .= "</select>\n";
	}

	$output = apply_filters('wp_dropdown_pages', $output);

	if ( $echo )
		echo $output;

	return $output;
}
/////////////////////////////





/* Use the admin_menu action to define the custom boxes */
add_action('admin_menu', 'myplugin_add_custom_box');

/* Use the save_post action to do something with the data entered */
add_action('save_post', 'myplugin_save_postdata');



/* Adds a custom section to the "advanced" Post and Page edit screens */
function myplugin_add_custom_box() {

  if( function_exists( 'add_meta_box' )) {
    add_meta_box( 'myplugin_sectionid', __( 'WP Sub Posts', 'myplugin_textdomain' ), 'myplugin_inner_custom_box', 'post', 'side','high' );
	//add_meta_box( $id,                  $title,                                      $callback,                  $page, $context, $priority ); 
    add_meta_box( 'myplugin_sectionid', __( 'WP Sub Posts', 'myplugin_textdomain' ), 'myplugin_inner_custom_box', 'page', 'advanced' );
   } else {
    add_action('dbx_post_advanced', 'myplugin_old_custom_box' );
    add_action('dbx_page_advanced', 'myplugin_old_custom_box' );
  }
}
   

function myplugin_inner_custom_box() {

echo '<style type="text/css">
select#parent_id, select#parent_id option {
	width:250px;
}
</style>';

 echo '<input type="hidden" name="myplugin_noncename" id="myplugin_noncename" value="' . 
    wp_create_nonce( plugin_basename(__FILE__) ) . '" />';  ?>
	
	<h5><?php _e('Parent') ?></h5>
	
<p><label for="post_parent">Please select the parent of this post</label></p>

  
<?php
global $post; 
$currentid = $_GET['post'];
wp_dropdown_posts(array('exclude_tree' 			=> $currentid, 
							'selected' 			=> $post->post_parent, 
							'name' 				=> 'parent_id', 
							'show_option_none' 	=> __('Main Post (no parent)'), 
							'sort_column'		=> 'menu_order, post_title'));
 }

/* Prints the edit form for pre-WordPress 2.5 post/page */
function myplugin_old_custom_box() {

  echo '<div class="dbx-b-ox-wrapper">' . "\n";
  echo '<fieldset id="myplugin_fieldsetid" class="dbx-box">' . "\n";
  echo '<div class="dbx-h-andle-wrapper"><h3 class="dbx-handle">' . 
        __( 'WP Sub Posts', 'myplugin_textdomain' ) . "</h3></div>";   
   
  echo '<div class="dbx-c-ontent-wrapper"><div class="dbx-content">';

  // output editing form

  myplugin_inner_custom_box();

  // end wrapper

  echo "</div></div></fieldset></div>\n";
}

/* When the post is saved, saves our custom data */
function myplugin_save_postdata( $post_id ) {

  // verify this came from the our screen and with proper authorization,
  // because save_post can be triggered at other times

  if ( !wp_verify_nonce( $_POST['myplugin_noncename'], plugin_basename(__FILE__) )) {
    return $post_id;
  }

  // verify if this is an auto save routine. If it is our form has not been submitted, so we dont want
  // to do anything
  if ( defined('DOING_AUTOSAVE') && DOING_AUTOSAVE ) 
    return $post_id;

  
  // Check permissions
  if ( 'page' == $_POST['post_type'] ) {
    if ( !current_user_can( 'edit_page', $post_id ) )
      return $post_id;
  } else {
    if ( !current_user_can( 'edit_post', $post_id ) )
      return $post_id;
  }

  // OK, we're authenticated: we need to find and save the data

  $mydata = $_POST['parent_id'];

   return $mydata;
}

function filtercontentprior(){

    $all_plugins = get_plugins();

    foreach ( (array)$all_plugins as $plugin_file => $plugin_data) {

    //Translate, Apply Markup, Sanitize HTML
    $plugin_data = _get_plugin_data_markup_translate($plugin_file, $plugin_data, false, true);
    $all_plugins[ $plugin_file ] = $plugin_data;

    //Filter into individual sections
        if ( is_plugin_active($plugin_file) ) {
            $active_plugins[ $plugin_file ] = $plugin_data;
        }
    }
    $total_active_plugins = count($active_plugins);
    return $total_active_plugins+1;
} 


add_filter('posts_where','where_no_parent'); 
add_filter('the_content','subpost_template', 0, 2 ); 
add_action('wp_print_scripts', 'disable_autosave');


function disable_autosave() {
wp_deregister_script('autosave');
}



function subpost_template($content) {
global $post;

$parentID = get_the_ID(); 
       $childposts = get_posts(array(
                                'post_type' => 'post',
                                'numberposts' => -1,
                                'post_status' => 'publish',
                                'post_parent' => $parentID 
                                ));
      $subcontent = "";
    foreach($childposts as $childpost){
        $subcontent .= "<blockquote class=\"sub_post\" id=\"subpost_".$childpost->ID."\">";
        $subcontent .= "<h3>".$childpost->post_title."</h3>";
        $subcontent .= $childpost->post_content;
        $subcontent .= '<p class="postmetadata"><small>This sub post was added on: '.date('l, dS F, Y',strtotime($childpost->post_date)).' <a href="'.get_edit_post_link($childpost->ID).'" rel="nofollow">Edit</a></small></p>';
        $subcontent .= "</blockquote>";
    }
    
        if($post->post_parent !== 0) {
        
        $parent_info = '<blockquote>This post is a child post of <strong>'.get_the_title($post->post_parent).'</strong>. To view the parent post, please <a href="'.get_permalink($post->post_parent).'">click here.</a></blockquote>';
        $content = $parent_info.$content;
        }
    
    $content .= $subcontent;
    return $content;
}

function where_no_parent($where) {
	global $wpdb;
	if(!is_single()) {
	 $where .= " AND post_parent  = 0";
	}
	else {
	$where .= " AND post_type = 'post'";
	}
	return $where;
}
?>
```

Revision by **polvocdo**
*subpost_template()*

```
function subpost_template($content) {

    if(is_singular()) {
        remove_filter('posts_where','where_no_parent');
    }

    $parentID = get_the_ID();
       $childposts = get_posts(array(
                                'post_type' => 'post',
                                'numberposts' => -1,
                                'post_status' => 'publish',
                                'post_parent' => $parentID
                                ));
      $subcontent = "";
    foreach($childposts as $childpost){
        $subcontent .= "

<blockquote>

";
        $subcontent .= "

<h3>".$childpost->post_title."</h3>


";
        $subcontent .= $childpost->post_content;
        $subcontent .= '

<a rel="nofollow" href="'.get_edit_post_link($childpost->ID).'">Edit</a>

';
        $subcontent .= "</blockquote>


";
    }

    $content .= $subcontent;

    return $content;
} 
```

**WP Dropdown Post**

*wp_dropdown_posts()*

```
global $post;
$currentid = $_GET['post'];
wp_dropdown_posts(array('exclude_tree'             => $currentid,
                            'selected'             => $post->post_parent,
                            'name'                 => 'parent_id',
                            'show_option_none'     => __('Main Post (no parent)'),
                            'sort_column'        => 'menu_order, post_title')); 
```


<div class="information" style="overflow: visible; position: relative; width: 100%;"><div class="box-title">Download</div><div class="box-content" style="background: rgb(239, 239, 239);">You can download alpha version of this plugin here: <a href="http://web.archive.org/web/20120107145543/http://takien.com/wp-content/plugins/wp-sub-post.zip">Click here </a></div></div>


### Warning



This plugin is **Alpha** version, use it for testing purpose only. Any problem caused by this plugin is not my responsibility.

Demo:

See below:



### Code Update WP Sub Post



**There are some changes to the WP Sub Post:**

- Fixed/Added, now child post can be viewed as a single post, with link to the Parent Post instead of displaying blank post with 'Post not found' title.
- Added, CSS class and id to the blockquote of the child post. It would be useful to make a link like http://example.com/parentpost.html#childpostXXX. while XXX is your child post ID.
- Two functions that are changed subpost_template() and where_no_parent()

```
function subpost_template($content) {
global $post;

$parentID = get_the_ID(); 
       $childposts = get_posts(array(
                                'post_type' => 'post',
                                'numberposts' => -1,
                                'post_status' => 'publish',
                                'post_parent' => $parentID 
                                ));
      $subcontent = "";
    foreach($childposts as $childpost){
        $subcontent .= "<blockquote class=\"sub_post\" id=\"subpost_".$childpost->ID."\">";
        $subcontent .= "<h3>".$childpost->post_title."</h3>";
        $subcontent .= $childpost->post_content;
        $subcontent .= '<p class="postmetadata"><small>This sub post was added on: '.date('l, dS F, Y',strtotime($childpost->post_date)).' <a href="'.get_edit_post_link($childpost->ID).'" rel="nofollow">Edit</a></small></p>';
        $subcontent .= "</blockquote>";
    }
    
        if($post->post_parent !== 0) {
        
        $parent_info = '<blockquote>This post is a child post of <strong>'.get_the_title($post->post_parent).'</strong>. To view the parent post, please <a href="'.get_permalink($post->post_parent).'">click here.</a></blockquote>';
        $content = $parent_info.$content;
        }
    
    $content .= $subcontent;
    return $content;
}

function where_no_parent($where) {
    global $wpdb;
    if(!is_single()) {
     $where .= " AND post_parent  = 0";
    }
    else {
    $where .= " AND post_type = 'post'";
    }
    return $where;
} 
```

**Finally you can see the demo here**

<blockquote>
    This sub post was added on: Tuesday, 09th February, 2010



Yesterday, I was failed to add a demo directly in this site because of incompatibility with smart tags (all smart tags are not working when WP Sub Post is activated).

The problem comes from my old stupid function subpost_template():D

Thanks and sorry to polvocdo :) , actually your revision is the answer.
Ha ha I'm forget to replace mine with your revision  :hammer: ....
</blockquote>



<blockquote>
This sub post was added on: Friday, 29th January, 2010 Edit

This is a child post

This is an individual post (http://takien.com/536/this-is-a-child-post.php) that attached to the another post ( http://takien.com/550/wordpress-plugin-wp-sub-post.php)

    

![chimpanzee](/images/uploads/1788783493041_chimpanzee.jpg)
*Image on a sub-post*


Child post could be useful when you want to add an additional information to the main post,  news analysis, or update. Instead of editing the main post, you can now simply Add New post and mark it as child post.

Child post also has it's own functionality, can handle attachment, displaying image. etc.

But you can't see this post in the post editing page (wp-admin/edit.php) because of filter  in the plugin to prevent child post to be displayed individually in the main page, post listing, feed, etc.  Hahaha.. don't worry, I will fix it soon.
</blockquote>
