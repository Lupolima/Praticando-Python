'''PROBLEMA: Faça um contador de palavras. O projeto deve receber uma frase do usuário e contar quantas vezes cada palavra aparece.

Leia o pdf Praticando-Python-trabalhando_projetos para entender o que foi feito para evitar erros de digitacao do usuario, tratamento de problemas.

'''
# Função para "higienizar" o texto (remover pontuação e padronizar)
def limpar_texto(texto):
    # Converte tudo para minúsculo para que 'Brasil' e 'brasil' sejam iguais
    texto = texto.lower()
    # Define uma lista de símbolos que não queremos contar como palavras
    caracteres = ",.!|?;:\"'()[]{}"
    # Percorre cada símbolo da lista acima
    for char in caracteres:
        # Substitui o símbolo encontrado por nada (apaga o símbolo)
        texto = texto.replace(char, "")
    return texto

# Função principal que faz a contagem
def contar_palavras(frase):
    # Primeiro, limpa a frase usando a função que criamos acima
    frase = limpar_texto(frase)
    # Verifica se sobrou algo na frase após a limpeza (evita erros com frases só de símbolos)
    if not frase.strip():
        return {}
    
    # Transforma a frase limpa em uma lista de palavras
    palavras = frase.split()
    # Cria um dicionário vazio para guardar os resultados (Palavra: Quantidade)
    contagem = {}
    
    # Percorre a lista de palavras uma por uma
    for palavra in palavras:
        # O pulo do gato: o .get(palavra, 0) tenta pegar o valor atual da palavra no dicionário.
        # Se a palavra não existir lá ainda, ele retorna 0.
        # Então, ele soma +1 ao valor encontrado (ou ao zero) e guarda de volta.
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

# --- Fluxo Principal do Programa ---

# Captura a frase e remove espaços inúteis no início e fim
frase = input("Digite uma frase: ").strip()

# Tratamento de erro: verifica se o usuário deu ENTER sem digitar nada
if not frase:
    print("Erro: Nenhuma frase foi digitada.")
else:
    # Chama a função de contagem
    resultado = contar_palavras(frase)
    # Se o dicionário retornado não estiver vazio
    if resultado:
        print("Contagem de palavras:")
        # O .items() nos dá o par (Chave, Valor) para o loop for
        for palavra, quantidade in resultado.items():
            print(f"{palavra}: {quantidade}")
    else:
        print("Nenhuma palavra encontrada na frase.")
        

'''
como fazer essa mesma contagem de um jeito ainda mais rápido usando uma biblioteca nativa do Python chamada collections

from collections import Counter # Importa a ferramenta especialista em contagem

def limpar_texto(texto):
    texto = texto.lower()
    caracteres = ",.!|?;:\"'()[]{}"
    for char in caracteres:
        texto = texto.replace(char, "")
    return texto

def contar_palavras_ninja(frase):
    frase = limpar_texto(frase)
    if not frase.strip():
        return Counter() # Retorna um contador vazio
    
    palavras = frase.split()
    # O Counter faz todo o trabalho do loop 'for' e do '.get()' sozinho!
    return Counter(palavras)

# --- Uso ---
frase_usuario = "O Brasil é verde, o Brasil é grande!"
resultado = contar_palavras_ninja(frase_usuario)

# O Counter já se comporta como um dicionário
for palavra, qtd in resultado.items():
    print(f"{palavra}: {qtd}")

'''