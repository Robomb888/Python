cubes=[i**3 for i in range(50)]
squares=[i**2 for i in range(350)]

for i in cubes:
    for j in cubes:
        if i+j in squares:
            a=[]
            a.append(i**(1/3))
            a.append(j**(1/3))
            a.append((i+j)**(1/2))
            print(a)



    
