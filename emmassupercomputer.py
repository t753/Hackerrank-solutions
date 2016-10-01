 
class Pos:
    x = 0
    y = 0

    def __init__(self,i, j):
        self.x = i
        self.y = j
 
def initFlag(flag):
    for i in range(0, len(flag)):
        for j in range(0, len(flag)):
            flag[i][j] = False;
  
def isValid(i,  j, length, grid, flag):
    if grid[i][j] != 'G' or flag[i][j] == True:
        return False
    
    for k in range(i - length//2, i + length//2 + 1):
        if grid[k][j] != 'G' or flag[k][j] == True:
            return False
    
    for k in range(j - length//2, j + length//2 + 1):
        if grid[i][k] != 'G' or flag[i][k] == True:
            return False;
    
    return True;
 
def mark(i, j, length, flag):
    for k in range(i - length//2, i + length//2 + 1):
        flag[k][j] = True
    
    for k in range(j - length//2, j + length//2 + 1):
        flag[i][k] = True;
 
def search(length, n, m, flag, grid):
    start = (length-1)//2
    iend = n-1-(length-1)//2
    jend = m-1-(length-1)//2;
    validPos = []
    for i in range(start, iend + 1):
        for j in range(start,jend + 1):
            if isValid(i,j,length, grid, flag):
                mypos = Pos(i, j)
                validPos.append(mypos)
    return validPos
 
def solve(n, m, grid, flag):
    longest = min(n, m);
    if longest % 2 == 0:
        longest -= 1
    ret = 1;
    for i in range(longest, 0 ,- 2): 
        initFlag(flag);
        fstPos = search(i, n, m, flag, grid)
        if len(fstPos) != 0:
            for iPos in range(0, len(fstPos)):
                initFlag(flag);
                mark(fstPos[iPos].x, fstPos[iPos].y, i, flag);
                for j in range(longest,0,-2):
                    search_j = search(j, n, m, flag, grid)
                    if len(search_j) != 0:
                        ret = max(ret, (2*i-1)*(2*j-1));
                        break;
    return ret;
 
 
n,m = [int(x) for x in input().strip().split()]
grid = []
for grid_i in range(n):
    grid.append([x for x in list(input().strip())])
    
flag = [[False for i in range(16)] for j in range(16)]
result =  solve(n, m, grid, flag)

print(result)
