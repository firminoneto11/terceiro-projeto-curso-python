from tkinter import *
from interfaces.functions import centralize
from csv import DictReader
from tkinter import messagebox
from interfaces.functions import update_session_data, update_clients

SESSION_DATA = r".\bank_databases\session_data.csv"
HEADER = "Número da conta", "Saldo", "Nome", "CPF", "Data de nascimento", "Login", "Senha"


class DepositarGUI:

    def __init__(self):
        # Creating another window for the 'depositar' section
        gui_depositar = Toplevel()
        gui_depositar['bg'] = '#393e46'
        gui_depositar.resizable(False, False)
        gui_depositar.title("Depositar")
        centralize(width=900, height=500, element=gui_depositar)

        # State of the system
        self.state_label = Label(gui_depositar, text='Depositar', bg='#393e46', fg='#eeeeee', font=('Helvetica', 24))

        # Main frame
        self.main_frame = LabelFrame(gui_depositar, text='Dados do depósito', fg='#00adb5', bg='#393e46',
                                     font=('Helvetica', 14))

        # Data
        self.deposit_amount_label = Label(self.main_frame, text='Insira o valor do depósito - ', font=('Helvetica', 14),
                                          bg='#393e46', fg='#eeeeee')
        self.deposit_amount = Entry(self.main_frame, font=('Helvetica', 14), borderwidth=3)

        # Buttons
        self.deposit_button = Button(self.main_frame, text="Depositar", width=20, font=('Helvetica', 14), bg='#00adb5',
                                     fg='#eeeeee', borderwidth=3, command=self.depositing)
        self.cancel_button = Button(self.main_frame, text="Cancelar", width=20, font=('Helvetica', 14), bg='#222831',
                                    fg='#eeeeee', borderwidth=3, command=gui_depositar.destroy)

        # Inserting the elements onto the screen
        self.state_label.pack(pady=50)
        self.main_frame.pack()

        self.deposit_amount_label.grid(row=0, column=0, pady=10)
        self.deposit_amount.grid(row=0, column=1, pady=10)

        self.deposit_button.grid(row=1, column=0, padx=10, pady=50)
        self.cancel_button.grid(row=1, column=1, padx=10, pady=50)

    def depositing(self):
        # Storing the gathered data into a variable
        data = self.deposit_amount.get()

        # Collecting the current balance
        with open(SESSION_DATA, mode='r', newline='', encoding='utf-8') as file:
            archive = DictReader(f=file, fieldnames=HEADER)
            next(archive)
            for client in archive:
                current_balance = client["Saldo"]
                break

        # Checking if the deposit amount is valid
        if len(data) == 0:
            self.deposit_amount.delete(0, END)
            messagebox.showerror("Campo vazio", "O campo de entrada está vazio!")
            return None
        elif ',' in data:
            data = data.replace(',', '.')
        try:
            # Checking inserted values
            data = float(data)
        except ValueError:
            # Taking care of possible exceptions
            self.deposit_amount.delete(0, END)
            messagebox.showerror("Valor inválido", "O valor informado para depósito é inválido. Insira apenas os "
                                                   "dígitos do depósito.")
            return None
        else:
            # Before updating stuff, i need to get a confirmation from the user
            response = messagebox.askyesno("Confirmar depósito", f"Deseja efeutar o depósito no valor de R${data} na "
                                                                 f"sua conta?")
            # If response is 'Yes' or True
            if response:
                # Casting to float the old amount and adding it to the new deposit
                current_balance = current_balance.replace("R$", '')
                current_balance = round((float(current_balance) + data), 2)
                # Updating session_data.csv
                update_session_data(new_balance=current_balance)
                # Updating clients.csv
                update_clients(new_balance=current_balance)
            # If response is 'No' or False
            else:
                print("Depósito não confirmado!")
                return None
