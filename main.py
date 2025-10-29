def calcular_soma(a, b):
    """
    Função que calcula a soma de dois números
    """
    return a + b

def mostrar_mensagem(nome):
    """
    Função que mostra uma mensagem de boas-vindas
    """
    return f"Olá {nome}, bem-vindo ao sistema!"

def main():
    # Exemplo de uso das funções
    print("=== Sistema Básico em Python ===")
    
    # Teste da função de soma
    numero1 = 10
    numero2 = 5
    resultado = calcular_soma(numero1, numero2)
    print(f"\nSoma de {numero1} + {numero2} = {resultado}")
    
    # Teste da função de mensagem
    nome_usuario = input("\nPor favor, digite seu nome: ")
    mensagem = mostrar_mensagem(nome_usuario)
    print(mensagem)

if __name__ == "__main__":
    main()