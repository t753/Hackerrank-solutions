'''
Created on Sep 5, 2016

@author: Tom
'''

def solve(in_str):
    
    letters = {}
    
    str_len = len(in_str)
    half_len = str_len // 2
    
    if str_len % 2 != 0:
        result = -1

    else:
        
        for i in range(half_len):
            char = in_str[i]
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
                
        diff = 0
                
        for i in range(half_len, str_len):
            char = in_str[i]
            if char in letters and letters[char] > 0:
                letters[char] -= 1
            else:
                diff += 1
                 
        result = diff
    
    print (result)

 

def main():

 
        cases = int(input().strip())
        for _i in range(cases):
            in_str = input().strip()
            solve(in_str)
       

if __name__  ==  '__main__':
    main()

