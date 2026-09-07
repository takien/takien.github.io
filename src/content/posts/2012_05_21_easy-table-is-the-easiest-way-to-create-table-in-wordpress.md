---
title: "Easy Table is The Easiest Way to Create Table in WordPress"
date: "2012-05-21T08:26:51+00:00"
categories: ["Article"]
tags: ["Plugins", "easy table", "table", "wordpress table"]
slug: "2012/05/21/easy-table-is-the-easiest-way-to-create-table-in-wordpress"
legacyUrl: "/2012/05/21/easy-table-is-the-easiest-way-to-create-table-in-wordpress/"
comments: [
  {
    "author": "Eric Scott",
    "date": "",
    "text": "Hi, Can I please get a hand with centering the table on a page? Also, how do enlarge the font size of the column headers?"
  },
  {
    "author": "Rene",
    "date": "",
    "text": "I want to create a field with a list – how i can build in one field a new line? i tried something like this “test1, test2 n test, test3″?"
  },
  {
    "author": "Tara",
    "date": "",
    "text": "Is it possible to have a “click here” or “link to” in the cells of the table? Thanks for the help!"
  },
  {
    "author": "Mauricio",
    "date": "",
    "text": "Any idea why is this happening? I’ve built two other tables with no problems, but I can’t find what’s wrong here. http://img707.imageshack.us/img707/9278/7dz.gif"
  },
  {
    "author": "takien",
    "date": "",
    "text": "You forgot to put comma after `pcas/min` in the second row"
  },
  {
    "author": "Mauricio",
    "date": "",
    "text": "wow. I was so focused on the first line that I didn’t noticed that. thanks!"
  },
  {
    "author": "Eco_Evolver",
    "date": "",
    "text": "Hi there, I’ve attempted to align the table with the following: [table width=\"300\" align=\"center\"] but the table does not center align.  How do you align the entire table please.  thank you for your time."
  },
  {
    "author": "takien",
    "date": "",
    "text": "Hi,\n\nThere’s a bug on aligning table.\n\nyou can temporary use this solution\n\nAdd this to your style.css of your theme\n\n```\ntable.easy-table.center {\n\n    margin-left:auto;\n\n    margin-right:auto;\n}\n```\n\nNow, whenever you want to centering table, just add .center class to the table\n\n```\n[table class=\"center\" width=\"200\"]\n\netc,etc,\n\n[/table]\n```"
  },
  {
    "author": "Billy",
    "date": "",
    "text": "This works in IE and Firefox, however, it is not working in chrome,"
  },
  {
    "author": "Ruud",
    "date": "",
    "text": "Hi, got this message : [table \"0\" not found /]\n\nwith this [table delimiter=\"t\" file=\"http://xxxxxxxx/wp-content/plugins/csv-to-base/test2.csv\"][/table]\n\nwhere other plugins are getting the file.\n\nTried with of without double quotes, with or without delimiter, tried a comma delimited file and a tab delimited file.Tried even to open without http and domainname, starting at /wp-content.\n\nAny idea?"
  },
  {
    "author": "Ruud",
    "date": "",
    "text": "found: table » tabel and it works fine"
  },
  {
    "author": "emlang",
    "date": "",
    "text": "could you explain your fix in greater detail? I’m not getting any error message, but my [table file=\"http://xxxxxxxxxx/tester.csv\"][/table] just doesn’t display anything on the WordPress page in which it’s placed."
  },
  {
    "author": "Ruud",
    "date": "",
    "text": "Hi emlang, my problem was – as described earlier by the author – another plugin using the same shortcut. Changing this shortcut-name from table to tabel made the solution. Give it a try"
  },
  {
    "author": "ericvic",
    "date": "",
    "text": "Hello, I’m a complete beginner. I installed Easy Table. Now what?\n\nWhere are the instructions on how to insert a table into a page?"
  },
  {
    "author": "shane",
    "date": "",
    "text": "It’s all shortcode. You go to your page in WordPress in the visual editor. Then you put code like this straight into the body:\n\n[table caption=\"Ericvic's Sample Table\" class=\"table table-bordered\" tablesorter=\"0\"]\n\nericvic,likes,tables\n\nand,these,words\n\nare,all,in\n\ncompletely,separate,cells,\n\n[/table]\n\nNow view your page through a browser. You now have a table."
  },
  {
    "author": "w",
    "date": "",
    "text": "I’m very new to wordpress and .css and most .html, and I promise I’ve spent a couple hours on this already, *but* I still can’t figure out how to get my table to center on the page.\n\nTo which theme do I add the style.css–the overall site theme, or the theme inside your plugin? And where exactly do I add the other code in order to center the specific table? I’ve tried every combination I can think of.\n\nThanks for humoring a newbie"
  },
  {
    "author": "Nico",
    "date": "",
    "text": "Hello,\n\nIs it possible to make the plugin visible for authors and editors. Currently the plugin is only accesible for admins, would be great if these users could also reach the option page"
  },
  {
    "author": "takien",
    "date": "",
    "text": "Easy Table option is intended to initial setting, which is not changed frequently.\n\nImagine editors change the shortcode tag, and you will lose everything.\n\nSo you don’t need to authorize editors to edit Easy Table option because the table setting can be managed per table basis, using inline parameter.\n\nIt means that people who has capability to write/edit posts, they can write table and do some setting on their table using inline parameter."
  },
  {
    "author": "Nico",
    "date": "",
    "text": "Yeah I understand that but the biggest problem is that there no other “Test area”  available  where editors or authors can test there code?"
  },
  {
    "author": "LiewCF",
    "date": "",
    "text": "Do you have examples of using colspan & rowspan in Easy Table? Thank you."
  },
  {
    "author": "takien",
    "date": "",
    "text": "You can see example here: http://takien.com/plugins/easy-table\n\nor here: http://wordpress.org/extend/plugins/easy-table/"
  },
  {
    "author": "LiewCF",
    "date": "",
    "text": "How do we use Easy Table to create multiple header rows (using rowspan and colspan)? Example: http://jsfiddle.net/yqQsP/ and http://www.w3.org/TR/html401/struct/tables.html#h-11.4.1 (see complex example)\n\nThanks."
  },
  {
    "author": "takien",
    "date": "",
    "text": "Easy Table currently not supports multiple row header,\n\nuse regular row as header instead."
  },
  {
    "author": "tracy",
    "date": "",
    "text": "hello..i want to add a 2 column table to one of my pages. i have activated the plug in so now what do i do?"
  },
  {
    "author": "takien",
    "date": "",
    "text": "Just write/type table shortcode in your post/page.\n\nSee example above."
  },
  {
    "author": "Reno Website Design",
    "date": "",
    "text": "I don’t want a ‘head1,head2,head3′ so I removed that code. But now the 1st row is BOLD. How can I make is so it is not bold. Thanks."
  },
  {
    "author": "Reno Website Design",
    "date": "",
    "text": "Disregard. I found it. th=”0″"
  },
  {
    "author": "takien",
    "date": "",
    "text": "no problem"
  },
  {
    "author": "Jamie C",
    "date": "",
    "text": "Hi I had a real quick question on the table, I have the default style selected and was wondering if there was any way to take the white hover state off the the table. I am using a darker theme and the table when scrolled over washes out the text making it hard to read for users. I have looked in the editor for the specific setting but haven’t found it and thought I would ask you to point me in the right direction. Thank you"
  },
  {
    "author": "Reno Website Design",
    "date": "",
    "text": "Yes, I would like to know the answer to this also. Can’t figure out the CSS."
  },
  {
    "author": "Bryan",
    "date": "",
    "text": "Thanks for a great plug-in!\n\nI am using the following [table] entry:\n\n[table caption=\"My Caption\" tablesorter=\"1\" sort=\"asc,asc\"]\n\n…\n\n[/table]\n\nbut I have found zero documentation on the tablesorter option, and very little on the sort option.\n\nSome questions:\n\n1) What effect is the tablesorter=”1″ supposed to have?  To use the jQuery Tablesorter to cause the sort to happen?\n\n2) Do you assume that the jQuery Tablesorter is activated?  That is, that there is already an appropriate  tag such as:\n\n?  (In other words, you don’t install Tablesorter with your plugin, correct?)\n\n3) If Tablesorter is not present, what effect does the sort option have, and if it is still functional, how do you cause the sort to happen?\n\n4) I would like to make the  elements of my table be clickable so that Tablesorter can do its thing and sort by various columns.  Do I have to implement that myself, using Tablesorter?  (I’ve done it before, in a different, non-WordPress environment, but don’t want to produce a conflict with whatever you to in this plug-in.)\n\n5) Could you please add a little documentation on the tablesorter and sort options, so we can figure out how to use them with your plugin?\n\nThanks for your patience and help"
  },
  {
    "author": "Bryan",
    "date": "",
    "text": "I hope my questions were not:\n\n1) interpreted as negative (definitely not the intention)\n\n2) too numerous/complex for convenient responses\n\nHow can I encourage a response to these questions?\n\nThanks!"
  },
  {
    "author": "Steve Karam",
    "date": "",
    "text": "Tablesorter is installed with the plugin, you have to activate it in the Plugin options page. Then when you use tablesorter=”1″ it will automatically work."
  },
  {
    "author": "Bryan",
    "date": "",
    "text": "Thanks, Steve!  Very helpful, and indeed it worked!\n\nTo: takien (creator of Easy Table):  Could you add just a little more along these lines to the plug-in documentation about tablesorter?  Steve’s information was just what I needed, but it would have been unnecessary for me to ask if the information was in the documentation for the plug-in.  Others would probably benefit, too. Thanks!"
  },
  {
    "author": "Hans Hafner",
    "date": "",
    "text": "A great plug-in!!\n\nOne question though: how do I create a hyperlink within a cell?"
  },
  {
    "author": "Mari",
    "date": "",
    "text": "Love this plugin! I was wondering if it was possible to make the text wrap around the table, though?"
  },
  {
    "author": "Bryan",
    "date": "",
    "text": "I’m not the developer of this plugin, but just trying to be helpful…\n\nI suggest placing the [table]…[/table] inside a <div>, and use CSS to style that div appropriately (for example, using float:left;).  You’ll most likely also have to set the width attribute to something less than 100%."
  },
  {
    "author": "Mari",
    "date": "",
    "text": "That worked perfectly, thank you!"
  },
  {
    "author": "AlingDarma",
    "date": "",
    "text": "One of the easiest table plugin that i have ever used before….btw all of these comment make me confuse but great job :-bd"
  },
  {
    "author": "Peter Smith",
    "date": "",
    "text": "How do I get a euro symbol € to work in the table? I can’t see it and the delimiter dosen’t work."
  },
  {
    "author": "Camille",
    "date": "",
    "text": "I don’t understand how to do this– there’s no button in the visual editor toolbar, so where do I even begin on creating/inserting a table? Do I have to type some sort of coding? Sorry for asking such a basic question."
  },
  {
    "author": "techguy",
    "date": "",
    "text": "I’ve been trying to remove lines from the tables and I added your code to my themes style.css file but it still shows the grey lines.  Anyone got any solutions?"
  },
  {
    "author": "Calvin",
    "date": "",
    "text": "How do I make my data centered in the columns of a table instead of left justified?"
  },
  {
    "author": "Wendy",
    "date": "",
    "text": "I like this plugin very much. I would like to adjust the columns padding from heading text, example below:\n\nHeading Text\n\nRow1col1\n\nRow2col1\n\nRow3col1\n\nChange to:\n\nHeading Text\n\n    Row1col1\n\n    Row2col1\n\n    Row3col1\n\nMay I know how to do so ?\n\nThanks."
  },
  {
    "author": "maxim",
    "date": "",
    "text": "Thank you for the plugin. But I have an issue. Whet put a row into another widget it forgets how many rows it has and put everything in one line. Any other sugestions how can I end the row?"
  },
  {
    "author": "Billy",
    "date": "",
    "text": "Working great, between the built in help, and the people here, I have been able to find every thing I need with the exception of my row heights. For some reason, they are higher than what they should be. You can see what I am talking about here http://www.sharptown.net/?page_id=225 , it really doesnt look bad, just makes me curious why it isn’t shrinking to the data.\n\nThanks again for a great and usefull plugin."
  },
  {
    "author": "Mike Munter",
    "date": "",
    "text": "It does not sort properly for values above 1,000.  Had the same problem with “Ultimate Tables” plug-in.  Is there a fix for this?"
  },
  {
    "author": "Daria F.",
    "date": "",
    "text": "Absolutely brilliant plug-in! Thank you very much.\n\nOne question: I’m attempting to make every row in the table a link. I’ve been able to add alternating colour values and hover effects in CSS, but when I add a , only the value in the first column turns into a link. Is there anyway to turn the entire row into a clickable link? \n\nThe page in question: http://goatseyeview.co.uk/contact/\n\nI’ve applied a  to the top row in the first table."
  },
  {
    "author": "CRN",
    "date": "",
    "text": "Can you update the flexslider.css file in the Trusted theme"
  },
  {
    "author": "Adrian Toma",
    "date": "",
    "text": "i cant make a sortable table with the current plugin version"
  },
  {
    "author": "emlang",
    "date": "",
    "text": "I’m currently unable to use the Easy Table shortcode to call a csv file from one I posted to WordPress’s media page. I’ve also tried this with a dropbox account. I’m calling them with the URL that is listed as their location on my website. Any idea on how to get it to work?"
  },
  {
    "author": "izumitelj",
    "date": "",
    "text": "there is a bug with cell data starting with certain unicode characters (in my case eastern european ČčĆćŠšĐđŽž). all first letters get trimmed.\n\n[table] Čaaaa, Šiiii, Đeeee, Ćiiii\n\n1,2,3,4 [/table]\n\nwill render like “aaaa, iiii, eeee, iiii”.\n\nplease fix this"
  },
  {
    "author": "izumitelj",
    "date": "",
    "text": "it works fine if the strings is enclosed in double quotes."
  },
  {
    "author": "arbakul",
    "date": "",
    "text": "It sitll doesn’t work, as it should. Can’t put latin letter in first place. Please fix it."
  },
  {
    "author": "Stephen Davies",
    "date": "",
    "text": "How can I include a comma in the text of a row?"
  },
  {
    "author": "Madis",
    "date": "",
    "text": "Change “Delimiter” value (default comma) in options to something else, for example semicolon, and use that for separation."
  },
  {
    "author": "Stephen Davies",
    "date": "",
    "text": "Thank you very much. Seems obvious now.\n\nLove the plug-in."
  },
  {
    "author": "jr",
    "date": "",
    "text": "anyway easy table can cache the remote csv until its updated?"
  },
  {
    "author": "tomatow",
    "date": "",
    "text": "Hi, I don’t have table sroting in default tables. Please help…"
  },
  {
    "author": "tomatow",
    "date": "",
    "text": "False alarm. Sorry!"
  },
  {
    "author": "Susan",
    "date": "",
    "text": "I have read the documentation and I still don’t have a clue as to how to create a table. Am I supposed to paste the code from the samples into the stylesheet?"
  },
  {
    "author": "James",
    "date": "",
    "text": "Is there a way to change the background color, color of the text in the table"
  },
  {
    "author": "Khaled AlShami",
    "date": "",
    "text": "How to preview CSV file, that include different encoding, like Arabic (Windows)."
  },
  {
    "author": "Jeffrey",
    "date": "",
    "text": "CSV loads but it doesn’t display properly. It mashes everything into one row, how to you tell it to break after the 3rd column?"
  },
  {
    "author": "Peter",
    "date": "",
    "text": "I can’t get to to work. have loaded files and saved settings then tried first example of U.S. pick-up trucks. I pasted the code beginning [table] in the text field…No table  displays on my post – only the text of the example in non-table format. . Help."
  },
  {
    "author": "takien",
    "date": "",
    "text": "don’t use full link on the comment,\n\nthat will automatically held by disqus to prevent spam."
  },
  {
    "author": "takien",
    "date": "",
    "text": "Hi John,\n\nEasy Table currently having bug with character encoding.\n\nFor best result, the source data must be UTF-8 encoded.\n\nOther than that may shows unexpected character output.\n\nTry to copy the file and resave on your pc and see the result.\n\nBe patient while I’m trying to fix it. Once it fixed, the patch or update will be released.\n\nUpdate:\n\nIf you’re using FTP client to transfer text file, make sure you use Binary and NOT Auto or ASCII on the transfer type."
  },
  {
    "author": "John",
    "date": "",
    "text": "Can you give me your mail address ?"
  },
  {
    "author": "takien",
    "date": "",
    "text": "please use contact form on this blog.\n\ntakien.com/contact"
  },
  {
    "author": "John",
    "date": "",
    "text": "@takien:disqus, I sent a message from contact form. Can you see my previous message? Under this message, there is a message about my problem which sent 2 days ago. Can you see links on this message?"
  }
]
---

