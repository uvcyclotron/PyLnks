#PyLnks
import subprocess,os

print "Welcome to PyLnks\n"
print "D--Creates a directory symbolic (soft/shortcut) link. Default is a file symbolic link.\
		\nH--Creates a hard link instead of a symbolic link. (Works for files) \
		\nJ--Creates a Directory Junction. (For Directory Hard links)\n"
opt=raw_input("[D]irectory Symlink or [H]ard link or Directory [J]unction?\n")
if str(opt).upper() == 'D' or str(opt).upper() == 'J':
	_fileOrDir = "Dir"
	tgt=raw_input("\nEnter path for target source directory\n")
	while not os.path.exists(str(tgt)):
		print "Target not found! "
		tgt=raw_input("\nPlease enter a valid target source path..\n")
	lnk=raw_input("\nEnter path where dir link is to be created\n")
	while os.path.exists(str(lnk)):
		print "A dir already exists here."
		lnk=raw_input("\nEnter a new path for link directory..\n")
else:
	_fileOrDir = "File"
	tgt=raw_input("\nEnter path for target source file\n")
	while not os.path.isfile(str(tgt)):
		print "Target file not found."
		tgt=raw_input("\nPlease enter a valid target filepath..\n")
	lnk=raw_input("\nEnter path for link file with linkname\n")
	while os.path.isfile(str(lnk)):
		print "A file already exists here with that name."
		lnk=raw_input("\nEnter a new path for link file..\n")
#print os.path.exists(str(lnk))


if (len(opt)>0):
	param=" /"+str(opt).upper()
else:
	param=""  #--?why. just quit.

callcmd="mklink"+param+" "+str(lnk)+" "+str(tgt) #uppercase not rqd, still put
print "\nrunning.."
y=subprocess.call(callcmd,shell=True)
if (y==0):
	print "Success!" #0 sucess
else:
	print "Error occurred"



