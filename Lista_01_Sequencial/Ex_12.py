"""Crie um programa que calcule a área total da superfície de um cilindro. 
Peça o raio e a altura ao usuário, e continue usando o math.pi para os cálculos. 
Exiba a área total na tela no final."""

import math
altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o valor do raio da base do cilindro: "))
area_base = math.pi * (raio ** 2)
area_lateral = 2 * math.pi * raio * altura
area_total = (2 * area_base) + area_lateral
print("A área total da superfície desse cilindro é: ", area_total)