'''
Created on Sep 5, 2016

@author: Tom
'''

U = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
L = U.lower()

n, word, key = input(), input(), int(input()) % len(U)
ceaser = str.maketrans(U + L, U[key:] + U[:key] + L[key:] + L[:key])

print(word.translate(ceaser))


