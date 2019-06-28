import tkinter as tk

root = tk.Tk()

tk.Label(root, text='Label left', bg='blue').pack(side='left', fill='both', expand=True)

tk.Label(root, text='Label 1', bg='green').pack(side='top', fill='both', expand=True)
tk.Label(root, text='Label 2', bg='red').pack(side='top', fill='both', expand=True)

tk.Label(root, text='Label left', bg='yellow').pack(side='left', fill='both', expand=True)

root.mainloop()