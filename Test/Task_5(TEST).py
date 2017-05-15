print("Программа для вычисления ближайшего к 10 из двух чисел")
num_1 = int(input ("Введите первое число: "))
num_2 = int(input ("Введите второе число: "))
condition_1 = 10 - num_1
condition_2 = 10 - num_2

if abs(condition_1) < abs(condition_2):
    print("Число %d ближе всего к 10" % (num_1))
elif abs(condition_1) > abs(condition_2):
    print("Число %d ближе всего к 10" % (num_2))
elif abs(condition_1) == abs(condition_2):
    print("Числа равноотдалённые от 10")


