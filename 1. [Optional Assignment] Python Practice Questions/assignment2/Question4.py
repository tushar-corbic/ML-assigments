n = int(input("Enter the total number of objects"))
r = int(input("Enter the number of objects you want to select"))
def fact(n):
    if(n<=1):
        return 1
    result = 1
    for i in range(2, n+1, 1):
        result = result*i
    return result
if r<=n:
    combination = fact(n)/(fact(n-r)*fact(r))
    permutation = combination*fact(r)
    print("The permutation is {0} and the combination is {1}".format(permutation, combination))
else:
    print("The number of selection objects must be less than or equal to total objects")