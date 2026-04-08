"""Escreva um programa que solicite ao usuário um número. 
O programa deve verificar se o número está na faixa entre 1 e 9 (inclusive). 
Caso esteja, exiba "Valor na faixa.". Caso contrário, exiba "Valor fora da faixa."."""

numero = int(input("Digite um número: "))
if numero >= 1 and numero <= 9:
    print("Valor na faixa")
else:
    print("Valor fora da faixa")