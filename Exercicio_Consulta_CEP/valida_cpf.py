def testar_cpf():
    print("=== Validador de CPF (ADS Unic) ===")
    cpf_digitado = input("Digite o CPF para testar: ")

    # 1. Limpa a formatação (tira pontos e traços)
    cpf = cpf_digitado.replace(".", "").replace("-", "").replace(" ", "")

    # 2. Verifica se tem 11 dígitos ou se são todos números repetidos (ex: 111.111.111-11)
    if len(cpf) != 11 or not cpf.isdigit() or cpf == cpf[0] * 11:
        print("\n❌ CPF Inválido: Formato incorreto ou números repetidos.")
        return

    # 3. CÁLCULO DO 1º DÍGITO VERIFICADOR
    soma = 0
    peso = 10
    # Multiplica os 9 primeiros números por pesos decrescentes (de 10 até 2)
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1
    
    resto = soma % 11
    digito_1 = 0 if resto < 2 else 11 - resto

    # Verifica se o primeiro dígito calculado bate com o digitado
    if digito_1 != int(cpf[9]):
        print("\n❌ CPF Inválido: Falhou no 1º dígito verificador.")
        return

    # 4. CÁLCULO DO 2º DÍGITO VERIFICADOR
    soma = 0
    peso = 11
    # Multiplica os 10 primeiros números (incluindo o digito 1) por pesos (de 11 até 2)
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
        
    resto = soma % 11
    digito_2 = 0 if resto < 2 else 11 - resto

    # Verifica se o segundo dígito calculado bate com o digitado
    if digito_2 != int(cpf[10]):
        print("\n❌ CPF Inválido: Falhou no 2º dígito verificador.")
        return

    # Se passou por todas as barreiras acima, o CPF é verdadeiro!
    print(f"\n✅ CPF Válido! O número {cpf_digitado} é matematicamente correto.")

# Ponto de entrada do script
if __name__ == "__main__":
    testar_cpf()