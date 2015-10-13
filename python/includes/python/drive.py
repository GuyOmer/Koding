#!/usr/bin/python

import mechanize
import cookielib
import sys
from bs4 import BeautifulSoup

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
br.open('https://motssl5.mot.gov.il/motmf/exams.php')

# Select the first (index zero) form
br.select_form(nr=0)

counter = 1
month_i = 0
date = {"day":1, "month":["01","02","03","04","05","06","07","08","09","10","11","12"], "year":2014}

if len(sys.argv) == 1:
	id_num = 208994798#209040740-beiman#208721399-udi#208994798-yuval
	month_i = 0
	date["year"] = 2014
	print "\nPossilbe usage: python " + sys.argv[0] + " <id> <statring month> <starting year>\n\n"
else:
    id_num = int(sys.argv[1])
    month_i = int(sys.argv[2])-1
    date["year"] = int(sys.argv[3])


print "ID: "  + str(id_num)
print "starting date: " + str(date["day"]) + '/'+ date["month"][month_i] + '/'+ str(date["year"]) + "\n"


# User credentials
br.form['id'] = str(id_num)

br.form['theory_exam_date'] = str(date["day"]) + '/'+ date["month"][month_i] + '/'+ str(date["year"])

# Login
resp = br.submit()

soup = BeautifulSoup(resp.read())

while soup.findAll("div", { "class" : "warning" }):
	print str(counter) + " - ",
	counter += 1

	print str(date["day"]) + '/'+ date["month"][month_i] + '/'+ str(date["year"])

	date["day"]+=1
	if date["day"] == 32:
		date["day"] = 1
		month_i += 1
		print "Month Swap!"
		if month_i == 12:
			date["year"] += 1
			month_i = 0

	br.open('https://motssl5.mot.gov.il/motmf/exams.php')

	# Select the first (index zero) form
	br.select_form(nr=0)

	# User credentials
	br.form['id'] = str(id_num)
	br.form['id'] = str(id_num)

	br.form['theory_exam_date'] = str(date["day"]) + '/'+ date["month"][month_i] + '/'+ str(date["year"])

	# Submit
	resp = br.submit()

	soup = BeautifulSoup(resp.read())

print str(id_num)
print str(date["day"]) + '/'+ date["month"][month_i] + '/'+ str(date["year"])

out = open('drive_results.txt','a')
out.write("\n" + str(id_num) + "-->" + str(date["day"]) + '/'+ date["month"][month_i] + '/'+ str(date["year"]))
out.close
