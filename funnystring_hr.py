'''
Created on Sep 4, 2016

@author: Tom
'''

def solve(in_str):
    
    funny = True
    
    for i in range(1,len(in_str)):
        j = len(in_str) - 1 - i
        value1 = abs(ord(in_str[i]) - ord(in_str[i - 1]))
        value2 = abs(ord(in_str[j]) - ord(in_str[j + 1]))
        if (value1 != value2):
            funny = False
            break
        
    if funny:
        result = "Funny"
    else:
        result = "Not Funny"

    print (result)

 

def main():

 
        cases = int(input().strip())
        for _i in range(cases):
            in_str = input().strip()
            solve(in_str)
       

if __name__  ==  '__main__':
    main()
