from csv import DictReader, DictWriter


def centralize(width, height, element):
    """
    This function creates a window centralized accordingly to the screen that is displayed.
    :param width: Width desired for the window
    :param height: Height desired for the window
    :param element: Tk() main element
    :return: None
    """
    screen_width, screen_height = element.winfo_screenwidth(), element.winfo_screenheight()
    posx, posy = screen_width / 2 - width / 2, screen_height / 2 - height / 2
    element.geometry("%dx%d+%d+%d" % (width, height, posx, posy))


def update_session_data_csv(new_balance):
    """
    This function updated the session_data.csv file with the new balance that was given by the user. It only updates the
    balance!
    :param new_balance: New balance typed by the user and previously verified by the system.
    :return: Returns a list containing the updated data for the session data.
    """
    session_data = r".\bank_databases\session_data.csv"
    header = "Número da conta", "Saldo", "Nome", "CPF", "Data de nascimento", "Login", "Senha"

    #               Updating the session_data

    # Gathering the old content
    with open(session_data, mode='r', newline='', encoding='utf-8') as archive:
        file = DictReader(f=archive, fieldnames=header)
        next(file)
        for client in file:
            updated_data = {
                "Número da conta": client["Número da conta"],
                "Saldo": f"R${new_balance}",
                "Nome": client["Nome"],
                "CPF": client["CPF"],
                "Data de nascimento": client["Data de nascimento"],
                "Login": client["Login"],
                "Senha": client["Senha"]
            }
            break
    # Updating the file with the old + new content
    with open(session_data, mode='w', newline='', encoding='utf-8') as archive:
        file = DictWriter(f=archive, fieldnames=header)
        file.writeheader()
        file.writerow({
            "Número da conta": updated_data["Número da conta"],
            "Saldo": updated_data["Saldo"],
            "Nome": updated_data["Nome"],
            "CPF": updated_data["CPF"],
            "Data de nascimento": updated_data["Data de nascimento"],
            "Login": updated_data["Login"],
            "Senha": updated_data["Senha"]
        })

    updated_data_listed = []
    for value in updated_data.values():
        updated_data_listed.append(value)

    return updated_data_listed


def update_clients_csv(updated_data):
    """
    This function updated the clients.csv file with the new balance that was given by the user. It only updates the
    balance!
    :param updated_data: The entire updated data from the client from the session data.
    :return: None
    """
    database = r".\bank_databases\clients.csv"

    # Saving the old information into a variable
    with open(database, mode='r', encoding='utf-8', newline='') as file:
        old_db_content = file.readlines()

    # Overwriting the old information and replacing for the updated data, only if is from the user from the current
    # session
    with open(database, mode='w', encoding='utf-8', newline='') as file:
        for line in old_db_content:
            if line.startswith(updated_data[0]):
                file.write(','.join(updated_data))
                file.write('\n')
            else:
                file.write(line)


def get_current_balance():
    """
    This function opens the 'session_data.csv' file and gets the current 'Saldo'/'Balance' amount and returns it as a
    float pointing number.
    :return: The current balance from the current client accessing the system, in float pointing number.
    """
    session_data = r".\bank_databases\session_data.csv"
    header = "Número da conta", "Saldo", "Nome", "CPF", "Data de nascimento", "Login", "Senha"

    with open(session_data, mode='r', newline='', encoding='utf-8') as file:
        archive = DictReader(f=file, fieldnames=header)
        next(archive)
        for client in archive:
            current_balance = client["Saldo"]
            current_balance = current_balance.replace('R$', '')
            current_balance = float(current_balance)
            return current_balance


def get_account_numbers():
    """
    This functions opens the 'clients.csv' file and gets every account number and returns it as a list.
    :return: A list containing every account number in the clients.csv file. The numbers are integers.
    """
    database = r".\bank_databases\clients.csv"
    header = "Número da conta", "Saldo", "Nome", "CPF", "Data de nascimento", "Login", "Senha"
    account_numbers = []

    with open(database, mode='r', encoding='utf-8', newline='') as file:
        archive = DictReader(f=file, fieldnames=header)
        next(archive)
        for client in archive:
            account_numbers.append(int(client[header[0]]))

    return account_numbers
