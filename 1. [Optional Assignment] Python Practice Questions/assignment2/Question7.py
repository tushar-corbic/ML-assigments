digit = input("Enter the digit")
result = 1
for i in range(len(digit)):
    result = result *int(digit[i])
print(result)