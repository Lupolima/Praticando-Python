'''
Sara trabalha no setor de atendimento de uma empresa e precisa verificar rapidamente se os clientes estão digitando seus números de CPF no formato correto antes de registrar os dados no sistema.

O formato esperado do CPF é: três blocos de 3 dígitos separados por pontos (.), seguidos por um bloco de 2 dígitos separados por um traço (-).

Ajude Sara a criar um programa que solicite o CPF de um cliente e verifica se ele está no formato correto.

Exemplo de Entrada:

Digite o CPF no formato XXX.XXX.XXX-XX: 123.456.789-00

Saída esperada:

O CPF está no formato correto.

'''
'''
O ponto vem antes da barra invertida () porque o ponto tem um significado especial em expressões regulares: ele representa "qualquer caractere". Para que o ponto seja interpretado como um ponto literal, precisamos "escapá-lo" com a barra invertida, transformando-o em contrabarra e ponto

Já o traço (-) não tem um significado especial dentro da expressão regular que estamos utilizando, então ele é interpretado como um traço normal, sem a necessidade de "escapá-lo" com a barra invertida.
'''

import re

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
cpf_padrao = r"\d{3}\.\d{3}\.\d{3}-\d{2}"
if re.search(cpf_padrao, cpf):
    print("O CPF está no formato correto.")
else:
    print("O CPF está no formato incorreto.")
(exit)

