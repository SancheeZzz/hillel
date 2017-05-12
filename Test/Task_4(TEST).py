summ=0
multiply=1
while True:
    n = input("введите любое пятизначное число")
    if len(n)<5 or len(n) >5:
        print("Введите 5 символов!")
    else:
        for i in n:
            if int(i)%2!=0:
                multiply = multiply * int(i)
        break
print(multiply)