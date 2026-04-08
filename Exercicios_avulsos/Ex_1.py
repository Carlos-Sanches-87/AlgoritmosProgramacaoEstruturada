"""Data: 17/03/2026
Enunciado: Demonstrar as quatro estruturas condicionais principais: 
Simples, Composta, Encadeada e Múltipla Escolha (match-case)."""

# 1) Condicional Simples (if)
idade = 18
if idade >= 18:
    print("1) Simples: Maior de idade")

print("-" * 30)

# 2) Condicional Composta (if-else)
a = 10
b = 20
if a > b:
    print("2) Composta: A é maior que B")
else:
    print("2) Composta: B é maior ou igual a A")

print("-" * 30)

# 3) Condicional Encadeada (if-elif-else)
nota = 7.5
if nota >= 9:
    print("3) Encadeada: Desempenho Excelente")
elif nota >= 7:
    print("3) Encadeada: Desempenho Bom")
else:
    print("3) Encadeada: Precisa melhorar")

print("-" * 30)

# 4) Seleção de Múltipla Escolha (match-case)
# Equivalente ao switch-case de outras linguagens
dia_semana = 1
match dia_semana:
    case 1:
        print("4) Múltipla Escolha: Domingo")
    case 2:
        print("4) Múltipla Escolha: Segunda-feira")
    case _:
        print("4) Múltipla Escolha: Outro dia")