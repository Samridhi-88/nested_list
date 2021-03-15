string="this is a book"
a=[]
m=' '
i=0
while i<len(string):
    if string[i]==' ':
        a.append(m)
        m=' '
    else:
        m=m+string[i]
    i+=1
if m:
    a.append(m)
print(a)