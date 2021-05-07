def cubeSum(n):
    ans = 0
    while(n>0):
        ans = ans + (n%10)**3
        n = n//10
    return ans
def numOfDigits(n):
    count  = 0
    while(n>0):
        count = count+1
        n = n//10
    return count
def isArmstrong(n):
    if n== cubeSum(n):
        return True
    else:
        return False
def printArmstrong(n):
    for i in range(2,1000,1):
        if n>0:
            if isArmstrong(i)==True:
                print(i)
                n = n-1
        else:
            break