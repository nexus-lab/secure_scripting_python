# Read in the file
with open('connect2.csv', 'r') as file:
    filedata = file.read()
    # Replace the target string
    filedata = filedata.replace(',', ' ')

    # Write the file out again
with open('connect3.csv', 'w') as file:
    file.write(filedata)
