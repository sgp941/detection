#!/usr/bin/python

import os
from subprocess import call

dirs = os.listdir(".")

configFileName = "config.txt"

for dir in dirs:
	os.chdir(dir)
	print call("pwd")
	call(["../HoughForests", "0", configFileName])
	os.chdir("..")
	# call("cd ..", shell=True)





