squares=[i**2 for i in range(100)]

for i in squares:
    for j in squares:
        if i+(15*j) in squares:
         print('i= '+str(i)+" and j= "+str(j))   
         
         
###solves equations of the form x^2+15y^2=z^2
###prints x and y
         
