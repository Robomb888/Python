squares=[i**2 for i in range(10000)]

for i in squares:
    if 1+15*i in squares:
        a=[]
        a.append(i**(1/2))
        a.append((1+15*i)**(1/2))
        print(a)
