"""Escreva um programa que leia os três lados de um triângulo e 
verifique se ele é equilátero (todos os lados iguais)."""

ladoA = int(input("Digite o primeiro lado: "))
ladoB = int(input("Digite o segundo lado: "))
ladoC = int(input("Digite o terceiro lado: "))

if ladoA == ladoB == ladoC:
    print("O triângulo é equilátero.")
else:
    print("O triângulo não é equilátero.")