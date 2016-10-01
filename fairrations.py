'''
Created on Sep 8, 2016

@author: Tom
'''
#import sys
n = int(input().strip())
b = [int(B_temp) for B_temp in input().strip().split(' ')]

sum1 = 0
carry = False
for x in b:
   
    carry = (carry + x) % 2
    sum1 += carry * 2

if carry:
    print("NO")
else:
    print (sum1)
