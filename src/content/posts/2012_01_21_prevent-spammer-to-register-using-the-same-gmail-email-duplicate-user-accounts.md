---
title: "Prevent Duplicate Registered User Accounts from The Same Gmail Email, Strip All Gmail Aliases"
date: "2012-01-21T00:00:00.000Z"
categories: ["Uncategorized"]
tags: ["duplicate aliases in gmail","gmail","gmail aliases"]
slug: "2012/01/21/prevent-spammer-to-register-using-the-same-gmail-email-duplicate-user-accounts"
legacyUrl: "/2012/01/21/prevent-spammer-to-register-using-the-same-gmail-email-duplicate-user-accounts/"
source: "takien.com"
author: "takien"
comments: [{"author":"ecommerce development","date":"","text":"This is really a fact.Spammers do spam without our will. Thanks for sharing."}]
---

![Gmail logo new look](/images/uploads/1788663673816_gmail-new-look-logo.jpg)
<p>Gmail,  Gmail is &#8230;, ah I really don&#8217;t need to explain this. So, continue reading <img src="/images/misc/simple-smile.png" alt=":)" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>
<h2>The Facts</h2>
<h3>Gmail ignores . (dot) in username</h3>
<p>If you have Gmail account <em>example@gmail.com</em>, actually you also have ex.ample@gmail.com, exam.ple@gmail.com, and so on until all characters in the username are separated with dot. These all have same inbox, and you can login using each of them. Also, emails come to that address will be received into one inbox example@gmail.com See: <a href="https://web.archive.org/web/20151118074229/http://www.dailytut.com/technology/gmail-dot-trick-bug-or-a-feature.html" target="_blank"><em>Gmail Dot Trick Bug or a Feature ?</em> </a></p>
<h3>Gmail ignores all character after + (plus sign) in username</h3>
<p>While you think the dot feature is not enough, Gmail also has another feature; you can add acceptable character in your username, separated by + (plus sign). It can be example+one@gmail.com, example+two@gmail.com, etc. An email sent to example@gmail.com or example+one@gmail.com or example+two@gmail.com will all be redirected to one common email address and that is example@gmail.com.<em> See: <a href="https://web.archive.org/web/20151118074229/http://labnol.blogspot.com/2006/09/gmail-easter-eggs-dot-blindess-email.html" target="_blank">GMail Easter Eggs: Dot Blindess &amp; Email Aliases</a></em>.<em><a href="https://web.archive.org/web/20151118074229/http://labnol.blogspot.com/2006/09/gmail-easter-eggs-dot-blindess-email.html" target="_blank"><br/>
</a></em></p>
<p>Gmail does not recognize characters after the PLUS symbol but the gmail search filter can distinguish between the different address and you can therefore redirect these email to separats gmail folders or apply different labels.</p>
<h3>Gmail user can use @googlemail.com instead of @gmail.com</h3>
<p>Again, example@gmail.com can be replaced with example@googlemail.com as well as if it combined with <em>dot</em> and <em>plus</em>.</p>

<h2>The Problem</h2>

![Spammer in SMF forum](/images/uploads/1788663695112_spammer-in-smf-forum-278x300.png)

<p>Besides the advantage of filtering, this feature has disadvantage for website owner, eg Community Forum and or website that requires unique membership. Yes, persons with Gmail account could have as many as possible <strong>duplicate accounts</strong> in our website. Of course this is very undesirable. Moreover, this way mostly used by <strong>spammer</strong> to register in our forum as they only need one Gmail account to register their hundreds clone. Imagine this, how many accounts can be generated from one Gmail account? It almost infinite, if I can&#8217;t say unlimited.</p>
<h2>The Solution</h2>
<p>If you think Gmail feature is bad for membership website, the only solution is to strip all gmail aliases and leave only original <em>example@gmail.com</em> during member registration process. The following lines of code is a PHP functions for this task.</p>

```php
function strip_gmail_email_aliases($email){
if(preg_match('/gmail|googlemail/i',$email)){ /*detect if email string matches gmail or googlemail using preg_match() regex*/
$emailbody         = explode('@',strtolower($email)); /*separate email at @ sign using explode()*/
$mailusername     = preg_replace('/([\.]+)|((\+)+([\+\.\-_a-z0-9]+))/i','',$emailbody[0]); /*most important part, strip all dot and everything after 'plus' */
$email             = $mailusername.'@gmail.com'; /*rebuild email string, and use only gmail.com*/
}
return $email; /* return the new email string*/
}
```

