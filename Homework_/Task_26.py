lst= [2,2,2,3,3]

def sum_diff (lst):
    sum_of_even=0
    sum_of_odd=0
    for i in lst:
        if i%2==0:
            sum_of_even+=i
        else:
            sum_of_odd+=i
    sum_different=sum_of_even-sum_of_odd
    return sum_different

print("Sum different =",sum_diff(lst))