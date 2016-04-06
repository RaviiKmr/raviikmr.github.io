---
layout: post
published: true
title: Tags in Jekyll Github Blog without Plugins
date: 2016-04-06
permalink: /blog/tags-in-jekyll-github-blog-without-plugins
category: tutorial
tags:
  - jekyll
  - github pages
  - tags
---

When [I created this blog](http://raviikmr.github.io/blog/my-website-launched) I was searching all over the internet to include tags in my blog posts. There is a jekyll plugin to do that but it won't work on github pages. So, I found a blog post ([here it is](http://charliepark.org/tags-in-jekyll)), which showed us how to get it to work.

Here is an outline of what we're going to do:

- We'll create some files (plugins files)
- Then we'll use yaml front matter 'tags' to tag posts
- Create the site locally and copy the 'tags' folder to the main directory

## Creating Plugin files

Create two files:

```
_layouts/tag_index.html
```
and

```
_plugins/_tag_gen.rb
```
In the **tag_index** file:

```html
---
layout: default
---
<h2 class="post_title">{{page.title}}</h2>
 <ul>
 {% raw %}
  {% for post in site.posts %}
  {% for tag in post.tags %}
  {% if tag == page.tag %}
  <li class="archive_list">
    <time style="color:#666;font-size:11px;" datetime='{{post.date | date: "%Y-%m-%d"}}'>{{post.date | date: "%m/%d/%y"}}</time> <a class="archive_list_article_link" href='{{post.url}}'>{{post.title}}</a>
    <p class="summary">{{post.summary}}</p>
    <div id="tags_cloud">
 <ul class="tag_list">
      {% for tag in post.tags %}
      <li class="inline archive_list"><div class="link-cont"><a class="tag_list_link" href="/tag/{{ tag }}">{{ tag }}</a></div></li>
      {% endfor %}
      </ul>
  </div>
  </li>
  {% endif %}
  {% endfor %}
  {% endfor %}
  {% endraw %}
</ul>
```

Now, in the **_tag_gen.rb** file:

```ruby
module Jekyll
  class TagIndex < Page
    def initialize(site, base, dir, tag)
      @site = site
      @base = base
      @dir = dir
      @name = 'index.html'
      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'tag_index.html')
      self.data['tag'] = tag
      tag_title_prefix = site.config['tag_title_prefix'] || 'Posts Tagged with &ldquo;'
      tag_title_suffix = site.config['tag_title_suffix'] || '&rdquo;'
      self.data['title'] = "#{tag_title_prefix}#{tag}#{tag_title_suffix}"
    end
  end
  class TagGenerator < Generator
    safe true
    def generate(site)
      if site.layouts.key? 'tag_index'
        dir = site.config['tag_dir'] || 'tag'
        site.tags.keys.each do |tag|
          write_tag_index(site, File.join(dir, tag), tag)
        end
      end
    end
    def write_tag_index(site, dir, tag)
      index = TagIndex.new(site, site.source, dir, tag)
      index.render(site.layouts, site.site_payload)
      index.write(site.dest)
      site.pages << index
    end
  end
  	end	
```

To show **tags** in posts, In your blog post or in the post's layout file, add these:

```html
<div id="tags_cloud">
  <ul class="tag_list">
    {% for tag in page.tags %}
    <li class="inline archive_list"><div class="link-cont"><a class="tag_list_link" href="/tag/{{ tag }}">{{ tag }}</a></div></li>
    {% endfor %}
  </ul>
</div>
```


When we create our site locally, these two files will create a folder **tags** in the **_site** directory. Inside the **tags** folder there will a folder for each tag and inside that folder there will be an **index.html** file which shows all the posts tagged with that tag.

## Creating YAML front matter 'tags'

Now, in blog posts front matter we add these lines:

```yaml
tags:
  - sometag
  - someother tag
```

Add the tags you like and these tags will be created in the **tags** folder.

## Final Steps

Now, we create our site locally by using these commands:

```
jekyll serve -w
```

This will create our site locally. Now go to the **_site** directory and copy the **tags** folder and paste this folder in root of your project directory.

Now we'll push the changes to **github** and when we do that our **tags** system will be working now.

> Check out my other article: [Automating Post Generation]({{site.url}}/blog/automating-post-generation-with-python)
