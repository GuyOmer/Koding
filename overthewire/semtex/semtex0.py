#!/usr/bin/python

import socket
import os, sys, stat

con = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
address = "www.semtex.labs.overthewire.org"
PORT = 24001
print "Trying to connect to " + str(address) + " on port "+ str(PORT) +"..."
con.connect((address, PORT))
print "Connected!"

data = ""
counter = 1

while True:
	good = con.recv(1)
	data += good
	dump = con.recv(1)
	if not good or not dump:
		break
	counter+=1

print "Recived " + str(counter) + " Bytes!"

con.close()

print "Closed Connection!"
print "Starting to write exe..."

out = open("semtex0py" ,"w")
out.write(data)
out.close()

print "Finished writing!"
print "Executing..."

os.chmod("semtex0py",0700)

print "Output:"
os.system("./semtex0py")
os.remove("semtex0py")

print ""
print ""
print "Done!"