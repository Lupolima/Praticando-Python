#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = "Estou estudando python python é muito legal, a linguagem python é divertida"
numero_palavras = {}
palavras = frase.split() 
for palavra in palavras:
    numero_palavras[palavra] = numero_palavras.get(palavra, 0)+ 1
print(numero_palavras)


# split() é utilizada para dividir uma string em uma lista de substrings, usando um separador como referência. Se nenhum separador for especificado, o split() usa o espaço em branco como padrão