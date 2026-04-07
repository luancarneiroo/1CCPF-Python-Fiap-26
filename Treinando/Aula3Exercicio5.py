numeroA = int(input('Me diga um número:'))
numeroB = int(input('Me diga um número:'))
RestoNumero = numeroA % numeroB
print(RestoNumero)

if RestoNumero == 0:
    print("ELES SAO MULTIPLOS")
elif RestoNumero == numeroA:
    print("ELES SAO MULTIPLOS")
else:
    print("eles nao sao multiplos")