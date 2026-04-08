"""Escreva um programa que leia a idade de 20 pessoas usando uma estrutura de repetição. 
O programa deve verificar, contar e exibir ao final a quantidade exata de 
pessoas que possuem 30 anos de idade."""

contador_30 = 0
for i in range(1, 21):
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    if idade == 30:
        contador_30 += 1
print("Quantidade de pessoas com 30 anos:", contador_30)