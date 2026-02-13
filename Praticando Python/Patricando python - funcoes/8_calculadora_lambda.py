'''
Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

Exemplo de entrada:
Digite o primeiro número: 10   
Digite o segundo número: 5   
Escolha a operação (| + | - | * | / |): + 

Saída esperada:
O resultado é: 15 
'''
# Define as funções lambda e as atribui a variáveis nomeadas
soma = lambda x, y: x + y
subtrai = lambda x, y: x - y
multiplica = lambda x,y: x * y
# No lambda de divisão, ele incluiu um "if" interno para evitar o erro de dividir por zero
divide = lambda x,y: x / y if y != 0 else "Erro: Divisão por zero"

# Captura os números como float para aceitar decimais
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

# Recebe o símbolo da operação
operador = input("Escolha a operação (| + | - | * | / |): ")

# Estrutura de decisão para verificar qual símbolo o usuário digitou
if operador == "+":
    print(f"O resultado é: {soma(x, y)}")
elif operador == "-":
    print(f"O resultado é: {subtrai(x, y)}")
elif operador == "*":
    print(f"O resultado é: {multiplica(x, y)}")
elif operador == "/":
    print(f"O resultado é: {divide(x, y)}")
else:
    # Caso o usuário digite algo que não esteja na lista
    print("Operação inválida")

'''
Uma abordagem mais eficiente para evitar múltiplas estruturas if-elif é utilizar um dicionário para armazenar as operações matemáticas. Isso torna o código mais organizado, fácil de manter e escalável, como mostrado a seguir: 

# {action_respond_info} Definimos o dicionário já criando as lambdas dentro dele
# Assim, economizamos as linhas de criação de variáveis separadas
operacoes = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Erro: Divisão por zero"
}

# Captura dos dados do usuário
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (| + | - | * | / |): ")

# {action_respond_info} A lógica de busca e execução permanece a mesma
if operacao in operacoes:
    # Busca a lambda correspondente e já a executa com (x, y)
    resultado = operacoes[operacao](x, y)
    print(f"O resultado é: {resultado}")
else:
    print("Operação inválida")
'''