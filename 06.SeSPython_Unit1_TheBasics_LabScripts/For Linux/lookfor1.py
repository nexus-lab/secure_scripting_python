from subprocess import check_output
output = check_output(['grep', 'gry', 'dict.txt']).decode("utf-8")
print(output)
