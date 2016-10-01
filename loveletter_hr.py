'''
Created on Sep 3, 2016

@author: Tom
'''


def love_letter(in_str):
   
    str_len = len(in_str)
    half = str_len // 2
    count = 0
    for i in range(half):
        first = ord(in_str[i])
        last = ord(in_str[-(i+1)])
        while first - last != 0:
            if first > last:
                first -= 1
            else:
                last -= 1
            count += 1
          
        
        
    
    result = count

    print (result)

  
def main():

    cases = int(input().strip())
    while cases > 0:
        inp = input().strip()
        love_letter(inp)
        cases -= 1


if __name__  ==  '__main__':
    main()
    
    