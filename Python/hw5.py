import math
n=79434323

nums=[i for i in range(n,n+100)]
print(nums)

factor_list=[]

def factorize(n):
    i=n
    while i!=1:
        


#factoring the numbers into a list called factor_list
for i in nums:
    factors=[]
    for k in range(2,int(i**(1/2)+1)):
        if i%k==0:
            factors.append(k)
    factor_list.append(factors)

#number of primes
print("Primes: "+str(len([i for i in factor_list if i==[]])))

#number of perfect squares
print("Perfect squares: "+str(len([i for i in nums if int(i**(1/2))==i**(1/2)])))

#returns true if it has x distinct prime factors
def x_primes(x,factors):
    if len(set(factors))==x:
        return True
    else:
         return False

for i in range(2,8):
    count=0
    for factor in factor_list:
        if x_primes(i,factor):
            print(nums[factor_list.index(factor)])
            count+=1
    print(str(i)+" prime factors: "+str(count))
