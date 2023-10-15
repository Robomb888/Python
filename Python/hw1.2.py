t=10

f=set()
for i in range(1,t):
    for j in range(1,t):
        f.add(i*i+(j*(j+1)/2))

print(f)
