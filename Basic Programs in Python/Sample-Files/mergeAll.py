import glob
import datetime

filenames = glob.glob("*.txt")
with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")+".txt", "a") as file:
	for current_file in filenames:
		with open(current_file, "r") as curr_f:
			file.write(curr_f.read()+"\n")