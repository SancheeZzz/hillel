v1= int(input("Введите скорость 1 поезда: "))
v2= int(input("Введите скорость 2 поезда: "))

time_1 = 4/v1 #находим время, за которое поезда пройдут 4 и 6 км соответственно
time_2 = 6/v2

if time_2>time_1:
    print("Поезда столкнутся!")
else:
    print("Поезда не столкнутся! Отставить панику!")
