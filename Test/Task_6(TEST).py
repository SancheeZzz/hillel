from math import sqrt
import random
#отбираем простые числа в любом диапазоне
simple_numbers=[]

for i in range (2,101):
    is_simple = True
    for n in range (2, int(sqrt(i))+1):
        if i%n==0:
            is_simple=False
            break
    if is_simple==True:
        simple_numbers.append(i)
print(simple_numbers)

#создаём пустой массив
ten_numbers=[]

#создаем переменную для подсчёта кол-ва цифр в массиве
count=0

#наполняем массив ранее отобранными простыми числами
while count<10:
    rand_num = random.choice(simple_numbers)
    ten_numbers.append(rand_num)
    count += 1

#выводим на экран массив из 10 простых чисел, рандомно отобранных
print(ten_numbers)