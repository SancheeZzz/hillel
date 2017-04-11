s = "qwe rty uio"
spase_1 = s.find(" ")
space2 = s.find (" ", spase_1+1)
mid_of_s = s[ spase_1 +1:space2]
letters_1 = s[:spase_1]
letters_2 = s[space2 + 1:]
result = str(letters_1) + " " + str(mid_of_s.upper()) + " " + str(letters_2)
print(result)