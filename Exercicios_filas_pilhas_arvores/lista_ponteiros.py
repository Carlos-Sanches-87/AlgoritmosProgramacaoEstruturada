"""
=============================================================================
RESPOSTAS TEÓRICAS
=============================================================================
QUESTÃO 1: O que é um ponteiro em programação?
Resposta: Um ponteiro é uma variável cujo valor é o endereço de memória de 
outra variável. Em vez de guardar um dado (como o número 10), ele guarda o local 
físico na memória RAM onde esse dado está armazenado.

QUESTÃO 2: Em C, o que significa armazenar o endereço de memória de outra variável?
Resposta: Significa que a variável (ponteiro) aponta diretamente para o local 
físico no hardware onde a outra variável está. Se você altera o valor no endereço 
apontado, a variável original é modificada automaticamente, pois ambas compartilham 
o mesmo espaço na RAM.

QUESTÃO 3: Python possui ponteiros como C? Como Python trabalha com referências?
Resposta: Python não possui ponteiros explícitos (você não manipula endereços 
de memória diretamente como em C). Em vez disso, Python usa "Referências". Tudo 
em Python é um Objeto. Variáveis são apenas "etiquetas" (nomes) que colamos nesses 
objetos na memória. 

QUESTÃO 5: O valor de referência também muda ao alterar "numero"?
Resposta: Não. Números inteiros são tipos IMUTÁVEIS em Python. Quando alteramos 
"numero", o Python cria um novo objeto na memória com o novo valor e move a etiqueta 
"numero" para ele. A variável "referencia" continua apontando para o objeto antigo.

QUESTÃO 7: Por que, no caso de listas, duas variáveis apontam para o mesmo objeto?
Resposta: Porque listas são tipos MUTÁVEIS. Ao fazer "lista2 = lista1", o Python 
não cria uma cópia dos dados, ele apenas cola uma segunda etiqueta no mesmo 
objeto na memória. Alterar a lista por qualquer uma das variáveis afetará o objeto 
único que ambas referenciam.

QUESTÃO 10: Qual a diferença entre usar == e is em Python?
Resposta: O operador "==" compara os VALORES (se o conteúdo é igual). O operador 
"is" compara a IDENTIDADE (se ambas as variáveis apontam exatamente para o mesmo 
endereço de memória / mesmo objeto).

QUESTÃO 14: Por que objetos mutáveis (listas/dicionários) podem ser alterados em funções?
Resposta: Porque a função recebe a referência (o endereço) do objeto original. 
Como o objeto é mutável, a função consegue alterar o conteúdo daquele endereço, 
refletindo a mudança fora da função.

QUESTÃO 15: Por que objetos imutáveis (inteiros/strings) não são alterados em funções?
Resposta: Porque não é possível alterar o valor de um objeto imutável na memória. 
Qualquer tentativa de alteração dentro da função faz o Python criar um novo objeto 
localmente, não afetando a variável original que ficou fora da função.

QUESTÃO 19: Diferença entre Cópia Rasa (Shallow) e Cópia Profunda (Deep Copy).
Resposta: A cópia rasa (copy) cria um novo objeto principal, mas se houver objetos 
mutáveis dentro dele (como uma lista dentro de outra lista), as referências internas 
são mantidas. A cópia profunda (deepcopy) cria um clone completo de absolutamente tudo, 
garantindo independência total.
=============================================================================
"""

import copy

print("=== EXECUTANDO EXERCÍCIOS DE REFERÊNCIAS (ADS - UNIC) ===\n")

# =============================================================================
# QUESTÃO 4: Crie numero e referencia. Exiba ambas.
# =============================================================================
print("--- Questão 4 ---")
numero = 10
referencia = numero
print(f"Número: {numero} | Referência: {referencia}\n")


# =============================================================================
# QUESTÃO 5: Altere o numero. A referencia muda? (Demonstração prática)
# =============================================================================
print("--- Questão 5 ---")
numero = 20
print("Alteramos 'numero' para 20.")
print(f"Número agora é: {numero} | Referência continua: {referencia}")
print("Explicação: Inteiros são imutáveis!\n")


# =============================================================================
# QUESTÃO 6: Listas, ponteiros e mutabilidade.
# =============================================================================
print("--- Questão 6 ---")
valores = [10, 20, 30]
ponteiro_lista = valores
ponteiro_lista[0] = 999  # Alterando usando a segunda variável

print(f"Lista 'valores' original após alteração via ponteiro: {valores}")
print("Explicação: Listas são mutáveis, ambas as variáveis apontam para o mesmo local.\n")