<div class="content-wrap">
					<div class="add">

</div>
<figure id="attachment_1127" style="width: 300px" class="wp-caption alignleft"><a href="https://web.archive.org/web/20160611200616/http://img.takien.com/2012/05/easy-table-wordpress-plugins.png"><img src="/images/2012/05/easy-table-wordpress-plugins-300x213.png" alt="easy table wordpress plugins" title="easy table wordpress plugins" class="rounded-lg my-6 max-w-full h-auto shadow-md" loading="lazy" /></a><figcaption class="wp-caption-text">Easy table wordpress plugins screenshot</figcaption></figure>
<p>Hello, this is the official post about my newest WordPress plugins, Easy Table. As it&#8217;s name, Easy Table is WordPress plugin to create table in post, page, or widget in easy way using CSV format. This can also display table from CSV file.</p>
<p>Easy Table is a WordPress plugin that allow you to insert table in easy way. Why it&#8217;s easy? Because you don&#8217;t need to write any complicated HTML syntax. Note that this plugin is not a graphical user interface table generator, so you can simply type your table data directly in your post while you writing. No need to switch to another window nor click any toolbar button.</p>
<p>Easy Table using standard CSV format to generate table data, it&#8217;s easiest way to build a table.</p>
<h2>Some Features</h2>
<ul>
<li>Easy to use, no advanced skill required</li>
<li>Display table in post, page or even in widget</li>
<li>Read data from CSV file and display the data in table</li>
<li>Sortable table column (using tablesorter jQuery plugin)</li>
<li>Fancy table design (using Twitter CSS bootstrap)</li>
<li>WYSIWYG safe, I mean you can switch HTML/View tab in WordPress editor without breaking the table data.</li>
</ul>
<h2>Example:</h2>
<p><strong>1. Basic Example</strong></p>
<pre>[table]Year,Make,Model,Length
1997,Ford,E350,2.34
2000,Mercury,Cougar,2.38[/table]</pre>
<p><strong>Result:</strong><br/>
<div class="table-responsive"><table style="width:100%; " class="easy-table easy-table-default tablesorter  table-striped">
<thead>
<tr><th class=" ">Year</th>
<th class=" ">Make</th>
<th class=" ">Model</th>
<th class=" ">Length</th>
</tr>
</thead>
<tbody>
<tr><td>1997</td>
<td>Ford</td>
<td>E350</td>
<td>2.34</td>
</tr>

