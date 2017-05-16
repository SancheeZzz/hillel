print("Программа для вычисления ближайшего к 10 из двух чисел")
num_1 = int(input ("Введите первое число: "))
num_2 = int(input ("Введите второе число: "))
distance_1 = 10 - num_1
distance_2 = 10 - num_2

if abs(distance_1) < abs(distance_2):
    print("Число %d ближе всего к 10" % (num_1))
elif abs(distance_1) > abs(distance_2):
    print("Число %d ближе всего к 10" % (num_2))
elif abs(distance_1) == abs(distance_2):
    print("Числа равноотдалённые от 10")


