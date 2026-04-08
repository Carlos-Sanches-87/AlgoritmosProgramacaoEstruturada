"""Crie um programa que solicite ao usuário quatro valores (A, B, C e D). 
O programa deve calcular a média ponderada desses valores, sabendo que:
Valor A tem peso 3
Valor B tem peso 4
Valor C tem peso 2
Valor D tem peso 5"""

valor_A = float(input("Digite o valor 1: "))
valor_B = float(input("Digite o valor 2: "))
valor_C = float(input("Digite o valor 3: "))
valor_D = float(input("Digite o valor 4: "))
media = round((valor_A * 3 + valor_B * 4 + valor_C * 2 + valor_D * 5) / 14, 2)
print("A média ponderada dos valores é: ", media)