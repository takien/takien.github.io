---
title: "Searching File Within Directory Recursively Using PHP Scandir Function"
date: "2011-10-27T00:00:00Z"
categories: ["Uncategorized"]
tags: []
slug: "2011/10/27/searching-file-within-directory-recursively-using-php-scandir"
legacyUrl: "/blog/2011/10/27/searching-file-within-directory-recursively-using-php-scandir/"
comments: [{"author": "Prahastu", "date": "", "text": "top"}, {"author": "TionTux", "date": "", "text": "thanks for the information, this is exactly what I was looking for."}, {"author": "tamil", "date": "", "text": "nice"}]
---

<p>Recently I had to find my file stored somewhere in my server. Although I can do this easily using the built-in feature in cPanel File Manager, but what I need is to search file programaticallyusing a script. So, I created this function.</p>

```php
function find_file($dirs,$filename,$exact=false){

	$dir = @scandir($dirs);
	if(is_array($dir) AND !empty($dir)){
	foreach($dir as $file){
	if(($file !== '.') AND ($file!=='..')){
	if (is_file($dirs.'/'.$file)){
		$filepath =  realpath($dirs.'/'.$file);

		if(!$exact){
			$pos = strpos($file,$filename);
			if($pos === false) {
			}
			else {
				if(file_exists($filepath) AND is_file($filepath)){
				echo str_replace($filename,'<span style="color:red;font-weight:bold">'.$filename.'</span>',$filepath).' ('.round(filesize($filepath)/1024).'kb)<br />';
				}
			}
		}
		elseif(($file == $filename)){

			if(file_exists($filepath) AND is_file($filepath)){
				echo str_replace($filename,'<span style="color:red;font-weight:bold">'.$filename.'</span>',$filepath).' ('.round(filesize($filepath)/1024).'kb)<br />';
			}
		}
	}
	else{
		find_file($dirs.'/'.$file,$filename,$exact);
	}
	}
	}
	}
}
```

<p>The function accepts three parameters:</p>

<ol>
<li>$dir (string), absolute path of the directory to start the search, to use current directory use dirname(__FILE__).</li>
<li>$filename (string), the keyword to search for.</li>
<li>$exact (bool), true/false, default is false. If you set it to true it will find the exact &#8216;index.php&#8217; not &#8216;anotherindex.php&#8217; for keyword &#8216;index.php&#8217;.</li>
</ol>
<h2>How to use this function?</h2>
<p>This will find all file name contains <strong>content</strong> within current directory and all it&#8217;s sub directories.</p>

```php
< ?php find_file(dirname(__FILE__),'content');
?>
```

<p>And the search result will be like this:</p>
<div id="attachment_959" style="width: 310px" class="wp-caption aligncenter"><a href="https://web.archive.org/web/20160103044015/http://img.takien.com/2011/10/search-file-using-php.png"><img src="/images/2011/10/search-file-using-php-300x186.png" alt="Search file using PHP functions" title="search-file-using-php" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">Search file using PHP functions</p></div>
<h2>Another Approach</h2>
<p>Another way to search file in directory is using PHP <a href="https://web.archive.org/web/20160103044015/http://php.net/manual/en/function.glob.php" target="_blank"><strong>glob</strong> </a>function, as written <a href="https://web.archive.org/web/20160103044015/http://www.electrictoolbox.com/php-glob-find-files/" target="_blank">here</a>.</p>
