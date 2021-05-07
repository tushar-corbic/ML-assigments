def cube(x):
    return x*x*x
isEven = lambda x: x%2==0
try:
    my_list = []
    while True:
        my_list.append(int(input()))
except:
    my_list = list(map(cube, list(filter(isEven, my_list))))
    print(my_list)