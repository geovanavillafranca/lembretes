from tkinter import *
from tkinter import ttk


def login():
    pass


def cadastro():
    pass




root = Tk()
root.title("Login")
root.geometry("350x250")


Label(root, text="Usuário").place(x=100, y=20)
usuario_entry = Entry(root)
usuario_entry.place(x=100, y=50, width=145)


Label(root, text="Senha").place(x=100, y=90)
senha_entry = Entry(root)
senha_entry.place(x=100, y=130, width=145)

cadastro_botao = Button(root, text="CADASTRAR", command=cadastro)
cadastro_botao.place(x=100, y=170)

logar_botao = Button(root, text="LOGIN", command=login)
logar_botao.place(x=200, y=170)





root.mainloop()




















