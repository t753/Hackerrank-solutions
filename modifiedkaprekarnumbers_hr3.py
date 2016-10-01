'''
Created on Sep 11, 2016

@author: Tom
'''
'''
Created on Sep 11, 2016

@author: Tom
'''
p = int(input().strip())
q = int(input().strip())

kap = []

for i in range(p, q + 1):
    
    sq = i ** 2
    sq_str = str(sq)
    sq_len = len(sq_str)
 
    if sq == 1:
        kap.append(i)
 
    if sq_len > 1:
 
        left_lst = []
        left_len = sq_len // 2
        right_len = sq_len - left_len
        left_num = int(''.join(x for x in (sq_str[:left_len]))) 
        right_num = int(''.join(x for x in (sq_str[left_len:sq_len])))
        if right_num != 0:
            if right_num + left_num == i:
                kap.append(i)
            
if len(kap) > 0:               
    for i in kap:
        print(i, end=' ')
else:
    print("INVALID RANGE")
