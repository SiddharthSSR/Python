# To check if there is any curse word in the document
#The docs of built-in functions --> https://docs.python.org/2/library/functions.html


import urllib # It is used to open a website (urllib.urlopen)

def read_text():
	quotes = open("/Users/siddharthsingh/Desktop/Python/movie_quotes.txt")
	contents_of_file = quotes.read()
	#print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	#print (output)
	if "true" in output:
		print ("Profanity found")
	elif "false" in output:
		print ("All perfect")
	else :
		print("Could not read the document") 
	connection.close()
	
read_text()