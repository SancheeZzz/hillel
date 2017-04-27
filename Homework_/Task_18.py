def sum_of_unicodes (symbol_1,symbol_2):
    unicode_symb_1 = ord (symbol_1)
    unicode_symb_3 = ord (symbol_2)
    sum=0
    for i in range (unicode_symb_1+1,unicode_symb_3):
        sum+=i
    unicodes_sum= unicode_symb_1 + sum + unicode_symb_3
    return unicodes_sum

print("---Программа для рассчёта суммы чисел Unicode символов---")
symbol_1 = str(input("Введите ПЕРВЫЙ символ: "))
symbol_2 = str(input("Введите ВТОРОЙ символ: "))
print("Sum unicodes of is equal to",sum_of_unicodes(symbol_1,symbol_2))