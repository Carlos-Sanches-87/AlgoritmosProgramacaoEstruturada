"""
=============================================================================
QUESTÃO 1: Explique com suas palavras o que é uma pilha em programação.
=============================================================================
Resposta: Uma pilha é uma estrutura de dados linear e sequencial onde a inserção 
e a remoção de elementos acontecem sempre por uma única extremidade chamada "topo". 
Novos elementos são colocados sempre acima dos existentes, impossibilitando o acesso 
direto aos elementos que estão no meio ou na base da estrutura sem que os de cima 
sejam removidos primeiro.

=============================================================================
QUESTÃO 2: Qual é a principal regra de funcionamento de uma pilha? Explique o conceito de LIFO.
=============================================================================
Resposta: A principal regra de funcionamento é o princípio LIFO (Last In, First Out), 
que se traduz como "O Último a Entrar é o Primeiro a Sair". Isso significa que o 
elemento mais recentemente adicionado à estrutura será, obrigatoriamente, o primeiro 
a ser removido em uma operação de exclusão.
"""

print("=== EXECUTANDO EXERCÍCIOS DE PILHA (ADS - UNIC) ===\n")

# =============================================================================
# QUESTÃO 3: Crie uma pilha vazia usando uma lista em Python.
# =============================================================================
print("--- Questão 3 ---")
pilha_q3 = []
print(f"Pilha criada com sucesso. Conteúdo atual: {pilha_q3}\n")


# =============================================================================
# QUESTÃO 4: Adicione cinco elementos em uma pilha usando o método append().
# =============================================================================
print("--- Questão 4 ---")
pilha_q4 = []
pilha_q4.append("Elemento 1")
pilha_q4.append("Elemento 2")
pilha_q4.append("Elemento 3")
pilha_q4.append("Elemento 4")
pilha_q4.append("Elemento 5")
print(f"Pilha após 5 inclusões (Base -> Topo): {pilha_q4}\n")


# =============================================================================
# QUESTÃO 5: Remova o último elemento de uma pilha usando o método pop() e exiba o valor removido.
# =============================================================================
print("--- Questão 5 ---")
valor_removido = pilha_q4.pop()
print(f"Valor removido do topo: {valor_removido}")
print(f"Estado atual da pilha: {pilha_q4}\n")


# =============================================================================
# QUESTÃO 6: Crie um programa que adicione os números 10, 20, 30 e 40 em uma pilha e depois exiba a pilha completa.
# =============================================================================
print("--- Questão 6 ---")
pilha_numeros = []
pilha_numeros.append(10)
pilha_numeros.append(20)
pilha_numeros.append(30)
pilha_numeros.append(40)
print(f"Pilha de números completa: {pilha_numeros}\n")


# =============================================================================
# QUESTÃO 7: Crie um programa que remova todos os elementos de uma pilha, um por vez, mostrando cada elemento removido.
# =============================================================================
print("--- Questão 7 ---")
print(f"Pilha antes de esvaziar: {pilha_numeros}")
while len(pilha_numeros) > 0:
    removido = pilha_numeros.pop()
    print(f"-> Elemento removido: {removido}")
print(f"Pilha após esvaziamento completo: {pilha_numeros}\n")


# =============================================================================
# QUESTÃO 8: Faça um programa que verifique se uma pilha está vazia antes de remover um elemento.
# =============================================================================
print("--- Questão 8 ---")
pilha_teste = [] 
print("Tentando remover de uma pilha vazia com verificação de segurança:")
if len(pilha_teste) == 0:
    print("Underflow evitado! A pilha está vazia. Operação pop() cancelada.")
else:
    pilha_teste.pop()
print("")


# =============================================================================
# QUESTÃO 9: Crie uma pilha com nomes de livros e mostre qual livro está no topo da pilha.
# =============================================================================
print("--- Questão 9 ---")
pilha_livros = ["Dom Casmurro", "O Alquimista", "Duna", "O Hobbit"]
if len(pilha_livros) > 0:
    livro_topo = pilha_livros[-1] 
    print(f"Pilha de Livros: {pilha_livros}")
    print(f"O livro que está no topo é: '{livro_topo}'\n")


