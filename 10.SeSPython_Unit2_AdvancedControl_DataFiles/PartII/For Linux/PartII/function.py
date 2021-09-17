import subprocess

def call(args):
	proc = subprocess.Popen([args], stdout = subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	return out

def main():
	cmd = input(">")
	callAndPrint(cmd)
	
def callAndPrint(args):
	args = call(args)
	for result in args:
		print (result, "\n")
main()
