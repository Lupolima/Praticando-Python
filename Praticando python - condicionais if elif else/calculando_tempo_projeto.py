'''
Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.

Saída esperada:
Informe os dias para a atividade A: 5
Informe os dias para a atividade B: -8
Informe os dias para a atividade C: 10
Erro: Os dias ndo podem ser negativos.


'''

atividadeA = int(input("Informe os dias da Atividade A: "))
atividadeB = int(input("Informe os dias da Atividade B: "))
atividadeC = int(input("Informe os dias da Atividade C: "))

if atividadeA >= 0 and atividadeB >= 0 and atividadeC >= 0:
    total = atividadeA + atividadeB + atividadeC
    print(f"O tempo total dos 3 projetos é: {total} dias\n")
else:
    print("ERRO: Os dias não podem ser negativos\n")