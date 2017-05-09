lst = [1,2,3,4,5]
def avr_of_lst (lst):
    sum=0
    for i in lst:
        sum+=i
    avr = sum/len(lst)
    return avr
print("Average = ",avr_of_lst(lst))