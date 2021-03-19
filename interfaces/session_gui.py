from tkinter import *
from interfaces.depositar_gui import DepositarGUI
from csv import DictReader

SESSION_DATA = r".\bank_databases\session_data.csv"
HEADER = "Número da conta", "Saldo", "Nome", "CPF", "Data de nascimento", "Login", "Senha"


class GUISession:

    @staticmethod
    def get_data(information):
        with open(SESSION_DATA, mode='r', encoding='utf-8', newline='') as archive:
            file = DictReader(f=archive, fieldnames=HEADER)
            next(file)
            for client in file:
                if information == "Número da conta":
                    return client["Número da conta"]
                elif information == "Saldo":
                    return client["Saldo"]
                elif information == "Nome":
                    return client["Nome"]
                elif information == "CPF":
                    return client["CPF"]
                elif information == "Data de nascimento":
                    return client["Data de nascimento"]
                elif information == "Login":
                    return client["Login"]
                else:
                    return client["Senha"]

    def __init__(self, root, main_window):
        # State of the system, main frame and data frame creation
        self.state_label = Label(root, text='Suas informações', bg='#393e46', fg='#eeeeee', font=('Helvetica', 24))
        self.buttons_frame = LabelFrame(root, bg='#393e46')
        self.data_frame = LabelFrame(root, bg='#393e46', text='Seus dados', fg='#00adb5', font=('Helvetica', 14))

        # Showing all the users info
        self.account_number_label = Label(self.data_frame, text=f"Número da conta - {self.get_data('Número da conta')}",
                                          font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')

        self.balance_label = Label(self.data_frame, text=f"Saldo - {self.get_data('Saldo')}", font=('Helvetica', 14),
                                   bg='#393e46', fg='#eeeeee')

        self.name_label = Label(self.data_frame, text=f"Nome - {self.get_data('Nome')}", font=('Helvetica', 14),
                                bg='#393e46', fg='#eeeeee')

        self.cpf_label = Label(self.data_frame, text=f"CPF - {self.get_data('CPF')}", font=('Helvetica', 14),
                               bg='#393e46', fg='#eeeeee')

        self.birth_date_label = Label(self.data_frame, text=f"Data de nascimento - "
                                                            f"{self.get_data('Data de nascimento')}",
                                      font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')

        self.login_label = Label(self.data_frame, text=f"Login - {self.get_data('Login')}", font=('Helvetica', 14),
                                 bg='#393e46', fg='#eeeeee')

        self.password_label = Label(self.data_frame, text=f"Senha - {self.get_data('Senha')}", font=('Helvetica', 14),
                                    bg='#393e46', fg='#eeeeee')

        # Inserting the 'depositar' button
        self.deposit_button = Button(self.buttons_frame, text='Depositar', width=25, font=('Helvetica', 14),
                                     bg='#eeeeee', fg='#393e46', borderwidth=3, command=self.depositar)

        # Inserting the 'sacar' button
        self.withdrawal_button = Button(self.buttons_frame, text='Sacar', width=25, font=('Helvetica', 14),
                                        bg='#393e46', fg='#eeeeee', borderwidth=3)

        # Inserting the 'transferir' button
        self.transfer_button = Button(self.buttons_frame, text='Transferir', width=25, font=('Helvetica', 14),
                                      bg='#00adb5', fg='#eeeeee', borderwidth=3)

        # Inserting a back button in the session area
        self.back_button = Button(self.buttons_frame, text='Voltar ao menu inicial', width=25, font=('Helvetica', 14),
                                  bg='#222831', fg='#eeeeee', borderwidth=3,
                                  command=lambda: self.back(root=root, main_window=main_window))

        #               Putting all the widgets created onto the screen
        self.state_label.pack(pady=50)
        self.data_frame.pack()
        self.buttons_frame.pack(pady=25)

        # Data frame
        self.account_number_label.grid(row=0, column=0, pady=10)
        self.balance_label.grid(row=1, column=0, pady=10)
        self.name_label.grid(row=2, column=0, pady=10)
        self.cpf_label.grid(row=3, column=0, pady=10)
        self.birth_date_label.grid(row=4, column=0, pady=10)
        self.login_label.grid(row=5, column=0, pady=10)
        self.password_label.grid(row=6, column=0, pady=10)

        # Buttons Frame
        self.deposit_button.grid(row=0, column=0, padx=5)
        self.withdrawal_button.grid(row=0, column=1, padx=5)
        self.transfer_button.grid(row=0, column=2, padx=5)
        self.back_button.grid(row=0, column=3, padx=5)

    def back(self, root, main_window):
        """
        This function works like a 'back' button. Every time a button calls this function, it destroys every content
        from the current window and returns to the main window.
        :param root: Root window for the __init__ method to be executed.
        :param main_window: Main window object that has the __init__.
        :return: None
        """
        self.state_label.destroy()
        self.data_frame.destroy()
        self.buttons_frame.destroy()
        main_window.__init__(root)

    @staticmethod
    def depositar():
        DepositarGUI()
