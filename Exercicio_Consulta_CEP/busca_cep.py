import requests

def consultar_cep():
    print("=== Buscador de CEP (ADS Unic) ===")
    cep_digitado = input("Digite o CEP (ex: 78015480 - Beira Rio): ")

    # 1. Limpamos o input: removemos hífens ou espaços caso o usuário digite "78015-480"
    cep_limpo = cep_digitado.replace("-", "").replace(" ", "")

    # 2. Validação básica: verifica se tem 8 caracteres e se são apenas números
    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        print("Erro: Por favor, digite um CEP válido contendo exatamente 8 números.")
        return

    # 3. Montamos a URL da API da ViaCEP com o CEP limpo usando f-string
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

    try:
        # 4. Fazemos a requisição GET
        resposta = requests.get(url)
        
        # 5. Transformamos a resposta de texto puro para um Dicionário Python
        dados = resposta.json()

        # 6. A ViaCEP retorna um JSON com a chave "erro": true se o CEP não existir
        if "erro" in dados:
            print("\nCEP não encontrado na base de dados da ViaCEP!")
        else:
            # 7. Imprimimos o resultado pegando as chaves do dicionário
            print("\n--- Resultado da Busca ---")
            print(f"Logradouro: {dados.get('logradouro')}")
            print(f"Bairro: {dados.get('bairro')}")
            print(f"Cidade/UF: {dados.get('localidade')} / {dados.get('uf')}")
            print(f"DDD: {dados.get('ddd')}")

    except requests.exceptions.RequestException as erro:
        # Se você estiver sem internet ou a API cair, ele trata o erro aqui sem quebrar o programa
        print(f"\nOcorreu um erro ao tentar se conectar com a API: {erro}")

# Ponto de entrada do script Python
if __name__ == "__main__":
    consultar_cep()