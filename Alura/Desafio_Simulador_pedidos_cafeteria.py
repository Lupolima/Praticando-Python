"""
Você foi contratado por uma cafeteria que deseja automatizar o atendimento no balcão. O sistema deve permitir que o atendente registre os pedidos de cada cliente, calcule o valor total e aplique um desconto de 10% para clientes cadastrados.

O processo deve funcionar da seguinte forma:

    O atendente informa quantos itens o cliente vai pedir.
    Para cada item, o sistema solicita o nome e o preço.
    Ao final, o sistema pergunta se o cliente é cadastrado.
    Se for, aplica o desconto e exibe o valor com desconto.
    Caso contrário, exibe o valor cheio.
"""

import tkinter as tk
from tkinter import simpledialog, messagebox


root = tk.Tk()
root.withdraw()

qtd_item = simpledialog.askinteger("Input", "Quantos itens Precisa?")
valor_total = 0.0
if qtd_item is not None and qtd_item > 0:
    for i in range(qtd_item):
        nome_item = simpledialog.askstring("Item", f"Digite o nome do {i+1}º item")
        preco_item = simpledialog.askfloat("Preco", f"Digite o preço do {nome_item}")

        if preco_item is not None and preco_item > 0:
            # {action_respond_info} Somando o preço ao total acumulado
            valor_total = valor_total + preco_item
            print(f"Item: {nome_item} - R$ {preco_item:.2f} foi adicionado.")
    
    cliente_cadastrado = messagebox.askyesno("Possui Cadastro", "Cliente já possui cadastro?")
    if cliente_cadastrado:
        valor_final = valor_total * 0.9
        messagebox.showinfo(f"Total do Pedido", f"Valor total do Pedido com desconto: {valor_final:.2f} Reais")
    else:
        messagebox.showinfo(f"Total do Pedido", f"Valor total do Pedido sem desconto: {valor_total:.2f} Reais")
        
else:
    print("Quantidade de item inválida ou operação cancelada")


root.destroy()