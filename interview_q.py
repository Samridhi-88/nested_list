a=int(input("enter the number"))
i=0
while i<=a:
    n=int(input("enter the number"))
    first_digit=n%10
    sum=0
    while n>0:
        last_digit=n%10
        n=n//10
    sum=first_digit+last_digit
    print(sum)
    i+=1