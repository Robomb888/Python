s=[]
t=[]
for i in range(1, 100000):
    s.append(i*i)
    t.append(i*(i+1)/2)

for i in s:
    if i in t:
        print(i)
        print("N: " +str(s.index(i)+1))
        print("i: "+str(t.index(i)+1))
