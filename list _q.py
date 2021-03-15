# question number one
a=[3,4,5,6,7,8]
i=0
while i<len(a):
    print(a[i])
    i+=1
print("    ")
######
#question number two
a=[3,4,5,6,7,8,]
i=0
while i<len(a)-1:
    print(a[i]+a[i+1])
    i+=1
print("     ")
#######
#question number three
a=[3,4,5,6,7,8]
i=0
while i<len(a)-2:
    print(a[i]+a[i+2])
    i+=2
print("      ")
########
#question number 4
a=[3,4,5,6,7,8]
i=0
while i<len(a):
    j=0
    c=len(a)-1
    while j<len(a):
        d=a[i]+a[c]
        print(d)
        j-=1
    i+=1




