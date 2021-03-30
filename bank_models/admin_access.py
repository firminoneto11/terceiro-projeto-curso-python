from os.path import exists
from os import mkdir
import pickle as pk


class Admin:

    def __init__(self):
        """
        This __init__ method initializes a simple Admin object, having only getters and login | password as 'admin'.
        """
        self.__login = 'admin'
        self.__password = 'admin'

    @property
    def login(self):
        """
        Login getter
        :return: Login
        """
        return self.__login

    @property
    def password(self):
        """
        Password getter
        :return: Password
        """
        return self.__password


class AdminAccess:
    DIRECTORY = r'.\bank_databases'
    ADMIN_DATA = r'.\bank_databases\admin_data.pickle'

    @classmethod
    def check_dir(cls):
        """
        This method checks if the directory for the admin data exists, and if it doesn't, it creates a new one.
        :return: None
        """
        if exists(cls.DIRECTORY) is False:
            mkdir(cls.DIRECTORY)

    @classmethod
    def check_admin_data(cls):
        """
        This method checks if the admin_data file exists and if doesn't, it creates a new pickle file that contains the
        initial data for the AdminAccess class which came from the Admin class and returns it. If it does exists, it
        reads the file and returns the data from the file.
        :return: None
        """
        # Checking the directory existence
        cls.check_dir()

        # Creating a pickle file with the Admin class data if it doesn't exists and returning it
        if exists(cls.ADMIN_DATA) is False:
            with open(cls.ADMIN_DATA, mode='wb') as file:
                adm = Admin()
                data = adm.login, adm.password
                pk.dump(obj=adm, file=file)
                return data
        # Reading the pickle file and returning the data that was in it
        else:
            with open(cls.ADMIN_DATA, mode='rb') as file:
                adm = pk.load(file=file)
                data = adm.login, adm.password
                return data

    def __init__(self):
        """
        This __init__ method initializes the AdminAccess class with the data originated from the check_admin_data class.
        """
        initial_data = AdminAccess.check_admin_data()
        self.__login = initial_data[0]
        self.__password = initial_data[1]

    @property
    def login(self):
        """
        Login getter
        :return: Login
        """
        return self.__login

    @property
    def password(self):
        """
        Password getter
        :return: Password
        """
        return self.__password

    @login.setter
    def login(self, new_value):
        """
        Login setter. It also updates the pickle file everytime someone changes the login with the setter method.
        :param new_value: New login inputted by the user.
        :return: None
        """
        arch = AdminAccess.ADMIN_DATA
        with open(arch, mode='wb') as file:
            self.__login = new_value
            pk.dump(file=file, obj=self)

    @password.setter
    def password(self, new_value):
        """
        Password setter. It also updates the pickle file everytime someone changes the password with the setter method.
        :param new_value: New password inputted by the user.
        :return: None
        """
        arch = AdminAccess.ADMIN_DATA
        with open(arch, mode='wb') as file:
            self.__password = new_value
            pk.dump(file=file, obj=self)