<tr><td>2000</td>
<td>Mercury</td>
<td>Cougar</td>
<td>2.38</td>
</tr>
</tbody></table></div></p>

<p><strong>2. More complicated table data:</strong></p>
<pre>[table]Year,Make,Model,Description,Price
1997,Ford,E350,"ac, abs, moon",3000.00
1999,Chevy,"Venture ""Extended Edition""","",4900.00
1999,Chevy,"Venture ""Extended Edition, Very Large""","",5000.00
1996,Jeep,Grand Cherokee,"MUST SELL! air, moon roof, loaded",4799.00[/table]</pre>
<p><strong>Result:</strong></p>
<div class="table-responsive"><table style="width:100%; " class="easy-table easy-table-default tablesorter  table-striped">
<thead>
<tr><th class=" ">Year</th>
<th class=" ">Make</th>
<th class=" ">Model</th>
<th class=" ">Description</th>
<th class=" ">Price</th>
</tr>
</thead>
<tbody>
<tr><td>1997</td>
<td>Ford</td>
<td>E350</td>
<td>ac, abs, moon</td>
<td>3000.00</td>
</tr>

<tr><td>1999</td>
<td>Chevy</td>
<td>Venture "Extended Edition"</td>
<td></td>
<td>4900.00</td>
</tr>

