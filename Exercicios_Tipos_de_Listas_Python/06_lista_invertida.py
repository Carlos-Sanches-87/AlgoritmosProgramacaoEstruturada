# Exercício 6: Lista Invertida
# Crie uma lista com 8 números e mostre a lista na ordem inversa.

# 1. Criando a lista com 8 números
numeros = [10, 20, 30, 40, 50, 60, 70, 80]

print(f"Lista original: {numeros}")

# 2. Invertendo a lista
# Forma 1: Usando fatiamento (Slicing) - cria uma nova lista invertida
lista_invertida = numeros[::-1]

print(f"Lista invertida (Forma 1): {lista_invertida}")

# Forma 2: Usando o método reverse() - inverte a lista original "no lugar"
numeros.reverse()
print(f"Lista invertida (Forma 2): {numeros}")
