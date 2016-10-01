'''
Created on Sep 7, 2016

@author: Tom
'''

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

count = 0
i = 0
while i < n - 1:
  
    if i < n-2:
        
        if (c[i + 1] == 0 and c[i + 2] == 1):
            i += 1
        elif (c[i + 1] == 0 and c[i + 2] == 0) or (c[i + 1] == 1):
            i += 2
    else:
        i += 1
        
    count += 1
    
print(count)
    
