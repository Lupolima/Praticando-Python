'''
Carlos é analista de dados em um hospital e está organizando informações de pacientes em um banco de dados. Ele recebe os dados no formato: "PrimeiroNome Sobrenome - Ano". Por exemplo, “Monalisa Silva - 1994”.

Carlos precisa de um programa que leia as informações, capture cada parte separadamente, nome, o sobrenome e o ano de nascimento para preencher os campos do sistema.

Ajude Carlos criando um programa que solicite o nome completo e o ano de nascimento de um paciente e exiba-os separadamente.

Exemplo de Entrada:

Digite o nome completo e o ano de nascimento do paciente: Ana Silva - 1990

Saída esperada:
Primeiro Nome: Ana
Sobrenome: Silva
Ano de Nascimento: 1990

'''
import re

dados = input("Digite o nome completo e o ano de nascimento do paciente: ")
padrao = r"(\w+) (\w+) - (\d{4})"
padronizado = re.search(padrao, dados)

if padronizado:
    nome = padronizado.group(1)
    sobrenome = padronizado.group(2)
    nascimento = padronizado.group(3)

    print(f"Primeiro nome: {nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Ano de Nascimento: {nascimento}")
else:
    print("Formato inválido")