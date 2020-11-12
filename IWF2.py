n=int(input("dati un numar: "))
suma = 0  
for i in range(1, n+1):
    f=1
    for n in range(1, i+1):
        f*=n 
    suma += f
print("1!+2!+3!+...+", n, "!=", suma) 
