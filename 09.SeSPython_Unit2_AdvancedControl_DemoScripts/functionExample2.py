result = 0


def main():
	incrementby1()
	print result


def incrementby1():
	global result
	result = result + 1


main()
