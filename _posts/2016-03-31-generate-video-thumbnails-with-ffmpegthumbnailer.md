---
layout: post
published: true
title: Generate Video Thumbnails with 'ffmpegthumbnailer'
date: 2016-03-31
category: tutorial
tags:
  - ubuntu
  - linux
---

Here is a simple trick to show video thumbnails faster in Ubuntu. I'm using ubuntu 15.10.

### Step 1:

First, install the ‘ffmpegthumbnailer’ package. For that, open your Terminal window and enter the below command.

        sudo apt-get install ffmpegthumbnailer

### Step 2:

Now, what we are doing is simple. We are going to replace a some line of code in the configuration file of the ‘totem-thumbnailer’ so that every time it is being called by the file manager, it will execute ‘ffmpegthumbnailer’.

Open the file /usr/share/thumbnailers/totem-thumbnailer or in Terminal type

        gedit /usr/share/thumbnailers/totem-thumbnailer

and do the following changes. From this:

        [Thumbnailer Entry]
        TryExec=/usr/bin/totem-video-thumbnailer
        Exe=/usr/bin/totem-video-thumbnailer -s %s %u %o

to this:

        [Thumbnailer Entry]
        TryExec=ffmpegthumbnailer
        Exe=ffmpegthumbnailer -s %s -i %i -o %o -c png -f -t 10

### Step 3:

Now restart your computer or just quit Nautilus by typing:

        nautilus -q

Now video thumbnails should be working fine.
