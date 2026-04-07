nota1 = int(input("FALA SUA PRIMEIRA NOTA:"))
nota2 = int(input("FALA SUA SEGUNDA NOTA:"))
nota3 = int(input("FALA SUA TERCEIRA NOTA:"))
nota4 = int(input("FALA SUA QUARTA NOTA:"))

SomaNotas = nota1 + nota2 + nota3 + nota4
print (SomaNotas)
MediaNotas = SomaNotas / 4
print (MediaNotas)

if MediaNotas < 5:
    print("REPROVADO - renasça")
elif MediaNotas < 7:
    print("RECUPERAÇÃO - vagabundo ordinario")
else:
    print("APROVADO - parabens fez o minimo")



