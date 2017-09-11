#For providing break each after 2 hours and playing your 
# favourite site

import time
import webbrowser

total = 3
count = 0

while(count <= total):
	time.sleep(20)
	webbrowser.open("https://soundcloud.com/kristianpedersen/this-dot-feat-daniel-shiffman")
	count = count + 1

