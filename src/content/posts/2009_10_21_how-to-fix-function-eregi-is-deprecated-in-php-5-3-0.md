---
title: "How to fix ‘Function eregi() is deprecated’ in PHP 5.3.0?"
date: "2009-10-21T00:00:00.000Z"
categories: ["PHP"]
tags: ["PHP","deprecated functions","email validation"]
slug: "2009/10/21/how-to-fix-function-eregi-is-deprecated-in-php-5-3-0"
legacyUrl: "/2009/10/21/how-to-fix-function-eregi-is-deprecated-in-php-5-3-0/"
source: "takien.com"
author: "takien"
comments: [{"author":"vv","date":"","text":"Deprecated: Function ereg() is deprecated in C:\\xampp\\htdocs\\catalog\\admin\\configuration.php on line 80"},{"author":"Keith","date":"","text":"Depreciated functions are really a pain, I hope there are no more of these in the next releases."},{"author":"Miki (Pixela.hu)","date":"","text":"Sometimes it is better to use explode() instead of suggested split() —> preg_split()"},{"author":"takien","date":"","text":"yeah, sometimes explode is much easier and may be faster"},{"author":"dade","date":"","text":"so how do I fix this? I have searched and when I do apply the changed I still get an error. any assistance would greatly be appreciated.\n\nif ( eregi( ‘index.php\\?’, $row->link ) ) {\nif ( !eregi( ‘Itemid=’, $row->link ) ) {\n$row->link .= ‘&Itemid=’. $row->id;\n}\n}"},{"author":"mike","date":"","text":"If you haven’t solved it yet…\n\nSounds like a joomla template error change to:\n\nif ( explode( ‘index.php\\?’, $row->link ) ) {\n\nif ( !explode( ‘Itemid=’, $row->link ) ) {\n$row->link .= ‘&Itemid=’. $row->id;\n}\n}"},{"author":"ajith","date":"","text":"if(!preg_match(“/^[_\\.0-9a-zA-Z-]+@([0-9a-zA-Z][0-9a-zA-Z-]+\\.)+[a-zA-Z]{2,6}$/i”, $str))\n\nthis work fine in php 5.3..\n\nthankjs for solving"},{"author":"BandenX","date":"","text":"Ayo ramai2 gunakan PHP 5.2.x. Dah bosen gw pake PHP 5.3.x. Permasalahan deprecated function nggak ada solusi yg bener2 menyelesaikan masalah"},{"author":"takien","date":"","text":"wah, apa gak salah tuh keputusannya untuk mengingalkan PHP 5.3.x?\nDeprecated itu bukanlah masalah besar, hanya kode kita saja yang perlu di update (disesuaikan dengan perkembangan zaman), nanti di PHP 6, fungsi2 yang deprecated tersebut benar2 tidak ada lagi.\nya, karena sudah ada fungsi lain yang sejenis yang bisa menggantikannya, biasanya lebih lengkap/mudah dsb."},{"author":"websoldier","date":"","text":"Waduh kayaknya kamu masih pemula yah??\n\nNamanya pemula harusnya belajar, siap menghadapi tantangan versi baru. Karena versi lama bisa jadi boomerang tersendiri bagi kamu. Lah, yg satu ini malah aneh, ada-ada aja kamu malah pengen migrasi ke versi sebelumnya.\n\nSebenernya kalo kamu mempelajari apa yang ada pasti masalah-masalah itu pasti bisa dibereskan,\n\nSalah satunya adalah masalah migrasi function deprecated ini, ini sebenarnya masih mudah loh masih bisa dengan mudah diselesaikan dibanding persoalan bug/vulnerability/error.\n\nCoba anda bayangkan persoalan error/bug/vulnerability codding itu, bukankah lebih rumit??\n\nSo, belajar coding lah anda untuk mematangkan skill walaupun “Trial & Error”, jangan cuma “script kiddies” semata."},{"author":"marek","date":"","text":"you can use ‘@’ (at sign) to suppress errors that would be generated from that expression.\ne.g:\n[php]\nif(!@preg_match(“/^[_\\.0-9a-zA-Z-]+@([0-9a-zA-Z][0-9a-zA-Z-]+\\.)+[a-zA-Z]{2,6}$/i”, $str))\n[/php]\nthen the errors won’t show up"},{"author":"amol sawant","date":"","text":"Nice Answer… it works for me……… tnks"},{"author":"Nguyễn Thế Bình","date":"","text":"Thank you so much! DONE!"},{"author":"Arief","date":"","text":"yes it works !!\n\nPlease do what Mike suggest ..\n\n”\nIf you haven’t solved it yet…\n\nSounds like a joomla template error change to:\n\nif ( explode( ‘index.php\\?’, $row->link ) ) {\n\nif ( !explode( ‘Itemid=’, $row->link ) ) {\n$row->link .= ‘&Itemid=’. $row->id;\n}\n}\n\n”\n\nit works for me !\n\nthanks Mike!\n\nregards,\nArief"},{"author":"Puiu Darlea","date":"","text":"Can anyone helpt me with this?\n\nforeach($bad as $b) {\nif(eregi($b, $this->message)) {\n$this->naughty = true;\n}\n}\n\nIf I replace “eregi” with “explode” I do not have the error anymore but I do not receive the mail either.\n\nIf I replace “eregi” with “preg_match” I get this error\n“Warning: preg_match() [function.preg-match]: Delimiter must not be alphanumeric or backslash in /mnt/users/oopsydai/public_html/contact/process_form.php on line 109″\nBUT the mail is received.\n\nAny ideas would be highly apreciated!\n\nPuiu."},{"author":"Puiu Darlea","date":"","text":"I got it the right way, I am posting it in case others are in the same situation:\n\nif(eregi($b, $this->message))\nbecomes:\nif(preg_match(“/\\b”.$b.”\\b/i”, $message))\n\nAll the best to all!\nP."},{"author":"takien","date":"","text":"Hello, Puiu Darlea. I was just about to reply to your comment but then you have found the solution. \nFurthermore, you need to use preg_quote in case your $b may contains special regex characters.\n\ngood luck"},{"author":"Sdsd","date":"","text":"sdsds"},{"author":"Ss","date":"","text":"sdsdsd"},{"author":"Prasetya Rahastu","date":"","text":"sadgagf"},{"author":"Prasetya Rahastu","date":"","text":"afsafdad"},{"author":"Puiu si Andreea","date":"","text":"Hi Takien, and THANK you for beeing present!\n\nSince I am no programmer, you mean simply change “preg_match” to “preg_quote” ?\n\nSome one helped me with this so I do not know the implications \n\nThanks again for beeing present on this forum!\nPuiu"},{"author":"takien","date":"","text":"Sorry, I wasn’t so clearly explained you.\nNo, not to change preg_match to preg_quote, they has different task.\nit should be like this:\n[php]\nif(preg_match(“/\\b”.preg_quote($b).”\\b/i”, $message))\n[/php]\n\nfor more example and usability of preg_quote, just follow my link above."},{"author":"Roberto79","date":"","text":"if(!ereg(“^[a-zA-Z0-9]*$”,$username))"},{"author":"Puiu Darlea","date":"","text":"ROBERTO79…\n\nI think it goes like this:\n\nif(preg_match(“/^[a-zA-Z0-9]*$/i”,$username))\n\nLet us know if it works!\n\nCiao"},{"author":"Roberto79","date":"","text":"Works like a charm, thank you"},{"author":"kevin","date":"","text":"it’s work fine for me.!\n//if (eregi(‘(googlebot|slurp|crawler|spider|teoma|ask jeeves|robot|archiv|fireball|scooter|bot)’,$_agent)) {\nif(preg_match(‘(googlebot|slurp|crawler|spider|teoma|ask jeeves|robot|archiv|fireball|scooter|bot)’,$_agent)){"},{"author":"Eric Scalf","date":"","text":"I’ve got the following code that is giving me fits in translating form eregi to preg_replace…\nif (eregi(“^” . rtrim(‘/’, $test) . “.*”, rtrim(‘/’, realpath($victim)))) {\nreturn true;\n}\nJust can’t get it down right… any ideas?"},{"author":"jay","date":"","text":"Thanks for very nice and easy solution"},{"author":"Faiz","date":"","text":"plz help me\nit is my code and i have problem in it\nif (eregi(“^(-)?[0-9]+\\..$”, $totalbalance)) {\n$totalbalance .= “0″;\n}\n\nand this is error\nDeprecated: Function eregi() is deprecated in C:\\wamp\\www\\echeckbook\\echeckbook\\checkbook.php on line 140"},{"author":"sachit","date":"","text":"Please solve this i can’t convert it\n\nif (eregi(‘^Version: [^0-9]*([ 0-9\\\\.\\\\:Q/]+)(http|file)\\:’, $versionstring[1].’#i’, $matches)) {"},{"author":"Andre","date":"","text":"plz help me, ive tried every way, but i cant do it work ;x\n\nif(eregi(“[^0-9a-zA-Z_@:.?,]“, $post)){"},{"author":"Celeste","date":"","text":"Hi all,\n\nPlz help! I am stumped! Don’t understand what I’m doing wrong!!!\n\nI changed:\n/* Check is numeric*/\n$regex = “[0-9]{10}”;\nif(!ereg($regex,$field)){\n$form->setError($fieldValue, “* Contact number invalid”);\n}\nto:\n/* Check is numeric*/\nif(!preg_match(‘/[0-9]{10}/’,$field)){\n$form->setError($fieldValue, “* Contact number invalid”);\n}\nbut still getting errors…..\nWhat am I doing wrong?"},{"author":"pathros","date":"","text":"Thanks a lot! It worked!"},{"author":"patrick","date":"","text":"i have same problem Deprecated: Function ereg() is deprecated in and my php lines are\n\nif ( (eregi(‘create’, $next)) || (eregi(‘insert’, $next)) || (eregi(‘drop t’, $next)) ) {\n$next = ”;\n$sql_array[] = substr($restore_query, 0, $i);\n$restore_query = ltrim(substr($restore_query, $i+1));\n$sql_length = strlen($restore_query);\n$i = strpos($restore_query, ‘;’)-1;\n\nhow should rewrite it?\nthanks"},{"author":"Anonymous","date":"","text":"try\nif ( (preg_match(‘/create/i’, $next)) || (preg_match(‘/insert/i’, $next)) || (preg_match(‘/drop/i’, $next)) ) {"},{"author":"Klary","date":"","text":"was very helpful … thank you"},{"author":"Alex","date":"","text":"Cab¡n anyone hlep me with this one?\n\nfunction swap_formats($date, $startFormat, $endFormat) {\n$startreg = $this->get_regular_expression($startFormat);\nereg($startreg['format'], $date, $regs);\n$newDate = $endFormat;"},{"author":"Mehdi Baaboura","date":"","text":"thanks! that was very helpful!"},{"author":"Domain registration","date":"","text":"Great information Thanks to sharing it helping more"},{"author":"Jeffshead","date":"","text":"How do I fix this:\n\n!eregi(basename($_SERVER['PHP_SELF']), $fileName) && ereg(‘^[^./][^/]*$’, $fileName))"},{"author":"Suasssh","date":"","text":"Thank you this was a great help"},{"author":"Joomla Development","date":"","text":"Several things in here’ haven’t considered before.Thank you for making this type of awesome publish that is really perfectly written, is going to be mentioning lots of buddies relating to this. Maintain blogging."},{"author":"Dejavucomplete","date":"","text":"sathish\n\nFunction ereg() is deprecated\n if(!ereg(“.*/index.php$”, $_SERVER['PHP_SELF'])\n    && !ereg(“.*/axfr_get.php$”, $_SERVER['PHP_SELF'])) {\n    header(“Location:../index.php”);\n    exit;\n}"},{"author":"joomla developers","date":"","text":"Great work to fix this issue. Thanks for the code here."},{"author":"Anonymous","date":"","text":"you’re welcome"},{"author":"Vincent","date":"","text":"preg_match(‘/^(http|ftp)://’, substr($url, 0, 10))\ncant get this preg match working  any1 that can help me with this one?"},{"author":"Nocniagenti","date":"","text":"Thnx for the info , is there any way to replace get_called_class()  to work with php 5.2 ?"},{"author":"Mohamed Tair","date":"","text":"Thanks a lot !!\n^^"}]
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
