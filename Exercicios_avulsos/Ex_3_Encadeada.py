"""
ID: Ex_3_Encadeada.py
Data: 14/04/2026
Enunciado: Implementar uma Lista Encadeada Simples onde cada elemento (Nó) 
aponta para o próximo.
"""

# 1. Criamos o molde do vagão (Nó)
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None  # No começo, o vagão não está engatado em nada

# 2. Criamos o molde da Lista (o Trem)
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  # A lista começa vazia (sem primeiro vagão)

    def inserir(self, novo_dado):
        novo_no = No(novo_dado)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            # Percorre a lista até achar o último vagão
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def exibir(self):
        atual = self.cabeca
        elementos = []
        while atual:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        print(" -> ".join(elementos) + " -> None")

# --- Teste ---
lista = ListaEncadeada()
lista.inserir(10)
lista.inserir(20)
lista.inserir(30)

print("Estrutura da Lista Encadeada:")
lista.exibir()