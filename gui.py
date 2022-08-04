import tkinter as tk
from tkinter import ttk

def printfun():
    texto = "Ola"
    texto_tela["text"] = texto

cor = "#ffffff"

janela = tk.Tk()
janela.title("Cadastro de cliente")
janela.geometry("500x400")
janela.configure(background='#ffffff')


texto_inicial = tk.Label(janela, text="Realize o cadastro do cliente")
texto_inicial.grid(column=3, row=1, padx=4, pady=2, sticky='nswe')

nome_cliente = tk.Entry()
nome_cliente.grid(column=3, row=2, padx=4, pady=2, sticky='nswe')

botao = tk.Button(janela, text="Clique aqui", command=printfun)
botao.grid(column=1, row=2)

texto_tela = tk.Label(janela, text="")
texto_tela.grid(column=1, row=4)

janela.mainloop()

