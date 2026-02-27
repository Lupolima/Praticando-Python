# \r\n -> CRLF para Windows
# \n -> LF para Linux/MAC

print(12, 34, 1011, sep="-", end='#')
print(45, 32, 8745, sep="-")            # por padrao ele adiciona \n quebra de linha caso nao tenha nenhum end definido
print(56, 78, 1011, sep="-", end='\n')
print('09', 10, 1011, sep="-", end='\n')

"""
No python 3 números que iniciam com 0 não são aceitos como válidos, mas você pode simplesmente criar a
data como texto e não número (utilizando aspas).
Exemplo
>>> dia = 25
>>> mes = '01'
>>> ano = 2020
>>> print(dia, mes, ano, sep="/")
25/01/2020
"""


