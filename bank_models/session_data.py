from os.path import exists


def check_session_file():
    session_data = r".\bank_databases\session_data.csv"
    if exists(session_data) is False:
        with open(session_data, mode='w', newline="", encoding='utf-8'):
            pass
