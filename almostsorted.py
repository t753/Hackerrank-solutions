n = int(input().strip())
arr = [0] + [int(i) for i in input().strip().split(' ')] + [10000001]

num_highs = num_lows = num_inverts = high_index = low_index = 0
invert_index_start = 10000001
invert_index_end = 0

for i in range(1, n+1):
    prev = arr[i-1]
    cur = arr[i]
    nexti = arr[i+1]

    if prev < cur > nexti and nexti > prev:  
        high_index = i
        num_highs += 1
    elif prev > cur < nexti and prev < nexti: 
        low_index = i
        num_lows += 1
    elif prev > cur > nexti: 
        invert_index_start = min(invert_index_start, i - 1)
        invert_index_end = max(invert_index_end, i + 1)
        num_inverts += 1

if num_highs == num_lows == 1 and num_inverts <= 1:  # D
    print("yes\nswap {} {}".format(high_index, low_index))
elif num_highs == num_lows == 1 and num_inverts > 1:  # E
    print("yes\nreverse {} {}".format(
        invert_index_start, invert_index_end))
elif num_highs or num_lows or num_inverts:  # F
    print("no")
else:
    print("yes")