<tr><td>1999</td>
<td>Chevy</td>
<td>Venture "Extended Edition, Very Large"</td>
<td></td>
<td>5000.00</td>
</tr>

<tr><td>1996</td>
<td>Jeep</td>
<td>Grand Cherokee</td>
<td>MUST SELL!<br/>air, moon roof, loaded</td>
<td>4799.00</td>
</tr>
</tbody></table></div>
<p>In the second example above, the cell data that has commas and quote should be wrapped with &#8221; (double quote).</p>

<p><strong>3. Table with no heading</strong></p>
<pre>[table th="0"]
row1col1,row1col2,row1col3
row2col1,row2col2,row2col3
row3col1,row3col2,row3col3
[/table]</pre>
<p>Result:</p>
<div class="table-responsive"><table style="width:100%; " class="easy-table easy-table-default tablesorter  table-striped">
<tbody>
<tr><td>row1col1</td>
<td>row1col2</td>
<td>row1col3</td>
</tr>

<tr><td>row2col1</td>
<td>row2col2</td>
<td>row2col3</td>
</tr>

<tr><td>row3col1</td>
<td>row3col2</td>
<td>row3col3</td>
</tr>
</tbody></table></div>

<p><strong>4. Table with caption, custom class and no <em>tablesorter</em><br/>
</strong></p>
<pre>[table caption="This is example table in WordPress" class="table table-bordered" tablesorter="0"]
row1col1,row1col2,row1col3
row2col1,row2col2,row2col3
row3col1,row3col2,row3col3
[/table]</pre>
<p>Result:</p>
<div class="table-responsive"><table style="width:100%; " class="easy-table easy-table-default table table-bordered">
<caption>This is example table in WordPress</caption>
<thead>
<tr><th>heading1</th>
<th>heading2</th>
<th>heading3</th>
</tr>
</thead>
<tbody>
<tr><td>row1col1</td>
<td>row1col2</td>
<td>row1col3</td>
</tr>

