from csv import DictReader


def get_db_data():
    """
    This function reads the clients.csv file and returns a string containing the account number and the name of each
    client in the file.
    :return: A list containing the account number and name of each client.
    """
    db = r'.\bank_databases\clients.csv'
    header = "Número da conta", "Saldo", "Nome", "CPF", "Data de nascimento", "Login", "Senha"
    account_and_name_data = []
    with open(db, mode='r', encoding='utf-8', newline='') as file:
        archive = DictReader(f=file, fieldnames=header)
        next(archive)
        for dictionary in archive:
            line = f"{dictionary['Número da conta']} | {dictionary['Nome']}"
            account_and_name_data.append(line)
    return account_and_name_data
