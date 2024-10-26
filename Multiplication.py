# Ques- Print the multiplication table of a number n.

num = int(input("Enter a Number"))
i = 1

while i <= 10:
  print(num,"x",i,"=",num*i)
  i+=1

# we can do with the For loop as well

num = int(input("Enter a Number"))
for i in range(1,11):
  print(num,"x",i,"=",num*i)
  
  
  