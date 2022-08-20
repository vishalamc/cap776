# This is the program for displaying sum of List Elements
# Author:Kumar Vishal
# Python Version:3.4.10

list1=[] # empty list
sum=0
limit=input("Enter size for list")
limitType=limit.isdigit()
if limitType==True:
    for i in range(int(limit)):
        item=input("Enter List element")
        itemType=item.isdigit()
        if itemType==True:
            list1.append(int(item))
            sum=sum+list1[i]
        else:
            print("Invalid Input")
            exit()
else:
    print("Invalid Input")
    exit()
print(list1)
print("Sum of list elements are:",sum)

    
