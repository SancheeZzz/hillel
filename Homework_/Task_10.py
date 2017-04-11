s= "Leo Tolstoy*1828-08-28*1910-11-20"
idxstar_1 = s.find ("*")
idxstar_2 = s.find ("*",idxstar_1+1)
name = s [:idxstar_1]
idxdelimiter_1= s.find ("-")
idxdelimiter_2 = s.find ("-", idxstar_2+1)
year_of_birth = s [idxstar_1+1: idxdelimiter_1]
year_of_death = s [idxstar_2+1: idxdelimiter_2]
years_of_life = int(year_of_death) - int(year_of_birth)
print('"',name,'"',",",years_of_life)