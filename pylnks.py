#PyLnks
import subprocess

print "Welcome to PyLnks\n"
print "D--Creates a directory symbolic (soft) link.  Default is a file symbolic link.\nH--Creates a hard link instead of a symbolic link. (Works for files) \nJ--Creates a Directory Junction. (For directory hard links)\n"
opt=raw_input("[D]irectory Symlink or [H]ard link or Directory [J]unction?\n")
tgt=raw_input("\nEnter path for target file\directory\n")
lnk=raw_input("\nEnter path for link file\directory\n")
if (len(opt)>0):
	param=" /"+str(opt).upper()
else:
	param=""
callcmd="mklink"+param+" "+str(lnk)+" "+str(tgt) #uppercase not rqd, still put
print "\nrunning.."
y=subprocess.call(callcmd,shell=True)
if (y==0):
	print "Success!" #0 sucess
else:
	print "Error occurred"
