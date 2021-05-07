def cube(x):
    return x*x*x
try:
    my_list = []
    while True:
        my_list.append(int(input()))
except:
    my_list_cube = map(cube, my_list)
    print(my_list)
    print(list(my_list_cube))

