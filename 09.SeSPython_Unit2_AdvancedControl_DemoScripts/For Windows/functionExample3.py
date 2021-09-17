import sys


def main():
	print (roundto10(13))
	print (roundto10(50))
	print (roundto10(97))


def roundto10(num):
	units = num % 10
	tens = num / 10
	if units >= 5:
		tens = tens + 1
	return tens * 10


main()
