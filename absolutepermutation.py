t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    
    ans = 0
    pos = []
    
    if k != 0:
        dev = n // k
    else:
        ans = n
        
    if ans != n:
        
        if k != 0 and k <= n //2 and n % k == 0 and dev % 2 == 0:
            for i in range(n):
                if (i // k) % 2 == 0:
                    pos.append(i + k + 1)
                else:
                    pos.append(i - k + 1)
        else:
            ans = -1
    
    if ans == -1:
        print("-1")
        
    elif ans == n:
        for i in range(1, n + 1):
            print(i, end=' ')
        print("\n", end='')
    else:
        for i in range(n):
            print(pos[i], end=' ')
        print("\n", end='')
