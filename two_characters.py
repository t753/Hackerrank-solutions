n = int(input())
s = input()
pairs = []
maxl = 0
temp = ''
k = list(set(s))
#create unique pairs
for i in range(len(k)-1):
    for char in k[i+1:]:
        pairs.append(k[i]+char)
        
for upair in pairs:
    temp = s
    flag = False
    #check whether any of the  probable resulting letters repeat in the given string
    if upair[0] * 2 in temp or upair[1] * 2 in temp:
        continue
    #remove every character that is not in the testing pair    from string 
    for char in k:
        if char not in upair:
            temp = temp.replace(char, '')
    #if resulting string has 2 same consecutive characters it is not correct
    for letter in set(temp):
        if letter * 2 in temp:
            flag = True
    #if no same consecutive and length more than previous max length - store
    if not flag and maxl < len(temp):
        maxl = len(temp)
        
print (maxl)