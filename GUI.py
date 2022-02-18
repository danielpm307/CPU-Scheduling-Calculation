#### tk_ui.py
import tkinter as tk
from tkinter import ttk




root = tk.Tk()

ttk.Label(root, text="1st Number").grid(row=0, column=0)
ttk.Label(root, text="2nd Number").grid(row=1, column=0)
result_label = ttk.Label(root, text="Result")
result_label.grid(row=2, column=1)


root.mainloop()