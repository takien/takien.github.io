---
title: "Tips for Developing WordPress Plugins"
date: "2014-11-18T23:31:47+00:00"
categories: ["Tips & Tutorial"]
tags: ["WordPress"]
slug: "2014/11/18/tips-for-developing-wordpress-plugins"
legacyUrl: "/2014/11/18/tips-for-developing-wordpress-plugins/"
comments: []
---

<div class="content-wrap">
					<div class="add">

</div>
<figure id="attachment_1425" style="width: 491px" class="wp-caption aligncenter"><img src="/images/2014/11/wordpress-plugin-development-tips.jpg" alt="WordPress" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /><figcaption class="wp-caption-text">WordPress</figcaption></figure>
<p>Do you love WordPress? Having may sites built with WordPress. Got many advantage from free plugins out there? It&#8217;s the time to give back to the community. Making WordPress plugin. Especially free plugins. This is not a tutorial, just a tips if you want to make a plugin. Here is my tips for new plugin developer. Note that it&#8217;s my old draft &#8212; I don&#8217;t know why I wrote this last day &#8212;  so, may be there is an irrelevance to be applied right now. And note that, I&#8217;m not doing all of these, but it&#8217;s worth to try.</p>
<h2>1. Before everything</h2>
<ul>
<li>Before you decide to make a plugin and publish it as opensource (to WordPress org), it&#8217;s recommeded that you make some research to know if your plugin will be useful to others (and make sure there&#8217;s no identical plugin out there)</li>
<li>If it not possible (likely it is), make sure you serve better plugin or with different approach.</li>
</ul>
<h2>2. Make your plugin attractive</h2>
<ul>
<li>Naming; plugin name must be easy to remember, representative, and simple. Generic if possible. Avoid embed your name (or your website,company etc) in your plugin name. Do not use trademark name.</li>
<li>Cover image, plugin with cover image is more attractive to the user. Prepare image named banner-772&#215;250.png, place it on /assets directory (/assets directory is in the same level with /trunk directory)</li>
<li>Screenshots, don&#8217;t forget to include screenshots in your plugin (place it under /assets directory, named screenshot-1.png and so on), give description for each screenshot.</li>
<li>Now you can also provide plugin thumbnail to be shown in plugin search page on WordPress admin.</li>
</ul>
<h2>3. Support and accept feedback</h2>
<ul>
<li>Always check for your plugin support forum on WordPress org. Answer the questions from the user. For this, I can only check it for at least once per month.</li>
<li>Some users usually post some feedbacks/critics to your plugin. Do not be offended if they give negative feedback. Note each feedback for your future plugin development (update).</li>
</ul>
<h2>4. Keep update</h2>
<ul>
<li>What to update? the first thing you must update is users request. As in point #2 above, you should note all feedback and make it as new feature/fix in the next update.</li>
<li>Write down your todo list about your plugin. But don&#8217;t force yourself to make it.</li>
</ul>
<h2>5. Assets</h2>
<ul>
<li>You do not need to create all assets your own, such as CSS, JavaScript, icon, image etc. There&#8217;re many resource over the Internet. Make sure they&#8217;re licnesed under GPL, Creative Common or opensource.</li>
<li>If you&#8217;re unsure, ask the creator if their stuff can be used in your plugin.</li>
<li>Give credit to the author, if you use those assets don&#8217;t forget to give feedback link to the original author.</li>
</ul>
<h2>6. Coding</h2>
<ul>
<li>Use WordPress coding standard to code your plugin</li>
<li>Give comment to your code. It will help you in the next development and others.</li>
<li>Avoid use WordPress or PHP deprecated functions.</li>
<li>Pay attention with security issues.</li>
<li>Do not encode your code, otherwise it will be rejected by WordPress plugin reviewer.</li>
<li>Make sure you test your plugin in some WordPress instalation (current version and previous version), also test on live site (not only on localhost), if possible also test on diffrent server environment (eg. Linux and Windows)</li>
</ul>
<h2>7. Don&#8217;t</h2>
<ul>
<li>Do not force users to donate you. I saw some plugin author placed BIG DONATE BUTTON on plugin setting page and keep alert us to donate. This is kind of annoying. They will donate if they want to.</li>
</ul>
<h2>8. Promote your plugin</h2>
<ul>
<li>Do not spam to promote your plugin</li>
<li>Use social (Twitter, Facebook etc) to share your plugin</li>
<li>Post a video tutorial about your plugin in Youtube will boost your plugin popularity</li>
<li>Post your plugin in your blog/website</li>
<li>Use your own plugin in your client project if needed (If you&#8217;re web developer)</li>
</ul>
<h2>9. Use it</h2>
<ul>
<li>You should also use your own plugin for your own wesite. Act as you use other&#8217;s plugin. By doing this you will know what your plugin bugs, error, advantages, disadvantages, etc.</li>
</ul>
<h2>10. Keep update with WordPress Development</h2>
<ul>
<li>It&#8217;s important. You need to know what happened to WordPress community and code right now, and the future. Subscribe to it&#8217;s developer newsletter is a good choice.</li>
<li>And here is a place the you should frequently visit, https://make.wordpress.org/plugins/</li>
</ul>
</p><div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/wordpress/">WordPress</a> </div>										
									</div>
