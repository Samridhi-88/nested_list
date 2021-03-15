element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum1=0
sum2=0
list1=[]
list2=[]
while i<len(element):
    if element[i]%2==0:
        sum1+=element[i]
        list1.append(element[i])
        everaj=sum1/len(list1)
    else:
        sum2+=element[i]
        list2.append(element[i])
        everaj1=sum2/len(list2)
    i+=1
print(sum1,"even")
print(sum2,"even")
print(list1)
print(list2)
print(everaj)
print(everaj1)