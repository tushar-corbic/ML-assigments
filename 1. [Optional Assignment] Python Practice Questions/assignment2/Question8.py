def productOfDigits(x):
    result = 1
    while(x>0):
        result = result * (x%10)
        x = x//10
    return  result
def getDigit(x):
    count = 0
    while(x>0):
        x= x//10
        count = count+1
    return count
def MultiplicativeDigitalRoot(x,cp):
    if(getDigit(x)==1):
        return x,cp
    return MultiplicativeDigitalRoot(productOfDigits(x), cp+1)
a = int(input())
MDR, MPersistence = MultiplicativeDigitalRoot(a,0)
print(MDR, MPersistence)
