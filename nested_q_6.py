element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
#sum1=0
#sum2=0
e=[]
o=[]
while i<len(element):
    if element[i]%2==0:
        e.append(element[i])
        print("even")
    else:
        o.append(element[i])
        print("odd")
    i+=1
print(e)
print(o)
#print(even)
#print(odd)