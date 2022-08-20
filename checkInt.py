l1=[1,2,3,"hi","hello",12.5,16.5]
count1=0
count2=0
count3=0
for i in l1:
    if type(i)==int:
        count1=count1+1
    if type(i)==float:
        count2=count2+1
    if type(i)==str:
        count3=count3+1
print("Type:integer Values:",count1)
print("Type:float Values:",count2)
print("Type:String Values:",count3)

