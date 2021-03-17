import time
import sys
import re
import os
import urllib.request
import urllib.parse
import threading
from datetime import datetime

try:
    from googlesearch import search
except ImportError:
    print("[!] No module named \"google\" found")
    print("    Please Install it by using:")
    print("\n    python3 -m pip install google")
    exit()

GUI = None
GUI_ACTIVATED = False
SAVE = "scrapped_%s.txt" % datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
global_threads = list()
terminate_threads = False
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


def linkcheck(url):
    print("\nTrying URL:", url, end='\r')
    try:
        r = urllib.request.urlopen(url)
    except:
        return ('', '')
    if(r.getcode() != 404):
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
    match2 = re.findall(
        r"(https:\/\/chat\.whatsapp\.com\/(invite\/)?[a-zA-Z0-9]{22})", txt)
    match = [item[0] for item in match2]
    match = list(set(match))
    for lmt in match:
        if terminate_threads:
            raise Exception('Terminating Threads, nothing to be worried.')
        lmt = pad(lmt)
        nm, url = linkcheck(lmt)
        if nm != '':
            print("[i] Group Name: " + (nm + ' ' * (65 - len(nm))))
            print("[i] Group Link: ", url)

            if GUI_ACTIVATED:
                GUI.appendObjectToList((
                    (nm + ' ' * (65 - len(nm))),
                    url
                ))

            f = open(SAVE, "ab")
            f.write(str.encode(nm + " : " + url + '\n'))
            f.close()


def start(index=0):
    print("[*] Initializing...")
    if index >= len(availabledom):
        return
    query = "intext:chat.whatsapp.com inurl:" + availabledom[index]
    print("[*] Querying Google By Dorks ...")
    for url in search(query, tld="com", num=10, stop=None, pause=2):
        txt = urllib.request.urlopen(url).read().decode("utf8")
        scrape(txt)


def scrap_from_link(index=0):
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
    global GUI
    global GUI_ACTIVATED
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
        if 'g' in sys.argv[1] or '-g' in sys.argv[1] or '--gui' in sys.argv[1]:
            from GUI import MainFrame
            import wx

            class _MainFrame(MainFrame):
                def startScraper(self, event):
                    global global_threads
                    global terminate_threads
                    if self.button_StartScraper.GetLabel() == 'Start Scraper':
                        terminate_threads = False
                        self.button_StartScraper.SetLabel('Stop Scraping')
                        thread = None
                        if self.SelectedInformationOrigin == 0:
                            thread = threading.Thread(target=start)
                        if self.SelectedInformationOrigin == 1:
                            thread = threading.Thread(target=scrap_from_link)
                        if self.SelectedInformationOrigin == 2:
                            thread = threading.Thread(target=star)

                        thread.start()
                        global_threads.append(thread)
                    else:
                        print(f"[*] Stopping threads")
                        terminate_threads = True
                        for thread in global_threads:
                            print(f"\n[*] Stopping thread: {thread.name}\n")
                            thread.join(10)
                            print(
                                f"[i] {thread.name} is {'Alive' if thread.is_alive() else 'Dead'}")
                            del global_threads[global_threads.index(thread)]
                        print(f"[$] Threads stopped")

                        self.button_StartScraper.SetLabel('Start Scraper')

                def RadioGoogle(self, event):
                    self.SelectedInformationOrigin = 0

                def RadioListSite(self, event):
                    self.SelectedInformationOrigin = 1

                # TODO: Add checkfile dialog
                # def RadioCheckFile( self, event ):
                # 	self.SelectedInformationOrigin = 2

            GUI_ACTIVATED = True
            app = wx.App()
            GUI = _MainFrame(None)

            GUI.Show()
            app.MainLoop()

            exit()
        elif 'u' in sys.argv[1] or '-u' in sys.argv[1]:
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
   4> Update WhatScrapper
	""")

    try:
        inp = int(input("[#] Enter Choice: "))
    except:
        print("\t[!] Invalid Choice..")
        exit()

    if inp != 4:
        newSave = str(
            input("[#] Enter Saving File (Default is scrapped.txt): "))
        SAVE = "scrapped.txt" if newSave == '' else newSave

        f = open(SAVE, 'w')
        f.write(
            "Group Links Generated By WhatScrapper \nGet it at https://github.com/TheSpeedX/WhatScrapper\r\n")
        f.close()

    if inp == 1:
        for i in range(0, int(input("[#] Enter the number of threads(1-" + str(len(availabledom)) + "):- "))):
            thread = threading.Thread(target=start, args=(i,), daemon=True)
            thread.start()
            threads.append(thread)

        for i in threads:
            i.join()
    elif inp == 2:
        for i in range(0, int(input("[#] Enter the number of threads(1-" + str(len(site_urls)) + "):- "))):
            thread = threading.Thread(
                target=scrap_from_link, args=(i,), daemon=True)
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
                thread = threading.Thread(
                    target=scrape, args=(b'\n'.join(head),), daemon=True)
                thread.start()
                threads.append(thread)
            thread = threading.Thread(
                target=scrape, args=(strm.read(),), daemon=True)
            thread.start()
            threads.append(thread)
        for i in threads:
            i.join()
    elif inp == 4:
        print("[*] Updating Please Wait...", end='\r')
        try:
            txt = urllib.request.urlopen(
                "https://github.com/TheSpeedX/WhatScraper/raw/master/whatscraper.py").read()
            f = open(sys.argv[0], "wb")
            f.write(txt)
            f.close()
            print("[$] WhatScraper updated successfully")
            print("[i] Run " + sys.argv[0] + " Again..")
        except:
            print("[!] Update Failed !!!     ")
        exit()
    else:
        print("[!] Invalid Choice..")


if __name__ == "__main__":
    main()
