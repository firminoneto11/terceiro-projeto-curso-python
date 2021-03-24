from tkinter import *
from interfaces.functions import centralize
from interfaces.main_window_gui import InitialGUI
from bank_models.session_data import closing_on_x


# Initial GUI settings
main_window = Tk()
main_window.title("ValWare Bank")
main_window.iconbitmap(r'.\assets\valware.ico')
main_window.configure(background='#393e46')
main_window.resizable(False, False)
centralize(1200, 700, main_window)


# Starting the main UI
InitialGUI(main_window)


# Wiping the data from session_data_csv in case the user closes the main_window on the 'X' button
main_window.protocol('WM_DELETE_WINDOW', lambda: closing_on_x(main_window))


# Main Loop ending
main_window.mainloop()
