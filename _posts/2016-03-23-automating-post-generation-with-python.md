---
layout: post
published: true
title: Automating Post Generation with Python
date: 2016-03-23
---

Blogging on Github pages and Jekyll is awesome. Jekyll uses markdown for blog posts. Jekyll requires to name the posts in a particular way and provide other header information like which layout to use, title and date etc.

I have found a simple way to generate all the above mentioned information in one go. I have created a python script to do automation process effortlessly. I also created a batch script (.BAT) file to run the python script in a single click. Here is the batch + python script. Save the script as *blog_post.bat* or whatever you want but the file extension must be *.bat*

```python
@echo off & python -x "%~f0" %*& goto :eof

#python script here

import os
import string
import datetime
import Tkinter
from tkSimpleDialog import askstring

root = Tkinter.Tk()
root.withdraw()
title = askstring('Blog Post Title','Title')
postname = title.lower().strip().replace(" ","-")
today = datetime.date.today().strftime("%Y-%m-%d")
postname = today+"-"+postname+".md"
header = "---\nlayout: default\npublished: false\ntitle: {0}\ndate: {1}\n---\n".format(title, today)

string.capwords(title)
f=open(postname,'w')
f.write(header)
os.startfile(postname)

```

I used python's built in Tkinter for post title prompt.