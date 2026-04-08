"""Escreva um programa que receba a idade de 50 pessoas usando uma estrutura de repetição. 
O programa deve calcular a soma de todas as idades digitadas e, ao final, exibir a 
média aritmética das idades em valor inteiro."""

soma_idades = 0
for i in range(50):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    soma_idades += idade
media = soma_idades // 50
print("A média de idade do grupo é:", media, "anos.")