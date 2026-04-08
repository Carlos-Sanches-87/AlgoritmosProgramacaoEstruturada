"""Crie um programa semelhante ao anterior, pedindo quatro valores ao usuário (A, B, C e D). 
Desta vez, calcule a média ponderada sabendo que:
Valor A tem peso 7
Valor B tem peso 3
Valor C tem peso 4
Valor D tem peso 2"""

valor_A = float(input("Digite o valor 1: "))
valor_B = float(input("Digite o valor 2: "))
valor_C = float(input("Digite o valor 3: "))
valor_D = float(input("Digite o valor 4: "))
media = round((valor_A * 7 + valor_B * 3 + valor_C * 4 + valor_D * 2) / 16, 2)
print("A média ponderada dos valores é: ", media)