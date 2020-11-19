from fractions import Fraction
m = int(input("dati numaratorul1: "))
n = int(input("dati numitorul1: "))
a = int(input("dati numaratorul2: "))
b = int(input("dati numitorul2: "))
if ((n!=0) and (b!=0)):
    print("Suma este:", Fraction(a,b)+Fraction(m,n))
    print("Produsul este:", Fraction(a,b)*Fraction(m,n))
else:
    print("Numitorul unei fractii nu poate fi 0") 