def square_of_right_triangle (catheter_1,catheter_2):
        result = 1/2 * (catheter_1*catheter_2)
        return result

def perimeter_of_right_triangle(catheter_1,catheter_2):
        import math
        result= math.sqrt(catheter_1**2+catheter_2**2)
        return result

catheter_1 = int(input("Enter the length of the first catheter:" ))
catheter_2 = int(input("Enter the length of the second catheter:" ))

print( "A square of right triangle -" ,int(square_of_right_triangle(catheter_1,catheter_2)))
print( "A perimeter of right triangle -" ,int(perimeter_of_right_triangle(catheter_1,catheter_2)))
# c**2=a**2 + b**2