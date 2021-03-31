from tkinter import *
from bank_models.catch_db_data import get_db_data
from interfaces.update_admin_data_gui import UpdateAdminDataGUI
from interfaces.admin_seeing_data import AdminSeeDataGUI
from tkinter import messagebox


class AdminAreaGUI:

    def __init__(self, main_window, back_function):
        """
        This init method initializes the GUI for the Admin area.
        :param main_window: The root window application.
        """
        # Saving the root window and back function into a attribute
        self.root = main_window
        self.back_function = back_function

        # State of the system label
        self.system_state = Label(self.root, bg='#393e46', text='Administrador', fg='#eeeeee', font=('Helvetica', 24))

        # Giving to the admin, some tips off how to use this section
        self.tips_label = Label(self.root, bg='#393e46', fg='#eeeeee', font=('Helvetica', 12), text='Selecione uma das '
                                                                                                    'contas abaixo para'
                                                                                                    ' visualizar ou '
                                                                                                    'excluir - ')

        # Creating the listbox area with frames
        self.framebox = Frame(self.root)

        self.scrollbar = Scrollbar(self.framebox, orient=VERTICAL)
        self.accounts_listbox = Listbox(self.framebox, yscrollcommand=self.scrollbar.set, width=100, bg='#222831',
                                        fg='#eeeeee', borderwidth=3, relief=RIDGE, font=('Helvetica', 12))

        self.scrollbar.config(command=self.accounts_listbox.yview)

        # Inserting the clients data into the listbox
        self.listbox_data = get_db_data()
        for client in self.listbox_data:
            self.accounts_listbox.insert(END, client)

        # Creating the admin actions with frame
        self.buttons_frame = Frame(self.root, bg='#393e46')

        self.see_data = Button(self.buttons_frame, text='Ver dados da conta', width=25, font=('Helvetica', 14),
                               bg='#00adb5', fg='#eeeeee', borderwidth=3, state=DISABLED, command=self.__see_data)
        self.delete_account = Button(self.buttons_frame, text='Excluir conta', width=25, font=('Helvetica', 14),
                                     bg='red', fg='#eeeeee', borderwidth=3, state=DISABLED,
                                     command=self.__delete_account)
        self.update_login_password = Button(self.buttons_frame, text='Atualizar Login e Senha', width=25,
                                            font=('Helvetica', 14), bg='#393e46', fg='#eeeeee', borderwidth=3,
                                            command=self.__update_admin_login_password)
        self.back_to_main_menu = Button(self.buttons_frame, text='Voltar ao menu Inicial', width=25,
                                        font=('Helvetica', 14), bg='#222831', fg='#eeeeee', borderwidth=3,
                                        command=self.__back)

        # Binding the ListboxSelect event to change the state of the see_data and delete_account buttons
        if len(self.listbox_data) != 0:
            self.accounts_listbox.bind("<<ListboxSelect>>", self.__alter_state)

        # Putting it onto the screen
        self.system_state.pack(pady=50)

        self.tips_label.pack()

        self.framebox.pack(pady=15)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.accounts_listbox.pack()

        self.buttons_frame.pack(pady=65)

        self.see_data.grid(row=0, column=0, padx=5)
        self.delete_account.grid(row=0, column=1, padx=5)
        self.update_login_password.grid(row=0, column=2, padx=5)
        self.back_to_main_menu.grid(row=0, column=3, padx=5)

    def __alter_state(self, event):
        """
        This method alters the state of the see_data and delete_account buttons to NORMAL.
        :param event: The event passed by the .bind() method, which in this case is 'FocusIn'.
        :return: None
        """
        self.see_data.config(state=NORMAL)
        self.delete_account.config(state=NORMAL)

    def __back(self):
        """
        This function works like a 'back' button. Every time a button calls this function, it destroys every content
        from the current window and returns to the main window.
        :return: None
        """
        # Destroying the old widgets
        self.system_state.destroy()
        self.tips_label.destroy()
        self.framebox.destroy()
        self.buttons_frame.destroy()

        # Calling the back function that was passed as argument to the __init__ method
        self.back_function()

    @staticmethod
    def __update_admin_login_password():
        """
        This method initializes the UpdateAdminDataGUI class, that will be responsible for updating the login and pass
        word from the admin.
        :return: None
        """
        # Initializing the UpdateAdminDataGUI
        UpdateAdminDataGUI()

    def __see_data(self):
        """
        This method initializes the AdminSeeDataGUI class, that will show the data from the selected client in the list
        box.
        :return: None
        """
        # Splitting the string from the listbox selection to get the number only
        selected = self.accounts_listbox.get(ANCHOR)
        selected = selected.split()
        selected = selected[0]

        # Initializing the AdminSeeDataGUI class
        AdminSeeDataGUI(account_selected=selected)

    def __delete_account(self):
        """
        This method deletes the selected account from the listbox. Only the administrator of the system has access to
        this operation.
        :return: None
        """
        def delete_client(selection):
            """
            This function deletes the account data from the clients database
            :return: None
            """
            database = r'.\bank_databases\clients.csv'
            with open(database, mode='r', newline='', encoding='utf-8') as file:
                clients = file.readlines()
            with open(database, mode='w', newline='', encoding='utf-8') as file:
                for line in clients:
                    if line.startswith(selection):
                        pass
                    else:
                        file.write(line)
        # Saving the selected content for deletion later
        element = self.accounts_listbox.get(ANCHOR)

        # Splitting the string from the listbox selection to get the number only
        selected = self.accounts_listbox.get(ANCHOR)
        selected = selected.split()
        selected = selected[0]

        # Asking the administrator if hes really sure of what he is about to do
        response = messagebox.askyesno('Confirmar exclusão', f'Você tem certeza que deseja excluir a conta de número '
                                                             f'{selected}? Esta operação é permanente e não pode ser '
                                                             f'desfeita.')
        # If response is True/Yes
        if response:
            # Updating the elements in the listbox
            self.accounts_listbox.delete(ANCHOR)
            self.listbox_data.remove(element)

            # Updating the state of the buttons
            self.see_data.config(state=DISABLED)
            self.delete_account.config(state=DISABLED)

            # Deleting the account from the system
            delete_client(selection=selected)

            # Showing the user that the request was successfully completed
            messagebox.showinfo('Conta removida', f'A conta de número {selected} foi removida com sucesso do sistema!')

            # Changing the state of the button if theres no accounts left
            if len(self.listbox_data) == 0:
                self.see_data.config(state=DISABLED)
                self.delete_account.config(state=DISABLED)
                self.accounts_listbox.unbind('<<ListboxSelect>>')
        # If response is False/No
        else:
            pass
