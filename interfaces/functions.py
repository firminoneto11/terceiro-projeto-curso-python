

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
