majic=[[8,3,4],[1,5,9],[6,7,2]]
i=0
r1,r2,r3=0,0,0
c1,c2,c3=0,0,0
d=0
while i<len(majic):
    r1+=majic[i][0]
    r2+=majic[i][1]
    r3+=majic[i][0]
    c1+=majic[i][0]
    c2+=majic[1][i]
    c3+=majic[2][i]
    d+=majic[i][i]
    i+=1
if r1==r2==r3==c1==c2==c3==d:
    print("majic square")
else:
    print("not majic square")