for i in range(1000):
    i_into_str = str(i)
    str_1=i_into_str.find('1')
    str_7=i_into_str.find('7')
    if str_1 != -1 and str_7 != -1:
        print(i)
    else:
        continue