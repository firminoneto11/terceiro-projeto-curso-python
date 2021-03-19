from os.path import exists


def check_session_file():
    """
    This function checks if the session_data.csv exists and create a new one if it doesn't.
    :return: None
    """
    session_data = r".\bank_databases\session_data.csv"
    if exists(session_data) is False:
        with open(session_data, mode='w', newline="", encoding='utf-8'):
            pass


def wipe_session_data():
    """
    This function wipes all content from the session_data.csv file.
    :return: None
    """
    session_data = r".\bank_databases\session_data.csv"
    with open(session_data, mode='w', newline="", encoding='utf-8'):
        pass


def closing_on_x(window):
    """
    This functions wipes all content from the session_data.csv file when the 'X' button is pressed in the main_window.
    :param window: Root/main window
    :return: None
    """
    wipe_session_data()
    window.quit()
