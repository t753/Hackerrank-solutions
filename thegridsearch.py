'''
Created on Sep 12, 2016

@author: Tom
'''
def pattern_match(G, row, col, P, r, c):
    
    match = True
    row_p = 0
    for i in range(row, row + r):
        col_p = 0
        for j in range (col, col + c):
            if G[i][j] != P[row_p][col_p]:
                match = False
                break
            col_p += 1
        row_p += 1
        if not match:
            break
                
    return match
 
t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
        G_t = str(input().strip())
        G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
        P_t = str(input().strip())
        P.append(P_t)
        
    match = False   
    for row in range(R-r+1):
        for col in range(C-c+1):
            if G[row][col] == P[0][0]:
                match = pattern_match(G, row, col, P, r, c)
                if match:
                    break
        if match:
            break
      
    if match:
        print("YES")   
    else:
        print("NO")       