'''
Created on Sep 13, 2016

@author: Tom
'''
import sys
    
def rotate(i, a, n):
    
    if i >= 1 and i < n - 1:
             
            temp = a[i - 1]
            a[i - 1] = a[i]
            a[i] = a[i + 1]
            a[i + 1] = temp
            return i - 1
            
    elif i == n - 1:
         
            temp = a[i - 1]
            a[i - 1] = a[i]
            a[i] = a[i - 2]
            a[i - 2] = temp
            return i - 1
                
t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    a = [int(x) for x in input().split()]
    a_d = {k:v for k,v in zip(a,[int(x) for x in range(len(a))])}
          
    possible = False 
    
    for i in range(1, n):

        start_idx = a_d[i]
        
        start = start_idx    
        while start > i - 1  and start >= 0 and a[start] < a[i - 1]:
            start = rotate(start, a, n)
            
        a_d = {k:v for k,v in zip(a,[int(x) for x in range(len(a))])}
        
    possible = True
    for i in range(1, n):
        
        if a[i] < a[i - 1]:
            
            possible = False
            break             
             
    if possible:
        print ("YES")
    else:
        print ("NO")
        