import math
a=43.2
b=25
c=42
result_1= a + b * (c/2)
print("Answer of 1 task is -","%.2f"%result_1)
result_2 = ((a**2)+(b**2))%2
print("Answer of 2 task is -","%.2f"%result_2)
result_3=  (a+b)/ 12 * c % 4 + b
print("Answer of 3 task is -","%.2f"%result_3)
result_4= (a - b * c ) / ( a + b ) % c
print("Answer of 4 task is -","%.2f"%result_4)
result_5=  abs(a - b)  /( a + b)**3 - math.cos( c )
print("Answer of 5 task is -","%.2f"%result_5)
result_6= (math.log(1 + c)/(-b))**4 + abs(a)
print("Answer of 6 task is -","%.2f"%result_6)