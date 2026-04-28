# Atividade 2: Problema da validação
def verificar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input(f"Digite a nota novamente: "))
    return nota

A = float(input(f"Digite a primeira nota: "))
verificar_nota(A)

B = float(input(f"Digite a segunda nota: "))
verificar_nota(B)

MediaArit = (A + B) / 2

print(MediaArit)

