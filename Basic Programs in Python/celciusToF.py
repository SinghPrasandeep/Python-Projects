def celcius_to_fahrenheit(celcius):
	if celcius < -273.15:
		return "This temperature is not possible!"
	else:
		fahrenheit = celcius * (9/5) + 32
		return fahrenheit

temperatures = [10, -20, -289, 100]
for temp in temperatures:
	print(celcius_to_fahrenheit(temp))