def quadratic_equation (a,b,c):
    import math
    D = b ** 2 - (4 * a * c)
    if D>0:
        root_of_d = int(D) / (1 / 2)
        x1 = (-b + root_of_d) / (2 * a)
        x2 = (-b - root_of_d) / (2 * a)
        return x1,x2
    elif D==0:
        x = -b/(2*a)
        return x,None
    else:
        return None,None

a = int(input("Введите а(первый коэффициент квадр. уравнения): "))
b = int(input("Введите b(второй коэффициент квадр. уравнения): "))
c = int(input("Введите c(третий коэффициент квадр. уравнения): "))

print(quadratic_equation(a,b,c))



# x1,x2 = quadratic_equation(a,b,c)
# print("Корни квадратного уравнения при a=" ,a,",","b=",b ,",","c=",c,",", "равны: ",x1,",",x2)
