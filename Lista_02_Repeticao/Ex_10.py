"""Escreva um programa que leia a idade de 10 alunos. 
O programa deve calcular e exibir a média das idades APENAS dos alunos 
que tenham mais de 25 anos E menos de 40 anos."""

soma_idades = 0
contador = 0
for i in range(1, 6):
    idade = int(input(f"Digite a idade do aluno {i}: "))
    if idade > 25 and idade < 40:
        soma_idades += idade
        contador += 1
if contador > 0:
    media = soma_idades / contador
    print("A média das idades (entre 26 e 39 anos) é:", media)
else:
    print("Nenhum aluno com idade entre 26 e 39 anos.")