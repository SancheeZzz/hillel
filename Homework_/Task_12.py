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
# f_number = n // 100
# s_number = n % 100 // 10
# th_number = n % 10

def sum_of_3_numbers (n):
    result = n//100 + (n%100//10)+ n%10
    return result

n = int(input("Enter random number "))

result = sum_of_3_numbers(n)

print ("Sum of 3 number is -", result)