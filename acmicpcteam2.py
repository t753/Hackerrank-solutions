'''
Created on Sep 10, 2016

@author: Tom
'''
'''
Created on Sep 10, 2016

@author: Tom
'''


import time
#import numpy as np
#import bitstring.Bits
#t = time.time()

n,m = [int(x) for x in input().strip().split()]
topic = []
for topic_i in range(n):
    topic.append([int(x) for x in list(input().strip())])

#t = time.time()

max_teams = 0
max_topics = 0   

for i in range(n):
    for j in range( i + 1, n):
        count = 0
        bits = [a | b for a, b in zip(topic[i], topic[j])]
        result = bits.count(1)
        count = result
        if count > max_topics:
            max_topics = count
            max_teams = 1
        elif count == max_topics:
            max_teams += 1
    
print(max_topics)

print(max_teams)       
    
#print ("\nExecution time: ", time.time() - t, "seconds")
