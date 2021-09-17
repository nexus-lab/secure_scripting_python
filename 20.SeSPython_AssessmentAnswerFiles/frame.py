import sys

if len(sys.argv)-1 != 1:
	print("Usage: "+sys.argv[0]+" file")
	sys.exit(1)
	
print(sys.argv[0]+":")
f = open(sys.argv[1],'r')
print(f.read())
sys.exit(0)