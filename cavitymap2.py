'''
Created on Sep 9, 2016

@author: Tom
'''
from itertools import product

def neighbours(cell, size):
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < size for n in c):
            yield c

n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
    grid_t = str(input().strip())
    grid.append(grid_t)

cavity_map = [[int(y) for y in x] for x in grid]

for i in range(n):
    for j in range(n):
        num = cavity_map[i][j]
        if num != -1:
            print(num, end='')
        else:
            print("X", end='')
    print("\n", end='')
print("\n")
    
for row in range(n):
    for col in range(n):
        cavity_find = True
        num = int(grid[row][col])
        adj_list = list(neighbours((row, col), n))
        for i in adj_list:
            adj = list(i)
            x = adj[0]
            y = adj[1]
            adj_num = int(grid [x][y])
            if adj_num > num:
                cavity_find = False
                    
        if cavity_find:
            cavity_map[row][col] = -1

for i in range(n):
    for j in range(n):
        num = cavity_map[i][j]
        #print(num, end='')
        if num != -1:
            print(num, end='')
        else:
            print("X", end='')
    print("\n", end='')
        

