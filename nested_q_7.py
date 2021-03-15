element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
e_sum=0
o_sum=0
while i<len(element):
    if element[i]%2==0:
        e_sum+=element[i]
    else:
        o_sum+=element[i]
    i+=1
print(e_sum)
print(o_sum)