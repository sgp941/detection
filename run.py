#!/usr/bin/python

import os
from subprocess import call

dirs = os.listdir(".")
dirs = [x[0] for x in os.walk(".") if "git" not in x[0]]
dirs.pop(0)
print dirs

configFileName = "config.txt"

totalDirs = len(dirs)


for (count, dir) in enumerate(dirs):
	print "=============================================================================="
	print "WE ARE ON FILE " + str(count) + " OF " + str(totalDirs)
 	print "=============================================================================="

	os.chdir(dir)
	print call("pwd")
	call(["../HoughForests", "0", configFileName])
	os.chdir("..")
	# call("cd ..", shell=True)





