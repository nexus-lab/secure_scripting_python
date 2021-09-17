import sys
try:
	num1 = int(input("enter a number: "))
	num2 = int(input("enter a number: "))
except ValueError:
	print("Error: numbers only")
	sys.exit()
else:
	print(num1 + num2)