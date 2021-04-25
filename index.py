# Importar as bibliotecas
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import DataBaser

# Criar Nossa Janela
jan = Tk()
jan.title("DuranGAMES - Painel de Acesso")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="logo.ico")

# =========Carregar Imagens===============
logo = PhotoImage(file="logo.png")

# =========Widgets===============
LeftFrame = Frame(jan, width=200, height=300, bg="white", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=398, height=300, bg="white", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="white")
LogoLabel.place(x=10, y=80)

MensagemLabel = Label(RightFrame, text="Bem vindo ao painel de acesso", font=("Century Gothic", 13), bg="white", fg="black")
MensagemLabel.place(x=5, y=70)

UserLabel = Label(RightFrame, text="User:", font=("Century Gothic", 10), bg="white", fg="black")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=50)
UserEntry.place(x=75, y=100)

PassLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 10), bg="white", fg="black")
PassLabel.place(x=5, y=125)

PassEntry = ttk.Entry(RightFrame, width=50, show="*")
PassEntry.place(x=75, y=125)

RegistrarLabel = Label(RightFrame, text="Primeiro acesso?", font=("Century Gothic", 13), bg="white", fg="black")
RegistrarLabel.place(x=5, y=220)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso OK.")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado.")

# Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=10, command=Login)
LoginButton.place(x=200, y=150)

def Register():
    # Removendo Widgets de Login
    LoginButton.place(x=50000)
    CadastroButton.place(x=50000)
    RegistrarLabel.place(x=50000)
    MensagemLabel.place(x=50000)

    # Inserindo Widgets de Cadastro
    MenLabel = Label(RightFrame, text="Efetue seu Cadastro", font=("Century Gothic", 13), bg="white", fg="black")
    MenLabel.place(x=5, y=25)
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 10), bg="white", fg="black")
    NomeLabel.place(x=5, y=50)
    NomeEntry = ttk.Entry(RightFrame, width=50)
    NomeEntry.place(x=75, y=50)
    MensagemLabel.place(x=120, y=70)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 10), bg="white", fg="black")
    EmailLabel.place(x=5, y=75)
    EmailEntry= ttk.Entry(RightFrame, width=50)
    EmailEntry.place(x=75, y=75)

    def RegisterToDataBase():
        Nome = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Nome == "" and Email == "" and User == "" and Pass ==""):
            messagebox.showerror(title="Register Error", message="Preencha todos os Campos")
        else:
            DataBaser.cursor.execute("""
                    INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
                    """, (Nome, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta criada com sucesso.")

    Register = ttk.Button(RightFrame, text="Cadastrar", width=10, command=RegisterToDataBase)
    Register.place(x=120, y=150)

    def BackToLogin():
        #Removendo Widgets de Cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        RegistrarLabel.place(x=5000)
        MenLabel.place(x=5000)

        #Inserindo Widgets de Login
        LoginButton.place(x=200)
        CadastroButton.place(x=200)
        RegistrarLabel.place(x=5, y=220)
        MensagemLabel.place(x=5)

    Back = ttk.Button(RightFrame, text="Voltar", width=10, command=BackToLogin)
    Back.place(x=250, y=150)

CadastroButton = ttk.Button(RightFrame, text="Cadastrar", width=10, command=Register)
CadastroButton.place(x=200, y=220)

SairButton = ttk.Button(RightFrame, text="Sair", width=10)
SairButton.place(x=305, y=260)

jan.mainloop()
