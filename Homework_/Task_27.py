import random
lst=[]
#наполняем список
while len(lst)<=50 :
    num= random.randint (1,100)
    if num%2==0:
        continue
    lst.append(num)

print(lst)
#переводим в строку и выводим на экран
lst_in_str = " , ".join([str(c) for c in lst])
print(lst_in_str)
#перемешиваем список, переводим в строку и выводим на экран
random.shuffle (lst)
lst_in_str_2 =" , ".join([str(c) for c in lst])
print(lst_in_str_2)