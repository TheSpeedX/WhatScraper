import time
import sys
import re, os
import urllib.request, urllib.parse, threading
import requests
from bs4 import BeautifulSoup
from datetime import datetime

try:
    from googlesearch import search
except ImportError:
    print("[!] No module named \"google\" found")
    print("    Please Install it by using:")
    print("\n    python3 -m pip install google")
    exit()

SAVE = "scrapped_%s.txt" % datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
availabledom = ["pastebin",
                "throwbin",
                "pastr",
                "pasteio",
                "paste2",
                "paste"]
site_urls = ["https://whatsgrouplink.com/",
             "https://whatsappgroups.app/job-alerts-whatsapp-group-links/",
             "https://whatsappgroups.app/whatsapp-group-links/",
             "https://whatsappgroups.app/pubg-whatsapp-group-links-india/",
             "https://whatsappgroups.app/funny-jokes-whatsapp-group-links/",
             "https://allinonetrickz.com/new-whatsapp-groups-invite-links/"]


def save_url():
    # This method is natively coded by MushtaqAlvi if you use this anymore dont forget to reference https://github.com/MushtaqAlvi
    print('Please paste your Whatsapp Group Link:\n')
    GroupLink = input()
    GroupIconLink = ""
    GroupName = ""
    print('\n     !--------------------!\n\nAnalyzing Group link : ')
    print(GroupLink)
    # requesting webpage for html content
    try:
        r = requests.get(GroupLink)
    except:
        print('\nInternet Connection Error!')

    # creating soup object for better vision and scrapping
    soup = BeautifulSoup(r.content, 'html.parser')

    # data scraping from html through all meta tags

    for meta in soup.find_all('meta'):
        # getting all links in content value of meta tags one by one
        IconLink = meta.get('content')
        if str(meta.get('property')) == str('og:title'):
            GroupName = str(meta.get('content'))

        if type(IconLink) == type('string'):

            if IconLink.find('pps.what') != -1:

                GroupIconLink = IconLink
                # GroupIconLink = IconLink
                try:
                    print('Trying to fetch Group Icon')
                    rr = requests.get(IconLink)
                    print('done...!')
                except:
                    print('     !--------------------!\nInter net Connection Error!\n')
                try:
                    print('Trying to save Group Details')
                    file_name = '' + GroupLink[26:] + ' - ' + GroupName + '.png'
                    file = open(str(file_name), 'wb')
                    file.write(rr.content)
                    file.close()
                    print('Group Icon Downloaded and Renamed with Group ID + Group Name')

                except:
                    print('\n!---Failed to Save Group Details---!\n')

    if str(GroupIconLink) != "":
        print('Group name is : ')
        print(GroupName)
        print('Group icon (DP) Image file link is:')
        print(GroupIconLink)
        print('\n     !--------------------!')
    else:
        print('Group not Found')
        print('\n     !--------------------!')
    print('Contributor: MushtaqAlvi')
    print('https://github.com/MushtaqAlvi/WhatsDiger-v1.0')


def linkcheck(url):
    print("\nTrying URL:", url, end='\r')
    try:
        r = urllib.request.urlopen(url)
    except:
        return ('', '')
    if (r.getcode() != 404):
        r = r.read().decode("utf-8")
        p = r.find("</h2>")
        name = r[r.rfind("\">", 0, p) + 2:p]
        if name.strip() == '':
            return ('', '')
        return (name, url)
    return ('', '')


def pad(s):
    if not "invite" in s:
        p = s.find(".com")
        s = s[:p + 4] + "/invite" + s[p + 4:]
    return s


def scrape(txt):
    if type(txt) == type(b''):
        txt = txt.decode("utf-8")
    match = []
    match2 = re.findall(r"(https:\/\/chat\.whatsapp\.com\/(invite\/)?[a-zA-Z0-9]{22})", txt)
    match = [item[0] for item in match2]
    match = list(set(match))
    for lmt in match:
        lmt = pad(lmt)
        nm, url = linkcheck(lmt)
        if nm != '':
            print("[i] Group Name: " + (nm + ' ' * (65 - len(nm))))
            print("[i] Group Link: ", url)
            f = open(SAVE, "ab")
            f.write(str.encode(nm + " : " + url + '\n'))
            f.close()


def start(index):
    print("[*] Initializing...")
    if index >= len(availabledom):
        return
    query = "intext:chat.whatsapp.com inurl:" + availabledom[index]
    print("[*] Querying Google By Dorks ...")
    for url in search(query, tld="com", num=10, stop=None, pause=2):
        txt = urllib.request.urlopen(url).read().decode("utf8")
        scrape(txt)


