'''
Created on Sep 4, 2016

@author: Tom
'''

def solve(in_str):
    
    str_len = len(in_str)
    count = 0
    if in_str[0].islower():
        count += 1
        for i in range(1, str_len - 1):
            if in_str[i].isupper():
                count += 1
     
    result = count
  
    print (result)

def main():
  
    inp = input().strip()
    input_str = inp
    solve(input_str)
 


if __name__  ==  '__main__':
    main()
