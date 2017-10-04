#@echo off & python -x "%~f0" %*& goto :eof

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
slugline = "---\nlayout: post\npublished: false\ntitle: {0}\ndate: {1}\ncategory: general\n---\n".format(title, today)

string.capwords(title)
f=open(postname,'w')
f.write(slugline)
os.startfile(postname)