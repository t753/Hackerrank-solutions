'''
Created on Sep 7, 2016

@author: Tom
'''
import sys

n = int(input().strip())
sticks = [int(arr_temp) for arr_temp in input().strip().split(' ')]


for i in range(n):
    sticks_cut = 0
    smallest = sys.maxsize
    for k in range(n):
        if (sticks[k] > 0) and (sticks[k] < smallest):
            smallest = sticks[k]
    for j in range(n):
        if (sticks[j] > 0) and (smallest < sys.maxsize):
            sticks_cut += 1
            sticks[j] -= smallest
    if sticks_cut > 0:
        print(str(sticks_cut))
    