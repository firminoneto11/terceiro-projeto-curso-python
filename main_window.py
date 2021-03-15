from tkinter import *
from interfaces.functions import centralize
from interfaces.classes import InitialGUI

# Initial GUI settings
main_window = Tk()
main_window.title("ValWare Bank")
main_window['bg'] = '#393e46'
main_window.resizable(False, False)
centralize(1200, 700, main_window)


# Starting the main UI
widgets = InitialGUI(main_window)


# Main Loop ending
main_window.mainloop()
