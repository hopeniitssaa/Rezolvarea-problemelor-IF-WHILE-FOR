m, n = eval(input("Dati 2 numere: "))
exp=0
da = ''
nu = ''
if m < n: 
    for i in range(1, n):
        exp = m ** i
        if (exp == n):
             da = 'Da'
        else:
            nu = 'Nu'
    if (da == 'Da'):
        print("Da") 
    else: 
        print("Nu")
else: 
        print("Alegeti alte 2 numere")