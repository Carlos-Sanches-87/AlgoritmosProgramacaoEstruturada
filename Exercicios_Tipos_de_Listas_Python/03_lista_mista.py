# Exercício 3: Lista Mista
# Crie uma lista com diferentes tipos de dados:
# - nome (string)
# - idade (int)
# - altura (float)
# - aprovado (bool)
# Exiba cada elemento separadamente.

# Criando a lista mista
pessoa = ["Carlos", 20, 1.75, True]

# Exibindo cada elemento separadamente acessando pelos índices
print(f"Nome: {pessoa[0]} (Tipo: {type(pessoa[0])})")
print(f"Idade: {pessoa[1]} (Tipo: {type(pessoa[1])})")
print(f"Altura: {pessoa[2]} (Tipo: {type(pessoa[2])})")
print(f"Aprovado: {pessoa[3]} (Tipo: {type(pessoa[3])})")

# Também podemos fazer usando um loop 'for' para mostrar que a lista aceita tudo
print("\nPercorrendo a lista com um loop:")
for item in pessoa:
    print(f"Valor: {item} - Tipo: {type(item)}")
