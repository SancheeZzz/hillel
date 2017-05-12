import random
lst = []
while len(lst)<=11 :
    num= random.randint (-1,1)
    lst.append(num)
print(lst)
zeros = lst.count(0)
ones = lst.count(1)
minus_ones = lst.count(-1)
if zeros==ones or  zeros==minus_ones or minus_ones==ones:
    print('')
else:
    if zeros == max(zeros,ones,minus_ones):
        print("Наиболее часто встречается число 0")
    elif ones == max(zeros,ones,minus_ones):
        print("Наиболее часто встречается число 1")
    elif minus_ones == max(zeros, ones, minus_ones):
        print("Наиболее часто встречается число -1")
