number=30
n=[10,11,12,13,14,17,18,19]
l=len(n)
i=0
m=[]
while i<l:
    j=0
    a=[]
    while j<l:
        if n[i]+n[j]==number and n[i]<n[j]:
            a.append(n[i])
            a.append(n[j])
            m.append(a)
        j=j+1
    i=i+1
print(m)