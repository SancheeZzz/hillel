# import math
# x_1,y_1 = int(input("Введите через запятую координаты центра ПЕРВОГО круга: "))
# radius_1 = int(input("Введите длину радиуса первого круга: "))
# x_2,y_2 = int(input("Введите через запятую координаты центра ВТОРОГО круга: "))
# radius_2 = int(input("Введите длину радиуса второго круга: "))
# distance_between_centers = math.sqrt((x_2-x_1)**2 + (y_2-y_1**2))
# sum_of_radii = radius_1+radius_2
# if distance_between_centers > sum_of_radii :
#     print("круги не пересекаются")
# else:
#     distance_between_centers < sum_of_radii
#     print("Круги пересекаются")

import math
x_1 = int(input("Введите первую координату центра ПЕРВОГО круга: "))
y_1 = int(input("Введите вторую координату центра ПЕРВОГО круга: "))
radius_1 = int(input("Введите длину радиуса первого круга: "))
x_2 = int(input("Введите первую координату центра ВТОРОГО круга: "))
y_2 = int(input("Введите вторую координату центра ВТОРОГО круга: "))
radius_2 = int(input("Введите длину радиуса второго круга: "))
distance_between_centers = math.sqrt(((x_2-x_1)**2) + ((y_2-y_1)**2))
sum_of_radii = radius_1+radius_2
if distance_between_centers > sum_of_radii :
    print("круги не пересекаются")
else:
    print("Круги пересекаются")

