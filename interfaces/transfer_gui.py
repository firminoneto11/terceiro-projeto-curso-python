from tkinter import *
from interfaces.functions import centralize, get_current_balance, get_account_numbers
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
        self.transfer_gui['bg'] = '#393e46'
        self.transfer_gui.resizable(False, False)
        self.transfer_gui.title("Transferir")
        centralize(width=900, height=500, element=self.transfer_gui)

        # State of the system
        self.state_label = Label(self.transfer_gui, text='Transferir', bg='#393e46', fg='#eeeeee',
                                 font=('Helvetica', 24))

        # Main frame
        self.main_frame = LabelFrame(self.transfer_gui, text='Dados da transferência', fg='#00adb5', bg='#393e46',
                                     font=('Helvetica', 14))

        # Data
        self.transfer_amount_label = Label(self.main_frame, text='Insira o valor que deseja transferir - ',
                                           font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')
        self.transfer_amount = Entry(self.main_frame, font=('Helvetica', 14), borderwidth=3)

        self.destiny_account_label = Label(self.main_frame, text='Insira o número da conta de destino - ',
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

        self.transfer_amount_label.grid(row=0, column=0, pady=10)
        self.transfer_amount.grid(row=0, column=1, pady=10)
        self.destiny_account_label.grid(row=1, column=0, pady=10)
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
            error = messagebox.showerror('Campos vazios', 'Há campos vazios!')
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
            error = messagebox.showerror('Dados inválidos', 'Os dados que você informou são inválidos. Verifique a '
                                                            'conta de destino e a quantia desejada para transferência.')
            if error == 'ok':
                self.transfer_gui.destroy()
                return None

        # Checking if the destiny account typed exists
        account_numbers = get_account_numbers()
        if destiny_account not in account_numbers:
            self.transfer_amount.delete(0, END)
            self.destiny_account.delete(0, END)
            error = messagebox.showerror('Conta destino não existe', 'A conta destino informada não se encontra '
                                                                     'cadastrada no sistema.')
            if error == 'ok':
                self.transfer_gui.destroy()
                return None
        # Checking if the destiny account typed isn't the same from the user
        elif destiny_account == self.current_account:
            self.transfer_amount.delete(0, END)
            self.destiny_account.delete(0, END)
            error = messagebox.showerror('Conta destino inválida', 'A conta destino não pode ser a mesma conta atual.')
            if error == 'ok':
                self.transfer_gui.destroy()
                return None
        else:
            print('poggiers')
