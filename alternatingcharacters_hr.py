'''
Created on Sep 4, 2016

@author: Tom
'''

def  solve(in_str):
    
    count = 0
    good_char = in_str[0]
    for i in range(1,len(in_str)):
        if in_str[i] == good_char:
            count +=1
        else:
            good_char = in_str[i]
            
    print(count)

def main():
    
    cases = int(input().strip())
    for _i in range(cases):
        in_str = input().strip()
        solve(in_str)
    
if __name__  ==  '__main__':
    main()
