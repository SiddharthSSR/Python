i = 2
sum = 0
while(i < 20000000):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : 
   	 	sum += i
   i = i + 1

print (sum)


