'''
Created on Sep 11, 2016

@author: Tom
'''
h = int(input().strip())
m = int(input().strip())

minutes = {1:"one", 2:"two", 3:"three" ,4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight",\
           9:"nine",  10:"ten", 11:"eleven", 12:"tweleve" , 13:"thirteen", 14:"fourteen", \
           15: "quarter ", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty"}
 
words = []

if m == 0:
    words.append(minutes[h] + " o' clock")
elif m == 30:
    words.append("half past " + minutes[h])
else:
    if m == 1 or m == 59:
        mins = " minute "
    else:
        mins = " minutes "
    if m >= 1 and m < 30:
        mins2 = "past "
        to_h = h
    else:
        mins2 = "to "
        m = 60 - m
        if h < 12:
            to_h = (h + 1)
        else:
            to_h = 1
    if m == 15:
        words.append(minutes[15] + mins2 + minutes[to_h])
    elif m > 20:
        words.append(minutes[20] + " " + minutes[m-20] + mins + mins2 + minutes[to_h])
    else:
        words.append(minutes[m] + mins+ mins2 + minutes[to_h])
        
for i in words:
    print(i)