# =============================================================================
# QUESTÃO 10 e 11: Leitura de 5 nomes e exibição na ordem inversa (LIFO).
# =============================================================================
print("--- Questão 10 e 11 ---")
pilha_nomes = []
print("Por favor, digite 5 nomes para a pilha:")
for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    pilha_nomes.append(nome)

print("\nExibindo e removendo os nomes na ordem inversa (Conceito LIFO):")
while len(pilha_nomes) > 0:
    print(f"-> Saiu da pilha: {pilha_nomes.pop()}")
print("")


# =============================================================================
# FUNÇÕES ENCAPSULADAS (QUESTÕES 12, 13, 14 e 15)
# =============================================================================

def empilhar(pilha, valor):
    pilha.append(valor)

def esta_vazia(pilha):
    return len(pilha) == 0

def desempilhar(pilha):
    if not esta_vazia(pilha):
        return pilha.pop()
    return "Erro: A pilha está vazia!"

def topo(pilha):
    if not esta_vazia(pilha):
        return pilha[-1]
    return "Erro: A pilha está vazia!"


# =============================================================================
# QUESTÃO 18 e 19: Inversão de Strings e Palíndromos via Pilha
# =============================================================================
print("--- Questão 18 e 19 ---")
palavra_original = input("Digite uma palavra para testar palíndromo: ").lower().strip()
pilha_letras = []

for letra in palavra_original:
    pilha_letras.append(letra)

palavra_invertida = ""
while len(pilha_letras) > 0:
    palavra_invertida += pilha_letras.pop()

print(f"Palavra invertida via Pilha: {palavra_invertida}")

if palavra_original == palavra_invertida:
    print("Resultado: É UM PALÍNDROMO!\n")
else:
    print("Resultado: Não é um palíndromo.\n")


# =============================================================================
# QUESTÃO 20: Caso Real (Mecanismo de Undo - Desfazer)
# =============================================================================
print("--- Questão 20 (Caso Real: Histórico de Ações - Undo) ---")
historico_editor = []

print("Simulando digitação no editor de texto:")
empilhar(historico_editor, "Digitou: 'Trabalho de ADS'")
empilhar(historico_editor, "Inseriu: Parágrafo 1")
print(f"Histórico de ações: {historico_editor}")

print("Usuário desfez a última ação (Ctrl + Z):")
if not esta_vazia(historico_editor):
    print(f"-> Desfazendo: '{desempilhar(historico_editor)}'")
print(f"Estado final do histórico: {historico_editor}\n")


# =============================================================================
# QUESTÃO 16 e 17: Simulação de pilha de pratos e menu interativo.
# Mantido no final do script por controle de fluxo de execução.
# =============================================================================
print("--- Questão 16 e 17 (Sistema de Menu Interativo) ---")
pilha_pratos = []

while True:
    print("\n======== GERENCIADOR DE PILHA DE PRATOS ========")
    print("1. Empilhar Prato (Adicionar)")
    print("2. Desempilhar Prato (Remover)")
    print("3. Mostrar Topo da Pilha")
    print("4. Mostrar Pilha Completa")
    print("5. Sair do Sistema")
    print("=================================================")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == '1':
        cor_prato = input("Digite a cor ou tipo do prato: ")
        empilhar(pilha_pratos, cor_prato)
        print(f"Prato '{cor_prato}' adicionado com sucesso.")
    elif opcao == '2':
        resultado = desempilhar(pilha_pratos)
        print(f"Prato removido do topo: {resultado}")
    elif opcao == '3':
        print(f"Prato no topo atualmente: {topo(pilha_pratos)}")
    elif opcao == '4':
        print(f"Estrutura da Pilha (Base -> Topo): {pilha_pratos}")
    elif opcao == '5':
        print("Saindo do gerenciador... Lista finalizada com sucesso!")
        break
    else:
        print("Opção inválida! Digite um número de 1 a 5.")