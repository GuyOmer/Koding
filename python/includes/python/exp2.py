#!/usr/bin/python
#import json
import mechanize
import cookielib
from bs4 import BeautifulSoup

def strip(text):
	"""returns given string with any html tags and whitespace"""
	text = str(text)
	while text[0] == '<':
		start_index = text.find('>')+1
		end_index = text.rfind('<')
		if start_index == -1 or end_index == -1:
			return False
		#print str(start_index) + " s-e " + str(end_index)
		text = text[start_index:end_index].lstrip().rstrip()
	return text

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

# User-Agent (iPhone iOS 7)
br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; CPU \
                   iPhone OS 7_0_4 like Mac OS X) AppleWebKit\
                   /537.51.1 (KHTML, like Gecko) Version/7.0 \
                   Mobile/11B554a Safari/9537.53')]

# The site we will navigate into, handling it's session
br.open('http://www.webtop.co.il/mobile/')

# Select the first (index zero) form
br.select_form(nr=0)

#read username from username.txt
user = open('user.txt','r')
username = user.readline()
password = user.readline()
user.close

# User credentials
br.form['ctl00$body$username'] = str(username)
br.form['ctl00$body$password'] = str(password)

# Login
resp = br.submit()

#navigate into messages
for link in br.links():
    if link.url == "messagesBox.aspx?view=inbox":
		break

response = br.follow_link(link)
br.select_form(nr=0)
senders = ""
count = 1

#finds all messages senders name
while True:
	print count
	count+=1
	#BeautifulSoup
	soup = BeautifulSoup(response.read())

	#print soup.prettify()

	messageboard = soup.find_all('td')
	i = 0
	for message in messageboard:
		if not message.has_attr('class') and not message.has_attr('id') and i%2==0:
			tmp = strip(message)
			if not tmp:
				print "error!\n"
			else:
				senders += tmp + "\n"
		i+=1
	for link in br.links():
		temp_link = str(link)
		found = temp_link.find("pageID=" + str(count))
		#print found
		if found != -1:
			response = br.follow_link(link)
			br.select_form(nr=0)
			print "Found page number: " + str(count)
			break
	if found == -1:
		break

#prints senders' names into senders.txt
out = open('senders2.txt','w')
out.write(senders)
out.close