import requests
import re
import unicodedata
import string
import conf

emailBody = ""

for ip in open(conf.iplist, "r"):
    url = "http://www.ipvoid.com/scan/%s" % (ip)
    emailBody = emailBody + "IP: "+ip
    resp = requests.get(url)
    string1 = unicodedata.normalize('NFKD', resp.text).encode('ascii','ignore')
    r = string1.translate(string.maketrans("\n\t\r", "   "))
    blacklist = re.search(r'Blacklist Status</td><td><span.+>(\w.+)</span>', r)
    if blacklist != None and blacklist.group(1) == "BLACKLISTED":
         emailBody = emailBody + 'The IP is blacklisted! \n'
         detection = re.search(r'Detection Ratio</td><td>(\d+ / \d+) \(<font', r)
         emailBody = emailBody + 'Detection Ratio was %s \n' % detection.group(1)
         detected_line = re.search(r'\s+<tr><td><img src="(.+)', r)
         detected_sites = re.findall(r'Favicon" />(.+?)</td><td><img src=".+?" alt="Alert" title="Detected!".+?"nofollow" href="(.+?)" title', detected_line.group(1))
         for site in detected_sites:
             emailBody = emailBody + "List Name:" + site[0] + "Url: "+ site[1] + "\n\n"
    else:
         emailBody = emailBody + 'Not blacklisted...\n\n'

print emailBody

import datetime
dates = []
today = datetime.date.today()
dates.append(today)

import smtplib


session = smtplib.SMTP_SSL(conf.hostname, conf.port)
session.login(conf.username,conf.password)
headers = ["from: " + conf.fromAdd,
           "subject: " + "Blacklist check ",
           "to: " + conf.toAdd,
           "mime-version: 1.0",
           "content-type: text/plain"]
headers = "\r\n".join(headers)

session.sendmail(conf.fromAdd, conf.toAdd, headers + "\r\n\r\n" + emailBody)

