num=int(input("enter the question"))
i=1
m=[]
while i<=num:
    j=1
    x=[]
    m.append(i)
    while j<=10:
        d=j*i
        x.append(d)
        j+=1
    i+=1
    m.append(x)
print(m)
