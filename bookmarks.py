# This is a script I wrote to convert the 'Bookmarks' file at Chrome/User Data/{Profile}/Bookmarks to a .html format such that it can easily imported into any browser.
# Replace the path with your 'Bookmarks' file path, this saves the file to path.html

import json

def blist(b):
    for k in b:
        if k["type"] == "folder":
            folder(k)
        if k["type"] == "url":
            sf.write('<A HREF="' + k["url"] + '">' + k["name"] + "</A>\n")

def folder(d):
    if d["type"] == "folder":
        sf.write("<DT><H3>" + d["name"] + "</H3>\n")
        sf.write("<DL>\n")
        blist(d["children"])
        sf.write("</DL>\n")

path = ""
with open(path, "r") as read_file:
    data = json.load(read_file)

sf = open(path + ".html", "w")

sf.write('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n<TITLE>Bookmarks</TITLE>')
sf.write("<DL>\n")
for k, v in data["roots"].items():
    if(k!="synced"):
        folder(v)
        sf.write("<h3>"+k+"</h3>\n")
sf.write("</DL>\n")
