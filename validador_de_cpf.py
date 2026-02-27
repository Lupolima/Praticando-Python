import re  # Usaremos apenas para limpar o texto inicial

def validar_cpf(cpf_sujo):
    # 1. Limpeza: Mantém apenas os números usando Regex
    cpf = re.sub(r'\D', '', cpf_sujo)

    # Verifica se o CPF tem 11 dígitos ou se são todos iguais (ex: 111.111...)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # --- CÁLCULO DO PRIMEIRO DÍGITO ---
    soma = 0
    peso = 10
    
    # Multiplica os 9 primeiros dígitos por 10, 9, 8... até 2
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1
        
    resto = (soma * 10) % 11
    # Se o resto for 10 ou 11, o dígito deve ser 0
    primeiro_digito = 0 if resto >= 10 else resto

    # --- CÁLCULO DO SEGUNDO DÍGITO ---
    soma = 0
    peso = 11
    
    # Agora incluímos o primeiro dígito calculado na conta (10 dígitos no total)
    # Multiplica por 11, 10, 9... até 2
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
        
    resto = (soma * 10) % 11
    segundo_digito = 0 if resto >= 10 else resto

    # --- CONFERÊNCIA FINAL ---
    # Verifica se os dígitos calculados batem com os dígitos reais do CPF
    if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
        return True
    else:
        return False

# Testando o código
meu_cpf = input("Digite seu cpf: ")
if validar_cpf(meu_cpf):
    print(f"O CPF {meu_cpf} é válido!")
else:
    print(f"O CPF {meu_cpf} é INVÁLIDO!")

# {action_respond_info} executando validação manual de CPF via algoritmo de restos