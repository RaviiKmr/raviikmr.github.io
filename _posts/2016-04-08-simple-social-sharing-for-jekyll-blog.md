---
layout: post
published: true
title: Simple Social Sharing For Jekyll Blog
date: 2016-04-08
category: tutorial
tags:
   - social
   - jekyll
---

I am going to show you how to add simple static social sharing links/buttons on your jekyll blog. So let's begin!

## Step 1: Create _share-page.html

Make a file **_share-page.html** inside your **_includes/** directory.
Now inside the **_share-page.html** put these lines :

```html
<div>
Share this on &rarr;
{% raw %}    
<a href="http://facebook.com/sharer.php?u={{ site.url }}{{ page.url }}" rel="nofollow" target="_blank" title="Share on Facebook" style="color:#fff; background:#3b5998; padding: 4px; text-decoration: none;">Facebook</a>
    
<a href="http://twitter.com/intent/tweet?text={{ page.title }}&url={{ site.url }}{{ page.url }}&via={{ site.twitter_username }}&related={{ site.twitter_username }}" rel="nofollow" target="_blank" title="Share on Twitter" style="color:#fff; background:#00aced; padding: 4px; text-decoration: none;">Twitter</a>
	
<a href="http://plus.google.com/share?url={{site.url }}{{page.url }}" rel="nofollow" target="_blank" title="Share on Google+" style="color:#fff; background:#dd4b39; padding: 4px; text-decoration: none;">Google+</a>
{% endraw %}
</div>
```

The output of this file will be like this:
<div style="background-color: #ccffcc;">
 {% include _share-page.html %}
</div>

We just added only facebook, twitter and google+ share urls. But this is how we can do many more. We have added the static share links of the social networks and added a little inline style to the a (anchor) tag so that it look good.

## Step 2: Include share-page.html to Post Layout

To show the social sharing buttons on blog post we have to include it to the our post layout.
We can do this by including the following line to our post layout:

```html
{% raw %}
{% include _share-page.html %}
{% endraw %}
```

This is it! Now we have a working social sharing buttons in our blog!