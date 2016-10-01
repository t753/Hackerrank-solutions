'''
Created on Sep 5, 2016

@author: Tom
'''
import string

def solve(in_str1, in_str2):
    
    dict_1 = dict.fromkeys(string.ascii_lowercase, 0)
    dict_2 = dict.fromkeys(string.ascii_lowercase, 0)
  
    
    result = "NO"
    
    for i in in_str1:
        dict_1[i] += 1
    
    for i in in_str2:
        dict_2[i] += 1
        
    for char, _count1 in dict_1.items():
        match = False
        if dict_1[char] > 0 and dict_2[char] > 0:
                result = "YES"
                match = True
                break
        if match == True:
            break
        
    
    print (result)

def main():

 
        cases = int(input().strip())
        for _i in range(cases):
            in_str1 = input().strip()
            in_str2 = input().strip()
            
            solve(in_str1, in_str2)
       

if __name__  ==  '__main__':
    main()
