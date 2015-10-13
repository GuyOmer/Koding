#!/usr/bin/python
import json, sys,re

json_f = open("id.json","r")
data = json.load(json_f)

if len(sys.argv) == 1:

	count = 0

	with open("id.txt","w") as u_list:
		for user in data["data"]:
			u_list.write(user["name"].encode('utf8') + ": " + str(user["id"]) + "\n")
			count+=1
	print "Done!"
	print "Got %s enteries!" % count
else:
	parsed = {"names":{"lname":[],"fname":[]},"id":[]}
	for user in data["data"]:
		# print user["name"].split()
		# print user["name"]
		# sys.exit()
		#parsed["names"].append(user["name"].decode('utf8'))

		splitted = user["name"].split()
		parsed["names"]["lname"].append(splitted[0])
		parsed["names"]["fname"].append(splitted[1])
		parsed["id"].append(user["id"])
	print "Parsed!"

	# for name in parsed["names"]["lname"]:
	# 	print name.encode('utf8')

	print "Looking for\n" + sys.argv[1]
	for i in range(len(parsed["id"])):
		# print type(parsed["names"]["lname"][i]) #unicde
		# print type(sys.argv[1])                 #str
		# sys.exit()
		if sys.argv[1] == parsed["names"]["lname"][i].encode('utf8'):
			print parsed["names"]["lname"][i].encode('utf8')
			print str(parsed["id"][i])