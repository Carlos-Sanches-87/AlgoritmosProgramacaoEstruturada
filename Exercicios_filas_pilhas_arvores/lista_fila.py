"""
=============================================================================
QUESTÃO 1: Explique com suas palavras o que é uma fila em programação.
=============================================================================
Resposta: Uma fila é uma estrutura de dados linear e sequencial onde os elementos
são inseridos em uma extremidade (o final da fila) e removidos pela outra 
extremidade (o início da fila). É exatamente como uma fila de banco: novos 
elementos entram atrás, e o atendimento ocorre na frente.

=============================================================================
QUESTÃO 2: Qual é a principal regra de funcionamento de uma fila? Explique o conceito de FIFO.
=============================================================================
Resposta: A regra principal de uma fila é o princípio FIFO (First In, First Out), 
que se traduz como "O Primeiro a Entrar é o Primeiro a Sair". O elemento que 
chegou primeiro à estrutura e está aguardando há mais tempo será, obrigatoriamente, 
o próximo a ser removido (atendido).
"""

print("=== EXECUTANDO EXERCÍCIOS DE FILA (ADS - UNIC) ===\n")

# =============================================================================
# QUESTÃO 3: Crie uma fila vazia usando uma lista em Python.
# =============================================================================
print("--- Questão 3 ---")
fila_q3 = []
print(f"Fila criada com sucesso. Conteúdo: {fila_q3}\n")


# =============================================================================
# QUESTÃO 4: Adicione cinco elementos em uma fila usando o método append().
# =============================================================================
print("--- Questão 4 ---")
fila_q4 = []
fila_q4.append("Cliente A")
fila_q4.append("Cliente B")
fila_q4.append("Cliente C")
fila_q4.append("Cliente D")
fila_q4.append("Cliente E")
print(f"Fila após 5 chegadas (Início -> Fim): {fila_q4}\n")


# =============================================================================
# QUESTÃO 5: Remova o primeiro elemento de uma fila usando pop(0) e exiba o valor.
# =============================================================================
print("--- Questão 5 ---")
valor_removido = fila_q4.pop(0) # pop(0) remove especificamente o primeiro índice
print(f"Atendido (removido do início): {valor_removido}")
print(f"Estado atual da fila: {fila_q4}\n")


# =============================================================================
# QUESTÃO 6: Crie um programa que adicione os números 10, 20, 30 e 40 em uma fila.
# =============================================================================
print("--- Questão 6 ---")
fila_numeros = []
fila_numeros.append(10)
fila_numeros.append(20)
fila_numeros.append(30)
fila_numeros.append(40)
print(f"Fila de números completa: {fila_numeros}\n")


# =============================================================================
# QUESTÃO 7: Remova todos os elementos de uma fila, um por vez, mostrando cada um.
# =============================================================================
print("--- Questão 7 ---")
print(f"Fila antes de esvaziar: {fila_numeros}")
while len(fila_numeros) > 0:
    removido = fila_numeros.pop(0)
    print(f"-> Elemento desenfileirado: {removido}")
print(f"Fila após esvaziamento total: {fila_numeros}\n")


# =============================================================================
# QUESTÃO 8: Verifique se uma fila está vazia antes de remover um elemento.
# =============================================================================
print("--- Questão 8 ---")
fila_teste = [] 
print("Tentando remover de uma fila vazia com validação (Underflow):")
if len(fila_teste) == 0:
    print("A fila está vazia. Não há ninguém para atender! Operação cancelada.")
else:
    fila_teste.pop(0)
print("")


# =============================================================================
# QUESTÃO 9: Crie uma fila com nomes e mostre quem é o primeiro da fila.
# =============================================================================
print("--- Questão 9 ---")
fila_nomes = ["Ana", "Bruno", "Carlos", "Diana"]
if len(fila_nomes) > 0:
    primeiro_da_fila = fila_nomes[0] # Índice 0 sempre espia o início sem remover
    print(f"Fila de Pessoas: {fila_nomes}")
    print(f"Quem é o primeiro da fila para ser atendido? '{primeiro_da_fila}'\n")


# =============================================================================
# QUESTÃO 10 e 11: Leitura de 5 nomes e exibição na mesma ordem (FIFO).
# =============================================================================
print("--- Questão 10 e 11 ---")
fila_digitada = []
print("Por favor, digite 5 nomes para a fila:")
for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    fila_digitada.append(nome)

