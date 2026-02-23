'''
Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.

Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

Exemplo de entrada:
Digite um texto: A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais

Saída esperada:
Palavras longas encontradas: programação, estruturada, desenvolvimento, computacionais 

Se nenhum palavra longa for encontrada:
Nenhuma palavra longa foi encontrada no texto.  
'''
texto = input("Digite um texto: ")
palavras_longas = []

for palavra in texto.split():
    if len(palavra) > 10:
        palavras_longas.append(palavra)

if palavras_longas:
    print("Palavras longas encontradas: "+", ".join(palavras_longas))
else:
    print("Nenhuma palavra longa foi encontrada no texto.")


'''
#Utilizando o List Comprehension
# Captura o texto da usuária e remove espaços inúteis nas extremidades
texto = input("Digite um texto: ").strip()

# Divide o texto em uma lista de palavras (usando os espaços como separador)
palavras = texto.split()

# Criamos uma nova lista filtrada usando "List Comprehension"
# Lógica: coloque na lista 'longas' a 'p' para cada 'p' em 'palavras' se o tamanho de 'p' for > 10
longas = [p for p in palavras if len(p) > 10]

# Verificamos se a lista 'longas' contém algum item
if longas:
    # O comando ", ".join(longas) junta as palavras da lista em uma única frase separada por vírgula
    print(f"Palavras longas encontradas: {', '.join(longas)}")
else:
    # Caso a lista 'longas' tenha ficado vazia
    print("Nenhuma palavra longa foi encontrada no texto.")
'''