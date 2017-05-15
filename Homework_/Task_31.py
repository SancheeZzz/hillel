import random


symbols_for_pass_num = ['1','2','3','4','5','6','7','8','9',]
symbols_for_pass_low=["a",'b',"c","d","e","f","g","h","i","j","k","l",'m','n','o','p','q','r','s','t','u','v','w','x','y','z','_',]
symbols_for_pass_cap=["A",'B',"C","D","E","F","G","H","I","J","K","L",'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


password=[]
max_len= 8
condition= 6

while len(password)< max_len:
    rand_symbol_low = random.choice(symbols_for_pass_low)
    rand_symbol_num = random.choice(symbols_for_pass_num)
    password.append(rand_symbol_low)
    password.append(rand_symbol_num)

password.remove(random.choice(password))
password.append(random.choice(symbols_for_pass_cap))

random.shuffle(password)

password = "".join([str(c) for c in password])
print("Password - " , password)