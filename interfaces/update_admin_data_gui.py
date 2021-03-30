from tkinter import *
from interfaces.functions import centralize
from tkinter import messagebox
from bank_models.admin_access import AdminAccess


class UpdateAdminDataGUI:

    def __init__(self):
        """
        This __init__ method initializes the sub window for the update login | password area.
        """
        # Creating a new window for the changes
        self.update_window = Toplevel()
        self.update_window.configure(background='#393e46')
        self.update_window.iconbitmap(r'.\assets\valware.ico')
        self.update_window.resizable(False, False)
        self.update_window.title("Trocar Login e Senha")
        centralize(width=900, height=500, element=self.update_window)

        # State of the system
        self.state_label = Label(self.update_window, text='Trocar Login e Senha', bg='#393e46', fg='#eeeeee',
                                 font=('Helvetica', 24))

        # Main frame
        self.main_frame = LabelFrame(self.update_window, text='Dados da atualização', fg='#00adb5', bg='#393e46',
                                     font=('Helvetica', 14))

        # Data
        self.login_label = Label(self.main_frame, text='Insira o novo login - ', font=('Helvetica', 14), bg='#393e46',
                                 fg='#eeeeee')
        self.new_login = Entry(self.main_frame, font=('Helvetica', 14), borderwidth=3)

        self.password_label = Label(self.main_frame, text='Insira a nova senha - ', font=('Helvetica', 14),
                                    bg='#393e46', fg='#eeeeee')
        self.new_password = Entry(self.main_frame, font=('Helvetica', 14), borderwidth=3)

        # Buttons
        self.update_button = Button(self.main_frame, text="Atualizar dados", width=20, font=('Helvetica', 14),
                                    bg='#00adb5', fg='#eeeeee', borderwidth=3, command=self.__update_admin_data)
        self.cancel_button = Button(self.main_frame, text="Cancelar", width=20, font=('Helvetica', 14), bg='#222831',
                                    fg='#eeeeee', borderwidth=3, command=self.update_window.destroy)

        # Inserting the elements onto the screen
        self.state_label.pack(pady=50)
        self.main_frame.pack()

        self.login_label.grid(row=0, column=0, pady=10, sticky=E)
        self.new_login.grid(row=0, column=1, pady=10)
        self.password_label.grid(row=1, column=0, pady=10, sticky=E)
        self.new_password.grid(row=1, column=1, pady=10)

        self.update_button.grid(row=2, column=0, padx=10, pady=50)
        self.cancel_button.grid(row=2, column=1, padx=10, pady=50)

    def __update_admin_data(self):
        """
        This method updates the user admin data in the pickle file.
        :return: None
        """
        # Getting the data inputted from the user
        new_login, new_password = self.new_login.get(), self.new_password.get()

        # Checking if one of the fields are empty
        if len(new_login) == 0 or len(new_password) == 0:
            error = messagebox.showerror('Campos vazios', 'Os campos de login ou senha se encontram vazios.')
            if error == 'ok':
                self.new_login.delete(0, END)
                self.new_password.delete(0, END)
                self.update_window.destroy()
                return None

        # Asking the user is sure of doing the changes
        self.new_login.delete(0, END)
        self.new_password.delete(0, END)
        response = messagebox.askyesno('Confirmar mudanças', 'Você tem certeza que deseja alterar o login e senha?')

        # If the user says 'yes' | True
        if response:
            # Updating the admin_data.pickle with the provided data
            current_admin = AdminAccess()
            current_admin.login = new_login
            current_admin.password = new_password

            # Showing the user that the change is complete
            completion = messagebox.showinfo('Mudanças efetuadas com sucesso', 'Seu login e senha foram alterados com '
                                                                               'sucesso.')
            if completion == 'ok':
                self.update_window.destroy()
                return None
        # If the user says 'no' | False
        else:
            # Closing the window
            self.update_window.destroy()
            return None
