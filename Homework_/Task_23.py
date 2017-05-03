def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n
print("---Функция нахождения факториала с числа---")
n = int(input("Введите число для нахождения факториала: "))
print("Факториал равен: ", factorial(n))