#!/usr/bin/env python

import urllib
import re

symbolslist = ["zch15.cbt","zsh15.cbt","zwh15.cbt","zmh15.cbt",
"zlh15.cbt","lej15.cme","gfh15.cme","hej15.cme"]

i=0
while i<len(symbolslist):
    url = "https://finance.yahoo.com/q?s=" +symbolslist[i] +"&ql=0"
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l10_'+symbolslist[i] +'">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    print symbolslist[i], price
    i+=1

