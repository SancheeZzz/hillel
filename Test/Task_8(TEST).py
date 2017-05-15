lst = [1,2,3,4,5,6,7,8,9,10,11,12]
maximum= max(lst)
minimum= min(lst)
for i in lst:
    if i == maximum:
        lst[i-1]=minimum
        continue
    if i == minimum:
        lst[i-1]=maximum
        continue
print(lst)