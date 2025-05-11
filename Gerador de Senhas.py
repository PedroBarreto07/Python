import random
import string

def gerar_senha(tamanho=12):
    """
    Gera uma senha segura com letras maiúsculas, minúsculas, números e símbolos.
    
    :param tamanho: Comprimento da senha (padrão: 12 caracteres)
    :return: String com a senha gerada
    """

    if tamanho < 4:
        raise ValueError("A senha deve ter pelo menos 4 caracteres.")

    # Caracteres que podem ser usados na senha
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Garante que a senha tenha pelo menos um de cada tipo de caractere
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Preenche o restante da senha com caracteres aleatórios de todos os tipos
    todos_os_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos
    senha += random.choices(todos_os_caracteres, k=tamanho - 4)

    # Embaralha a ordem dos caracteres
    random.shuffle(senha)

    # Junta os caracteres em uma única string
    return ''.join(senha)

# Exemplo de uso
if __name__ == "__main__":
    senha_gerada = gerar_senha(16)
    print("Senha segura gerada:", senha_gerada)
