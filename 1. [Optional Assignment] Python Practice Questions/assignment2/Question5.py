n = int(input("Enter the decimal number"))
binary = []
while(n>0):
    binary.append(n%2)
    n = n//2
binary.reverse()
ans = ''.join([str(i) for i in binary])
print(ans)