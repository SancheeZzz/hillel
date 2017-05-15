def create_random_list(num, lower_limit, upper_limit):
    import random
    lst = []
    for i in range(num):
        lst.append(random.randint(lower_limit, upper_limit))
    return lst

lst=create_random_list(10,-10,42)
print("Список до нормирования - ", lst)
norm_list=[]
abs_max=max([abs(i) for i in lst])
for elem in lst:
    norm_elem= elem/abs_max
    norm_list.append('%.1f' % (norm_elem))
# norm_list.sort()
print('Список после нормирования в диапазон [-1,1] -', norm_list)