# =============================================================================
# QUESTÃO 8: Use a função id() para mostrar o endereço de memória.
# =============================================================================
print("--- Questão 8 ---")
print(f"Endereço de memória de 'valores':       {id(valores)}")
print(f"Endereço de memória de 'ponteiro_lista': {id(ponteiro_lista)}")
print("Os IDs são idênticos, provando que é o mesmo objeto na memória.\n")


# =============================================================================
# QUESTÃO 9: Listas iguais, mas objetos diferentes.
# =============================================================================
print("--- Questão 9 ---")
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(f"ID da lista 1: {id(lista1)}")
print(f"ID da lista 2: {id(lista2)}")
print("Apesar de terem os mesmos números, são objetos distintos na memória!\n")


# =============================================================================
# QUESTÃO 11: Programa comparando == e is.
# =============================================================================
print("--- Questão 11 ---")
a = [5, 6, 7]
b = [5, 6, 7]
c = a

print(f"a == b (Valores são iguais?): {a == b}")
print(f"a is b (São o mesmo objeto?): {a is b}")
print(f"a is c (São o mesmo objeto?): {a is c}\n")


# =============================================================================
# QUESTÃO 12: Função que altera lista (Passagem por referência mutável).
# =============================================================================
print("--- Questão 12 ---")
def alterar_lista(lista):
    lista.append("NOVO")

minha_lista = ["A", "B", "C"]
print(f"Lista antes da função: {minha_lista}")
alterar_lista(minha_lista)
print(f"Lista depois da função: {minha_lista}\n")


# =============================================================================
# QUESTÃO 13: Função que tenta alterar inteiro (Imutável).
# =============================================================================
print("--- Questão 13 ---")
def alterar_numero(num):
    num = 100

meu_numero = 50
print(f"Número antes da função: {meu_numero}")
alterar_numero(meu_numero)
print(f"Número depois da função: {meu_numero} (Não mudou!)\n")


# =============================================================================
# QUESTÃO 16: Dicionários e referências.
# =============================================================================
print("--- Questão 16 ---")
aluno = {"nome": "Carlos", "idade": 25}
referencia_aluno = aluno

referencia_aluno["idade"] = 30 # Alterando pela referência
print(f"Dicionário original 'aluno': {aluno}\n")


# =============================================================================
# QUESTÃO 17: Usando o copy() para listas.
# =============================================================================
print("--- Questão 17 ---")
lista_base = [1, 2, 3]
lista_copiada = lista_base.copy()

lista_copiada.append(4)
print(f"Lista Base Original: {lista_base}")
print(f"Lista Copiada:       {lista_copiada}\n")


# =============================================================================
# QUESTÃO 18: O problema da cópia rasa (Listas aninhadas).
# =============================================================================
print("--- Questão 18 (Cópia Rasa) ---")
lista_externa = [[1, 2], 3, 4]
copia_rasa = lista_externa.copy()

copia_rasa[0][0] = 99  # Alterando a lista interna
print(f"Lista Externa Original foi afetada: {lista_externa}")
print("Isso ocorreu porque .copy() não copia os objetos internos profundos.\n")


# =============================================================================
# QUESTÃO 19: Exemplo de Shallow Copy vs Deep Copy.
# =============================================================================
print("--- Questão 19 ---")
original = [[1, 2], 3]

# Cópia Rasa (Shallow)
rasa = copy.copy(original)
rasa[0][0] = "MODIFICADO RASA"

# Cópia Profunda (Deep)
profunda = copy.deepcopy(original)
profunda[0][0] = "MODIFICADO DEEP"

print(f"Lista Original (afetada pela rasa): {original}")
print(f"Cópia Profunda (totalmente isolada): {profunda}\n")


# =============================================================================
# QUESTÃO 20: Simulando ponteiros de C em Python com Listas.
# =============================================================================
print("--- Questão 20 (Simulador de Ponteiro) ---")
# Para simular um ponteiro que aponta para um valor solto, colocamos o valor
# dentro de uma lista (que é mutável e seu endereço de memória será compartilhado).
variavel_simulada = [42]
ponteiro = variavel_simulada

print(f"Valor inicial lido pelo ponteiro: {ponteiro[0]}")

# O ponteiro modifica o dado no endereço de memória compartilhado
ponteiro[0] = 100

print(f"Variável original após o ponteiro alterar a memória: {variavel_simulada[0]}")
print("=== FIM DA EXECUÇÃO DAS LISTAS DA DISCIPLINA ===")