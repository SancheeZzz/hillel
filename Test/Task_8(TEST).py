lst = [1,2,3,4,5,6,7,8,9,10,11,12]
maximum= max(lst)
minimum= min(lst)
for i in lst:
    idx=i-1
    if i == maximum:
        lst[idx]=minimum
        continue
    if i == minimum:
        lst[idx]=maximum
        continue
print(lst)