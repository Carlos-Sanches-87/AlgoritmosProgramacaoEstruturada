"""Crie um programa que peça ao usuário os valores dos dois catetos 
(os dois lados menores) de um triângulo retângulo. 
O programa deve calcular e exibir o valor da hipotenusa."""

cat_1 = float(input("Digite o valor do primeiro cateto (em cm): "))
cat_2 = float(input("Digite o valor do segundo cateto (em cm): "))
hipot = round((cat_1 ** 2 + cat_2 ** 2) ** 0.5, 2)
print("O valor da hipotenusa é: ", hipot, "cm")