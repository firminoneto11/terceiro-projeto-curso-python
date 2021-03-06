from tkinter import *
from interfaces.functions import centralize, get_current_balance, get_account_numbers, db_transfer_update
from tkinter import messagebox


class TransferGUI:

    def __init__(self, frame, label, current_account):
        """
        This __init__ method initializes the sub window for the transfer area.
        :param frame: This is the self.buttons_frame from GUISession class. It's going to be used to update the new
        balance after a successfully transfer.
        :param label: This is the self.buttons_frame from GUISession class. It's going to be used to update the new
        balance after a successfully transfer.
        :param current_account: This is the current account from session_data.csv. It's going to be used to prevent the
        user from transferring to itself.
        """
        # Saving frame and label in order to update them after the transfer
        self.frame = frame
        self.label = label
        self.current_account = int(current_account)

        # Creating another window for the 'transfer' section
        self.transfer_gui = Toplevel()
        self.transfer_gui.configure(background='#393e46')
        self.transfer_gui.iconbitmap(r'.\valware.ico')
        self.transfer_gui.resizable(False, False)
        self.transfer_gui.title("Transferir")
        centralize(width=900, height=500, element=self.transfer_gui)

        # State of the system
        self.state_label = Label(self.transfer_gui, text='Transferir', bg='#393e46', fg='#eeeeee',
                                 font=('Helvetica', 24))

        # Main frame
        self.main_frame = LabelFrame(self.transfer_gui, text='Dados da transferĂȘncia', fg='#00adb5', bg='#393e46',
                                     font=('Helvetica', 14))

        # Data
        self.transfer_amount_label = Label(self.main_frame, text='Insira o valor que deseja transferir - ',
                                           font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')
        self.transfer_amount = Entry(self.main_frame, font=('Helvetica', 14), borderwidth=3)

        self.destiny_account_label = Label(self.main_frame, text='Insira o nĂșmero da conta de destino - ',
                                           font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')
        self.destiny_account = Entry(self.main_frame, font=('Helvetica', 14), borderwidth=3)

        # Buttons
        self.transfer_button = Button(self.main_frame, text="Transferir", width=20, font=('Helvetica', 14),
                                      bg='#00adb5', fg='#eeeeee', borderwidth=3, command=self.__transferring)
        self.cancel_button = Button(self.main_frame, text="Cancelar", width=20, font=('Helvetica', 14), bg='#222831',
                                    fg='#eeeeee', borderwidth=3, command=self.transfer_gui.destroy)

        # Inserting the elements onto the screen
        self.state_label.pack(pady=50)
        self.main_frame.pack()

        self.transfer_amount_label.grid(row=0, column=0, pady=10, sticky=E)
        self.transfer_amount.grid(row=0, column=1, pady=10)
        self.destiny_account_label.grid(row=1, column=0, pady=10, sticky=E)
        self.destiny_account.grid(row=1, column=1, pady=10)

        self.transfer_button.grid(row=2, column=0, padx=10, pady=50)
        self.cancel_button.grid(row=2, column=1, padx=10, pady=50)

    def __transferring(self):
        """
        This method does the whole transfer logic into the current client's session.
        :return: None
        """
        # Storing the gathered data into a variable
        transfer_amount = self.transfer_amount.get()
        destiny_account = self.destiny_account.get()

        # Collecting the current balance
        current_balance = get_current_balance()

        # Checking if the transfer amount and destiny account are valid
        if len(transfer_amount) == 0 or len(destiny_account) == 0:
            self.transfer_amount.delete(0, END)
            self.destiny_account.delete(0, END)
            error = messagebox.showerror('Campos vazios', 'HĂĄ campos vazios!')
            if error == 'ok':
                self.transfer_gui.destroy()
                return None
        elif ',' in transfer_amount:
            transfer_amount = transfer_amount.replace(',', '.')

        # Checking the inserted values
        try:
            transfer_amount = float(transfer_amount)
            destiny_account = int(destiny_account)

        # Taking care of possible exceptions
        except (ValueError, TypeError, Exception):
            self.transfer_amount.delete(0, END)
            self.destiny_account.delete(0, END)
            error = messagebox.showerror('Dados invĂĄlidos', 'Os dados que vocĂȘ informou sĂŁo invĂĄlidos. Verifique a '
                                                            'conta de destino e a quantia desejada para transferĂȘncia.')
            if error == 'ok':
                self.transfer_gui.destroy()
                return None

        # Checking if the destiny account typed exists
        account_numbers = get_account_numbers()
        if destiny_account not in account_numbers:
            self.transfer_amount.delete(0, END)
            self.destiny_account.delete(0, END)
            error = messagebox.showerror('Conta destino nĂŁo existe', 'A conta destino informada nĂŁo se encontra '
                                                                     'cadastrada no sistema.')
            if error == 'ok':
                self.transfer_gui.destroy()
                return None
        # Checking if the destiny account typed isn't the same from the user
        elif destiny_account == self.current_account:
            self.transfer_amount.delete(0, END)
            self.destiny_account.delete(0, END)
            error = messagebox.showerror('Conta destino invĂĄlida', 'A conta destino nĂŁo pode ser a mesma conta atual.')
            if error == 'ok':
                self.transfer_gui.destroy()
                return None

        # Validating the transfer amount that is going to be subtracted from the current balance
        user_new_balance = round((current_balance - transfer_amount), 2)
        if user_new_balance < 0:
            self.transfer_amount.delete(0, END)
            self.destiny_account.delete(0, END)
            error = messagebox.showerror("Saldo insuficiente", "O valor informado para a transferĂȘncia Ă© insuficiente, "
                                                               "pois o seu saldo atual Ă© menor do que a quantia a ser "
                                                               "transferida.")
            if error == 'ok':
                self.transfer_gui.destroy()
                return None

        # This part will only be executed if all the previous checks weren't activated
        else:
            # Cleaning the typed data from the input entry
            self.transfer_amount.delete(0, END)
            self.destiny_account.delete(0, END)

            # Before updating stuff, i need to get a confirmation from the user
            response = messagebox.askyesno('Confirmar transferĂȘncia', f'Deseja efetuar a transferĂȘncia no valor de '
                                                                      f'R${transfer_amount} para a conta de '
                                                                      f'nĂșmero {destiny_account}?')

            # If response is 'Yes' or True
            if response:
                # Updating the current balance in the session_gui class
                self.__update_balance_after_transfer(balance=user_new_balance)

                # Executing the function that updates the clients.csv and session_data.csv files, doing the transferring
                db_transfer_update(user_new_balance=user_new_balance, transfer_amount=transfer_amount,
                                   destiny_account=destiny_account)

                # Informing to the user that its deposit has been successfully made
                success = messagebox.showinfo("TransferĂȘncia feita com sucesso", f"ParabĂ©ns! Sua transferĂȘncia no "
                                                                                 f"valor de R${transfer_amount} foi "
                                                                                 f"efetuada com sucesso para a conta "
                                                                                 f"de nĂșmero {destiny_account}. Seu "
                                                                                 f"novo saldo Ă© de "
                                                                                 f"R${user_new_balance}.")
                if success == 'ok':
                    self.transfer_gui.destroy()
                    return None

            # If response is 'No' or False
            else:
                self.transfer_gui.destroy()
                return None

    def __update_balance_after_transfer(self, balance):
        """
        This method updates the balance label from the GUISession class that was previously passed to the __init__
        method. It will only be called after a successfully transfer.
        :param balance: The new overall balance from the user. Previous balance minus the transfer amount.
        :return: None
        """
        self.label.destroy()
        self.label = Label(self.frame, text=f"Saldo - R${balance}", font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')
        self.label.grid(row=1, column=0, pady=10)
