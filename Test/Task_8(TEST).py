import random
lst = [random.randint(1,100) for x in range(12)]
print("Первоначальный список - ", lst)
maximum= max(lst)
minimum= min(lst)
print("Наибольший элемент списка -", maximum)
print("Наименьший элемент списка -", minimum)
idx=0
for elem in lst:
    if elem==maximum:
        lst[idx]=minimum
        idx+=1
    elif elem==minimum:
        lst[idx]=maximum
        idx+=1
    else:
        idx+=1
print("Список после замены -",lst)