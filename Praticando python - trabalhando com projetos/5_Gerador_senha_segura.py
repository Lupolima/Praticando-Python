'''
Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.

Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. Exiba a senha gerada.

Saída esperada:
Senha gerada: A1b@C3d$E5f&  
'''
import string
import random


# Definindo nossos "reservatórios" de caracteres usando a biblioteca string
maiusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
numeros = string.digits
especial = string.punctuation
# Garantindo 1 caractere de cada tipo (Regra de segurança)
caractere1 = random.choice(maiusculas)
caractere2 = random.choice(minusculas)
caractere3 = random.choice(numeros)
caractere4 = random.choice(especial)
# Cria a variavel todos como uma lista e ja adiciona os 4 sorteados nessa lista
todos = string.ascii_letters + string.digits + string.punctuation
# Criamos uma lista começando já com os 4 obrigatórios
senha = [caractere1, caractere2, caractere3, caractere4]
# Loop para sortear os 8 caracteres que faltam para completar 12
senha += [random.choice(todos) for _ in range(8)]
# O _ é usado quando não precisamos da variável do loop, apenas queremos que ele rode 8 vezes
#p = 0
#while p < 8:
#    senha_lista.append(random.choice(todos))
#    p += 1
# Embaralha a lista para que os 4 primeiros não fiquem sempre na mesma posição
random.shuffle(senha)

# 
print(f"Senha gerada: {''.join(senha)}")