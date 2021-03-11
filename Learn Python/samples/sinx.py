import math
for i in range(0,1081):
    print(i,end=" ")
    if math.cos(math.degrees(i)/3)==math.sin(3*math.degrees(i)):
        print("/n/nx =",math.degrees(i))
print()
