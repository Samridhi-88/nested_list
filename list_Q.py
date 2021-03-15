a=[3,5,7,8,9,2,]
b=int(input("enter the num"))
i=0
list1=[]
j=0
while i<len(a):
    list2=[]
    while j<(b):
        list2.append(a[i])
        list2.append(a[j])
        list1.append(list2)
        j+=1
    i+=1
print(list1)