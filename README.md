# Python-Web-Scraper
A python script that searches the website from the url that had been entered to program.

Hey everyone ! 

In this particular code I used urllib to connect to URLs. 
I checked the entry URLs with Regular Expressions :

while True:
    link = input("insert your link: ")
    if re.search('^http://.+',link) or re.search('^https://.+',link): # regex part
        print('link is appropriate.')
        break
        
        
Then I pulled the data from the web page and used regular expressions again to check for the 
"href='...'" values among the code. I pulled all the datas but sometimes links can be broken.

What I do here is that I send GET requests and if the requests return 200 OK then I classify the link 
as valid. Otherwise they're classified as invalid.



