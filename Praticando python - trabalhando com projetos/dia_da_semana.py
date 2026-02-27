from datetime import date

# 1. Criamos uma lista com os nomes na ordem correta (0 a 6)
dias_da_semana = [
    "Segunda-feira", "Terça-feira", "Quarta-feira", 
    "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
]

# 2. Pegamos a data de hoje
hoje = date.today()

# 3. Usamos o número do weekday() como índice da lista
# Se for 0, pega 'Segunda-feira'. Se for 2, pega 'Quarta-feira', etc.
nome_do_dia = dias_da_semana[hoje.weekday()]

print(f"Hoje é dia {hoje.strftime('%d/%m/%Y')}, uma {nome_do_dia}.")