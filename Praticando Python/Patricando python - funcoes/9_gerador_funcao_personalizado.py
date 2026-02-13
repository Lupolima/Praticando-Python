'''
Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.

Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.

Exemplo de entrada:
Digite a porcentagem de desconto: 10 
Digite o valor da compra: 200 

Saída esperada:
Preço final com desconto: 180.0 

'''
# Define a função "mãe" que servirá como fábrica de descontos
def criar_desconto(desconto):
    # Define a função "filha" que usará o desconto da mãe para processar um valor
    def aplicar_desconto(valor):
        # Realiza o cálculo matemático e retorna o valor final (o número)
        return valor - (valor * (desconto / 100))
    # Retorna a função 'aplicar_desconto' (a ferramenta) sem executá-la (sem parênteses)
    return aplicar_desconto

# Recebe a porcentagem (desconto)
desconto = float(input("Digite a porcentagem de desconto: "))
# Cria a closure: 'preco_final' agora é uma função que "lembra" do desconto digitado
preco_final = criar_desconto(desconto)
# Captura o valor da compra que será processado pela ferramenta criada
compra = float(input("Digite o valor da compra: "))
# Chama a função 'preco_final' passando o valor da compra e formata para 2 casas decimais
print(f"Preço final com desconto: {preco_final(compra):.2f}")
'''
Se a questao nao tivesse pedindo closure (fechamento), poderia fazer assim:

def criar_desconto(desconto, compra):
    return compra - (compra * (desconto / 100))


desconto = float(input("Digite a porcentagem de desconto: "))
compra = float(input("Digite o valor da compra: "))

preco_final = criar_desconto(desconto, compra)

print(f"Preço final com desconto: {preco_final}")
'''