def celcius_to_fahrenheit(celcius):
	fahrenheit = celcius * (9/5) + 32
	return fahrenheit

temperatures = [10, -20, -289, 100]
with open("temps.txt", "w") as file:
	for temp in temperatures:
		if temp >= -273.15:
			file.write(str(celcius_to_fahrenheit(temp))+"\n")

