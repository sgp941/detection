#!/usr/bin/python
import string
import os

def saveFile(filename, data):
	# Saving new tokenised file
	dirname = filename + "txt1"
	if not os.path.exists(dirname):
		os.makedirs(dirname)
	fh = open(dirname + "/" + "config.txt", 'w+')
	fh.write(str(data))


def readFileContents(filename):
	# Opening Base file, and getting the base config
	with open(filename, 'r') as myfile:
	    data = myfile.read()
	return data


baseFileName = 'config_base.txt'
delim = ","

# Replacing tokens
for i in range(5):
	for j in range(5):
		for k in range(5):
			for l in range(5):
				for m in range(5):
					data = readFileContents(baseFileName)
					data = data.replace('<numTrees>', str(i))
					data = data.replace("<patchWidth>", str(j))
					data = data.replace("<patchHeight>", str(k))
					data = data.replace("<samplePatchesPos>", str(l))
					data = data.replace("<samplePatchesNeg>", str(m))
					filename = str(i) + delim + str(j) + delim + str(k) + delim + str(l) + delim + str(m)
					saveFile(filename, data)








	#	i :	 <numTrees>
	#	j :	 <patchWidth>
	#	k :	 <patchHeight>
	#	l :	 <samplePatchesPos>
	#	m :	 <samplePatchesNeg>


