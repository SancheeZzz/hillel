import random
#разделяем на разные списки для верхнего, нижнего регистра и цифр

symbols_for_pass_num = ['1','2','3','4','5','6','7','8','9',]
symbols_for_pass_low=["a",'b',"c","d","e","f","g","h","i","j","k","l",'m','n','o','p','q','r','s','t','u','v','w','x','y','z','_',]
symbols_for_pass_cap=["A",'B',"C","D","E","F","G","H","I","J","K","L",'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#создаём пустой список для пароля
password=[]

while len(password)< 8:

    #выбираем символы со списков

    rand_symbol_num = random.choice(symbols_for_pass_num)
    rand_symbol_low = random.choice(symbols_for_pass_low)
    rand_symbol_cap = random.choice(symbols_for_pass_cap)

    #добавляем их в password

    password.append(rand_symbol_num)
    password.append(rand_symbol_low)
    password.append(rand_symbol_cap)

    #перемешиваем password

    random.shuffle(password)

#делаем строку из списка и выводим на экран

password = "".join([str(c) for c in password])
print(password)