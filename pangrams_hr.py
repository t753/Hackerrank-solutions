'''
Created on Sep 4, 2016

@author: Tom
'''
import string

def solve(in_str):
    
    dict_lower = dict.fromkeys(string.ascii_lowercase, 0)
    dict_upper = dict.fromkeys(string.ascii_uppercase, 0)
    
    pangram = True
    
    str_len = len(in_str)
    for i in range(str_len):
        if in_str[i].isupper():
            dict_upper[in_str[i]] += 1
        elif in_str[i].islower():
            dict_lower[in_str[i]] += 1
            
    letter_list = []
    for letter, _count in dict_lower.items():
        if dict_lower [letter] == 0:
            pangram = False
            letter_list.append(letter.upper())
            
    for letter in letter_list:
        if dict_upper[letter] == 0:
            pangram = False
            break
        else:
            pangram = True
            
    if pangram:
        result = "pangram"
    else:
        result = "not pangram"
  
    print (result)

def main():
  
    inp = input()
    input_str = inp
    solve(input_str)
 


if __name__  ==  '__main__':
    main()
