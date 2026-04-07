anonasc = int(input("Insira seu ano de nascimento:"))
idade2026 = 2026 - anonasc
print(idade2026)
if idade2026 < 16:
    print("NAO VOTA")
elif idade2026 < 18:
    print("VOTO OPCIONAL")
else:
    print("pode votar caba")