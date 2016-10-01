'''
Created on Sep 11, 2016

@author: Tom
'''
t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]

    cost = 0

    if z < abs(x - y) and (x != y):
        
        if x < y:
            cost = (b * x) + (w * (x + z))
            
        else:
            cost = (b * (y + z)) + (w * y)
            
    else:
        cost = (b * x) + (w * y)
            
            
    print(cost)