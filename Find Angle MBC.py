import math

AB = int(input())
BC = int(input())

CA = math.hypot(AB,BC)


MBC = math.degrees(math.acos(BC/CA));


print(round(MBC),'\u00B0',sep='')