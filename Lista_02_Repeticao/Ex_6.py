"""Escreva um programa que leia as notas de 10 alunos. 
O programa deve calcular a soma total e, em seguida, 
calcular e exibir a média aritmética da turma."""

soma_notas = 0
for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i + 1}:").replace(',', '.'))
    soma_notas += nota
media = soma_notas / 10
print("A média aritmética da turma é:", round(media, 2))