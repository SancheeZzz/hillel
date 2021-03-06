

def intersection_of_circles (x_1,y_1,radius_1,x_2,y_2,radius_2):
    import math
    distance_between_centers = math.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2))
    sum_of_radii = radius_1 + radius_2
    if distance_between_centers > sum_of_radii:
        result = False
    elif distance_between_centers < abs(radius_2-radius_1) :
        result = False
    else:
        result = True
    return result

x_1 = int(input("Введите первую координату центра ПЕРВОГО круга: "))
y_1 = int(input("Введите вторую координату центра ПЕРВОГО круга: "))
radius_1 = int(input("Введите длину радиуса первого круга: "))
x_2 = int(input("Введите первую координату центра ВТОРОГО круга: "))
y_2 = int(input("Введите вторую координату центра ВТОРОГО круга: "))
radius_2 = int(input("Введите длину радиуса второго круга: "))

if not intersection_of_circles(x_1,y_1,radius_1,x_2,y_2,radius_2):
    print("круги не пересекаются либо один круг входит в другой")
else:
    print("Круги соприкасаются либо пересекаются")
