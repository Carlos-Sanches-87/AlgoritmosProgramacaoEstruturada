"""
ID: Ex_2_Hanoi.py
Data: 14/04/2026
Enunciado: Implementar o algoritmo da Torre de Hanói salvando os movimentos 
em uma lista (vetor) para armazenamento em memória RAM.
"""

# Agora a função recebe uma 'lista' como quinto parâmetro
def torre_hanoi(n, origem, destino, auxiliar, lista):
    if n == 1:
        # Em vez de print, adicionamos à lista na RAM
        lista.append(f"Disco 1: {origem} -> {destino}")
        return

    # Passo 1
    torre_hanoi(n - 1, origem, auxiliar, destino, lista)

    # Passo 2: Adiciona o movimento do disco atual à lista
    lista.append(f"Disco {n}: {origem} -> {destino}")

    # Passo 3
    torre_hanoi(n - 1, auxiliar, destino, origem, lista)

# --- Preparação ---
n_discos = int(input("Digite o número de discos: "))
historico_movimentos = [] # Este é o seu "vetor" que ficará na RAM

# --- Execução ---
torre_hanoi(n_discos, 'A', 'C', 'B', historico_movimentos)

# --- Exibição Final ---
print(f"\n--- Movimentos armazenados na RAM ({len(historico_movimentos)} totais) ---")

# Agora percorremos a lista para mostrar os resultados que salvamos
for movimento in historico_movimentos:
    print(movimento)

print("\nProcesso finalizado. Os dados foram mantidos na variável até agora!")