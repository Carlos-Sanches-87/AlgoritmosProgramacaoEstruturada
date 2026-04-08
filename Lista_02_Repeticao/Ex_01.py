"""Escreva um programa que receba a idade de 30 pessoas. 
O programa deve calcular e exibir na tela a soma de todas as idades digitadas."""

soma_idades = 0
for i in range(30):
    idade = int(input("Digite a idade: "))
    soma_idades += idade
print("A soma das idades é:", soma_idades, "anos.")