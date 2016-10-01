T = int(input().strip())   
for a0 in range(T):
    n = int(input().strip())
    q = map(int,input().strip().split(' '))
    # your code goes here

    position = 1
    bribes = 0
    plus2 = 0  

    for i in q:
        jumps = i - position

        if jumps > 2:
            bribes = "Too chaotic"
            break
        elif jumps > 0 and jumps != 2:
            bribes += 1
            plus2 = 0
        elif jumps == 2:
            bribes += 2
            plus2 += 1
        elif jumps <= 0 and plus2 > 0:
            if jumps == 1 - plus2:
                bribes += 1
            plus2 = 0
        position += 1
    print (bribes)  