import datetime

def merge(fromFile, toFile):
	current_file = open(fromFile, "r")
	content = current_file.read()
	with open(toFile, "a") as file:
		file.write(content+"\n")
	current_file.close()
	return toFile

now = datetime.datetime.now()
fileName = now.strftime("%Y-%m-%d-%H-%M"+".txt")
toFile = merge("Sample-Files/file1.txt", fileName)
toFile = merge("Sample-Files/file2.txt", fileName)
toFile = merge("Sample-F0iles/file3.txt", fileName)