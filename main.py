import tkinter as tk
from tkinter import messagebox

def adicionar_item(valor):
    atual = valor_total.get()
    valor_total.set(atual + valor)
    label_total.config(text=f"Total: R$ {valor_total.get():.2f}")

janela = tk.Tk()
janela.title("Sistema de PDV - Restaurante")
janela.geometry("350x450")
janela.config(bg="#f0f0f0")

valor_total = tk.DoubleVar()
valor_total.set(0.0)

titulo = tk.Label(janela, text="Menu do Restaurante", font=("Arial", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=20)

frame_produtos = tk.Frame(janela, bg="#f0f0f0")
frame_produtos.pack(pady=10)

btn_hamburguer = tk.Button(frame_produtos, text="Hambúrguer - R$ 25,00", width=25, font=("Arial", 12), command=lambda: adicionar_item(25.00))
btn_hamburguer.pack(pady=5)

btn_pizza = tk.Button(frame_produtos, text="Pizza - R$ 40,00", width=25, font=("Arial", 12), command=lambda: adicionar_item(40.00))
btn_pizza.pack(pady=5)

btn_refri = tk.Button(frame_produtos, text="Refrigerante - R$ 8,00", width=25, font=("Arial", 12), command=lambda: adicionar_item(8.00))
btn_refri.pack(pady=5)

label_total = tk.Label(janela, text="Total: R$ 0.00", font=("Arial", 14, "bold"), fg="green", bg="#f0f0f0")
label_total.pack(pady=20)

janela.mainloop()