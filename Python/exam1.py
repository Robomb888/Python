num=[i for i in range(1,10)]
list=[]
for i in num:
    for j in num:
        x=4*j*i+i+j
        if x in list:
            print("x: "+str(x))
            print("i: "+str(i))
            print("j: "+str(j))
        else:
            list.append(x)
        
