def list_of_12_numbers (num):
    import random
    lst = []
    for i in range(num):
        lst.append(random.randint(0,num))
    lst_for_max=lst
    maximum= max(lst_for_max)
    return lst,maximum
print("Список из 12 чисел, максимальное значение",list_of_12_numbers(12))