n=int(input("Dati virsta lui Mihai, mai mica de 20: "))
suma=1
suma2=0
v=0
for i in range (1, n + 1):
    suma = suma * 2 + i
print("La", n,"ani primeste", suma,"dolari")
while suma2 <= 100:
    v += 1
    suma2 = suma2 * 2 + v
print("Mihai primeste mai mult de 100 dolari la", v,"ani")