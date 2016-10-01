n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
    grid_t = str(input().strip())
    grid.append(grid_t)

cavity_map = [[int(y) for y in x] for x in grid]
    
for row in range(1, n - 1):
    for col in range(1, n - 1):
        
        num = int(grid[row][col])
        if int(grid[row][col - 1]) < num and \
           int(grid[row ][col + 1]) < num and \
           int(grid[row + 1][col]) < num and \
           int(grid[row - 1][col]) < num:
            cavity_map[row][col] = -1

for i in range(n):
    for j in range(n):
        num = cavity_map[i][j]
        if num != -1:
            print(num, end='')
        else:
            print("X", end='')
    print("\n", end='')
