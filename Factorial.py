#Ques- WAP to find the factorial of first n numbers. (using for loop)
x = int(input("Enter a Number : "))
factorial = 1

for i in range(1,x+1):
  factorial = factorial*i
  print(factorial)

# We can also do this by While  loop as well

x = int(input("Enter a Number : "))
i = 1 
factorial = 1

while i<=x:
   factorial = factorial*i
   i+=1
   print(factorial)

