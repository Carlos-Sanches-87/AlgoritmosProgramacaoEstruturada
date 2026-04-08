"""Escreva um programa que peça ao usuário para digitar um número inteiro. 
O programa deve verificar e exibir na tela se o número digitado é 
"Igual a Zero" ou "Diferente de Zero"."""

numero = int(input("Digite um número inteiro: "))
if numero == 0:
    print("Igual a zero")
else:
    print("Diferente de zero")