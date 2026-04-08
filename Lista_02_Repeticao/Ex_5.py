"""Escreva um programa que leia as notas de 10 alunos usando uma estrutura de repetição. 
O programa deve acumular o valor dessas notas e exibir a soma total ao final."""

soma_notas = 0
for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i + 1}:").replace(',', '.'))
    soma_notas += nota
print("A soma total das notas é:", soma_notas)