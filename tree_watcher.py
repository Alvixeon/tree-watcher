#A folder specific file watcher I guess.
#https://docs.python.org/3/howto/logging.html
#https://stackoverflow.com/questions/18194968/python-remove-duplicates-from-2-lists

#Imports
import logging,os,time,sys
#end of imports

#globals
#end of globabls


#The main watcher function
def watcher():
	ilog("Prompting user to set path.")
	path = input ("Enter in the path to the directory:")
	if checkdir(path):
		pass
	else:
		print ("[*] The path was not found.")
		watcher()
	ilog("Starting watcher in path: " + path)
	print ("Starting watcher, Press ctrl+c to quit.")
	while True:
		try:
			global ls
			ls = []
			for cuck,dirs,files in os.walk(path):
				for f in files:
					ls.append(f)
			time.sleep(3)
			global ts
			ts = []
			for cuck,dirs,files in os.walk(path):
				for f in files:
					ts.append(f)
			global gm
			gm = []
			for cuck,dirs,files in os.walk(path):
				for f in files:
					gm.append(f)
			ls,ts = listDestroy(ls,ts,gm)

			for i in ts:
				print (i + " Was created in " + path)
			for i in ls:
				print (i + " Was deleted from " + path)
			print ("WOIJHFFFFFFFFFFF")
		except KeyboardInterrupt:
			print ("[*] Ctrl+c detected,closing.")
			ilog("Ctrl+c detected, closing application.")
			time.sleep(3)
			sys.exit(1)
#end watcher function

#function to eliminate dupes from list
def listDestroy(ls,ts,gm):
	#ts = set(ls) - set(ts)
	ts = set(ts) - set(ls)
	ls = set(ls)-set(gm)
	return ls,ts
#end listDestroy function

#Info log function for easy access
def ilog(entry):
	logging.info(entry)
#end ilog function

#Warning log function for easy access
def wlog(entry):
	logging.warning(entry)
#end wlog function

#function to check if the specified directory exists	
def checkdir(path):
	if os.path.isdir(path):
		ilog(" path was queried and does exist.")
		return True
	else:
		wlog(" Specified path" + path + " does not exist.")
		return False
#end checkdir function

ilog("Initializing watcher")
watcher()
