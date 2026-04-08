"""Crie um programa que calcule o novo valor de uma prestação (boleto) em atraso. 
O programa deve pedir ao usuário três informações: o valor original da prestação, 
a quantidade de dias de atraso e a taxa de juros diária (em %). 
Por fim, o programa deve exibir o novo valor a ser pago."""

valor_prest = float(input("Valor original da prestação (R$): ").replace(',', '.'))
atraso = int(input("Quantidade de dias de atraso: "))
juros = float(input("Taxa de juros/dia (em %): ").replace(',', '.'))
novo_valor = valor_prest + (valor_prest * (juros / 100) * atraso)
print(f"O novo valor a ser pago é de R$ {novo_valor:.2f}")