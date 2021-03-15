from tkinter import *
from tkinter import messagebox
import datetime as dt


class InitialGUI:

    def __init__(self, root):
        """
        This __init__ method initializes the GUI widgets from our interface.
        :param root: The main window element.
        """
        self.button1 = Button(root, text='Entrar na conta', width=25, font=('Helvetica', 14), bg='#222831',
                              fg='#eeeeee', borderwidth=3)
        self.button2 = Button(root, text='Criar Conta', width=25, font=('Helvetica', 14), bg='#222831', fg='#eeeeee',
                              borderwidth=3, command=lambda: self.criar_conta(root))
        self.button3 = Button(root, text='Administrador', width=25, font=('Helvetica', 14), bg='#222831', fg='#eeeeee',
                              borderwidth=3)
        self.label1 = Label(root, text='Escolha uma das opções abaixo', font=('Helvetica', 20), bg='#393e46',
                            fg='#eeeeee')

        self.label1.grid(row=0, column=0, pady=250, columnspan=3)
        self.button1.grid(row=1, column=0, padx=55)
        self.button2.grid(row=1, column=1, padx=55)
        self.button3.grid(row=1, column=2, padx=55)

    def criar_conta(self, root):
        """
        This method creates the UI for the 'criar conta' option selected in the main menu. First, it destroys all the
        old content from the screen, and then creates and render a new UI with the elements needed to create an account.
        :param root: The main window element.
        :return: None
        """
        def reset():
            """
            This function works like a 'back' button. Every time a button calls this function, it destroys every content
            from the current window and returns to the main window.
            :return: None
            """
            main_frame.destroy()
            system_state.destroy()
            self.__init__(root)

        def account_creation():
            """
            This function creates the 'Cliente' instance and verifies the necessary data to do so. If a entry label has
            a unexpected data type, it pops up a warning accordingly to the mistake.
            :return: None
            """
            # Gathering the data from the entry fields
            gathered_data = name.get(), cpf.get(), data_de_nascimento.get(), login.get(), password.get()

            # Checking the data. This is a long process in order to ensure the data integrity of account creation. If
            # some of the data is not expected, a pop-up will be shown

            # Looking for blank entries
            for data in gathered_data:
                if len(data) == 0:
                    name.delete(0, END)
                    cpf.delete(0, END)
                    data_de_nascimento.delete(0, END)
                    login.delete(0, END)
                    password.delete(0, END)
                    messagebox.showerror("Dados inválidos!", "Existem campos vazios!")
                    return None
            # Checking 'cpf' field integrity
            numbers = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
            if len(gathered_data[1]) != 11:
                name.delete(0, END)
                cpf.delete(0, END)
                data_de_nascimento.delete(0, END)
                login.delete(0, END)
                password.delete(0, END)
                messagebox.showerror("CPF inválido", "O CPF informado é inválido. Insira apenas os 11 dígitos do CPF")
                return None
            for number in gathered_data[1]:
                if number not in numbers:
                    name.delete(0, END)
                    cpf.delete(0, END)
                    data_de_nascimento.delete(0, END)
                    login.delete(0, END)
                    password.delete(0, END)
                    messagebox.showerror("CPF inválido", "O CPF informado é inválido. Insira apenas os 11 dígitos do"
                                                         " CPF")
                    return None
            # Checking 'data de nascimento' field integrity
            for element in gathered_data[2]:
                if element not in numbers and element != '/':
                    name.delete(0, END)
                    cpf.delete(0, END)
                    data_de_nascimento.delete(0, END)
                    login.delete(0, END)
                    password.delete(0, END)
                    messagebox.showerror("Data de nascimento inválida", "A data de nascimento informada é inválida.")
                    return None
            date = gathered_data[2].split("/")
            try:
                date = dt.date(day=int(date[0]), month=int(date[1]), year=int(date[2]))
            except (ValueError, Exception):
                name.delete(0, END)
                cpf.delete(0, END)
                data_de_nascimento.delete(0, END)
                login.delete(0, END)
                password.delete(0, END)
                messagebox.showerror("Data de nascimento inválida", "A data de nascimento informada é inválida.")
                return None
            else:
                now = dt.datetime.now()
                if (now.year - date.year) < 18:
                    name.delete(0, END)
                    cpf.delete(0, END)
                    data_de_nascimento.delete(0, END)
                    login.delete(0, END)
                    password.delete(0, END)
                    messagebox.showerror("Menor de idade", "Você precisa ser maior de 18 anos para abrir uma conta.")
                    return None
                else:
                    final_data = {
                        "Nome": name.get(),
                        "CPF": cpf.get(),
                        "Data de nascimento": date,
                        "Login": login.get(),
                        "Senha": password.get()
                    }
                    name.delete(0, END)
                    cpf.delete(0, END)
                    data_de_nascimento.delete(0, END)
                    login.delete(0, END)
                    password.delete(0, END)
                    messagebox.showinfo("Conta criada", "Sua conta foi criada com sucesso!")
                    return None

        # Getting rid of the old widgets
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.label1.destroy()

        #                   Creating the new GUI
        main_frame = LabelFrame(root, bg='#393e46')
        system_state = Label(root, bg='#393e46', text='Criação de Conta', fg='#eeeeee', font=('Helvetica', 24))

        # Name
        label_name = Label(main_frame, text='Nome -', font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')
        name = Entry(main_frame, font=('Helvetica', 14), borderwidth=3)

        # CPF
        label_cpf = Label(main_frame, text='CPF (Apenas números) -', font=('Helvetica', 14), bg='#393e46',
                          fg='#eeeeee')
        cpf = Entry(main_frame, font=('Helvetica', 14), borderwidth=3)

        # Data de Nascimento
        label_data_de_nascimento = Label(main_frame, text='Data de Nascimento (dd/mm/aaaa) -', font=('Helvetica', 14),
                                         bg='#393e46', fg='#eeeeee')
        data_de_nascimento = Entry(main_frame, font=('Helvetica', 14), borderwidth=3)

        # Login
        label_login = Label(main_frame, text='Login -', font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')
        login = Entry(main_frame, font=('Helvetica', 14), borderwidth=3)

        # Senha
        label_password = Label(main_frame, text='Senha -', font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')
        password = Entry(main_frame, font=('Helvetica', 14), borderwidth=3)

        # Criar Conta
        criar_conta = Button(main_frame, text='Criar Conta', width=25, font=('Helvetica', 14), bg='#00adb5',
                             fg='#eeeeee', borderwidth=3, command=account_creation)

        # Voltar
        voltar = Button(main_frame, text='Voltar', width=25, font=('Helvetica', 14), bg='#222831', fg='#eeeeee',
                        borderwidth=3, command=reset)

        # Putting it onto the screen
        system_state.pack(pady=50)
        main_frame.pack()

        label_name.grid(row=0, column=0, padx=10, pady=15)
        name.grid(row=0, column=1, padx=15, pady=15)

        label_cpf.grid(row=1, column=0, padx=10, pady=15)
        cpf.grid(row=1, column=1, padx=15, pady=15)

        label_data_de_nascimento.grid(row=2, column=0, padx=10, pady=15)
        data_de_nascimento.grid(row=2, column=1, padx=15, pady=15)

        label_login.grid(row=3, column=0, padx=10, pady=15)
        login.grid(row=3, column=1, padx=15, pady=15)

        label_password.grid(row=4, column=0, padx=10, pady=15)
        password.grid(row=4, column=1, padx=15, pady=15)

        criar_conta.grid(row=5, column=0, padx=10, pady=15)
        voltar.grid(row=5, column=1, padx=10, pady=15)
