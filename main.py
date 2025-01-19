import os
import sys
tempDir = os.getenv("TEMP")
scriptDir = os.path.abspath(os.path.dirname(__file__))
launchPath = f"{tempDir}/ielaunch_temp.hta"
f = open(f"{scriptDir}/ielaunch.hta")
ielaunch = f.read()
f.close()
def launch():
	print(f"Launching {url} on Internet Explorer!")
	os.system(f"C:/Windows/System32/mshta.exe {launchPath}")
	if(os.path.exists(launchPath)):
		os.remove(launchPath)

if(len(sys.argv) == 2):
	url = sys.argv[1]
	ielaunch = ielaunch.replace("https://www.google.com", url)
	f = open(launchPath, "w")
	f.write(ielaunch)
	f.close()
	launch()

else:
	startPageError = False
	import winreg
	try:
		with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Internet Explorer\\Main") as key:
			url = winreg.QueryValueEx(key, "Start Page")[0]
	except:
		print("Failed to read start page.")
		startPageError = True
	if(startPageError):
		url = "https://www.google.com"
	
	ielaunch = ielaunch.replace("https://www.google.com", url)
	f = open(launchPath, "w")
	f.write(ielaunch)
	f.close()
	launch()