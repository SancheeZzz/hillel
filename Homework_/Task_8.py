str_1 = "abcdefgh"
str_2 = "qwertyuio"

mid_str_1 = int(len(str_1)/2)
mid_str_2 = int(len(str_2)/2)

part_1_str_1 = str_1 [:mid_str_1+1]
part_2_str_1 = str_1 [mid_str_1+1:]

part_1_str_2 = str_2 [:mid_str_2+1]
part_2_str_2 = str_2 [mid_str_2+1:]

result = part_1_str_1+part_1_str_2 + part_1_str_1+part_2_str_1 + part_2_str_2 + part_2_str_1


print (result)
