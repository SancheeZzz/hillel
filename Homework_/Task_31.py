import random
symbols_for_pass = ["a",'b',"c","d","e","f","g","h","i","j",
                    "k","l",'m','n','o','p','q','r','s','t','u','v','w','x',
                    'y','z','_','1','2','3','4','5','6','7','8','9',"A",'B',
                    "C","D","E","F","G","H","I","J","K","L",'M','N','O','P',
                    'Q','R','S','T','U','V','W','X','Y','Z']
password=[]
while len(password)< 8:
    rand_symbol = random.choice(symbols_for_pass)
    password.append(rand_symbol)
password = "".join([str(c) for c in password])
print(password)