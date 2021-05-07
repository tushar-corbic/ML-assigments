isodd = lambda x : x%2!=0
try:
    my_list = []
    while True:
        my_list.append(int(input()))
except:
    my_list = list(filter(isodd, my_list))
print(my_list)