# Exercício 8: Lista com Busca
# Crie uma lista com 10 números e verifique se um número digitado existe nela.

# 1. Criando a lista com 10 números
numeros = [5, 12, 28, 40, 7, 100, 3, 19, 55, 82]

# 2. Pedindo um número para busca
print(f"Lista de busca: {numeros}")
busca = int(input("Digite um número para pesquisar na lista: "))

# 3. Verificando a existência e a posição
if busca in numeros:
    # O método .index() retorna a posição (índice) do item
    posicao = numeros.index(busca)
    print(f"\nO número {busca} ESTÁ na lista!")
    print(f"Ele foi encontrado na posição (índice): {posicao}")
else:
    print(f"\nO número {busca} NÃO está na lista.")
