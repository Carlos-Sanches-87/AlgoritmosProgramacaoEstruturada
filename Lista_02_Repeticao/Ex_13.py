"""Escreva um programa que peça um número inteiro ao usuário e informe 
se esse número é primo ou não."""

numero = int(input("Digite um número para saber se é primo: "))
if numero <= 1:
    print(f"O número {numero} NÃO é primo.")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"O número {numero} NÃO é primo")
            break
    else:
        print(f"O número {numero} É primo")