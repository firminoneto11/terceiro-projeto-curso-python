from os.path import exists
from csv import DictWriter


def check_session_file():
    session_data = r".\bank_databases\session_data.csv"
    header = "Número da conta", "Saldo", "Nome", "CPF", "Data de nascimento", "Login", "Senha"
    if exists(session_data) is False:
        with open(session_data, mode='w', newline="", encoding='utf-8') as f:
            writer = DictWriter(f=f, fieldnames=header)
            writer.writeheader()
