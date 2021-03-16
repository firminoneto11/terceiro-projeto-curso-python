from csv import DictWriter
from os import mkdir
from os.path import exists


class Counter:
    TRACKER = r".\bank_databases\tracker.txt"

    @staticmethod
    def generate_account_number():
        Counter.__check_tracker_and_dir()
        f = Counter.TRACKER
        with open(f, mode='r') as file:
            current_number = int(file.read())
        with open(f, mode='w') as file:
            file.write(str(current_number + 1))
        return current_number

    @classmethod
    def __check_tracker_and_dir(cls):
        if exists(cls.TRACKER) is False:
            with open(cls.TRACKER, mode='w') as archive:
                archive.write("1001")


class Client:

    DB_DIR = r".\bank_databases"
    DB = r".\bank_databases\clients.csv"

    HEADER = "Número da conta", "Saldo", "Nome", "CPF", "Data de nascimento", "Login", "Senha"

    def __init__(self, name, cpf, birth_date, login, password):
        # Creating the object with the given data
        self.__name = name
        self.__cpf = cpf
        self.__birth_date = birth_date
        self.__login = login
        self.__password = password
        self.__account_number = Counter.generate_account_number()
        self.__balance = 0

        # Saving the data into the database
        self.__save_on_db()

    @property
    def name(self):
        return self.__name

    @property
    def cpf(self):
        return self.__cpf

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @classmethod
    def check_db_and_dir(cls):
        if exists(cls.DB_DIR) is False:
            mkdir(cls.DB_DIR)
            with open(cls.DB, mode='w', newline="", encoding='utf-8') as file:
                arch = DictWriter(f=file, fieldnames=cls.HEADER)
                arch.writeheader()

    def __save_on_db(self):
        with open(Client.DB, mode='a', newline="", encoding='utf-8') as file:
            arch = DictWriter(f=file, fieldnames=Client.HEADER)
            arch.writerow({
                "Número da conta": self.account_number,
                "Saldo": f"R${self.balance}",
                "Nome": self.name,
                "CPF": self.cpf,
                "Data de nascimento": self.birth_date,
                "Login": self.login,
                "Senha": self.password
            })
