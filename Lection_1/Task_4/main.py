import math
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
D = b**2-4*a*c
if D < 0:
    print ("no real roots exist")
else:
    print ("x1 =",(-b + math.sqrt(D))/(2*a))
    if D > 0:
        print ("x2 =",(-b - math.sqrt(D))/(2*a))
