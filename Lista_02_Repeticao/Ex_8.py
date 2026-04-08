"""Escreva um programa que receba a idade de 10 alunos. 
O programa deve calcular e exibir a soma das idades APENAS dos alunos que 
tenham mais de 25 anos."""

soma_idades = 0
for i in range(1, 11):
    idade = int(input(f"Digite a idade do aluno {i}: "))
    if idade > 25:
        soma_idades += idade
print("A soma das idades dos alunos maiores de 25 anos é:", soma_idades)