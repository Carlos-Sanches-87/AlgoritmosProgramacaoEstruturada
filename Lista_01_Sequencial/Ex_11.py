"""Desenvolva um programa para calcular o volume de um cone. 
Peça ao usuário o raio da base e a altura. 
Desta vez, no topo do seu código, digite import math e use math.pi 
para pegar o valor exato de Pi direto do sistema, em vez de digitar 3.14. 
Exiba o resultado."""

import math
altura = float(input("Digite a altura do cone: "))
raio = float(input("Digite o valor do raio da base do cone: "))
volume = (math.pi * (raio ** 2) * altura) / 3
print("O volume desse cone é de: ", volume)