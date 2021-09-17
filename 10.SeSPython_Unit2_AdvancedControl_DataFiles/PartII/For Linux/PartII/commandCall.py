from subprocess import call
output_result = call(["ls","-l"])
print(output_result)