element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
s=0
c=0
sum1=0
sum2=0
list1=[]
list2=[]
count1=0
count2=0
while i<len(element):
    s+=element[i]
    c+=1
    averaj_l=s/c
    if element[i]%2==0:
        sum1+=element[i]
        list1.append(element[i])
        everaj=sum1/len(list1)
        count1+=1
    else:
        sum2+=element[i]
        list2.append(element[i])
        everaj1=sum2/len(list2)
        count2+=1
    i+=1
print(sum1,"even")
print(sum2,"odd")
print(list1,"even ki list")
print(list2,"odd ki list")
print(everaj,"even ka averaj")
print(everaj1,"odd ka averaj")
print(count1,"even ka count")
print(count2,"odd ka count")
print(s,"puri list ka sum")
print(c,"puri list ka count")
print(averaj_l,"list ka avaraj")