---
title: "Display WordPress Archive Lists By Specific Year or Month"
date: "2012-02-05T00:00:00.000Z"
categories: ["Wordpress Plugins"]
tags: []
slug: "2012/02/05/display-wordpress-archive-lists-by-specific-year-or-month"
legacyUrl: "/2012/02/05/display-wordpress-archive-lists-by-specific-year-or-month/"
source: "takien.com"
author: "takien"
comments: [{"author":"Appearance Hehe Awaludin","date":"","text":"Numpang insert ke database gan.. :hammer:"},{"author":"Dodol","date":"","text":"alert(“XSS is posible”);"},{"author":"pawel","date":"","text":"Thanks for sharing this filter ( :"},{"author":"goldaccess","date":"","text":"Great post – helped me a lot today"},{"author":"Nick","date":"","text":"A clean solution! Wondering if you could expand on where to setup and call the callback?\n\n\nFor instance, can I add this to the functions.php file then call it in the apply_filters() function?\n\n\nI’ve found wp_get_archives() in wp-includes/general-template.php but still new to WordPress and unsure how to implement.\n\n\nLooking forward to hearing back!"}]
---

![WordPress archive by specific date](/images/uploads/1788663232305_archive-image-calendar.jpg)

						

<p>WordPress has <code>wp_get_archives</code> function to display date-based archives list. Here is the default args for wp_get_archives:</p>

```php
$args = array(
'type' => 'monthly',
'limit' => ,
'format' => 'html',
'before' => ,
'after' => ,
'show_post_count' => false,
'echo' => 1
);
```

<p>I can choose whether archive should be displayed yearly, monthly, daily or weekly by passing <em>type</em> argument.</p>
<h2>The Problem</h2>
<p>Unfortunately I &#8216;CAN NOT&#8217; filter archive only on specific date, in this case I want to display monthly archive on year 2011. I have googled this problem but no luck.</p>
<h2>The solution</h2>
<p>Then I went into the code in the file where the <em>wp_get_archives</em> function is <a href="https://web.archive.org/web/20150818060523/http://core.trac.wordpress.org/browser/tags/3.3.1/wp-includes/general-template.php" target="_blank">located</a>, and found this filer hook &#8216;<code>$where = apply_filters( 'getarchives_where', "WHERE post_type = 'post' AND post_status = 'publish'", $r );</code>&#8216;</p>
<p>That is the filter I was looking for, so I created this callback.</p>

```php
function takien_archive_where($where,$args){
$year = isset($args['year']) ? $args['year'] : ";
$month = isset($args['month']) ? $args['month'] : ";
$monthname = isset($args['monthname']) ? $args['monthname']: ";
$day = isset($args['day']) ? $args['day'] : ";
$dayname = isset($args['dayname']) ? $args['dayname'] : ";
if($year){
$where .= " AND YEAR(post_date) = '$year' ";
$where .= $month ? " AND MONTH(post_date) = '$month' " : ";
$where .= $day ? " AND DAY(post_date) = '$day' " : ";
}

if($month){
$where .= " AND MONTH(post_date) = '$month' ";
$where .= $day ? " AND DAY(post_date) = '$day' " : ";
}

if($monthname){

$where .= " AND MONTHNAME(post_date) = '$monthname' ";

$where .= $day ? " AND DAY(post_date) = '$day' " : ";

}

if($day){

$where .= " AND DAY(post_date) = '$day' ";

}

if($dayname){

$where .= " AND DAYNAME(post_date) = '$dayname' ";

}

return $where;

}
```

<p>Now, I have additional arguments than can be passed to <em>wp_get_archives</em> function:</p>
<ul>
<li><strong>year </strong>(string), year to display, eg 2011</li>
<li><strong>month </strong>(string), monthnum to display, eg 2 for February</li>
<li><strong>monthname </strong>(string), month name to display, eg January</li>
<li><strong>day </strong>(string), day of month to display, eg 9</li>
<li><strong>dayname </strong>(string), day name to display, eg Sunday</li>
</ul>
<h2>Usage</h2>