<tr><td>row2col1</td>
<td>row2col2</td>
<td>row2col3</td>
</tr>

<tr><td>row3col1</td>
<td>row3col2</td>
<td>row3col3</td>
</tr>
</tbody></table></div>

<p><strong>5. Table with auto index, start from number 1 (since 0.9)</strong></p>
<pre>[table ai="1"]
 head1,head2,head3
row1col1,row1col2,row1col3
row2col1,row2col2,row2col3
row3col1,row3col2,row3col3
row4col1,row4col2,row4col3 
[/table]</pre>
<p>Result:</p>
<div class="table-responsive"><table style="width:100%; " class="easy-table easy-table-default tablesorter  table-striped">
<thead>
<tr><th>No.</th><th class=" ">head1</th>
<th class=" ">head2</th>
<th class=" ">head3</th>
</tr>
</thead>
<tbody>
<tr><td style="width:30px">1</td><td>row1col1</td>
<td>row1col2</td>
<td>row1col3</td>
</tr>

<tr><td style="width:30px">2</td><td>row2col1</td>
<td>row2col2</td>
<td>row2col3</td>
</tr>

<tr><td style="width:30px">3</td><td>row3col1</td>
<td>row3col2</td>
<td>row3col3</td>
</tr>

<tr><td style="width:30px">4</td><td>row4col1</td>
<td>row4col2</td>
<td>row4col3</td>
</tr>
</tbody></table></div>

