from bank_models.account_management import Client
from bank_models.session_data import check_session_file
from interfaces.session_gui import GUISession
from os.path import exists
from csv import DictReader, DictWriter
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
                              fg='#eeeeee', borderwidth=3, command=lambda: self.acessar_conta(root))
        self.button2 = Button(root, text='Criar Conta', width=25, font=('Helvetica', 14), bg='#222831', fg='#eeeeee',
                              borderwidth=3, command=lambda: self.criar_conta(root))
        self.button3 = Button(root, text='Administrador', width=25, font=('Helvetica', 14), bg='#222831', fg='#eeeeee',
                              borderwidth=3)
        self.button4 = Button(root, text='Sair', width=25, font=('Helvetica', 14), bg='#222831', fg='#eeeeee',
                              borderwidth=3, command=root.quit)
        self.label1 = Label(root, text='Escolha uma das opções abaixo', font=('Helvetica', 20), bg='#393e46',
                            fg='#eeeeee')

        self.label1.grid(row=0, column=0, pady=250, columnspan=3)
        self.button1.grid(row=1, column=0, padx=55)
        self.button2.grid(row=1, column=1, padx=55)
        self.button3.grid(row=1, column=2, padx=55)
        self.button4.grid(row=2, column=1, padx=55, pady=50)

    def acessar_conta(self, root):
        """
        This method creates the UI for the 'entrar na conta' option selected in the main menu. First, it destroys all
        the old content from the screen, and then creates and render a new UI with the elements needed to access the
        account.
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

        def entering_account():
            """
            This function access the account created before and verifies the given data to do so. If a entry label has
            a unexpected data type, it pops up a warning accordingly to the mistake.
            :return: None
            """
            # Gathering the data
            gathered_data = account_number.get(), login.get(), password.get()

            # Checking the data. This is a long process in order to ensure the data integrity of account creation. If
            # some of the data is not expected, a pop-up will be shown

            # Checking for blank entries
            for data in gathered_data:
                if len(data) == 0:
                    account_number.delete(0, END)
                    login.delete(0, END)
                    password.delete(0, END)
                    messagebox.showerror("Dados inválidos!", "Existem campos vazios!")
                    return None

            # Checking if there is any register
            if exists(Client.DB) is False:
                account_number.delete(0, END)
                login.delete(0, END)
                password.delete(0, END)
                messagebox.showinfo("Não há contas cadastradas", "Não há contas cadastradas no sistema no momento.")
                return None

            # Checking if the 'account number' is valid
            with open(Client.DB, mode='r') as archive:
                account_numbers = []
                file = DictReader(f=archive, fieldnames=Client.HEADER)
                for client in file:
                    account_numbers.append(client["Número da conta"])
                if gathered_data[0] not in account_numbers:
                    account_number.delete(0, END)
                    login.delete(0, END)
                    password.delete(0, END)
                    messagebox.showerror("Número da conta inválido", "O número da conta informado é inválido! Não há"
                                                                     " registro do mesmo no sistema")
                    return None

            # Verifying if login and password for the account number are valid
            with open(Client.DB, mode='r') as archive:
                file = DictReader(f=archive, fieldnames=Client.HEADER)
                for client in file:
                    if client["Número da conta"] == gathered_data[0]:
                        if client["Login"] != gathered_data[1] or client["Senha"] != gathered_data[2]:
                            account_number.delete(0, END)
                            login.delete(0, END)
                            password.delete(0, END)
                            messagebox.showerror("Login ou senha incorretos", "O login ou senha informados são incorre"
                                                                              "tos.")
                            return None
                        else:
                            # This will be executed only if it passes on all the previous exams
                            check_session_file()
                            session_data = r".\bank_databases\session_data.csv"
                            with open(session_data, mode='w', newline="", encoding="utf-8") as archive_two:
                                document = DictWriter(f=archive_two, fieldnames=Client.HEADER)
                                document.writeheader()
                                document.writerow({
                                    "Número da conta": client["Número da conta"],
                                    "Saldo": client["Saldo"],
                                    "Nome": client["Nome"],
                                    "CPF": client["CPF"],
                                    "Data de nascimento": client["Data de nascimento"],
                                    "Login": client["Login"],
                                    "Senha": client["Senha"]
                                })
                            break
            account_number.delete(0, END)
            login.delete(0, END)
            password.delete(0, END)
            main_frame.destroy()
            system_state.destroy()

            # This class will be executed while the user is within the session
            GUISession(root=root, main_window=self)

        # Getting rid of the old Widgets
        self.label1.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()

        #                       Creating the new GUI
        system_state = Label(root, bg='#393e46', text='Acessar Conta', fg='#eeeeee', font=('Helvetica', 24))
        main_frame = LabelFrame(root, bg='#393e46')

        # Account number
        account_number_label = Label(main_frame, text='Número da conta -', font=('Helvetica', 14), bg='#393e46',
                                     fg='#eeeeee')
        account_number = Entry(main_frame, font=('Helvetica', 14), borderwidth=3)

        # Login
        login_label = Label(main_frame, text='Login -', font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')
        login = Entry(main_frame, font=('Helvetica', 14), borderwidth=3)

        # Password
        password_label = Label(main_frame, text='Senha -', font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')
        password = Entry(main_frame, font=('Helvetica', 14), borderwidth=3)

        # Accessing account
        access_account = Button(main_frame, text='Acessar Conta', width=25, font=('Helvetica', 14), bg='#00adb5',
                                fg='#eeeeee', borderwidth=3, command=entering_account)

        # Back
        back = Button(main_frame, text='Voltar', width=25, font=('Helvetica', 14), bg='#222831', fg='#eeeeee',
                      borderwidth=3, command=reset)

        # Putting it onto the screen
        system_state.pack(pady=50)
        main_frame.pack()

        account_number_label.grid(row=0, column=0, padx=10, pady=15)
        account_number.grid(row=0, column=1, padx=15, pady=15)

        login_label.grid(row=1, column=0, padx=10, pady=15)
        login.grid(row=1, column=1, padx=15, pady=15)

        password_label.grid(row=2, column=0, padx=10, pady=15)
        password.grid(row=2, column=1, padx=15, pady=15)

        access_account.grid(row=3, column=0, padx=15, pady=15)
        back.grid(row=3, column=1, padx=15, pady=15)

    def criar_conta(self, root):
        """
        This method creates the UI for the 'criar conta' option selected in the main menu. First, it destroys all the
        old content from the screen, and then creates and render a new UI with the elements needed to create an account.
        :param root: The main window element.
        :return: None
        """
        # Checking for the existence of the database and creating it in case it doesn't exists
        Client.check_db_and_dir()

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
            This function creates the 'Client' instance and verifies the necessary data to do so. If a entry label has
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
                messagebox.showerror("CPF inválido", "O CPF informado é inválido. Insira apenas os 11 dígitos do CPF.")
                return None
            for number in gathered_data[1]:
                if number not in numbers:
                    name.delete(0, END)
                    cpf.delete(0, END)
                    data_de_nascimento.delete(0, END)
                    login.delete(0, END)
                    password.delete(0, END)
                    messagebox.showerror("CPF inválido", "O CPF informado é inválido. Insira apenas os 11 dígitos do"
                                                         " CPF.")
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
                # Checking if the user is not under 18 years old
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
                    # Checking if the user is not already registered in the system
                    with open(Client.DB, mode='r') as archive:
                        archive_reader = DictReader(f=archive, fieldnames=Client.HEADER)
                        for client in archive_reader:
                            if client["CPF"] == gathered_data[1]:
                                name.delete(0, END)
                                cpf.delete(0, END)
                                data_de_nascimento.delete(0, END)
                                login.delete(0, END)
                                password.delete(0, END)
                                messagebox.showinfo("Conta já cadastrada", "O CPF informado já se encontra cadastrado "
                                                                           "no sistema.")
                                return None
                    # This will be executed only if it passes on all the previous exams
                    final_data = {
                        "Nome": name.get().strip().title(),
                        "CPF": cpf.get(),
                        "Data de nascimento": date,
                        "Login": login.get(),
                        "Senha": password.get()
                    }
                    # Creating the instance of 'Client' and saving it into the database
                    new_client = Client(
                        name=final_data["Nome"],
                        cpf=final_data["CPF"],
                        birth_date=final_data["Data de nascimento"],
                        login=final_data["Login"],
                        password=final_data["Senha"]
                    )
                    # Removing the typed data from the screen and show a success message to the user
                    name.delete(0, END)
                    cpf.delete(0, END)
                    data_de_nascimento.delete(0, END)
                    login.delete(0, END)
                    password.delete(0, END)
                    messagebox.showinfo("Conta criada", f"Sua conta foi criada com sucesso! O número da sua conta é "
                                                        f"{new_client.account_number}")
                    return None

        # Getting rid of the old widgets
        self.label1.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()

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

        # Create Account
        criar_conta = Button(main_frame, text='Criar Conta', width=25, font=('Helvetica', 14), bg='#00adb5',
                             fg='#eeeeee', borderwidth=3, command=account_creation)

        # Back
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
