from os.path import exists
from os import mkdir
import pickle as pk


class Admin:

    def __init__(self):
        self.__login = 'admin'
        self.__password = 'admin'

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password


class AdminAccess:
    DIRECTORY = r'.\bank_databases'
    ADMIN_DATA = r'.\bank_databases\admin_data.pickle'

    @classmethod
    def check_dir(cls):
        if exists(cls.DIRECTORY) is False:
            mkdir(cls.DIRECTORY)

    @classmethod
    def check_admin_data(cls):
        cls.check_dir()
        if exists(cls.ADMIN_DATA) is False:
            with open(cls.ADMIN_DATA, mode='wb') as file:
                adm = Admin()
                data = adm.login, adm.password
                pk.dump(obj=adm, file=file)
                return data
        else:
            with open(cls.ADMIN_DATA, mode='rb') as file:
                adm = pk.load(file=file)
                data = adm.login, adm.password
                return data

    def __init__(self):
        initial_data = AdminAccess.check_admin_data()
        self.__login = initial_data[0]
        self.__password = initial_data[1]

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @login.setter
    def login(self, new_value):
        arch = AdminAccess.ADMIN_DATA
        with open(arch, mode='wb') as file:
            self.__login = new_value
            pk.dump(file=file, obj=self)

    @password.setter
    def password(self, new_value):
        arch = AdminAccess.ADMIN_DATA
        with open(arch, mode='wb') as file:
            self.__password = new_value
            pk.dump(file=file, obj=self)
