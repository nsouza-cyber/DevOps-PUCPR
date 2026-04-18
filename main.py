import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Sistema de PDV - Restaurante")
janela.geometry("350x450")
janela.config(bg="#f0f0f0")

titulo = tk.Label(janela, text="Menu do Restaurante", font=("Arial", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=20)

frame_produtos = tk.Frame(janela, bg="#f0f0f0")
frame_produtos.pack(pady=10)

btn_hamburguer = tk.Button(frame_produtos, text="Hambúrguer - R$ 25,00", width=25, font=("Arial", 12))
btn_hamburguer.pack(pady=5)

btn_pizza = tk.Button(frame_produtos, text="Pizza - R$ 40,00", width=25, font=("Arial", 12))
btn_pizza.pack(pady=5)

btn_refri = tk.Button(frame_produtos, text="Refrigerante - R$ 8,00", width=25, font=("Arial", 12))
btn_refri.pack(pady=5)


janela.mainloop()