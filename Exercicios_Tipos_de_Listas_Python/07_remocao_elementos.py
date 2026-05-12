# Exercício 7: Lista com Remoção de Elementos
# Crie uma lista com 5 frutas e remova uma fruta escolhida pelo usuário.

# 1. Criando a lista inicial
frutas = ["Maçã", "Banana", "Morango", "Uva", "Laranja"]

print(f"Lista de frutas disponível: {frutas}")

# 2. Pedindo para o usuário escolher qual remover
fruta_remover = input("Qual fruta você deseja remover da lista? ").capitalize()

# 3. Verificando se a fruta existe e removendo
if fruta_remover in frutas:
    frutas.remove(fruta_remover)
    print(f"\nSucesso! '{fruta_remover}' foi removida.")
else:
    print(f"\nA fruta '{fruta_remover}' não foi encontrada na lista.")

# 4. Exibindo a lista atualizada
print(f"Lista atualizada: {frutas}")
