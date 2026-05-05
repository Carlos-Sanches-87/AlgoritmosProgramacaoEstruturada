# Exercício 10: Lista de Listas (Matriz 3x3)
# Crie uma matriz 3x3 e exiba os valores, a soma total e a diagonal principal.

# 1. Criando a matriz 3x3
matriz = [
    [1, 2, 3], # Linha 0
    [4, 5, 6], # Linha 1
    [7, 8, 9]  # Linha 2
]

print("--- Matriz 3x3 ---")
# 2. Exibindo todos os valores de forma organizada
soma_total = 0
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t") # \t adiciona um espaço de tabulação
        soma_total += elemento
    print() # Pula para a próxima linha após imprimir uma linha da matriz

# 3. Exibindo a soma total
print(f"\nA soma de todos os elementos é: {soma_total}")

# 4. Exibindo a diagonal principal
# A diagonal principal ocorre quando o índice da linha é igual ao da coluna
print("Diagonal principal:", end=" ")
for i in range(3):
    print(matriz[i][i], end=" ")
print()
