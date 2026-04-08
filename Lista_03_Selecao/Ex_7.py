"""Escreva um programa que leia dois valores. O programa deve identificar o maior 
e o menor valor e exibir o resultado da divisão do maior pelo menor."""

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
maior = max(valor1, valor2)
menor = min(valor1, valor2)
if menor == 0:
    print("Erro: Não é possível realizar a divisão por zero!")
else:
    resultado = maior / menor
    print("O resultado da divisão do maior pelo menor é:", round(resultado, 2))