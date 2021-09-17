#! /bin/sh
#
#
#if master file not there, create it
#
import subprocess
import os

for root, dirs, files in os.walk("."):
	for filename in files:
		proc = subprocess.Popen(["ls -sail " + filename],               ##for Linux
		## proc = subprocess.Popen(["dir" + filename],                  ##for Windows
								stdout=subprocess.PIPE, shell=True)
		(ls, err) = proc.communicate()

		proc = subprocess.Popen(["shasum " + filename],                           ##for Linux
		## proc = subprocess.Popen(["certutil -hashfile",'"', filename, '"'],     ##for Windows
								stdout=subprocess.PIPE, shell=True)
		(sha, err) = proc.communicate()
		print (ls.rstrip() + "" + sha.rstrip())