<p><strong>6. Table with new line in a cell (since 0.9)</strong><br/>
Any <em>nl </em>value would be replaced with new line while rendered. nl could be one character or more. Be wise to use character here, make sure it&#8217;s not very common character that may used in your data.</p>
<pre>[table nl="~~"]
head1,head2,head3
row1col1,row1col2,this~~should~~be~~in~~one cell
row2col1,row2col2,this~~
also~~
should~~
be~~
in~~
one~~
cell
row3col1,row3col2,row3col3
row4col1,row4col2,row4col3
[/table]</pre>
<p>Result:</p>
<div class="table-responsive"><table style="width:100%; " class="easy-table easy-table-default tablesorter  table-striped">
<thead>
<tr><th class=" ">head1</th>
<th class=" ">head2</th>
<th class=" ">head3</th>
</tr>
</thead>
<tbody>
<tr><td>row1col1</td>
<td>row1col2</td>
<td>this<br/>should<br/>be<br/>in<br/>one cell</td>
</tr>

<tr><td>row2col1</td>
<td>row2col2</td>
<td>this<br/>also<br/>should<br/>be<br/>in<br/>one<br/>cell</td>
</tr>

<tr><td>row3col1</td>
<td>row3col2</td>
<td>row3col3</td>
</tr>

<tr><td>row4col1</td>
<td>row4col2</td>
<td>row4col3</td>
</tr>
</tbody></table></div>
<p><strong>7. Table from file</strong></p>
<pre>[table file="http://img.takien.com/2012/05/test.csv"][/table]</pre>
<p>Result:<br/>
<div class="table-responsive"><table style="width:100%; " class="easy-table easy-table-default tablesorter  table-striped">
<thead>
<tr><th class=" ">a</th>
<th class=" ">b</th>
<th class=" ">c</th>
</tr>
</thead>
<tbody>
<tr><td>d</td>
<td>e</td>
<td>f</td>
</tr>

