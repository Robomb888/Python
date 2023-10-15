import math

z_square=[2*i*i for i in range(1,400)]
x=[i*i for i in range(1,2*400)]
y=[2*i*i for i in range(1,400)]
list=[]

z_values=[]

z_values_2=[]
for i in x:
    for j in y:
        if i+j in z_square:
            triple=[int(i**(1/2)),int((j/2)**(1/2)),int(((i+j)/2)**(1/2))]
            triple1=triple.copy()
            min_num=min(triple)
            triple1.remove(min_num)
            min_num_2=min(triple1)
            max_num=max(triple)
            gcd=math.gcd(min_num,min_num_2)
            if gcd==1:
                list.append(triple)
            else:
                for x in triple:
                    if x%gcd!=0:
                        list.append(triple)

for x in list:
    z_values.append(x[2])

for x in z_values:
    if z_values.count(x)>1:
        z_values_2.append(x)
        
z_values_2.sort()

list1=[]
for x in z_values_2:
    for j in list:
        if j[2]==x and j not in list1:
            print(j)
            list1.append(j) 

