'''
Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.

Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. Exiba a senha gerada.

Saída esperada:
Senha gerada: A1b@C3d$E5f&  
'''
import string
import random

def gerar_senha():
    # Definindo nossos "reservatórios" de caracteres usando a biblioteca string
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    especial = string.punctuation
    # Garantindo 1 caractere de cada tipo (Regra de segurança)
    senha = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especial)
        ]
    # Cria uma string todos como uma lista e ja adiciona os 4 sorteados nessa lista
    todos = string.ascii_letters + string.digits + string.punctuation
    # .choices com 'k' sorteia vários de uma vez e retorna uma lista
    # Como já temos 4, sorteamos o que falta para chegar no 'tamanho'
    senha.extend(random.choices(todos, k=8))

    # Embaralha a lista para que os 4 primeiros não fiquem sempre na mesma posição
    random.shuffle(senha)
    return ''.join(senha)

print(f"Senha gerada: {gerar_senha()}")