import sys
if len(sys.argv) != 3:
	file_name = sys.argv[0]
	print("Usage:",file_name,"string file")
else:
	with open(sys.argv[2]) as f:
		for line in f:
			if sys.argv[1] in line:
				print(line)
