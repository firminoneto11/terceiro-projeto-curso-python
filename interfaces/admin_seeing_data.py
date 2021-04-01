from tkinter import *
from interfaces.functions import centralize
from csv import DictReader


class AdminSeeDataGUI:

    def __get_data(self):
        """
        This method gets the data from the selected account number in the previous GUI (listbox).
        :return: A dictionary containing the whole data from the selected account.
        """
        database = r'.\bank_databases\clients.csv'
        header = "Número da conta", "Saldo", "Nome", "CPF", "Data de nascimento", "Login", "Senha"
        with open(database, mode='r', newline='', encoding='utf-8') as archive:
            file = DictReader(f=archive, fieldnames=header)
            for dictionary in file:
                if dictionary['Número da conta'] == self.account_selected:
                    return dictionary

    def __init__(self, account_selected):
        """
        This __init__ method initializes the GUI for the data visualization for the admin, after selecting one account
        in the listbox to do so.
        :param account_selected: A account selected in the previous GUI
        """
        # Saving the account number into an attribute
        self.account_selected = account_selected

        # Starting out the GUI for the data visualization
        self.admin_see_data_window = Toplevel()
        self.admin_see_data_window.configure(background='#393e46')
        self.admin_see_data_window.iconbitmap(r'.\valware.ico')
        self.admin_see_data_window.resizable(False, False)
        self.admin_see_data_window.title("Dados do cliente")
        centralize(width=1000, height=700, element=self.admin_see_data_window)

        # Executing the __get_data method and storing it into a variable
        self.client_data = self.__get_data()

        # State of the system frame and data frame creation
        self.state_label = Label(self.admin_see_data_window, text='Dados do cliente', bg='#393e46', fg='#eeeeee',
                                 font=('Helvetica', 24))
        self.data_frame = LabelFrame(self.admin_see_data_window, bg='#393e46', text='Dados', fg='#00adb5',
                                     font=('Helvetica', 14))

        # Showing all the users info
        self.account_number_label = Label(self.data_frame,
                                          text=f"Número da conta - {self.client_data['Número da conta']}",
                                          font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')

        self.balance_label = Label(self.data_frame, text=f"Saldo - {self.client_data['Saldo']}", font=('Helvetica', 14),
                                   bg='#393e46', fg='#eeeeee')

        self.name_label = Label(self.data_frame, text=f"Nome - {self.client_data['Nome']}", font=('Helvetica', 14),
                                bg='#393e46', fg='#eeeeee')

        self.cpf_label = Label(self.data_frame, text=f"CPF - {self.client_data['CPF']}", font=('Helvetica', 14),
                               bg='#393e46', fg='#eeeeee')

        self.birth_date_label = Label(self.data_frame, text=f"Data de nascimento - "
                                                            f"{self.client_data['Data de nascimento']}",
                                      font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')

        self.login_label = Label(self.data_frame, text=f"Login - {self.client_data['Login']}", font=('Helvetica', 14),
                                 bg='#393e46', fg='#eeeeee')

        self.password_label = Label(self.data_frame, text=f"Senha - {self.client_data['Senha']}",
                                    font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')

        # Creating a back button
        self.back_button = Button(self.admin_see_data_window, text="Voltar", width=20, font=('Helvetica', 14),
                                  bg='#222831', fg='#eeeeee', borderwidth=3, command=self.admin_see_data_window.destroy)

        #               Putting all the widgets created onto the screen
        self.state_label.pack(pady=50)
        self.data_frame.pack()

        self.account_number_label.grid(row=0, column=0, pady=10)
        self.balance_label.grid(row=1, column=0, pady=10)
        self.name_label.grid(row=2, column=0, pady=10)
        self.cpf_label.grid(row=3, column=0, pady=10)
        self.birth_date_label.grid(row=4, column=0, pady=10)
        self.login_label.grid(row=5, column=0, pady=10)
        self.password_label.grid(row=6, column=0, pady=10)

        self.back_button.pack(pady=30)
