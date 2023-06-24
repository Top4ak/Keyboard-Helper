import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

def start_app():
    root = tk.Tk()
    root.title("Anti-Anti-Paste")
    root.geometry("1280x720")
    root.resizable(width=False, height=False)
    root.mainloop()