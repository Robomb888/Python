while True:
    a=int(input("a: "))
    b=int(input("b: "))
    a1=[]
    b1=[]

    ab=set()
    for i in range(0,50):
        a1.append(a*i)
        b1.append(b*i)

    for i in a1:
        for j in b1:
            ab.add(i+j)
    print(ab)
    
    
