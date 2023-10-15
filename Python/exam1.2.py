import math

l=[i for i in range(1,10)]

for x in l:
    for y in l[l.index(x)::]:
        gcd=math.gcd(2*x+y,x*x)
        print((x,y,y**2,gcd))
        if (y**2)%gcd!=0:
            print("No")
