"""Escreva um programa que calcule o volume de um cilindro. 
O programa deve pedir ao usuário a altura do cilindro e o raio da base. 
Para este exercício, use o valor de Pi cravado como 3.14. 
Exiba o volume final na tela."""

altura = float(input("Digite a altura do cilindro (em cm): "))
raio = float(input("Digite o valor do raio da base do cilindro: "))
pi = 3.14
volume = pi * (raio ** 2) * altura
print("O volume desse cilindro é de: ", volume)