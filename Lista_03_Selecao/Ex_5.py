"""Escreva um programa que leia os três lados de um triângulo e 
verifique se ele é estritamente isósceles (possui exatamente dois lados iguais)."""

ladoA = int(input("Digite o primeiro lado: "))
ladoB = int(input("Digite o segundo lado: "))
ladoC = int(input("Digite o terceiro lado: "))
if (ladoA == ladoB or ladoA == ladoC or ladoB == ladoC) and not (ladoA == ladoB == ladoC):
    print("O triângulo é isósceles.")
else:
    print("O triângulo não é iósceles")