<tr><td>g</td>
<td>h</td>
<td>i</td>
</tr>
</tbody></table></div></p>
<div class="panel panel-warning"><div class="panel-heading"><h3 class="panel-title">Download latest version</h3></div><div class="panel-content" style="padding:5px 10px"><br/>
<a class="btn btn-primary" href="https://web.archive.org/web/20160611200616/http://wordpress.org/extend/plugins/easy-table/" target="_blank">Download from WordPress.org</a> or directly from your wp-admin, search &#8220;Easy Table&#8221; in the plugin installer.<br/>
</div></div>
<h2>Note:</h2>
<ul>
<li>If you creating custom theme, please make backup to another directory or local before update plugins</li>
<li><span style="text-decoration: line-through;">After installing you have to go to Settings-&gt;Options and click Save once to load the default settings.</span></li>
<li><span style="text-decoration: line-through;">Backward compatibility of function <strong>str_getcsv</strong> is not work. So if your PHP version is lower than 5.3.0, the table will only show first row.</span> Fixed in version 0.2, please update if you have installed the previous version.</li>
</ul>
<h2>Video Tutorial</h2>
<p>Still confusing how to install and create first table? Check out this video tutorial.</p>
<p><iframe width="500" height="281" src="https://web.archive.org/web/20160611200616if_/http://www.youtube.com/embed/Th0_qSleyDI?feature=oembed" frameborder="0" allowfullscreen></iframe></p>
<p><iframe width="500" height="375" src="https://web.archive.org/web/20160611200616if_/https://www.youtube.com/embed/0n1nS9h4Sr0?feature=oembed" frameborder="0" allowfullscreen></iframe><br/>
(video by: <a href="https://web.archive.org/web/20160611200616/http://webdesy.com/how-to-add-a-neat-table-in-wordpress/" target="_blank">webdesy.com</a>)</p>

<div id="bawah-artikel" style="clear:both"> 

</div><div class="post-tag" style="padding:5px;margin:20px 10px 10px 0;text-align:center;clear:both"><button class="btn btn-xs btn-inline">Tags:</button> <a class="label label-default" href="/tag/easy-table/">easy table</a> <a class="label label-default" href="/tag/wp-plugins/">Plugins</a> <a class="label label-default" href="/tag/table/">table</a> <a class="label label-default" href="/tag/wordpress-table/">wordpress table</a> </div>										
									</div>
