import random
#разделяем на разные списки для верхнего, нижнего регистра и цифр

symbols_for_pass_num = ['1','2','3','4','5','6','7','8','9',]
symbols_for_pass_low=["a",'b',"c","d","e","f","g","h","i","j","k","l",'m','n','o','p','q','r','s','t','u','v','w','x','y','z','_',]
symbols_for_pass_cap=["A",'B',"C","D","E","F","G","H","I","J","K","L",'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#создаём пустой список для пароля
password=[]
max_len= 8
condition= 6

while len(password)< max_len:

    rand_symbol_num = random.choice(symbols_for_pass_num)
    rand_symbol_low = random.choice(symbols_for_pass_low)
    rand_symbol_cap = random.choice(symbols_for_pass_cap)

    if len (password) >= condition:
        password.append(rand_symbol_num)
        password.append(rand_symbol_low)
    else:
        password.append(rand_symbol_num)
        password.append(rand_symbol_low)
        password.append(rand_symbol_cap)


    random.shuffle(password)
password = "".join([str(c) for c in password])
print("Password - " , password)