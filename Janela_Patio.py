# Importacao das bibliotecas
from tkinter import *
from tkinter import messagebox
from Verificar_Cliente import Verificar_Cliente

# Classe Segunda_Janela
class Janela_Patio(Toplevel):
    # Metodo construtor
    def __init__(self, parent):
        # Chamar o init da classe mae
        super().__init__(parent)
        self.geometry('250x250')
        self.title('Carros no Pátio')
        self.transient(parent)
        self.grab_set()

        # Widgets
        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_car1 = Button(self, width = 10, text= 'LOL-2012',command = self.verificar)
        self.btn_car2 = Button(self, width=10, text='PUB-2018',command = self.verificar)
        self.btn_car3 = Button(self, width=10, text='DES-2016',command = self.verificar)
        self.btn_car4 = Button(self, width=10, text='ORW-2017',command = self.verificar)
        self.btn_car5 = Button(self, width=10, text='ORI-2018',command = self.destruir)
        self.btn_car6 = Button(self, width=10, text='Atualizar Carros\nDsiponíveis')

        # Posicionando os widgets
        self.btn_close.place(x=10, y=200)
        self.btn_car1.place(x=20, y = 50)
        self.btn_car2.place(x=150, y=50)
        self.btn_car3.place(x=20, y=100)
        self.btn_car4.place(x=150, y=100)
        self.btn_car5.place(x=20, y=150)
        self.btn_car6.place(x=150, y=150)

        self.menu = Menu(self)
        #Criando um item de menu e subtitens
        self.menu_principal = Menu(self.menu, tearoff=0)
        self.menu_principal.add_command(label='Compradores')
        self.menu_principal.add_command(label='Vendedores', command=self.menu_click)
            #Criar terceira janela
        self.menu_principal.add_command(label='Carros Vendidos', command=self.menu_click)
            #Criar quarta janela
        self.menu_principal.add_separator()
        self.menu_principal.add_command(label='Sair', command=self.destroy)
        self.menu.add_cascade(label='Menu', menu=self.menu_principal)
            # Mostrando o menu
        self.config(menu=self.menu)

    # Metodo para fechar a janela
    def menu_click(self):
       messagebox.showinfo('Menu', 'Clicou no item de menu!')

    def destroy(self):
        # Janela de confirmacao
        if messagebox.askokcancel('Confirmação','Deseja sair?'):
            super().destroy()

    def verificar(self):
        Verificar_Cliente(self)

    def criar(self):

        self.menu_principal.add_command(label = (self.findlist(self.format(self.readfile('Cadastro_Carro')))))



    def readfile(sel, file):
        f = open(file, 'r')
        a = f.read()
        f.close()
        return a

    def format(self, a):
        s = a.split('\n')
        for i in range(0, len(s)):
            s[i] = s[i].split(':')
        s.pop()
        return s

    def contar(self, s):
        for i in range(0, len(s)):
            self.menu_principal.add_command(label = self.findlist(self.format(self.readfile('Cadastro_Carro'))))

    def findlist(self, lista):
        for i in lista:
            print(i[4])
            return i[4]

    def destruir(self):
        self.menu_principal.destroy()