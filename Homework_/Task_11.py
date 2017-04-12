import math
def Degrees2Radians (degrees):
    result= math.radians(degrees)
    return(result)

cos_60= "%.2f" % math.cos(Degrees2Radians(60))
cos_45= "%.2f" % math.cos(Degrees2Radians(45))
cos_40= "%.2f" % math.cos(Degrees2Radians(40))

print("Cos of 60 degrees=", cos_60)
print("Cos of 45 degrees=", cos_45)
print("Cos of 40 degrees=", cos_40)