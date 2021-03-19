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


def update_session_data(new_balance):
    """
    This function updated the session_data.csv file with the new balance that was given by the user. It only updates the
    balance!
    :param new_balance: New balance typed by the user and previously verified by the system.
    :return: None
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


def update_clients(new_balance):
    """
    This function updated the clients.csv file with the new balance that was given by the user. It only updates the
    balance!
    :param new_balance: New balance typed by the user and previously verified by the system.
    :return: None
    """
    database = r".\bank_databases\clients.csv"
