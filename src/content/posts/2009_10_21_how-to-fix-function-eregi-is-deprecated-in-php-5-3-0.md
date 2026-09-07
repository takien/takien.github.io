---
title: "How to fix ‘Function eregi() is deprecated’ in PHP 5.3.0?"
date: "2009-10-21T00:00:00Z"
categories: ["PHP"]
tags: ["PHP", "deprecated functions", "email validation"]
slug: "2009/10/21/how-to-fix-function-eregi-is-deprecated-in-php-5-3-0"
legacyUrl: "/2009/10/21/how-to-fix-function-eregi-is-deprecated-in-php-5-3-0/"
comments: []
---

<div style="float:left;margin-right:10px;margin-bottom:10px;">

</div>
						<p>I used to use eregi for validating email address input that matches to the regular expression.</p>



```php
if(!eregi("^[_\.0-9a-zA-Z-]+@([0-9a-zA-Z][0-9a-zA-Z-]+\.)+[a-zA-Z]{2,6}$", $str)) {
	$msg = 'email is not valid';
}
else {
$valid = true;
}
```


<p>That would return true if given email address is matches to <em>username@domain.ext</em> pattern. Unfortunately, after upgrading PHP to the earlier version (5.3.0), it wont work properly. This is because <em>eregi </em>is one of several functions that are deprecated in the new version of PHP.</p>
<h2>Solution how to fix Function Deprecated:</h2>
<p>Use <em>preg_match</em> with the <em>&#8216;i&#8217;</em> modifier instead. <em>i</em> means that regular expression is case insensitive. So the code become like this:</p>



```php
if(!preg_match("/^[_\.0-9a-zA-Z-]+@([0-9a-zA-Z][0-9a-zA-Z-]+\.)+[a-zA-Z]{2,6}$/i", $str)) {
	$msg = 'email is not valid';
}
else {
$valid = true;
}
```


<h2>The list of functions that are deprecated in PHP 5.3.0:</h2>
<p><div style="float:right;width:300px;height:250px;margin-left:20px">

</div></p>
<ul>
<li>call_user_method() (use call_user_func() instead)</li>
<li>call_user_method_array() (use call_user_func_array() instead)</li>
<li>define_syslog_variables()</li>
<li>dl()</li>
<li>ereg() (use preg_match() instead)</li>
<li>ereg_replace() (use preg_replace() instead)</li>
<li>eregi() (use preg_match() with the &#8216;i&#8217; modifier instead)</li>
<li>eregi_replace() (use preg_replace() with the &#8216;i&#8217; modifier instead)</li>
<li>set_magic_quotes_runtime() and its alias, magic_quotes_runtime()</li>
<li>session_register() (use the $_SESSION superglobal instead)</li>
<li>session_unregister() (use the $_SESSION superglobal instead)</li>
<li>session_is_registered() (use the $_SESSION superglobal instead)</li>
<li>set_socket_blocking() (use stream_set_blocking() instead)</li>
<li>split() (use preg_split() instead)</li>
<li>spliti() (use preg_split() with the &#8216;i&#8217; modifier instead)</li>
<li>sql_regcase()</li>
<li>mysql_db_query() (use mysql_select_db() and mysql_query() instead)</li>
<li>mysql_escape_string() (use mysql_real_escape_string() instead)</li>
<li>Passing locale category names as strings is now deprecated. Use the LC_* family of constants instead.</li>
<li>The is_dst parameter to mktime(). Use the new timezone handling functions instead.</li>
</ul>
<p>Ref:</p>
<p>http://php.net/manual/en/migration53.deprecated.php</p>
