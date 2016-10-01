'''
Created on Sep 5, 2016

@author: Tom
'''
from collections import Counter as Co

def solve(in_str1):
    
    if len([x for x in Co(in_str1).values() if x % 2 !=0]) <= 1:
        result = "YES"
    else:
        result = "NO"
        
    
    print (result)

def main():

    in_str1 = input().strip()
            
    solve(in_str1)
       

if __name__  ==  '__main__':
    main()
