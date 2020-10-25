import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def ask_directory():
    file_path = filedialog.askdirectory()

    return file_path