list=[2*i for i in range(1,25)]
not_prime=[]
for i in range(50):
    for j in list:
        if i%j==0 and i/j in list:
            not_prime.append(i)
            break
print(not_prime)
        
    
    
