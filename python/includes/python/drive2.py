#!/usr/bin/python

import mechanize
import cookielib
import sys
from bs4 import BeautifulSoup

def ParseDate(date):
	return str(date["day"]) + '/'+ date["month"][month_i] + '/' + str(date["year"])
def ArrBound(arr,i,defu):
	try:
		return int(arr[i])
	except IndexError:
		return defu

url = 'https://motssl5.mot.gov.il/motmf/exams.php'

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# The site we will navigate into, handling it's session
br.open(url)

# Select the first (index zero) form
br.select_form(nr=0)

counter = 1
month_i = 0
date = {"day":1, "month":["01","02","03","04","05","06","07","08","09","10","11","12"], "year":2014}

#209040740-beiman#208721399-udi#208994798-yuval

if len(sys.argv) == 1:
	print "\nusage: python " + sys.argv[0] \
	+ " <id> <statring month> <starting year>\n"
	sys.exit()
else:
    id_num = int(sys.argv[1])
    month_i = ArrBound(sys.argv,2,1)-1
    date["year"] = ArrBound(sys.argv,3,2013)


print "\nID: "  + str(id_num)
print "starting date: " + ParseDate(date) + "\n"

while True:
	print str(counter) + " - " + ParseDate(date)
	counter += 1

	if date["day"] == 32:
		date["day"] = 1
		month_i += 1
		print "Month Swap!"
		if month_i == 12:
			date["year"] += 1
			month_i = 0
			print "Year Swap!"
	date["day"]+=1
	br.open(url)

	# Select the first form
	br.select_form(nr=0)

	# User credentials
	br.form['id'] = str(id_num)
	br.form['theory_exam_date'] = ParseDate(date)

	# Submit
	resp = br.submit()

	soup = BeautifulSoup(resp.read())

	if not soup.findAll("div", { "class" : "warning" }):
		print "Got it!"
		break

print str(id_num)
print ParseDate(date) + "\n"

# Log results
out = open('drive_results.txt','a')
out.write("\n" + str(id_num) + " --> " + ParseDate(date))
out.close
