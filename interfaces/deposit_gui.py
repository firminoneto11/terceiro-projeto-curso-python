from tkinter import *
from interfaces.functions import centralize
from tkinter import messagebox
from interfaces.functions import update_session_data_csv, update_clients_csv, get_current_balance


class DepositGUI:

    def __init__(self, frame, label):
        """
        This __init__ method initializes the sub window for the deposit area.
        :param frame: This is the self.buttons_frame from GUISession class. It's going to be used to update the new
        balance after a successfully deposit.
        :param label: This is the self.balance_label from GUISession class. It's going to be used to update the new
        balance after a successfully deposit.
        """
        # Saving frame and label in order to update them after the deposit
        self.frame = frame
        self.label = label
        # Creating another window for the 'depositar' section
        self.gui_depositar = Toplevel()
        self.gui_depositar['bg'] = '#393e46'
        self.gui_depositar.resizable(False, False)
        self.gui_depositar.title("Depositar")
        centralize(width=900, height=500, element=self.gui_depositar)

        # State of the system
        self.state_label = Label(self.gui_depositar, text='Depositar', bg='#393e46', fg='#eeeeee',
                                 font=('Helvetica', 24))

        # Main frame
        self.main_frame = LabelFrame(self.gui_depositar, text='Dados do depósito', fg='#00adb5', bg='#393e46',
                                     font=('Helvetica', 14))

        # Data
        self.deposit_amount_label = Label(self.main_frame, text='Insira o valor do depósito - ', font=('Helvetica', 14),
                                          bg='#393e46', fg='#eeeeee')
        self.deposit_amount = Entry(self.main_frame, font=('Helvetica', 14), borderwidth=3)

        # Buttons
        self.deposit_button = Button(self.main_frame, text="Depositar", width=20, font=('Helvetica', 14), bg='#00adb5',
                                     fg='#eeeeee', borderwidth=3, command=self.__depositing)
        self.cancel_button = Button(self.main_frame, text="Cancelar", width=20, font=('Helvetica', 14), bg='#222831',
                                    fg='#eeeeee', borderwidth=3, command=self.gui_depositar.destroy)

        # Inserting the elements onto the screen
        self.state_label.pack(pady=50)
        self.main_frame.pack()

        self.deposit_amount_label.grid(row=0, column=0, pady=10)
        self.deposit_amount.grid(row=0, column=1, pady=10)

        self.deposit_button.grid(row=1, column=0, padx=10, pady=50)
        self.cancel_button.grid(row=1, column=1, padx=10, pady=50)

    def __depositing(self):
        """
        This method does the whole deposit logic into the current client's session.
        :return: None
        """
        # Storing the gathered data into a variable
        new_balance = self.deposit_amount.get()

        # Collecting the current balance
        current_balance = get_current_balance()

        # Checking if the deposit amount is valid
        if len(new_balance) == 0:
            self.deposit_amount.delete(0, END)
            error = messagebox.showerror("Campo vazio", "O valor para o depósito está vazio!")
            if error == 'ok':
                self.gui_depositar.destroy()
                return None
        elif ',' in new_balance:
            new_balance = new_balance.replace(',', '.')
        try:
            # Checking inserted values
            new_balance = float(new_balance)
        except ValueError:
            # Taking care of possible exceptions
            self.deposit_amount.delete(0, END)
            error = messagebox.showerror("Valor inválido", "O valor informado para depósito é inválido. Insira apenas "
                                                           "os dígitos/números do depósito.")
            if error == 'ok':
                self.gui_depositar.destroy()
                return None
        else:
            # Cleaning the typed data from the input entry
            self.deposit_amount.delete(0, END)
            # Before updating stuff, i need to get a confirmation from the user
            response = messagebox.askyesno("Confirmar depósito", f"Deseja efeutar o depósito no valor de "
                                                                 f"R${new_balance} na sua conta?")
            # If response is 'Yes' or True
            if response:
                # Adding the old amount with the new deposit
                current_balance = round((current_balance + new_balance), 2)

                # Updating the current balance in the session_gui class
                self.__update_balance_after_deposit(balance=current_balance)

                # Updating session_data.csv and clients.csv
                updated_data = update_session_data_csv(new_balance=current_balance)
                update_clients_csv(updated_data=updated_data)

                # Informing to the user that its deposit has been successfully made
                success = messagebox.showinfo("Depósito feito com sucesso", f"Parabéns! Seu depósito foi efetuado com "
                                                                            f"sucesso no valor de R$ {new_balance}. "
                                                                            f"Seu novo saldo é de R${current_balance}.")
                if success == 'ok':
                    self.gui_depositar.destroy()
                    return None

            # If response is 'No' or False
            else:
                self.gui_depositar.destroy()
                return None

    def __update_balance_after_deposit(self, balance):
        """
        This method updates the balance label from the GUISession class that was previously passed to the __init__
        method. It will only be called after a successfully deposit.
        :param balance: The new overall balance from the user. Previous balance plus the deposit.
        :return: None
        """
        self.label = Label(self.frame, text=f"Saldo - R${balance}", font=('Helvetica', 14),
                           bg='#393e46', fg='#eeeeee')
        self.label.grid(row=1, column=0, pady=10)
