import tkinter as tk
from tkinter import simpledialog, messagebox
import sys # Importamos sys para fechar o programa se necessário

# {action_respond_info} Iniciando sistema da cafeteria com opção de saída
root = tk.Tk()
root.withdraw()

qtd_item = simpledialog.askinteger("Input", "Quantos itens precisa?")
valor_total = 0.0

if qtd_item is not None and qtd_item > 0:
    for i in range(qtd_item):
        nome_item = simpledialog.askstring("Item", f"Digite o nome do {i+1}º item:")
        
        # Se o usuário cancelar o nome, podemos assumir um nome padrão
        if nome_item is None:
            nome_item = f"Item {i+1}"

        # --- VALIDAÇÃO COM OPÇÃO DE SAÍDA ---
        preco_item = None
        while preco_item is None or preco_item <= 0:
            preco_item = simpledialog.askfloat("Preço", f"Digite o preço do(a) {nome_item}:")
            
            # Se o usuário clicar em CANCELAR (retorna None)
            if preco_item is None:
                # {action_respond_info} Usuário tentou cancelar. Perguntando se quer sair do programa.
                confirmar_saida = messagebox.askyesno("Sair", "Deseja cancelar todo o pedido e fechar o sistema?")
                if confirmar_saida:
                    # {action_respond_info} Encerrando tudo a pedido do usuário
                    root.destroy()
                    sys.exit() # Fecha o script imediatamente
                else:
                    # Se ele não quiser sair, o loop continua e pede o preço de novo
                    continue 
            
            # Se ele digitar um valor inválido (zero ou negativo)
            elif preco_item <= 0:
                messagebox.showwarning("Erro", "O preço deve ser maior que zero!")
        # --- FIM DA VALIDAÇÃO ---

        valor_total += preco_item
        print(f"Confirmado: {nome_item} - R$ {preco_item:.2f}")

    # Fluxo final de desconto
    cliente_cadastrado = messagebox.askyesno("Possui Cadastro", "Cliente já possui cadastro?")
    if cliente_cadastrado:
        valor_final = valor_total * 0.90
        messagebox.showinfo("Total", f"Valor com desconto: R$ {valor_final:.2f}")
    else:
        messagebox.showinfo("Total", f"Valor total: R$ {valor_total:.2f}")

else:
    print("Operação cancelada no início.")

root.destroy()