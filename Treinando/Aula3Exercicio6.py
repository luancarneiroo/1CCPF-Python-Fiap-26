numA = int(input("INSIRA NUMERO:"))
numB = int(input("INSIRA OUTRO NUMERO:"))
caracas = str(input("INSIRA OPERADOR:"))

if caracas == "+":
    result = numA + numB
elif caracas == "-":
    result = numA - numB
elif caracas == "*":
    result = numA * numB
elif caracas == "/":
    result = numA / numB

print(result)