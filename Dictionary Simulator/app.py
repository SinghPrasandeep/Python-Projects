# To fetch all data from json file and store it in a python dictionary
import json

# To check similarity ratio of words. Specifically using SequenceMatcher in get_close_matches
import difflib

# To return all the words that are closely related to the input word
from difflib import get_close_matches

# Returns definition of the input word
def getMeaning(data, word):
	if word in data:
		return data[word]
	else:
		closest_match = get_close_matches(word, data.keys(), cutoff = 0.8)
		if len(closest_match) > 0:
			print("["+word+"] is not a correct word. Did you mean "+closest_match[0]+" ? ")
			user_input = input("Enter Y for Yes or N for No :")
			if user_input == 'Y' or user_input == 'y' or user_input == "yes":
				return data[closest_match[0]]
			elif user_input == 'N' or user_input == 'n' or user_input == "no":
				w = input("Enter the word again :")
				return getMeaning(data, w.lower())
			else:
				return "We didn't understand your query"
		else:	
			return "Word does not exist! Please check your input"

# Loads data from json into the python dictionary
data = json.load(open("data.json"))
word = input("Enter a word you wish to know the meaning :")
output =  getMeaning(data, word.lower())

# Format the output in a human friendly context
# If the input word has a definition(s), then getMeaning will return a list, else the error msg will be a string
if type(output) == list:
	for item in output:
		print(item) 
else:
	print(output)