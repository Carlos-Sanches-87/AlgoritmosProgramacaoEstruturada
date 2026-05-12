"""
ID: Ex_4_Ordenada.py
Data: 14/04/2026
Enunciado: Implementar uma Lista Ordenada que mantém os elementos em 
ordem crescente automaticamente durante a inserção.
"""

class ListaOrdenada:
    def __init__(self):
        self.lista = []

    def inserir(self, valor):
        # Encontra a posição correta para manter a ordem
        posicao = 0
        while posicao < len(self.lista) and self.lista[posicao] < valor:
            posicao += 1
        
        # Insere o valor na posição encontrada
        self.lista.insert(posicao, valor)
        print(f"Inserido {valor} na posição {posicao}")

    def exibir(self):
        print("Lista atual:", self.lista)

# --- Teste ---
minha_lista = ListaOrdenada()
minha_lista.inserir(50)
minha_lista.inserir(10)
minha_lista.inserir(30)

minha_lista.exibir()