def scrap_from_link(index):
    print("[*] Initializing...")
    if index >= len(site_urls):
        return
    r = urllib.request.urlopen(site_urls[index]).read().decode()
    scrape(r)


def get_terminal_size(fallback=(80, 24)):
    for i in range(0, 3):
        try:
            columns, rows = os.get_terminal_size(i)
        except OSError:
            continue
        break
    else:
        columns, rows = fallback
    return columns, rows


def main():
    global SAVE
    terminal_size = get_terminal_size()

    if terminal_size[0] < 80:
        print("""


              __            
   (   // __/(  _ _ _   _ _ 
   |/|//)(//__)( / (//)(-/  
                    /       


		""")
    else:
        print("""


    _       ____          __  _____                                
   | |     / / /_  ____ _/ /_/ ___/______________ _____  ___  _____
   | | /| / / __ \/ __ `/ __/\__ \/ ___/ ___/ __ `/ __ \/ _ \/ ___/
   | |/ |/ / / / / /_/ / /_ ___/ / /__/ /  / /_/ / /_/ /  __/ /    
   |__/|__/_/ /_/\__,_/\__//____/\___/_/   \__,_/ .___/\___/_/     
						/_/                 

	""")

    if len(sys.argv) >= 2:
        if 'u' in sys.argv[1] or '-u' in sys.argv[1]:
            print("[*] Updating Please Wait...", end='\r')
            try:
                txt = urllib.request.urlopen(
                    "https://github.com/TheSpeedX/WhatScraper/raw/master/whatscraper.py").read()
                f = open(sys.argv[0], "wb")
                f.write(txt)
                f.close()
                print("[$] Update Successful")
                print("[i] Run " + sys.argv[0] + " Again..")
            except:
                print("[!] Update Failed !!!     ")
            exit()

    threads = []
    print("""
   1> Scrape From Google
   2> Scrape From Group Sharing Sites [BEST]
   3> Check From File
   4> Check And Retrieve specific Group Details(+Download DP).
   5> Update WhatScrapper
	""")

    try:
        inp = int(input("[#] Enter Choice: "))
    except:
        print("\t[!] Invalid Choice..")
        exit()

    if inp != 4:
        newSave = str(input("[#] Enter Saving File (Default is scrapped.txt): "))
        SAVE = "scrapped.txt" if newSave == '' else newSave

        f = open(SAVE, 'w')
        f.write("Group Links Generated By WhatScrapper \nGet it at https://github.com/TheSpeedX/WhatScrapper\r\n")
        f.close()

    if inp == 1:
        for i in range(0, int(input("[#] Enter the number of threads(1-" + str(len(availabledom)) + "):- "))):
            thread = threading.Thread(target=start, args=(i,))
            thread.start()
            threads.append(thread)

        for i in threads:
            i.join()
    elif inp == 2:
        for i in range(0, int(input("[#] Enter the number of threads(1-" + str(len(site_urls)) + "):- "))):
            thread = threading.Thread(target=scrap_from_link, args=(i,))
            thread.start()
            threads.append(thread)

        for i in threads:
            i.join()
    elif inp == 3:
        path = input("[#] Enter Whatsapp Link File Path: ").strip()
        if not os.path.isfile(path):
            print("\t[!] No such file found...")
            exit()
        thn = int(input("[#] Enter the number of threads: "))
        op = open(path, "rb").read().decode("utf-8")
        op = op.count('\n') // thn
        with open(path, "rb") as strm:
            for i in range(thn - 1):
                head = [next(strm) for x in range(op)]
                thread = threading.Thread(target=scrape, args=(b'\n'.join(head),))
                thread.start()
                threads.append(thread)
            thread = threading.Thread(target=scrape, args=(strm.read(),))
            thread.start()
            threads.append(thread)
        for i in threads:
            i.join()
    elif inp == 5:
        print("[*] Updating Please Wait...", end='\r')
        try:
            txt = urllib.request.urlopen("https://github.com/TheSpeedX/WhatScraper/raw/master/whatscraper.py").read()
            f = open(sys.argv[0], "wb")
            f.write(txt)
            f.close()
            print("[$] WhatScraper updated successfully")
            print("[i] Run " + sys.argv[0] + " Again..")
        except:
            print("[!] Update Failed !!!     ")
        exit()
    elif inp == 4:
        save_url()
    else:
        print("[!] Invalid Choice..")


if __name__ == "__main__":
    main()
