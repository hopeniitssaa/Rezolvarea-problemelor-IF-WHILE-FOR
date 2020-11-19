n=int(input("Dati un numar: "))
suma=0
if (n != 0) and (n != 1):
    for i in range (1, n):
        if n % i == 0:
            suma += i
    if suma == n:
        print("Numarul", n,"este perfect")
    else:
        print("Numarul", n,"nu este perfect")