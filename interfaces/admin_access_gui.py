from tkinter import *
from tkinter import messagebox
from bank_models.admin_access import AdminAccess
from interfaces.admin_area_gui import AdminAreaGUI


class AdminAccessGUI:

    def __init__(self, root_window, back_function):
        """
        This init method initializes the GUI for the Admin access area.
        :param root_window: The root window element.
        :param back_function: The back function that was created in the InitialGUI class.
        """
        # Saving the main window and the back function into a instance attribute
        self.root_window = root_window
        self.back_function = back_function

        #                       Creating the admin access gui
        self.system_state = Label(self.root_window, bg='#393e46', text='Acessar Administração', fg='#eeeeee',
                                  font=('Helvetica', 24))
        self.main_frame = LabelFrame(self.root_window, bg='#393e46')

        # Login
        self.login_label = Label(self.main_frame, text='Login -', font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')
        self.login = Entry(self.main_frame, font=('Helvetica', 14), borderwidth=3)

        # Password
        self.password_label = Label(self.main_frame, text='Senha -', font=('Helvetica', 14), bg='#393e46', fg='#eeeeee')
        self.password = Entry(self.main_frame, font=('Helvetica', 14), borderwidth=3)

        # Accessing account
        self.access_account = Button(self.main_frame, text='Acessar Administração', width=25, font=('Helvetica', 14),
                                     bg='#00adb5', fg='#eeeeee', borderwidth=3, command=self.__log_in)

        # Back
        self.back = Button(self.main_frame, text='Voltar', width=25, font=('Helvetica', 14), bg='#222831', fg='#eeeeee',
                           borderwidth=3, command=self.__back)

        # Putting the widgets onto the screen
        self.system_state.pack(pady=50)
        self.main_frame.pack()

        self.login_label.grid(row=1, column=0, padx=10, pady=15, sticky=E)
        self.login.grid(row=1, column=1, padx=15, pady=15)

        self.password_label.grid(row=2, column=0, padx=10, pady=15, sticky=E)
        self.password.grid(row=2, column=1, padx=15, pady=15)

        self.access_account.grid(row=3, column=0, padx=15, pady=15)
        self.back.grid(row=3, column=1, padx=15, pady=15)

    def __back(self):
        """
        This function works like a 'back' button. Every time a button calls this function, it destroys every content
        from the current window and returns to the main window.
        :return: None
        """
        # Getting rid of the widgets
        self.system_state.destroy()
        self.main_frame.destroy()

        # Executing the back function that was passed by argument to __init__ method
        self.back_function()

    def __log_in(self):
        """
        This method gets the typed data from the user/admin and verifies with the database. If it matches, the Admin
        area pops up, else, it doesn't.
        :return: None
        """

        # Collecting the data inputted by the user
        login = self.login.get()
        password = self.password.get()

        # Initializing the AdminAccess class to have access to the current login and password
        adm = AdminAccess()

        # Verifying if the login and password typed are valid, showing an error if they aren't
        if len(login) == 0 or len(password) == 0:
            self.login.delete(0, END)
            self.password.delete(0, END)
            error = messagebox.showerror('Campos vazios', 'Há campos vazios!')
            if error == 'ok':
                return None
        elif login != adm.login or password != adm.password:
            self.login.delete(0, END)
            self.password.delete(0, END)
            error = messagebox.showerror('Login ou senha incorretos', 'O login ou senha inseridos estão incorretos.')
            if error == 'ok':
                return None
        else:
            # Cleaning the window area for the AdminAreaGUI class
            self.system_state.destroy()
            self.main_frame.destroy()

            # Executing the __admin_area method
            self.__admin_area()

    def __admin_area(self):
        """
        This method initializes the AdminAreaGUI class
        :return: None
        """
        AdminAreaGUI(main_window=self.root_window, back_function=self.back_function)
