# Exercício 5: Lista de Números Pares
# Crie uma lista com números de 1 a 20 e exiba apenas os números pares.

# 1. Criando a lista de 1 a 20 usando range()
# Note que range(1, 21) vai do 1 até o 20
numeros = list(range(1, 21))

print(f"Lista completa: {numeros}")
print("Números pares da lista:")

# 2. Percorrendo a lista para filtrar os pares
for num in numeros:
    # Se o resto da divisão por 2 for zero, o número é par
    if num % 2 == 0:
        print(num, end=" ") # end=" " serve para imprimir na mesma linha

# Dica extra: Também poderíamos criar a lista já apenas com os pares:
# pares_direto = list(range(2, 21, 2))
