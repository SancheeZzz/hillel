import random
random_number = random.randint(1,10)
print("Игра'Угадай число!'")
print("Программа загадала число, вам предлагается его отгадать, всё просто не так ли?")
while True:
    inp_num = int(input("Введите предполагаемое число ( 0(ноль) чтобы выйти): "))

    if inp_num == 0:
        print("Слабак!")
        break
    elif inp_num == random_number:
        print("Да ты Ванга!!!")
        break
    elif inp_num > random_number:
        print("--------*ПОДСКАЗКА* - 'Ты ввёл число больше загаданного!'------------")
    elif inp_num < random_number:
        print("--------*ПОДСКАЗКА* - 'Ты ввёл число меньше загаданного!'------------")