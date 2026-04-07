salario_colab = int(input("Informe o salário:"))

if salario_colab < 280:
    reajuste = salario_colab * 0.20
elif salario_colab < 700:
    reajuste = salario_colab * 0.15
elif salario_colab < 1500:
    reajuste = salario_colab * 10
else:
    reajuste = salario_colab * 5

salario_reaj = salario_colab + reajuste
print(f"O novo salario do colaborador é: R${salario_reaj}")
c
