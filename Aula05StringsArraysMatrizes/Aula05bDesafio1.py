# ATIVIDADE 1: Duplas – Repetições encadeadas
# Dado um conjunto de nomes de quatro pessoas, escreva um algoritmo que imprima todas as possíveis duplas que podem ser formadas.
# Primeiro, crie um vetor e coloque quatro nomes nele.
# A seguir, exiba as possíveis duplas.

pessoas = ["luan","iris","serena","miriam"]

tamanho = len(pessoas)
print(f"Pessoas: {pessoas[0]}")
print(f"Número de pessoas: {tamanho}")
print("===========================================")

for i in range (len(pessoas)):
    for j in range (i + 1, len(pessoas)):
        print(f"Dupla: {pessoas[i]} & {pessoas[j]}")