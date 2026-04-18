import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Sistema de PDV - Restaurante")
janela.geometry("350x450")
janela.config(bg="#f0f0f0")

titulo = tk.Label(janela, text="Menu do Restaurante", font=("Arial", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=20)

janela.mainloop()