# Exercício 9: Lista Ordenada
# Crie uma lista com 10 números aleatórios e exiba em ordem crescente e decrescente.

import random

# 1. Gerando uma lista com 10 números aleatórios entre 1 e 100
# Usamos um 'list comprehension' que é uma forma rápida de criar listas
numeros = [random.randint(1, 100) for _ in range(10)]

print(f"Lista original (aleatória): {numeros}")

# 2. Ordenando em ordem CRESCENTE
numeros.sort()
print(f"Ordem Crescente:  {numeros}")

# 3. Ordenando em ordem DECRESCENTE
numeros.sort(reverse=True)
print(f"Ordem Decrescente: {numeros}")
