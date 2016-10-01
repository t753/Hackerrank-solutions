#see if a point is out of bounds
def outOfBounds(xPos, yPos, rows, cols):

	thing = xPos >= 0 and xPos < cols and yPos >= 0 and yPos < rows
	return not thing

#print a given vector
def printVector(arr, rows, cols):

	for i in range(rows):
		for j in range(cols):
			print(arr[i][j], end='')
		print("\n", end='')

#explode the bombs in a given grid
def getExploded(inpt, rows, cols):

	arrAlt = [[ord('O') for _x in range(cols)] for _y in range(rows)]

	for i in range(rows):
		for j in range(cols):
			
			if inpt[i][j] == 'O':

				arrAlt[i][j] = ord('.')

				if not (outOfBounds(j-1, i, rows, cols)):
					arrAlt[i][j-1] = ord('.')

				if not (outOfBounds(j+1, i, rows, cols)):
					arrAlt[i][j+1] = ord('.')

				if not (outOfBounds(j, i+1, rows, cols)):
					arrAlt[i+1][j] = ord('.')
					
				if not (outOfBounds(j, i-1, rows, cols)):
					arrAlt[i-1][j] = ord('.')
				
	arrAlt_char = [[chr(x) for x in y] for y in arrAlt]

	return arrAlt_char

rows, cols, seconds = [int(x) for x in input().strip().split()]

arr = []
for arr_i in range(rows):
	arr.append([x for x in list(input().strip())])

arrFull = [['O' for x in range(cols)] for y in range(rows)]

if seconds == 1:
	printVector(arr, rows, cols)
else:
	case = seconds % 4
	if case == 1:
		printVector(getExploded(getExploded(arr, rows, cols), rows, cols), rows, cols)
	elif case == 3:
		printVector(getExploded(arr, rows, cols), rows, cols)
	else:
		printVector(arrFull, rows, cols)
