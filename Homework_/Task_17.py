def quadratic_equation (a,b,c):
    import math
    D = int(b ** 2) - 4 * int(a) * int(c)
    D = D/(1/2)
    x1 = (-b + D) / (2 * a)
    x2 = (-b - D) / (2 * a)
    return x1,x2

a = int(input("Введите а(первый коэффициент квадр. уравнения): "))
b = int(input("Введите b(второй коэффициент квадр. уравнения): "))
c = int(input("Введите c(третий коэффициент квадр. уравнения): "))

x1,x2 = quadratic_equation(a,b,c)
print("Корни квадратного уравнения при a=" ,a,",","b=",b ,",","c=",c,",", "равны: ",x1,",",x2)
