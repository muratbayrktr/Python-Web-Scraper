import urllib.request, urllib.error, urllib.parse
import re
import requests
import time

while True:
    link = input("insert your link: ")
    if re.search('^http://.+',link) or re.search('^https://.+',link):
        print('link is appropriate.')
        break
linklist = []


try:
    fhand = urllib.request.urlopen(link)
except:
    print('Cannot reach remote server. Exiting... ')
    exit(1)


print("connection successful!")

for line in fhand:
    dc_line = line.decode().strip()
    #print(dc_line)
    linklist = linklist + re.findall('href="(.*?)"', dc_line)
    linklist = linklist + re.findall("href='(.*?)'", dc_line)


valid_link_list = []
non_valid_link_list = []
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
ct = 0
for i in linklist:
    if re.search('^http.+?',i):
        try:
            if requests.get(i):
                print("1 valid link found."+ str(i) )
                valid_link_list.append(i)
        except:
            ConnectionError
    else:
        non_valid_link_list.append(i)
    ct += 1
    if ct == 10: time.sleep(2)
print("###############   HERE ARE THE VALID LINKS   ###############")
for i in valid_link_list:
    print(i)
print("###############   HERE ARE THE NON VALID LINKS   ###############")
for i in range(0,len(non_valid_link_list)):
    print(non_valid_link_list[i])
    if i == 5:
        print("list goes on \n.\n.\n.")
        break