list1=[2,3,8,5,9,2,7,4]
i=0
print("before list",list1)
while i<len(list1):
    j=0
    while j<i:
        if list1[i]<list1[j]:
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp
        j+=1
    i+=1
print("after",list1)