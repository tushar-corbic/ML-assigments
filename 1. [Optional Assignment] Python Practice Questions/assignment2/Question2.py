import numpy as np
def isPrime(n):
    for i in range(2,int(np.sqrt(n))+1, 1):
        if n%i==0:
            return 0
    return 1
for i in range(2,1001,1):
    if isPrime(i)==1:
        print(i, end=' ')