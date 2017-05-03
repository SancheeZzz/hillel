# lst=[]
# for i in range (1,101):
#     for n in range (2,i):
#         if i%n==0:
#             break
#         else:
#             lst.append(i)
#             break
# print (lst)

lst=[]
for i in range (2,101):
    a = True
    for n in range (2, i):
        if i%n==0:
            a=False
            break
    if a==True:
        lst.append(i)
print (lst)