def is_parity (n):
   if n % 2 == 0:
        result = True
   else:
        result = False
   return result
print ("-=Эта программа предназначена для проверки чисел на чётность=-")
n= int(input("Введите случайное число: "))
print (is_parity(n))