```php
//This is example to display archive list on year 2010.

//call the filter early before any output, the best place is in functions.php

add_filter( 'getarchives_where','takien_archive_where',10,2);

/* place the following code at where output to be displayed.*/

//display the archive list monthly based, on year 2010

//set the arguments

$args = array(

'type' => 'monthly',

'echo' => 0,

'year' => '2010'

);

//render the output

echo '

Monthly archive 2010

';

echo '<ul>'.wp_get_archives($args).'</ul>';

//display the archive list daily based, on February 2011

$args = array(

'type' => 'daily',

'echo' => 0,

'year' => '2011',

'month' => '12'

);

echo '

Daily archive December, 2011

';

echo '<ul>'.wp_get_archives($args).'</ul>';

//set the arguments

$args = array(

'type' => 'daily',

'echo' => 0,

'month' => '1'

);

echo '

Daily archive January, all years

';

echo '<ul>'.wp_get_archives($args).'</ul>';
```

<p>If there&#8217;s post on that specific date, the output result should look like this:</p>
<div class="panel panel-info"><div class="panel-heading"><h3 class="panel-title">Result</h3></div><div class="panel-content" style="padding:5px 10px"></p>
<h2>Monthly archive 2010</h2>
<ul>
<li><a title="December 2010" href="/date/2010/12">December 2010</a></li>
<li><a title="November 2010" href="/date/2010/11">November 2010</a></li>
<li><a title="August 2010" href="/date/2010/08">August 2010</a></li>
<li><a title="July 2010" href="/date/2010/07">July 2010</a></li>
<li><a title="March 2010" href="/date/2010/03">March 2010</a></li>
<li><a title="February 2010" href="/date/2010/02">February 2010</a></li>
<li><a title="January 2010" href="/date/2010/01">January 2010</a></li>
</ul>
<h2>Daily archive December, 2011</h2>
<ul>
<li><a title="December 30, 2011" href="/date/2011/12/30">December 30, 2011</a></li>
<li><a title="December 15, 2011" href="/date/2011/12/15">December 15, 2011</a></li>
</ul>
<h2>Daily archive January, all years</h2>
<ul>
<li><a title="January 24, 2012" href="/date/2012/01/24">January 24, 2012</a></li>
<li><a title="January 21, 2012" href="/date/2012/01/21">January 21, 2012</a></li>
<li><a title="January 1, 2011" href="/date/2011/01/01">January 1, 2011</a></li>
<li><a title="January 29, 2010" href="/date/2010/01/29">January 29, 2010</a></li>
<li><a title="January 28, 2010" href="/date/2010/01/28">January 28, 2010</a></li>
<li><a title="January 27, 2010" href="/date/2010/01/27">January 27, 2010</a></li>
<li><a title="January 27, 2008" href="/date/2008/01/27">January 27, 2008</a></li>
<li><a title="January 24, 2008" href="/date/2008/01/24">January 24, 2008</a></li>
<li><a title="January 23, 2008" href="/date/2008/01/23">January 23, 2008</a></li>
<li><a title="January 21, 2008" href="/date/2008/01/21">January 21, 2008</a></li>
<li><a title="January 20, 2008" href="/date/2008/01/20">January 20, 2008</a></li>
<li><a title="January 9, 2008" href="/date/2008/01/09">January 9, 2008</a></li>
<li><a title="January 8, 2008" href="/date/2008/01/08">January 8, 2008</a></li>
<li><a title="January 1, 2008" href="/date/2008/01/01">January 1, 2008</a></li>
</ul>
<p></div></div>
<p>In fact, you may add other MySQL date-time function to the arguments, see <a title="MySQL Date and Time Functions" href="https://web.archive.org/web/20150818060523/http://dev.mysql.com/doc/refman/5.5/en/date-and-time-functions.html" target="_blank">this for reference</a>.</p>
<p>Good luck.</p>
