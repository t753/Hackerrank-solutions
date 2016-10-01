'''
Created on Sep 5, 2016

@author: Tom
'''
import string

def get_all_substrings(input_string):
    length = len(input_string)
    return [input_string[i:j+1] for i in range(length) for j in range(i,length)]


def solve(in_str):
    
    dict_lower = dict.fromkeys(string.ascii_lowercase, 0)
    
    str_len = len(in_str)
    for i in range(str_len):
        dict_lower[in_str[i]] += 1
            
    letter_list = []
    for letter, _count in dict_lower.items():
        if dict_lower [letter] != 0:
            letter_list.append(letter)
            
    result = len(letter_list)

    print (result)

 

def main():

 
        cases = int(input().strip())
        for _i in range(cases):
            in_str = input().strip()
            solve(in_str)
       

if __name__  ==  '__main__':
    main()
