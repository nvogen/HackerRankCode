# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np



X = sorted([int(i) for i in [10, 40, 30, 50, 20]])
#7 13 15
#input: 12 4 17 7 14 18 12 3 16 10 4 4 12 output: 4 11 15
N = len(X)
#N = int(input())
#X = sorted([int(i) for i in input().split()])


#SD

mn = sum(X)/N
diff = sum([(i-mn)**2 for i in X ])
sd = round((diff/N)**(1/2),1)

# Quartiles
#if N%2 == 0:
#    med = ((X[int((N/2)-1)] + X[int((N/2))])/2 )
#
#    L = X[:int(N/2)]
#    NL = len(L)
#        
#else:
#    med = (X[int(N/2)])
#    
#    L = X[:int(N/2)]
#    NL = len(L)
    

def GetMeds(X):
    if len(X)%2 == 0:
        return int(sum(X[int(len(X)/2)-1:int(len(X)/2)+1])/2)
    else:
        return X[int(len(X)/2)]
GetMeds(X)


def GetQuants(N,X):
    Q1 = GetMeds(X[:int(len(X)/2)])
    Q2 = GetMeds(X)
    if N%2 == 0:
        Q3 = GetMeds(X[int(len(X)/2):])
    else:
        Q3 = GetMeds(X[int(len(X)/2+1):])
    return Q1,Q2,Q3

N = int(input())
X = sorted([int(num) for num in input().split()])
#Q1,Q2,Q3 = GetQuants(N,X)
print(GetQuants(N,X)[0])
print(GetQuants(N,X)[1])
print(GetQuants(N,X)[2])

# Output
print(np.mean(X))
if n%2 == 0:
    print((X[int((n/2)-1)] + X[int((n/2))])/2 )
else:
    print(X[int(n/2)])
print(mode(X)[0][0])    