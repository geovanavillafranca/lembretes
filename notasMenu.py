from tkinter import *
from tkinter import messagebox, ttk
from tkcalendar import *
from datetime import date
import mysql.connector



# --- O que falta? --- #

# Erro em campo vazio
# Criar tela de cadastro
# Salvar em um banco de dados


# ----- Conectando ao banco ----- #
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Mysql>1234",
    database="cadastro_lembretes"
    )


# ----- Metodos ----- #

def criar_novo():
    print("Criando um novo lembrete")


def sair():
    root.quit()


def ajuda():
    messagebox.showinfo(
                        "Ajuda",
                        "Esse é um programa para salvar seus lembretes"
    )


def salvar():
    titulo = str(titulo_entry.get())
    descricao = str(descricao_entry.get())
    data_lembrete = calendario.get_date()


    print(titulo)
    print(descricao)
    print(data_lembrete)

    cursor = banco.cursor()
    comandoSQL = "INSERT INTO lembrete (titulo, descricao, datalembrete) values (%s, %s, %s)"
    dados = (str(titulo), str(descricao), str(data_lembrete))
    cursor.execute(comandoSQL, dados)
    banco.commit()

    messagebox.showinfo("Aviso",
                        f"Lembrete salvo com sucesso! \nTitulo: {titulo} \nData: {data_lembrete}"
    )


# ----- Tela ----- #

root = Tk(className="Criando um lembrete")
root.config(bg="#9370DB")
root.geometry("900x400")

# ----- Menu ----- #

menu = Menu(root)

arquivo_menu = Menu(menu, tearoff=0)

arquivo_menu.add_command(label="Criar novo", command=criar_novo)

arquivo_menu.add_command(label="Ajuda", command=ajuda)

arquivo_menu.add_separator()

arquivo_menu.add_command(label="Sair", command=sair)

menu.add_cascade(label="Menu", menu=arquivo_menu)

root.config(menu=menu)

# ----- Corpo ----- #

titulo_label = Label(root, text="Titulo do lembrete", font=("Times", 12, 'bold'), bg="#9370DB")
titulo_label.place(x=100, y=50)

titulo_entry = Entry(root)
titulo_entry.place(x=100, y=100)

descricao_label = Label(root, text="Descricao", font=("Times", 12, 'bold'), bg="#9370DB")
descricao_label.place(x=100, y=150)

descricao_entry = Entry(root)
# descricao_entry.grid(row=3, column=1, sticky=W, padx=100)
descricao_entry.place(x=100, y=200, width=400, height=100)

botao_salvar = Button(root, text="SALVAR", command=salvar, font=("Times", 10, 'bold'), fg="black", bg="#4169E1")
botao_salvar.place(x=732, y=350)

calendario_label = Label(root, text="Selecione uma data", font=("Times", 12, 'bold'), bg="#9370DB")
calendario_label.place(x=610, y=50)

calendario = Calendar(root, setmode='day', date_pattern='d/m/yyyy')
calendario.place(x=550, y=100)

root.mainloop()
