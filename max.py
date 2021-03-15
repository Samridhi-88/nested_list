a=int(input("enter the element"))
b=int(input("enter the element"))
c=int(input("enter the element"))
n1=[]
n2=[]
n3=[]
n1.append(a)
n2.append(b)
n3.append(c)
if n1>n2 and n1>n3:
    print(n1,"maximum")
elif n2>n1 and n2>n3:
    print(n2,"maximum")
else:
    print(n3,"maximum")