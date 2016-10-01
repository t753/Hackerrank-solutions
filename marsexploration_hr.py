'''
Created on Sep 5, 2016

@author: Tom
'''

def solve(in_str):
    
    idx = 0
    count = 0
    str_len = len(in_str)
    
    while idx <= str_len - 3:
    
        if in_str[idx] != 'S':
            count += 1
        if in_str[idx + 1] != 'O':
            count += 1
        if in_str[idx + 2] != 'S':
            count += 1
            
        idx += 3
        
    
     
    result = count
  
    print (result)

def main():
  
    inp = input().strip()
    input_str = inp
    solve(input_str)
 


if __name__  ==  '__main__':
    main()
