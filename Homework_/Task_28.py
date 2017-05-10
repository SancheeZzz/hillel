import random
lst_1=[]
lst_2=[]

while len(lst_1)<=5 :
    num= random.randint (0,5)
    if num%2==0:
        lst_1.append(num)
while len(lst_2)<=5 :
    num= random.randint (0,5)
    lst_2.append(num)

lst_in_str_1 = " , ".join([str(c) for c in lst_1])
print(lst_in_str_1)

lst_in_str_2 = " , ".join([str(c) for c in lst_2])
print(lst_in_str_2)

avr_of_lst_1= sum(lst_1)/len(lst_1)
avr_of_lst_2= sum(lst_2)/len(lst_2)

if avr_of_lst_1 > avr_of_lst_2:
    print("Среднее значение первого списка больше за значение второго")
elif avr_of_lst_1 == avr_of_lst_2:
    print("Среднеие значения списков равны")
elif avr_of_lst_1 < avr_of_lst_2:
    print("Среднее значение второго списка больше за значение первого")