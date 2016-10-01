'''
Created on Sep 9, 2016

@author: Tom
'''
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    
    last_stones = []
    
    limit = n - 1
    start = min(a, b)
    start *= n-1
    last_stones.append(start)
    diff = abs(a - b)
    for j in range(n-1):
        start += diff
        if start not in last_stones:
            last_stones.append(start)
           
    last_stones.sort()
    for j in last_stones:
        print(j, end= " ")
    print("\n", end='')
    