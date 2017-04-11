def square_of_right_triangle (catheter_1,catheter_2):
        result = 1/2 * (catheter_1*catheter_2)
        return result

catheter_1 = int(input("Enter the length of the first catheter:" ))
catheter_2 = int(input("Enter the length of the second catheter:" ))

print(int(square_of_right_triangle(catheter_1,catheter_2)))