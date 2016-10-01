'''
Created on Sep 6, 2016

@author: Tom
'''
def main():
    
    inp = input().strip().split()
    
    n = int(inp[0])
    k = int(inp[1])
    q = int(inp[2])
    
    inp = input().strip().split()
    
    arr = []
    
    for i in range(n):
        arr.append(int(inp[i]))
        
    queries = []   
    
    for i in range(q):    
        inp = input().strip()
        queries.append(int(inp))
       
    k %= n   
         
    for i in range(q):
        j = queries[i] - k
        print(str(arr[j]))   
    
main()    
