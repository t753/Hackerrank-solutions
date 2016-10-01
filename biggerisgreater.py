'''
Created on Sep 13, 2016

@author: Tom
'''
t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    s_len = len(s)
    s_lst = list(s)
    s_lst_len = len(s_lst)
    
    no_answer = True
    idx = -1
    
    for i in range(s_len - 1):
        if s_lst[i + 1] > s_lst [i]:
            idx = i
            no_answer = False
            
    if idx != -1:
        
        for i in range(idx, s_len):
            if s_lst[idx] < s_lst [i]:
                idx2 = i
           
        
        temp = s_lst[idx]
        s_lst[idx] = s_lst[idx2]
        s_lst[idx2] = temp
            
        s_lst = s_lst[:idx + 1] + sorted(s_lst[idx + 1:])
        
        result = ''.join(s_lst)
        
    else:
        no_answer = True
        
    if no_answer:
        print("no answer")
    else:
        print(result)