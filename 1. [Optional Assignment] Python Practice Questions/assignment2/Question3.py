n = int(input("Enter the number whose you want prime factors"))
fac = 2
prime_factors= []
while(n>1):
    while(n%fac==0):
        prime_factors.append(fac)
        n = n// fac
    fac = fac+1
print(prime_factors)