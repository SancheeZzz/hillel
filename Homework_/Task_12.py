# def sum_of_3_numbers (number):
#     f_number = number.find(0)
#     s_number = number.find(1)
#     th_number = number.find(2)
#     result = int(f_number)+ int(s_number) + int(th_number)
#     return result
number = input("Enter random number " )
f_number = number[0]
s_number = number[0:1]
th_number = number[1:2]
sum_of_numbers = int(f_number)+ int(s_number) + int(th_number)
print(sum_of_numbers)