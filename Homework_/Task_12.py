#1попытка
# def sum_of_3_numbers (number):
#     f_number = number.find(0)
#     s_number = number.find(1)
#     th_number = number.find(2)
#     result = int(f_number)+ int(s_number) + int(th_number)
#     return result
#2попытка
#  f_number = number[0]
# s_number = number[0:1]
# th_number = number[1:2]
# sum_of_numbers = int(f_number)+ int(s_number) + int(th_number)
#3 попытка

import math
n = input("Enter random number ")
n = int(n)

f_number = n // 100
s_number = n % 100 // 10
th_number = n % 10

print ("Sum of 3 number is -", f_number + s_number + th_number)