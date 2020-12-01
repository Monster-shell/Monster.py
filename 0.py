# Decompiled By Monster
# Github : https://github.com/Monster-shell
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jul  8 2020, 22:53:57) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 Monster.py')

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16;')]

def exit():
    print '[!] Exit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def hamza(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


banner = '\n\x1b[1;96m    ______   ____    _____ \n\x1b[1;96m   |  ____| |  _ \\  |_   _|\n\x1b[1;96m   | |__    | |_) |   | |  \n\x1b[1;96m   |  __|   |  _ <    | |  \n\x1b[1;96m   | |      | |_) |  _| |_ \n\x1b[1;96m   |_|      |____/  |_____|\n\n                                                \n\x1b[1;91m-----------------------------------------------\n\x1b[1;92m\xe2\x9e\xa3 OWNER      :  KURD X TOOL \n\x1b[1;92m\xe2\x9e\xa3 Dev        :  Biyar Hussein\n\x1b[1;92m\xe2\x9e\xa3 Facebook   :  Biyar Hussein\n\x1b[1;92m\xe2\x9e\xa3 Telegarm   :  Biyar007\n\x1b[1;91m-----------------------------------------------'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r[\xe2\x9c\x94] Logging In ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
id = []

def tlogin():
    os.system('clear')
    print banner
    username = raw_input('[+] TOOL USERNAME: ')
    if username == 'monster':
        os.system('clear')
        print banner
        print '[\xe2\x9c\x93] TOOL USERNAME: ' + username + ' (correct)'
    else:
        print '[!] Invalid Username.'
        time.sleep(1)
        tlogin()
    passw = raw_input('[+] TOOL PASSWORD: ')
    if passw == 'hama':
        os.system('clear')
        print banner
        print '[\xe2\x9c\x93] TOOL USERNAME: ' + username + ' (Rasta)'
        print '[\xe2\x9c\x93] TOOL PASSWORD: ' + passw + '  (Rasta)'
        time.sleep(2)
    else:
        print '[!] Invalid Password.'
        time.sleep(1)
        tlogin()
    try:
        toket = open('login.txt', 'r')
        os.system('python2 .Monster.py')
    except (KeyError, IOError):
        methodlogin()
    else:
        print '[!] Invalid Password'
        time.sleep(1)
        tlogin()


def methodlogin():
    os.system('clear')
    print banner
    print '[1] Login With ID/Password.'
    print '[2] Login Using Token.'
    print '[0] Exit.'
    print '      '
    hos = raw_input('\nChoose Option >>  ')
    if hos == '':
        print '[!]  Wrong Input'
        exit()
    elif hos == '1':
        login()
    elif hos == '2':
        os.system('clear')
        print banner
        hosp = raw_input('[+] Give Token : ')
        tik()
        hopa = open('login.txt', 'w')
        hopa.write(hosp)
        hopa.close()
        print '\n[\xe2\x9c\x93] Logged In Successfully.'
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/Dzha.Maza.OZANMM')
        os.system('python2 .Monster.py')
    elif hos == '3':
        os.system('clear')
        os.system('python2 login.py')
    elif hos == '0':
        exit()
    else:
        print '[!] Wrong Input'
        exit()


def login():
    os.system('clear')
    try:
        tb = open('login.txt', 'r')
        os.system('python2 .Monster.py')
    except (KeyError, IOError):
        os.system('clear')
        print banner
        hamza('[!] HACK MHAMAD')
        hamza('[!] Use a New Facebook Account To Login')
        print '-------------------------------------'
        iid = raw_input('[+] Number/Email: ')
        id = iid.replace(' ', '')
        pwd = raw_input('[+] Password : ')
        tik()
        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + id + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        z = json.load(data)
        if 'access_token' in z:
            st = open('login.txt', 'w')
            st.write(z['access_token'])
            st.close()
            print '\n[\xe2\x9c\x93] Logged In Successfully.'
            time.sleep(1)
            os.system('xdg-open https://www.facebook.com/Dzha.Maza.OZANMM')
            os.system('clear')
            os.system('python2 .Monster.py')
        elif 'www.facebook.com' in z['error_msg']:
            print '[!] User Must Verify Account Before Login.'
            time.sleep(3)
            login()
        else:
            print '[!]Number/User Id/ Password Is Wrong !'
            time.sleep(1)
            login()


if __name__ == '__main__':
    tlogin()
