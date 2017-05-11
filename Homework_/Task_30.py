str=input("Введите строку, которую хотите зашифровать")
tab_of_encryption = ["a",'b',"c","d","e","f","g","h","i","j","k","l",'m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str_2 = ""

for i in str:
    idx_1 = str.find(i)
    idxPlus5 = idx_1 + 5
    if idxPlus5 > len(tab_of_encryption):
        elem_of_tab = tab_of_encryption[idxPlus5-len(tab_of_encryption)]
    else:
        elem_of_tab = tab_of_encryption [idxPlus5]
    str_2+= elem_of_tab
print("Зашифрованная строка-",str_2)
