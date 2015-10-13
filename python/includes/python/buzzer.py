#!/usr/bin/python
import urllib2, requests
import sys, os, time
from bs4 import BeautifulSoup

import smtplib
from email.mime.text import MIMEText

def strip(text):
	"""removes html tags from given string"""
	text = str(text)
	while text[0] == '<':
		start_index = text.find('>')+1
		end_index = text.rfind('<')
		if start_index == -1 or end_index == -1:
			return False
		#print str(start_index) + " s-e " + str(end_index)
		text = text[start_index:end_index].lstrip().rstrip()
	return text

def SendMail(results):
    return requests.post(
        "https://api.mailgun.net/v2/sandbox1430d61184d84a7da1a04bb7dab858c5.mailgun.org/messages",
        auth=("api", "key-41ca100913242ae5d0160aa2f1c27177"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox1430d61184d84a7da1a04bb7dab858c5.mailgun.org>",
              "to": "Ckone <ckone3000@gmail.com>",
              "subject": "Buzzer Test",
              "text": "Leumi Buzzer Benfits for the " + time.strftime("%x") + ":\n" \
              + results,
              "html": "<html><h1>Leumi Buzzer Benfits for the " + time.strftime("%x") + "</h1>" \
              + results + \
              "<a href=\"http://www.leumibuzzer.co.il/bidur.aspx\">Leumi Buzzer</a></html>"})

url = "http://www.leumibuzzer.co.il/bidur.aspx"
hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=hdr)).read())

res = soup.find("table", { "id" : "hatavotTbl" }).find_all("h4")
result = "<div>".encode("utf-8")

for det in res:
	result = result + "<p>" + strip(det.encode("utf-8"))+ "</p>"
result = result + "</div>"
SendMail(result)