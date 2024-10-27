#ques- Search for a number x in this list using loop:

# list =[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# i = 0
# num = int(input("Enter a Number :"))
# for i in range(len(list)):
#  if list[i]==num:
#     print("Number is found")
#     break
    
# else:
#  print("Number is not found")

# We can also do this by While  loop as well

list =[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i = 0
num = int(input("Enter a Number :"))
while(i<len(list)):
  if list[i]==num:
     print("Number is found")
     break
  i+=1
else:
 print("Number is not found")

