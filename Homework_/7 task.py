date_USA = "03.19.2017"
first_point = date_USA [2]
second_point = date_USA [5]
month = date_USA[0:2]
day = date_USA [3:5]
year = date_USA [6:]
date_EU = day + first_point + month + second_point + year
print(date_EU)