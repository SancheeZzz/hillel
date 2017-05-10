str=input("Введите строку, которую хотите зашифровать")
tab_of_encryption = ["z",'p',"a","г","i","е","1","2","3","-","5","6"]
str_2 = ""
for i in str:
    idx_1 = str.find(i)
    elem_of_tab = tab_of_encryption [idx_1+5]
    str_2+= elem_of_tab
print("Зашифрованная строка-",str_2)
