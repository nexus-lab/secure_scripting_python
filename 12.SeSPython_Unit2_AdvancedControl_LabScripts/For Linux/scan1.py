#! /bin/sh
#
#
#if master file not there, create it
#
import subprocess
import os

for root, dirs, files in os.walk("sample"):
	for filename in files:
		proc = subprocess.Popen(["ls -sail sample/" + filename],stdout=subprocess.PIPE, shell=True)
		(ls, err) = proc.communicate()

		proc = subprocess.Popen(["shasum sample/" + filename],stdout=subprocess.PIPE, shell=True)
		(sha, err) = proc.communicate()
		print (ls.rstrip() , sha.rstrip())