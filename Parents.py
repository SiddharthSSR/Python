# To check if the name matches with my parent's name

def parent(name):
	if name[0] == 'S' and name[5] == 'y':
		return "His name is same as my Dad"
	elif name[0] == 'R' and name[3] == 'u':
		return "Her name is same as my Mom"
	else :
		return "I don't know these people"

print parent('Sanjay')
print parent('Ritu')
print parent('Green')