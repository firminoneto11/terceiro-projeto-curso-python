from tkinter import *
from bank_models.catch_db_data import get_db_data


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
                               bg='#00adb5', fg='#eeeeee', borderwidth=3, state=DISABLED)
        self.delete_account = Button(self.buttons_frame, text='Excluir conta', width=25, font=('Helvetica', 14),
                                     bg='red', fg='#eeeeee', borderwidth=3, state=DISABLED)
        self.update_login_password = Button(self.buttons_frame, text='Atualizar Login e Senha', width=25,
                                            font=('Helvetica', 14), bg='#393e46', fg='#eeeeee', borderwidth=3)
        self.back_to_main_menu = Button(self.buttons_frame, text='Voltar ao menu Inicial', width=25,
                                        font=('Helvetica', 14), bg='#222831', fg='#eeeeee', borderwidth=3,
                                        command=self.__back)

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
