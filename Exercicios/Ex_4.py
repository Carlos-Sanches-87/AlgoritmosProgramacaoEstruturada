"""Crie um programa que peça ao usuário para digitar uma quantidade de horas (podendo ter casas decimais, como 2.5 horas)
 e converta esse valor para minutos, exibindo o resultado final na tela."""

hora = float(input("Escreva a hora: "))
minutos = int(hora * 60)
print("Essa hora possui ", minutos, " minutos.")