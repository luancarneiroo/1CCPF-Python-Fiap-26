numero01 = int(input("Informe um número:"))
numero02 = int(input("Informe outro número:"))

if numero01 > numero02:
    print(f"o primeiro número é o vencedor{numero01}")
elif numero01 < numero02:
    print(f"o segundo número é o vencedor:{numero02}")
else:
    print("sao gemeos")
