'''
A função split() é uma ferramenta poderosa em Python para manipular strings.
Ela permite que você divida uma string em várias partes menores, usando um separador
como referência.

string.split(separador)

string: A string que você deseja dividir.
separador: O caractere ou sequência de caracteres que será usado para dividir a string.
Se você não especificar um separador, o split() usará espaços em branco por padrão.

frase = "Olá mundo, este é um exemplo."
palavras = frase.split()  # Usando espaço em branco como separador padrão
print(palavras)
# Saída: ['Olá', 'mundo,', 'este', 'é', 'um', 'exemplo.']

'''

encomendas = input("Digite os números das encomendas separados por vírgula: ").split(",")
try:
    for encomenda in encomendas:
        print(int(encomenda))
except ValueError:
    print("Uma das entradas não é um número válido.")