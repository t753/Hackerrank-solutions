'''
Created on Sep 4, 2016

@author: Tom
'''

import re

def solve(in_str):
    
    sub_strs = [m.start() for m in re.finditer('(?=010)', in_str)]
    
    indexes = []
    for i in sub_strs:
        indexes.append(i+1)
        
    count = 0
    idx_count = True
    
    for i in range(len(indexes)):
        if idx_count == True:
            count += 1
            if i < len(indexes) - 1:
                if indexes[i + 1] - indexes[i] <= 2:
                    idx_count = False
                    continue
        else:
            idx_count = True
   
     
    result = count
  
    print (result)


def main():

    _N = int(input().strip())
    input_str = input().strip()
  
    solve(input_str)
       

if __name__  ==  '__main__':
    main()
    