import sys


def incrementby1(i):
	return i + 1


def main():
	print(incrementby1(int(sys.argv[1])))


main()
