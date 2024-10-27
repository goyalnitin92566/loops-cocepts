#printing the numbers in the range of 1 to n using for loop

x = int(input("Enter a Number :"))
y = int(input("Enter a Number :"))
 
for i in range(x,y,1):
  print(i)

# # We can also do this by while loop as well

x = int(input("Enter a Number :"))
i = 1

while(i<=x):
  i+=1
  print(i)