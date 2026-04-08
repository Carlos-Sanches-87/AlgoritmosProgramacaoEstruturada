"""Escreva um programa que peça ao usuário um número inteiro positivo. 
O programa deve calcular e exibir o fatorial desse número usando um laço de repetição."""

fatorial = 1
numero = int(input("Digite um número para calcular o fatorial: "))
for i in range(1, numero + 1):
    fatorial *= i
if fatorial >= 1000000:
    print(f"O fatorial de {numero} é: {fatorial:.2e}")
else:
    print(f"O fatorial de {numero} é: {fatorial}")