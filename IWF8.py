a, b, c = input("Dati masurile laturilor unui triunghi (separate prin spatiu): ").split()
a=int(a)
b=int(b)
c=int(c)
if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    if (a == b) and (a == c) and (b == c):
        print("Echilateral")
    elif (a == b) or (a == c) or (b == c):
        print("Isoscel")
    else:
        print("Scalen")
else:
    print("Dati alte masuri.")