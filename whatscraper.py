import time
import sys
import re
import urllib.request,urllib.parse

try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")
	print("Please Install it By ")
	print("\tpython3 -m pip install google")
	exit()


def linkcheck(url):
	print('\nTrying URL: '+url,end='\r')
	try:
		r = urllib.request.urlopen(url)
	except:
		return ("","")
	if(r.getcode()!=404):
		r=r.read().decode('utf-8')
		p=r.find('</h2>')
		name=r[r.rfind('">',0,p)+2:p]
		if name.strip()=="":
			return ("","")
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
		if nm!='':
			print('Group Name: '+(nm+" "*(65-len(nm))))
			print('Group Link: ',url)
			f=open('scraped.txt','ab')
			f.write(str.encode(nm+' : '+url+"\n"))
			f.close()
print(r"""

 __      __.__            __   _________                                        
/  \    /  \  |__ _____ _/  |_/   _____/ ________________  ______   ___________ 
\   \/\/   /  |  \\__  \\   __\_____  \_/ ___\_  __ \__  \ \____ \_/ __ \_  __ \
 \        /|   Y  \/ __ \|  | /        \  \___|  | \// __ \|  |_> >  ___/|  | \/
  \__/\  / |___|  (____  /__|/_______  /\___  >__|  (____  /   __/ \___  >__|   
       \/       \/     \/            \/     \/           \/|__|        \/       

""")

if len(sys.argv)>=2:
	if "u" in sys.argv[1]:
		print("Updating Please Wait...")
		try:
			txt=urllib.request.urlopen(url).read()
			f=open(sys.argv[0],'wb')
			f.write(txt)
			f.close()
			print("\tUpdate Successful")
			print("Run "+sys.argv[0]+" Again..")
		except:
			print("Update Failed !!!")
		exit()

print("Initializing...")

query = "intext:chat.whatsapp.com inurl:pastebin"

print("Querying Google By Dorks ...")
for url in search(query, tld="com", num=10, stop=None, pause=2):
	try:
		scrape(url)
	except:
		print("Some Exception Occured!!")
		ch=input("Do You Want To Continue(Y/N): ")
		if not  "Y" in ch:
			exit()
		else:
			continue
