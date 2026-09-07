---
title: "Use WordPress Auto-Draft As Future Post ID. Since it Can’t Be Disabled"
date: "2014-05-28T00:00:00Z"
categories: ["Uncategorized"]
tags: []
slug: "2014/05/28/use-wordpress-auto-draft-as-future-post-id-since-it-cant-be-disabled"
legacyUrl: "/2014/05/28/use-wordpress-auto-draft-as-future-post-id-since-it-cant-be-disabled/"
comments: []
---

<p>Unfortunately, WordPress auto-draft can&#8217;t be disabled, especially if you&#8217;re using post editor through your dashboard to write a post. Auto-draft will not be created if you&#8217;re call <code>wp_insert_post()</code> directly from your script or plugin. Unlike autosave or post revision that can be easily bypassed by line of code, auto-draft just leave as is. I don&#8217;t know how important it is and what exaclty happened in the backend so WordPress keep auto-draft to be created.</p>
<figure class="image-missing-placeholder" role="img" aria-label="wordpress disable autodraft">
  <div class="placeholder-inner">
    <svg class="placeholder-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect>
      <circle cx="9" cy="9" r="2"></circle>
      <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>
    </svg>
    <span class="placeholder-text">wordpress disable autodraft</span>
  </div>
</figure>
<p>Despite that WordPress cleaning up auto-draft every 24 hours, still, it makes some peoples feel inconvenience, because it leaves unused ID in the database.</p>
<p><strong>My solution</strong></p>
<p>1. Disable auto-draft deleting schedule. It&#8217;s important because we need it&#8217;s ID to be reserved.<br/>
2. Redirect &#8220;New Post&#8221; to &#8220;Edit Post&#8221; if auto-draft exists in the database. This will use auto-draft ID as the ID of your new post.</p>
<p><strong>The fun part</strong><br/>

```php
/**

 *  fix autodraft,sometimes WordPress can be sucks too..

 *  @author: takien

 */

remove_action( 'wp_scheduled_auto_draft_delete', 'wp_delete_auto_drafts',10 );

add_action('admin_init','takien_fix_autodraft');

function takien_fix_autodraft() {

	global $pagenow,$typenow;

	if( 'post-new.php' == $pagenow ) {

		$args = Array(

			'post_type'     => $typenow,

			'posts_per_page'=> 1,

			'order'         => 'ASC',

			'post_status'   => 'auto-draft',

			'author'        => get_current_user_id()

		);

		$expected_draft = get_posts($args);

		if(isset($expected_draft[0])) {

			$id = $expected_draft[0]->ID;

			if ( current_user_can( 'edit_post', $id ) AND (!wp_check_post_lock( $id )) ) {

				$link = get_edit_post_link( $id, false );

				if( $link ) {

					wp_redirect($link);

					exit;

				}

			}

		}

	}

}
```

<p>Copy and paste or re-type (seriously) the above code to your <code>functions.php</code> of your theme or your plugin file.<br/>
Now, whenever you hit &#8220;Post New&#8221; to create post, it will be redirected to edit post, eg <code>wp-admin/post.php?post=10&action;=edit</code> if there is unused auto-draft in database. Where 10 is the ID of the auto-draft.</p>
<p>To prevent conflict, the code above also check for post type and author, to ensure that auto-draft also has same post_type and author as the post you want to create.</p>
