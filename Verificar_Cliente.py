from tkinter import *
from tkinter import messagebox
from Janela_Comprador import Janela_Comprador
from Finalizando_Compra import Finalizando_Compra

class Verificar_Cliente(Toplevel):

    def __init__(self, parent):

        super().__init__(parent)
        self.geometry('200x200')
        self.title('Verificar Comprador')
        self.transient(parent)
        self.grab_set()


        self.btn_pesquisar = Button(self, width=10, text='Pesquisar', command = lambda: self.pesquisar(self.findlist(self.format(self.readfile('Cadastro_Comprador')), self.txt_cpf.get())))

        self.lbl_cpf = Label(self, width=10, text='CPF')

        self.txt_cpf = Entry(self,width=20)

        self.btn_pesquisar.place(x=50, y=150)

        self.lbl_cpf.place(x= -5, y=75)

        self.txt_cpf.place(x=50, y=75)



    def readfile(self, file):
        f = open(file, 'r')
        a = f.read()
        f.close()
        # print(a)
        return a

    def format(self, a):
        s = a.split('\n')
        for i in range(0, len(s)):
            s[i] = s[i].split(':')
        s.pop()
        # print(s)
        return s

    def findlist(self, lista, id):
        for i in lista:
            if i[0] == id:
            # print(i[3])
                return i

        return False

    def pesquisar(self, cpf):
        if cpf == (self.findlist(self.format(self.readfile('Cadastro_Vendedor')), cpf)):

            Janela_Comprador(self)

        else:
            Finalizando_Compra(self)

    def destroy(self):
         if messagebox.askokcancel('Confirmação', 'Deseja sair, o cadastro não foi finalizado?'):
            super().destroy()


''' def verificar(self, lista, id):
      for i in lista:
          if i[0] == id:
              Finalizando_Compra(self)
              break

      return Janela_Comprador(self)'''