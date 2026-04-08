"""Escreva um programa que receba a idade de 100 pessoas. 
O programa deve verificar e contar quantas dessas pessoas têm exatamente 30 anos.
Ao final, exiba a quantidade total de pessoas encontradas com essa idade."""

contador_30 = 0
for i in range(100):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    if idade == 30:
        contador_30 += 1
print("Quantidade de pessoas com 30 anos:", contador_30)