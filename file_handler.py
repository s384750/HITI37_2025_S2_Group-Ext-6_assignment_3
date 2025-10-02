
from tkinter import filedialog

def open_file():
    path = filedialog.askopenfilename(title="Select File")
    return path

def save_file():
    path = filedialog.asksaveasfilename(title="Save File")
    return path
