"""
Escreva um programa que receba dois números e um sinal,
e faça a operação matemática definida pelo sinal.
"""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Ditite o segundo número: "))
sinal = input("Digite o sinal: ")

if sinal == "+":
    op = n1 + n2

elif sinal == "-":
    op = n1 - n2

elif sinal == "*":
    op = n1 * n2

elif sinal == "/":
    op = n1 / n2

elif sinal == "**":
    op = n1 ** n2

else:
    print("Sinal inválido")

print(op)
