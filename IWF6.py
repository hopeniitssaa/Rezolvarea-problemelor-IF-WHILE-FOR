n = int(input("Dati un numar: "))
s1 = 0
s2 = 0
suma1 = 0
suma2 = 0

# a)
for i in range(1, (n + 1)):
    suma2 = (i ** 3)
    s1 += suma2
    suma1 += i
s2 = suma1 ** 2
if (s1 < s2):
    print("s1 < s2")
elif (s1 > s2):
    print("s1 > s2")
elif (s1 == s2):
    print("s1 = s2")

# b)
s1 = 0
s2 = 0
suma1 = 0
suma2 = 0
for i in range(1, (n + 1)):
    suma2 += (i ** 2) 
    suma1 += i
s1 = suma2 * 3
s2= (n ** 3) + (n ** 2) + suma1
if (s1 < s2):
    print("s1 < s2")
elif (s1 > s2):
    print("s1 > s2")
elif (s1 == s2):
    print("s1 = s2") 