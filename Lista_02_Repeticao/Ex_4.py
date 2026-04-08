"""Escreva um programa que leia as notas de 20 alunos. 
O programa deve verificar, contar e exibir a quantidade de alunos que 
obtiveram nota maior ou igual a 5.0."""

contador_nota = 0
for i in range(20):
    nota = float(input(f"Digite a nota no aluno {i + 1}: ").replace(',', '.'))
    if nota >= 5.0:
        contador_nota += 1
print("Quantidade de alunos com nota maior ou igual a 5.0:", contador_nota)