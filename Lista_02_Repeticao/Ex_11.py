"""Escreva um programa que leia as notas de 10 alunos. 
O programa deve calcular e exibir a média aritmética APENAS das notas 
que forem maiores que 5.0 E menores que 7.0."""

soma_notas = 0
contador = 0
for i in range(1, 11):
    nota = float(input(f"Digite a nota do aluno {i}: ").replace(',', '.'))
    if nota > 5.0 and nota < 7.0:
        soma_notas += nota
        contador += 1
if contador > 0:
    media = soma_notas / contador
    print("A média das notas (entre 5.1 e 6.9) é:", media)
else:
    print("Nenhum aluno com nota entre 5.1 e 6.9.")