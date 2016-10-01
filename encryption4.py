'''
Created on Sep 12, 2016

@author: Tom
'''
#import sys
import math as m

s = input().strip()
s_len = len(s)
cl = m.ceil(m.sqrt(s_len))
cols = cl

for i in range(cols):
    for j in range(i,s_len,cols):
        print(s[j], end='')
    print(" ", end='')
        
        
