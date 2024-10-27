#Ques- WAP to find the sum of first n numbers. (using while)

x = int(input("Enter a Number : "))
i = 1
sum = 0
while(i<=x):
  sum = sum + i
  i+=1
print(sum)

# We can also do this by for loop as well

x = int(input("Enter a Number : "))
y = int(input("Enter a Number : "))
sum = 0
for i in range(x,y):
 sum = sum + i
print(sum)