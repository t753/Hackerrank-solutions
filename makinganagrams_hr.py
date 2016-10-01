'''
Created on Sep 5, 2016

@author: Tom
'''

from collections import Counter

def solve(in_str1, in_str2):
    
    counts = Counter(in_str1)
    counts.subtract(in_str2)
    result = sum(abs(x) for x in counts.values())
    
    print (result)

def main():

    in_str1 = input().strip()
    in_str2 = input().strip()
            
    solve(in_str1, in_str2)

if __name__  ==  '__main__':
    main()
