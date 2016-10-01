'''
Created on Sep 8, 2016

@author: Tom
'''

n,m = map(int, input().split(' '))
c = sorted(map(int,input().split(' ')))
distances = [c[0]]  + [(((c[i] - c[i-1]))//2) for i in range(1, len(c))] + [(n-1-c[-1])]
try:
    print (max(distances))
except:
    print (0)