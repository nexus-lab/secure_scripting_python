import re
mystring = 'hello'
#pattern = re.compile(r's/l/X')
#newstring = pattern.sub(r's/l/X', mystring)
newstring = re.sub(r's/l/', "X", mystring)
print newstring
