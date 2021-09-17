import sys
print('we assign 1 to X and test if 0 <= $X <= 10')

X=1

if X >= 0 and X <= 10:
	print("X, which is ",X,", is between 0 and 10")
else:
	print("X, which is ",X,", is not between 0 and 10")


print('we assign -1 to X and test if $X < -7 or $X >= 10')

X=-1

if X <= -7  or X >= 10:
	print ("X, which is ",X,", is less than -7 or greater than or equal to 10")
else:
	print("X, which is ",X,", is not less than -7 nor greater than or equal to 10")

print('we assign 100 to X and test if 0 <= $X <= 10 or $X is 100')
X=100

if (X >= 0) and ( X <= 100 or X <= 10):
	print("X, which is ",X,", is between 0 and 10 or is 100")
else:
	print("X, which is ",X,", is not between 0 and 10 and is not 100")

sys.exit(0)
