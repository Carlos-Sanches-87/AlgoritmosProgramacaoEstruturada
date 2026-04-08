"""Escreva um programa que leia as notas de 10 alunos. 
O programa deve acumular a soma de todas as notas e, ao mesmo tempo, 
contar quantos alunos obtiveram nota 5.0 ou superior."""

soma_notas = 0
contador_5 = 0
for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i + 1}:").replace(',', '.'))
    soma_notas += nota
    if nota >= 5.0:
        contador_5 += 1
print("A soma de todas as notas é:", soma_notas)
print("A quantidade de alunos com nota igual ou maior que 5.0 é:", contador_5)