print("\nExibindo e atendendo os nomes na MESMA ordem em que chegaram (FIFO):")
while len(fila_digitada) > 0:
    print(f"-> Atendido: {fila_digitada.pop(0)}")
print("")


# =============================================================================
# FUNÇÕES ENCAPSULADAS (QUESTÕES 12, 13, 14 e 15)
# =============================================================================

def enfileirar(fila, valor):
    fila.append(valor)

def esta_vazia(fila):
    return len(fila) == 0

def desenfileirar(fila):
    if not esta_vazia(fila):
        return fila.pop(0)
    return "Erro: A fila já está vazia!"

def primeiro(fila):
    if not esta_vazia(fila):
        return fila[0]
    return "Erro: A fila está vazia!"


# =============================================================================
# QUESTÃO 18: Use uma fila para organizar a ordem de impressão de documentos.
# =============================================================================
print("--- Questão 18 (Spooler de Impressão) ---")
fila_impressao = []
enfileirar(fila_impressao, "Trabalho_Redes.pdf")
enfileirar(fila_impressao, "Curriculo_Carlos.docx")
enfileirar(fila_impressao, "Boleto_Faculdade.pdf")

print(f"Documentos aguardando na impressora: {fila_impressao}")
while not esta_vazia(fila_impressao):
    print(f"[IMPRIMINDO] -> {desenfileirar(fila_impressao)}")
print("Todas as impressões foram concluídas.\n")


# =============================================================================
# QUESTÃO 19: Simule uma fila de senhas de atendimento, exibindo a senha chamada.
# =============================================================================
print("--- Questão 19 (Painel de Senhas) ---")
fila_senhas = []
enfileirar(fila_senhas, "SENHA-001")
enfileirar(fila_senhas, "SENHA-002")
enfileirar(fila_senhas, "SENHA-003")

while not esta_vazia(fila_senhas):
    senha_chamada = desenfileirar(fila_senhas)
    print(f"DING DONG! Guichê 1 chama: {senha_chamada}")
print("Nenhuma senha aguardando atendimento.\n")


# =============================================================================
# QUESTÃO 20: Situação do mundo real com exemplo em Python.
# =============================================================================
print("--- Questão 20 (Caso Real: Fila de Servidor / Streaming) ---")
print("Explicação: Fila é usada no buffer de streaming (YouTube/Netflix) ou em")
print("servidores web. Requisições chegam e são atendidas na ordem de chegada.\n")

fila_requisicoes = []
print("Servidor recebendo acessos (Pico de tráfego):")
enfileirar(fila_requisicoes, "IP: 192.168.0.1 solicitou index.html")
enfileirar(fila_requisicoes, "IP: 10.0.0.5 solicitou imagem_logo.png")

print(f"Fila do servidor (Load Balancer): {fila_requisicoes}")
while not esta_vazia(fila_requisicoes):
    req = desenfileirar(fila_requisicoes)
    print(f"[PROCESSANDO] O servidor atendeu a requisição: '{req}'")
print("\n")


# =============================================================================
# QUESTÃO 16 e 17: Simulação de Fila de Atendimento e Menu Interativo.
# Mantido no final do script para não prender o usuário no meio da lista.
# =============================================================================
print("--- Questão 16 e 17 (Sistema de Menu Interativo - Fila) ---")
fila_atendimento = []

while True:
    print("\n======== SISTEMA DE FILA DE ATENDIMENTO ========")
    print("1. Enfileirar Pessoa (Pegar senha)")
    print("2. Desenfileirar Pessoa (Chamar próximo)")
    print("3. Mostrar o Primeiro da Fila (Próximo)")
    print("4. Mostrar Fila Completa")
    print("5. Sair do Sistema")
    print("=================================================")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == '1':
        nome_pessoa = input("Digite o nome do cliente: ")
        enfileirar(fila_atendimento, nome_pessoa)
        print(f"Cliente '{nome_pessoa}' entrou no final da fila.")
    elif opcao == '2':
        resultado = desenfileirar(fila_atendimento)
        print(f"Cliente chamado para atendimento: {resultado}")
    elif opcao == '3':
        print(f"Próximo a ser atendido: {primeiro(fila_atendimento)}")
    elif opcao == '4':
        print(f"Fila atual (Início -> Fim): {fila_atendimento}")
    elif opcao == '5':
        print("Saindo do sistema de fila... Lista finalizada com sucesso!")
        break
    else:
        print("Opção inválida! Digite um número de 1 a 5.")