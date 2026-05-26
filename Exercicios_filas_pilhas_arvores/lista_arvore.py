"""
=============================================================================
RESPOSTAS TEÓRICAS
=============================================================================
QUESTÃO 1: Explique o que é uma árvore em estrutura de dados.
Resposta: É uma estrutura de dados não-linear e hierárquica. Em vez de armazenar 
dados em uma linha reta (como listas ou filas), ela organiza os dados em níveis, 
semelhante ao formato de uma árvore invertida ou a um organograma de empresa.

QUESTÃO 2: O que é o nó raiz? Dê um exemplo.
Resposta: É o nó principal, o ponto de partida absoluto da árvore. Ele é o único 
nó que não possui um "pai" (nenhum nó aponta para ele). Exemplo: O diretor-geral 
no topo de um organograma ou a pasta "C:\" no Windows.

QUESTÃO 3: O que são nós filhos?
Resposta: São os nós que descendem de outro nó (o nó pai). Se o nó A aponta para 
o nó B e o nó C, então B e C são filhos de A.

QUESTÃO 4: O que é um nó folha?
Resposta: É um nó que fica na extremidade da árvore, ou seja, um nó que não possui 
nenhum filho. Ele é o fim daquela ramificação.

QUESTÃO 5: Diferença entre árvore e lista?
Resposta: A lista é linear (um elemento atrás do outro de forma sequencial). A 
árvore é não-linear e hierárquica (um elemento pode se dividir e levar a vários 
outros simultaneamente).

QUESTÃO 9: O que é uma árvore binária?
Resposta: É um tipo específico de árvore onde cada nó pode ter, no máximo, DOIS 
filhos. Eles são chamados de "filho esquerdo" e "filho direito".

QUESTÃO 14: O que significa percorrer uma árvore?
Resposta: Percorrer (ou fazer o "Traversal") significa visitar todos os nós de 
uma árvore de forma sistemática, passando por cada elemento exatamente uma vez 
para ler, imprimir ou alterar seus dados.

QUESTÕES 15, 16 e 17: Percursos em Árvores Binárias
- 15. Pré-ordem (Pre-order): Visita primeiro a Raiz, depois desce tudo pela 
      Esquerda, e por fim visita a Direita.
- 16. Em-ordem (In-order): Visita toda a Esquerda, depois sobe para a Raiz, 
      e por fim visita a Direita. (Gera dados em ordem crescente).
- 17. Pós-ordem (Post-order): Visita toda a Esquerda, depois toda a Direita, 
      e só no final visita a Raiz. (Muito usado para deletar árvores de baixo para cima).
=============================================================================
"""

print("=== EXECUTANDO EXERCÍCIOS DE ÁRVORE (ADS - UNIC) ===\n")

# =============================================================================
# QUESTÃO 6: Crie uma representação simples de uma árvore usando dicionários.
# =============================================================================
print("--- Questão 6 ---")
arvore_dict = {
    "Raiz": {
        "Filho_1": {},
        "Filho_2": {}
    }
}
print(f"Árvore Simples (Dicionário): {arvore_dict}\n")


# =============================================================================
# QUESTÃO 7: Crie uma árvore com um nó raiz e dois filhos, depois exiba tudo.
# =============================================================================
print("--- Questão 7 ---")
arvore_q7 = {
    "CEO (Raiz)": ["Gerente Vendas (Filho)", "Gerente TI (Filho)"]
}
print(f"Estrutura da Árvore: {arvore_q7}")
for raiz, filhos in arvore_q7.items():
    print(f"Nó Raiz: {raiz}")
    print(f"Nós Filhos: {filhos[0]} e {filhos[1]}\n")


# =============================================================================
# QUESTÃO 8: Crie uma árvore que represente família com avô, filhos e netos.
# =============================================================================
print("--- Questão 8 ---")
arvore_genealogica = {
    "Avô João": {
        "Filho Carlos": ["Neto Pedrinho", "Neta Aninha"],
        "Filha Maria": ["Neto Lucas"]
    }
}
print("Árvore Genealógica construída com sucesso!")
print(f"Estrutura completa: {arvore_genealogica}\n")


# =============================================================================
# QUESTÃO 10 e 11: Crie uma classe No com valor, esquerda e direita.
# =============================================================================
print("--- Questão 10 e 11 ---")
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

print("Classe 'No' (Árvore Binária) criada e carregada na memória!\n")


# =============================================================================
# QUESTÃO 12 e 13: Insira valores manualmente e exiba a raiz, esq. e dir.
# =============================================================================
print("--- Questão 12 e 13 ---")
# Criando os nós
raiz = No(10)          # Raiz
raiz.esquerda = No(5)  # Filho esquerdo
raiz.direita = No(15)  # Filho direito

print(f"Valor do Nó Raiz: {raiz.valor}")
print(f"Valor do Filho Esquerdo: {raiz.esquerda.valor}")
print(f"Valor do Filho Direito: {raiz.direita.valor}\n")


# =============================================================================
# QUESTÃO 18: Faça um programa que conte quantos nós existem na árvore.
# =============================================================================
print("--- Questão 18 ---")
def contar_nos(no_atual):
    if no_atual is None:
        return 0
    # Conta 1 (o nó atual) + a quantidade de nós da esquerda + da direita
    return 1 + contar_nos(no_atual.esquerda) + contar_nos(no_atual.direita)

# Adicionando mais um nó para teste (Filho do filho esquerdo)
raiz.esquerda.esquerda = No(2)

total_nos = contar_nos(raiz)
print(f"A árvore binária possui um total de: {total_nos} nós.\n")


# =============================================================================
# QUESTÃO 19: Faça um programa que calcule a altura de uma árvore binária.
# =============================================================================
print("--- Questão 19 ---")
def altura_arvore(no_atual):
    if no_atual is None:
        return -1 # Retorna -1 para que a folha tenha altura 0
    
    altura_esq = altura_arvore(no_atual.esquerda)
    altura_dir = altura_arvore(no_atual.direita)
    
    # A altura é 1 + o maior caminho encontrado
    return 1 + max(altura_esq, altura_dir)

altura = altura_arvore(raiz)
print(f"A altura da árvore atual é: {altura} níveis.\n")


# =============================================================================
# QUESTÃO 20: Situação do mundo real com exemplo em Python.
# =============================================================================
print("--- Questão 20 (Caso Real: Sistema de Arquivos do Computador) ---")
print("Explicação: O HD do seu computador é uma árvore perfeita. A unidade C:\\")
print("é a Raiz, as pastas são nós intermediários, e os arquivos são as folhas.")

sistema_arquivos = {
    "C:\\ (RAIZ)": {
        "Usuarios": {
            "Carlos": ["foto.jpg", "lista_arvore.py"]
        },
        "Windows": ["system32.dll"]
    }
}

print(f"\nExemplo de Árvore de Diretórios: {sistema_arquivos}")
print("Neste exemplo, 'foto.jpg' é um nó folha, e 'Carlos' é um nó filho de 'Usuarios'.")