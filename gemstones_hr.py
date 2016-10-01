'''
Created on Sep 4, 2016

@author: Tom
'''
import string

def  solve(rocks, common):
    
    gem_count = dict.fromkeys(string.ascii_lowercase, 0)
    
    for rock in rocks:
        rock_list = []
        for gem in rock:
            if gem not in rock_list:
                gem_count[gem] += 1
                rock_list.append(gem)
            
    result = 0  
        
    for gem, count in gem_count.items():
        if count >= common:
            result += 1;
   
            
    print(result)

def main():
    
    rocks = []
    count = int(input().strip())
    for _i in range(count):
        rock = input().strip()
        rocks.append(rock)
    solve(rocks, count)
    
if __name__  ==  '__main__':
    main()
