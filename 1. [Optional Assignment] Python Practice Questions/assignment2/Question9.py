def sumOfDivisors(n):
    result = [1]
    for i in range(2, n, 1):
        if n%i==0:
            result.append(i)
    return sum(result)


a = int(input("Enter the number"))
print('The sum of proper divisor of {0} is {1} '.format(a, sumOfDivisors(a)))