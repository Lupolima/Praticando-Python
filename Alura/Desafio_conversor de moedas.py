import tkinter as tk
from tkinter import simpledialog, messagebox


root = tk.Tk()
root.withdraw()

taxa_cambio = simpledialog.askfloat("Input", "Digite a Taxa de Cambio")
valor_reais = simpledialog.askfloat("Input", "Digite o valor em Reais")
valor_convertido = taxa_cambio*valor_reais
messagebox.showinfo("Com a taxa atual, o valor em dólares é:", f"$ {valor_convertido:.2f} Dollares")