from tkinter import *
from tkinter import messagebox

class Finalizando_Compra(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('500x600')
        self.title('Finalização da Compra')
        self.transient(parent)
        self.grab_set()

        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_ok = Button(self, width=10, text='Emitir NF')
        self.btn_atualizar = Button(self, width=40, text='Atualizar dados para emissão da NF', command=lambda: self.get_listas(self.txt_login.get(),self.txt_cpf.get(), self.txt_placa.get()))
        self.lbl_confirmarlogin = Label(self, text='Confirme o Login do vendedor')
        self.lbl_login = Label(self, width=20, text='Login')
        self.lbl_confirmarcpf = Label(self, text='Confirmar CPF do cliente')
        self.lbl_cpf = Label(self, width=20, text='CPF')
        self.lbl_confirmarplaca = Label(self, text='Confirme a placa do veículo e o valor da venda')
        self.lbl_placa = Label(self, width=20, text='Placa')
        self.lbl_valor = Label(self, width=20, text='Valor da venda')
        self.lbl_nf = Label(self, text='Dados da Compra')
        self.lbl_infovendedor = Label (self, text='Informaçõs vendedor')
        self.lbl_nomevendedor = Label(self, text='nome vend')
        self.lbl_telefonevendedor = Label(self, text='telefone vend')
        self.lbl_nummat = Label(self, text='N matricula')
        self.lbl_infocomprador = Label (self, text='Informações Cliente')
        self.lbl_nomecomprador = Label(self, text='nome')
        self.lbl_cpfcomprador = Label(self, text='cpf')
        self.lbl_telefonecomprador = Label(self, text='telefone')
        self.lbl_endcomrpador = Label(self, text='endereço')
        self.lbl_infcar = Label(self, text='Informações do carro')
        self.lbl_modelo = Label(self, text='modelo')
        self.lbl_ano = Label(self, text='ano')
        self.lbl_cor = Label (self, text='cor')
        self.lbl_valorconfirm = Label(self, text='Valor da Compra')
        self.lbl_placaconfirm = Label(self, text='placa')


        #self.lbl_senha = Label(self, width=20, text="Telefone")
        # self.lbl_obs = Label(self, width=20, text="Observações da venda")
        self.txt_login = Entry(self, width=50)
        self.txt_cpf = Entry(self, width=50)
        self.txt_placa = Entry(self, width=50)
        self.txt_valor = Entry(self, width=50)
        #self.txt_senha = Entry(self, width=50)
        # self.txt_obs = Entry(self, width=50)

        self.btn_close.place(x=100, y=510)
        self.btn_ok.place(x=300, y=510)
        self.btn_atualizar.place(x=150,y=280)
        self.lbl_confirmarlogin.place(x=10, y=20)
        self.lbl_login.place(x=10, y=50)
        self.lbl_confirmarcpf.place(x=10, y=90)
        self.lbl_cpf.place(x=10, y=120)
        self.lbl_confirmarplaca.place(x=10, y=160)
        self.lbl_placa.place(x=10, y=200)
        self.lbl_valor.place(x=10, y=240)
        self.lbl_nf.place(x=10, y=320)
        self.lbl_infovendedor.place(x=10, y=345)
        self.lbl_nomevendedor.place(x=10, y=370)
        self.lbl_telefonevendedor.place(x=120, y=370)
        self.lbl_infocomprador.place(x=10, y=395)
        self.lbl_nomecomprador.place(x=10, y=420)
        self.lbl_cpfcomprador.place(x=100, y=420)
        self.lbl_telefonecomprador.place(x=190, y=420)
        self.lbl_endcomrpador.place(x=290, y=420)
        self.lbl_infcar.place(x =10, y=445)
        self.lbl_modelo.place(x=10, y=470)
        self.lbl_ano.place(x=100, y=470)
        self.lbl_cor.place(x=180, y=470)
        self.lbl_valorconfirm.place(x=250, y=470)
        self.lbl_placaconfirm.place(x=350, y=470)
        #self.lbl_senha.place(x=10, y=150)
        # self.lbl_obs.place(x=10, y=190)
        self.txt_login.place(x=150, y=50)
        self.txt_cpf.place(x=150, y=120)
        self.txt_placa.place(x=150, y=200)
        self.txt_valor.place(x=150,y=240)
        #self.txt_senha.place(x=150, y=150)
        # self.txt_obs.place(x=150, y=190)

    def destroy(self):
            # Janela de confirmacao
        if messagebox.askokcancel('Confirmação', 'Deseja sair, o cadastro não foi finalizado?'):
            super().destroy()

    def readfile(self, file):
        f = open(file, 'r')
        a = f.read()
        f.close()
        #print(a)
        return a

    def format(self, a):
        s = a.split('\n')
        for i in range(0, len(s)):
            s[i] = s[i].split(':')
        s.pop()
        #print(s)
        return s

    def findlist(self, lista, id):
        for i in lista:
            if i[0] == id:
                #print(i[3])
                return i

        return False

    def findlistcar(self, lista, id):
        for i in lista:
            if i[4] == id:
                #print(i[3])
                return i

        return False

    def get_listas(self, login, cpf, placa):

        a = (self.findlist(self.format(self.readfile('Cadastro_Vendedor')), login))
        b = (self.findlist(self.format(self.readfile('Cadastro_Comprador')), cpf))
        c = (self.findlistcar(self.format(self.readfile('Cadastro_Carro')), placa))
        self.lbl_nomevendedor.config(text=a[2])
        self.lbl_telefonevendedor.config(text=a[3])
        self.lbl_nomecomprador.config(text=b[1])
        self.lbl_cpfcomprador.config(text=b[0])
        self.lbl_telefonecomprador.config(text=b[2])
        self.lbl_endcomrpador.config(text=b[3])
        self.lbl_modelo.config(text=c[0])
        self.lbl_ano.config(text=c[1])
        self.lbl_cor.config(text=c[2])
        self.lbl_placaconfirm.config(text=c[4])
        self.lbl_valorconfirm.config(text=self.txt_valor.get())
