# Exercício 4: Lista com Entrada do Usuário
# Peça ao usuário para digitar 5 números e armazene em uma lista.
# Depois: mostre a lista e a soma dos valores.

# 1. Criamos uma lista vazia para começar
numeros = []

print("Digite 5 números inteiros:")

# 2. Usamos um loop para pedir os números 5 vezes
for i in range(5):
    # Pedimos o número e convertemos para int (pois o input sempre recebe texto)
    num = int(input(f"Digite o {i+1}º número: "))
    
    # Adicionamos o número à nossa lista usando o append
    numeros.append(num)

# 3. Exibimos a lista completa
print(f"\nA lista criada foi: {numeros}")

# 4. Calculamos a soma usando a função sum()
soma = sum(numeros)
print(f"A soma de todos os valores é: {soma}")
