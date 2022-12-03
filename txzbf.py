from zipfile import ZipFile
import sys
import os

os.system("clear")

print("""\033[0;31m
			 _______  __  ________ ____  
			|_   _\ \/ / |__  /_ _|  _ \ 
			  | |  \  /    / / | || |_) |
			  | |  /  \   / /_ | ||  __/ 
			  |_| /_/\_\ /____|___|_|                         
	 ____  ____  _   _ _____ _____ _____ ___  ____   ____ _____ ____  
	| __ )|  _ \| | | |_   _| ____|  ___/ _ \|  _ \ / ___| ____|  _ \ 
	|  _ \| |_) | | | | | | |  _| | |_ | | | | |_) | |   |  _| | |_) |
	| |_) |  _ <| |_| | | | | |___|  _|| |_| |  _ <| |___| |___|  _ < 
	|____/|_| \_\\\___/  |_| |_____|_|   \___/|_| \_\\\____|_____|_| \_\\| MR.THENUX
                                               
\033[0;32m""")

while(True):
	try:
		exit=False
		action=input("\nENCRYPTED ZIP(PATH) >> ")
		if(action=="quit"):
			exit=True
			break
		else:
			pass
		try:
			zip=ZipFile(action,"r")
			break
		except:
			if(action==""):
				pass
			else:
				print("\n\033[0;31m[!] Unable to locate the zip file!\033[0;32m")
	except:
		pass
	
if (exit==True):
	sys.exit()
else:
	pass
list=input("\nPASSWORD LIST(PATH) >> ")
try:
	word=open(list,"rb")
	count=open(list,"r")
except:
	print("\n\033[0;31m[!] Unable to locate the password list!\033[0;32m")
	sys.exit()

line=count.readline()
condition=0
while(line):
	password=word.readline()
	try:
		zip.extractall(path="Extract",pwd=password.strip())
		print("\n\033[1;33m[Password Found!] :: {}".format(password.decode()))
		condition+=1
		break
	except:
		print(password.decode())
	line=count.readline()
if(condition==0):
	print("\n\033[0;31m[Password not found!]")
else:
	pass
		
zip.close()
word.close()
count.close()