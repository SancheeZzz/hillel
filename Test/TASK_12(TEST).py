import random
amount_of_multipliers = 15
lst_1=[x for x in range(2,10)]
lst_2=[x for x in range(2,10)]

def print_multiply(a,b):
    multiply = ("%d * %s" % (a, b))
    return multiply

def make_samples(lst_1,lst_2):
    lst_of_samples=[]
    samples=0
    while samples!=15:
        a = random.choice(lst_1)
        b = random.choice(lst_2)
        if print_multiply(a,b) in lst_of_samples:
            continue
        elif print_multiply(b,a) in lst_of_samples:
            continue
        else:
            lst_of_samples.append(print_multiply(a,b))
        samples+=1
    return lst_of_samples

print(make_samples(lst_1,lst_2))