import tkinter as tk
from tkinter import simpledialog
from tkinter import colorchooser
import numpy as np

def input_color():

    application_window = tk.Tk()

    # the input dialog
    rgb_color, _ =  (colorchooser.askcolor(parent=application_window,
                                             initialcolor=(255, 0, 0)))
    rgb_color = np.asarray(rgb_color)
    rgb_color = np.multiply(1/255,rgb_color)
    return rgb_color
