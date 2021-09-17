#!/usr/bin/python

import sys

from subprocess import check_output

output = check_output(["cat",sys.argv[1]]).decode("utf-8")

print (output)
