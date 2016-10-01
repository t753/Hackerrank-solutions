'''
Created on Sep 3, 2016

@author: Tom
'''

def reduce_before(i, current_str):
    
    index = i-2
    new_str = current_str[:index]
    new_str += current_str[i:]
    
    return new_str

def reduce_after(i, current_str):
    
    index = i + 3
    new_str = current_str[:i+1]
    new_str += current_str[index:]
    
    return new_str


def check_before(current_str):
    
    found = False
    i = 0
    for i in range (len(current_str)):
        if i < 2:
            continue
        else:
            if current_str[i-1] == current_str[i-2]:
                found = True
                break
            else:
                found = False
    return i, str(found)
        
def check_after(current_str):
    
    found = False
    i = 0
    for i in range (len(current_str) - 2):
        if current_str[i+1] == current_str[i+2]:
            found = True
            break
        else:
            found = False
    return i, str(found)

def solve(in_str):
    
    reduced = False
    current_str = in_str
    while reduced == False:
        
        if current_str:
        
            j, reduce = check_before (current_str)
            if reduce == "True":
                current_str = reduce_before(j, current_str)
                continue
            j, reduce = check_after (current_str)
            if reduce == "True":
                current_str = reduce_after(j, current_str)
                continue
            
        reduced = True
            
    if len(current_str) == 2:
        if current_str[0] == current_str[1]:
            ans = "Empty String"
    else:
        ans = current_str
     
    result = ans
  
    print (result)

def main():
  
    inp = input().strip()
    input_str = inp
    solve(input_str)
 


if __name__  ==  '__main__':
    main()
