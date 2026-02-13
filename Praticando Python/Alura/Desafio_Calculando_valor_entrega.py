import tkinter as tk
from tkinter import simpledialog, messagebox


root = tk.Tk()
root.withdraw()

distancia_local = simpledialog.askfloat("Input", "Digite a Distancia da entrega em km")
chovendo = messagebox.askyesno("Confirmação", "Esta Chovendo?")
valor_base = 5

if distancia_local is not None:

    if not chovendo:
        if distancia_local <=5:
            valor_entrega = valor_base
        elif 5 < distancia_local <= 10:
            valor_entrega = valor_base + 3
        elif distancia_local > 10:
            valor_entrega = valor_base + 5
    
    else:
        if distancia_local <=5:
            valor_entrega = valor_base + 2
        elif 5 < distancia_local <= 10:
            valor_entrega = valor_base + 5
        elif distancia_local > 10:
            valor_entrega = valor_base + 7

    messagebox.showinfo("Resumo da Entrega", f"O valor de Entrega ficou R$ {valor_entrega:.2f} reais")

else:
    print("Operação Cancelada")
    
root.destroy()