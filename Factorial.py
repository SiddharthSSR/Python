#To find factorial of a number 

def factorial(n):
  	fact = 1
  	while(n != 0):
  		fact = fact * n
  		n  = n - 1
  	
  	return fact


print factorial(3)
print factorial(4)
print factorial(6)