<h2>Implementations</h2>
<h3>In WordPress</h3>
<div id="attachment_1025" style="width: 295px" class="wp-caption aligncenter"><a href="https://web.archive.org/web/20151118074229/http://img.takien.com/2012/01/wordpress-logo.jpg"><img src="/images/2012/01/wordpress-logo.jpg" alt="wordpress logo" title="wordpress logo" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><p class="wp-caption-text">wordpress logo</p></div>
<p>It&#8217;s easy to call this function in WordPress platform, using <strong>user_registration_email</strong> filter <a href="/?s=hook" target="_blank">hook</a>. This function will be invoked immediately while user perform registration. Place this code in functions.php in your WordPress theme file or can be packaged into a <a href="/?s=plugin" target="_blank">plugin</a>.</p>

```php
add_filter( 'user_registration_email', 'strip_gmail_email_aliases'); /* this filter will call strip_gmail_email_aliases functions*/
function strip_gmail_email_aliases($email){
if(preg_match('/gmail|googlemail/i',$email)){
$emailbody         = explode('@',strtolower($email));
$mailusername     = preg_replace('/([\.]+)|((\+)+([\+\.\-_a-z0-9]+))/i','',$emailbody[0]);
$email             = $mailusername.'@gmail.com';
}
return $email;
}
```

<h3>In SMF (Simple Machines Forum)</h3>
![SMF Forum Logo](/images/uploads/1788663686934_smf-forum-300x158.jpg)
<p>Unlike WordPress, SMF needs more attention while doing modifications. Yes, you need to hardly editing existing file, so don&#8217;t forget to backup before you do anything with files in SMF.</p>
<ol>
<li>The file you will edit located in<strong> /Sources/Register.php</strong></li>
<li>Open file with code editor, eg. Notepad++</li>
<li>Find this set of codes:

```php
	// Set the options needed for registration.
	$regOptions = array(
		'interface' => 'guest',
		'username' => !empty($_POST['user']) ? $_POST['user'] : '',
		'email' => !empty($_POST['email']) ? $_POST['email'] : '',
		'password' => !empty($_POST['passwrd1']) ? $_POST['passwrd1'] : '',
		'password_check' => !empty($_POST['passwrd2']) ? $_POST['passwrd2'] : '',
		'openid' => !empty($_POST['openid_identifier']) ? $_POST['openid_identifier'] : '',
		'auth_method' => !empty($_POST['authenticate']) ? $_POST['authenticate'] : '',
		'check_reserved_name' => true,
		'check_password_strength' => true,
		'check_email_ban' => true,
		'send_welcome_email' => !empty($modSettings['send_welcomeEmail']),
		'require' => !empty($modSettings['coppaAge']) && !$verifiedOpenID && empty($_SESSION['skip_coppa']) ? 'coppa' : (empty($modSettings['registration_method']) ? 'nothing' : ($modSettings['registration_method'] == 1 ? 'activation' : 'approval')),
		'extra_register_vars' => array(),
		'theme_vars' => array(),
	);
```

</li>
<li>DO NOT edit anything inside the code above, yet add this code after it:

```php
/* strip all gmail aliases, comment here is useful when you want to do something in the future*/
if(preg_match('/gmail|googlemail/i',$regOptions['email'])){
	$emailbody 		= explode('@',strtolower($regOptions['email']));
	$mailusername 		= preg_replace('/([\.]+)|((\+)+([\+\.\-_a-z0-9]+))/i','',$emailbody[0]);
	$regOptions['email']= $mailusername.'@gmail.com';
}
/* end strip all gmail aliases*/
```

<p>As you see this is a direct code, not a PHP function, since it&#8217;s already in another SMF function, Register2()</li>
<li>Save file and re-upload it to server.</li>
</ol>
<h3>In Custom PHP</h3>
<p>If you using custom PHP code or CMS other than WordPress and SMF, call<em> strip_gmail_email_aliases()</em> right after registration form is submitted. Example:</p>

```php
/* define function*/
function strip_gmail_email_aliases($email){
if(preg_match('/gmail|googlemail/i',$email)){
$emailbody         = explode('@',strtolower($email));
$mailusername     = preg_replace('/([\.]+)|((\+)+([\+\.\-_a-z0-9]+))/i','',$emailbody[0]);
$email             = $mailusername.'@gmail.com';
}
return $email; /* return the new email string*/
}
if(isset($_POST['submit_register'])){ /* It's only an illustration and may differ with your actual code.*/
    $email = strip_gmail_email_aliases($_POST['email']);
    /* do the rest code here */
}
```

<h2>Conclusion</h2>
<p>If you put the code correctly and work well, the registration will only record example@gmail.com (without dot, without + and other character after it, and not googlemail.com domain) and all other alias combination will be considered as duplicate (already registered). 😀</p>
<p>Your comment are welcome. <img src="/images/misc/simple-smile.png" alt=":)" title="" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></p>
