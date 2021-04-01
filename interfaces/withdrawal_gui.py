from tkinter import *
from interfaces.functions import centralize
from tkinter import messagebox
from interfaces.functions import update_session_data_csv, update_clients_csv, get_current_balance


class WithdrawalGUI:

    def __init__(self, frame, label):
        """
        This __init__ method initializes the sub window for the withdrawal area.
        :param frame: This is the self.buttons_frame from GUISession class. It's going to be used to update the new
        balance after a successfully withdrawal.
        :param label: This is the self.buttons_frame from GUISession class. It's going to be used to update the new
        balance after a successfully withdrawal.
        """
        # Saving frame and label in order to update them after the withdrawal
        self.frame = frame
        self.label = label

        # Creating another window for the 'withdrawal' section
        self.withdrawal_gui = Toplevel()
        self.withdrawal_gui.configure(background='#393e46')
        self.withdrawal_gui.iconbitmap(r'.\valware.ico')
        self.withdrawal_gui.resizable(False, False)
        self.withdrawal_gui.title("Saque")
        centralize(width=900, height=500, element=self.withdrawal_gui)

        # State of the system
        self.state_label = Label(self.withdrawal_gui, text='Sacar', bg='#393e46', fg='#eeeeee',
                                 font=('Helvetica', 24))

        # Main frame
        self.main_frame = LabelFrame(self.withdrawal_gui, text='Dados do saque', fg='#00adb5', bg='#393e46',
                                     font=('Helvetica', 14))

        # Data
        self.withdrawal_amount_label = Label(self.main_frame, text='Insira o valor do saque - ',
                                             font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')
        self.withdrawal_amount = Entry(self.main_frame, font=('Helvetica', 14), borderwidth=3)

        # Buttons
        self.withdrawal_button = Button(self.main_frame, text="Sacar", width=20, font=('Helvetica', 14),
                                        bg='#00adb5', fg='#eeeeee', borderwidth=3, command=self.__withdrawing)
        self.cancel_button = Button(self.main_frame, text="Cancelar", width=20, font=('Helvetica', 14), bg='#222831',
                                    fg='#eeeeee', borderwidth=3, command=self.withdrawal_gui.destroy)

        # Inserting the elements onto the screen
        self.state_label.pack(pady=50)
        self.main_frame.pack()

        self.withdrawal_amount_label.grid(row=0, column=0, pady=10, sticky=E)
        self.withdrawal_amount.grid(row=0, column=1, pady=10)

        self.withdrawal_button.grid(row=1, column=0, padx=10, pady=50)
        self.cancel_button.grid(row=1, column=1, padx=10, pady=50)

    def __withdrawing(self):
        """
        This method does the whole withdrawal logic into the current client's session.
        :return: None
        """
        # Storing the gathered data into a variable
        withdrawal = self.withdrawal_amount.get()

        # Collecting the current balance
        current_balance = get_current_balance()

        # Checking if the withdrawal amount is valid
        if len(withdrawal) == 0:
            self.withdrawal_amount.delete(0, END)
            error = messagebox.showerror("Campo vazio", "O valor para o saque está vazio!")
            if error == 'ok':
                self.withdrawal_gui.destroy()
                return None
        elif ',' in withdrawal:
            withdrawal = withdrawal.replace(',', '.')

        # Checking inserted values
        try:
            withdrawal = float(withdrawal)
        # Taking care of possible exceptions
        except ValueError:
            self.withdrawal_amount.delete(0, END)
            error = messagebox.showerror("Valor inválido", "O valor informado para saque é inválido. Insira apenas "
                                                           "os dígitos/números para o saque.")
            if error == 'ok':
                self.withdrawal_gui.destroy()
                return None

        # Validating the withdrawal amount that is going to be subtracted from the current balance.
        new_balance_amount = round((current_balance - withdrawal), 2)
        if new_balance_amount < 0:
            self.withdrawal_amount.delete(0, END)
            error = messagebox.showerror("Saldo insuficiente", "O valor informado para o saque é insuficiente, pois o "
                                                               "seu saldo atual é menor do que a quantia solicitada.")
            if error == 'ok':
                self.withdrawal_gui.destroy()
                return None

        # This part will only be executed if it passes all the previous verifications
        else:
            # Cleaning the typed data from the input entry
            self.withdrawal_amount.delete(0, END)

            # Before updating stuff, i need to get a confirmation from the user
            response = messagebox.askyesno("Confirmar saque", f"Deseja efetuar o saque no valor de R${withdrawal} "
                                                              f"da sua conta?")

            # If response is 'Yes' or True
            if response:
                # Updating the current balance in the session_gui class
                self.__update_balance_after_withdrawal(balance=new_balance_amount)

                # Updating session_data.csv and clients.csv
                updated_data = update_session_data_csv(new_balance=new_balance_amount)
                update_clients_csv(updated_data=updated_data)

                # Informing to the user that its deposit has been successfully made
                success = messagebox.showinfo("Saque feito com sucesso", f"Parabéns! Seu saque foi efetuado com "
                                                                         f"sucesso no valor de R${withdrawal}. "
                                                                         f"Seu novo saldo é de R${new_balance_amount}.")
                if success == 'ok':
                    self.withdrawal_gui.destroy()
                    return None

            # If response is 'No' or False
            else:
                self.withdrawal_gui.destroy()
                return None

    def __update_balance_after_withdrawal(self, balance):
        """
        This method updates the balance label from the GUISession class that was previously passed to the __init__
        method. It will only be called after a successfully withdrawal.
        :param balance: The new overall balance from the user. Previous balance minus the withdrawal.
        :return: None
        """
        self.label.destroy()
        self.label = Label(self.frame, text=f"Saldo - R${balance}", font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')
        self.label.grid(row=1, column=0, pady=10)
