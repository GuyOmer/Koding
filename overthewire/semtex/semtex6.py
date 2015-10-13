#!/usr/bin/python

import socket, threading
import os, sys


class Socky(threading.Thread):
	ip =  "127.0.0."           # The website
	port = 24027
	data = ""
	sign = "Ckone20000"

	sock = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
	def __init__(self,name,id_num):
		threading.Thread.__init__(self)        #threads stuff
		self.name = name 					   #thread name
		ip = ip + str(id_num)                  #set ip to 127.0.0.X
		print name + ": Trying to connect as " + ip + " on port "+ str(port) +"..."
		self.sock.connect(ip, port)
		print name + ": Connected!"

		#run the thread
	def run(self):
		print self.name + " is starting!"
		get(self)
		print self.name + " is exiting!"

def get(me):
	me.data = me.soct.recv(80)
	print me.name + ": Got string!"
	password = me.data ^ lvl5pass
	print me.name + ": XOR'ed string!"
	if not me.soct.send(password + sign) == 10:
		print "Error ocurred!"
		break
	print me.name + ": Got back"
	print me.soct.recv(80)


# Create new threads
threads = []
for i in range(1,11):
	threads.append(Socky("Thread " + str(i),i))
	threads[i].start()

# Wait for threads to finish
for t in threads:
	t.join()

