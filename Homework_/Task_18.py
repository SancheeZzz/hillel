def sum_of_unicodes (symbol_1,symbol_2):
    unicode_symb_x = ord (symbol_1)
    unicode_symb_z = ord(symbol_2)
    unicode_symb_y = unicode_symb_x + 1
    sum= unicode_symb_x + unicode_symb_y + unicode_symb_z
    return sum
print("Sum unicodes of x,y,z is equal to",sum_of_unicodes('x','z'))