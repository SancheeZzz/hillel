n=10
fibonnachi=[1,1,2]
for num in range(3,n):
    fibonnachi.append(fibonnachi[num-1]+fibonnachi[num-2])

print(fibonnachi)

sum_of_fib=sum(fibonnachi)
print("Сумма первых 10 чисел ряда Фибоначчи равна %d" % (sum_of_fib))