import time
import re
import urllib.request,urllib.parse

try: 
	from googlesearch import search 
except ImportError:  
	print("No module named 'google' found") 


def linkcheck(url):
	print('\n\nTrying URL: '+url+'\n')
	try:
		r = urllib.request.urlopen(url)
	except:
		return ("","")
	if(r.getcode()!=404):
		r=r.read().decode('utf-8')
		p=r.find('</h2>')
		name=r[r.rfind('">',0,p)+2:p]
		return (name,url)
	return ("","")
def pad(s):
	if not "invite" in s:
		p=s.find('.com')
		s=s[:p+4]+"/invite"+s[p+4:]
	return s
def scrape(url):
	txt=urllib.request.urlopen(url).read().decode('utf8')
	match=re.findall(r'(https:\/\/chat\.whatsapp\.com\/[a-zA-Z0-9]{22})',txt)
	match=list(set(match))
	for lmt in match:
		lmt=pad(lmt)
		nm,url=linkcheck(lmt)
		if nm!='' and nm not in name:
			print('Group Name: ',nm)
			print('Group Link: ',url)
			f=open('scraped.txt','ab')
			f.write(str.encode(nm+' : '+url+"\n"))
			f.close()
query = "intext:chat.whatsapp.com inurl:pastebin"
for url in search(query, tld="com", num=10, stop=None, pause=2): 
	print(url)
	scrape(url)
