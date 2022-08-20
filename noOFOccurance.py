# This is the program for displaying no of occurance of List Elements
# Author:Kumar Vishal
# Pyhthon Version:3.4.10
list1=['A','B','C','D','A','A','B']
y=list(set(list1))
for i in range(0,len(y)):
    x=list1.count(list1[i])
    print("Total no of {} is: {}".format(y[i],x))
