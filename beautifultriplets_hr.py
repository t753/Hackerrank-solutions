'''

Created on Sep 9, 2016

@author: Tom
'''

n, d = input().strip().split(' ')
n, d = [int(n), int(d)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

triplets = 0
for i in range(n):
    num=a[i]
    if num+d in a and num+(d*2) in a:
        triplets+=1
       
print(triplets)
