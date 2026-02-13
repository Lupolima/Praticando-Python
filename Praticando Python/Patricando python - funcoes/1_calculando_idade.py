'''
Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

Exemplo de entrada: 
Digite o ano de nascimento: 2005  
Digite o ano atual: 2025 

Saída esperada:
A idade é 20 anos. 
'''
def calculaidade(nascimento, atual):
    return atual - nascimento

nascimento = int(input("Digite o ano de nascimento: "))
atual = int(input("Digite o ano atual: "))
idade = int(calculaidade(nascimento, atual))
print(f"A idade é {idade} anos.")