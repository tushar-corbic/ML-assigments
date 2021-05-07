import numpy as np
def sumOfDivisors(n):
    result = [1]
    for i in range(2, n, 1):
        if n%i==0:
            result.append(i)
    return sum(result)
def isAmicable(x, y):
    x1 = sumOfDivisors(x)
    y2 = sumOfDivisors(y)
    if((x1==y )& (y2==x)):
        return True
    else:
        return False
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
print(isAmicable(a,b))