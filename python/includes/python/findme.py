#!/usr/bin/python
import json,sys,re,os

json_f = open("id.json","r")
data = json.load(json_f)

findme = 208682187
date = "date"
for user in data["data"]:
    if findme == user["id"]:
        print "Got him!"
        with open("named.txt","a") as out:
        	out.write(user["name"][:user["name"].index("(")].encode('utf8') \
        		+ str(user["id"]) + " --> " + date + "\n")
        	os.system("cat named.txt")
        break