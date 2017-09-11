# To find the bigger number of the two

def bigger(a, b):
	if(a > b):
		return a
	elif(a == b) :
		return "equal"
	else :
		return b

print bigger(2, 7)
print bigger(3, 3)
print bigger(3, 1)