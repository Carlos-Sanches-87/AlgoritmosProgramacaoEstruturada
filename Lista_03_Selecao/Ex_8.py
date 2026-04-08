"""Escreva um programa que leia os coeficientes (a, b, c) de uma equação do 2º grau.
O programa deve calcular o Delta e, se existirem raízes reais, exibi-las."""

import math
a = float(input("Digite o valor de 'a': "))
b = float(input("Digite o valor de 'b': "))
c = float(input("Digite o valor de 'c': "))
if a == 0:
    print("Se 'a' é igual a zero, isso não é uma equação do 2º grau.")
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print(f"Delta = {delta}. Como o Delta é negativo, não existem raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Delta = 0. A equação possui uma única raiz real: {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Valor de x1: {x1:.2f}")
        print(f"Valor de x2: {x2:.2f}")