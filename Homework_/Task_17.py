import math
def quadratic_equation (a,b,D):
    if D > 0:
        D = math.sqrt(int(D))
        x1 = (-b + D) / (2 * a)
        print("x1 = ", x1)
        x2 = (-b - D) / (2 * a)
        print("x2 = ", x2)
    elif D == 0:
        D = -b / (2 * a)
        print("Вершина x = ", D)
    else:
        print("Корней нет.")
    return

a = int(input("Введите а(первый коэффициент квадр. уравнения): "))
b = int(input("Введите b(второй коэффициент квадр. уравнения): "))
c = int(input("Введите c(третий коэффициент квадр. уравнения): "))
D = int(b ** 2) - 4 * int(a) * int(c)
print("Дискриминант равен = ", D)
print(quadratic_equation(a,b,D))
