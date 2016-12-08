---
layout: post
title: jQuery - data() vs attr()
date: 2016-04-11 21:00:00.000000000 +09:00
---

[$.data()][jquery-data] and [$.attr()][jquery-attr] are very common functions we use daily. HTML5 introduces `data-*` attributes on DOM elemnts to store extra information.

####Data attributes defined inline on DOM element.

{% highlight html %}
<div id="div1" data-name="Bill"></div>
$("#div1").data("name");		//"Bill"
$("#div1").attr("data-name");	//"Bill"
{% endhighlight html %}
As you seen above, both data() and attr() can set and get the `name` on div1.

####Data attributes defined using JS.

{% highlight javascript %}
<div id="div1"></div>
$("#div1").data("name", "Bill");
$("#div1").data("name");		//"Bill"
$("#div1").attr("data-name", "Bob");
$("#div1").data("name");		//"Bill"
$("#div1").attr("data-name");	//"Bob"
{% endhighlight javascript %}
If you use data() to set data-* attribute on node, the actual value won't be changed later by using attr().


[jquery-data]: https://api.jquery.com/jquery.data
[jquery-attr]: http://api.jquery.com/attr/

