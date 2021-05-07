def sumOfDivisors(n):
    result = [1]
    for i in range(2, n, 1):
        if n%i==0:
            result.append(i)
    return n==sum(result)

a = int(input("Enter the starting of the range"))
b = int(input("Enter the ending of the range"))

my_list = list(range(a,b+1,1))
my_list = list(filter(lambda x: sumOfDivisors(x), my_list))
print(my_list)