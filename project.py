import tkinter as tk
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('budget.db')
c = con.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT,
    amount REAL,
    type TEXT,
    date TEXT,
    payment_method TEXT,
    priority INTEGER
)
''')
con.commit()

root = tk.Tk()
root.title(" Budget Assistant")
root.geometry("400x400")


tk.Label(root, text=" Name:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
item_entry = tk.Entry(root)
item_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="Amount:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="Type:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
Types = ["Ocassional", "Bills", "Transport", "Entertainment", "Saving"]
type_var = tk.StringVar()
type_var.set(Types[0])
type_menu = tk.OptionMenu(root, type_var, *Types)
type_menu.grid(row=2, column=1, pady=5)


tk.Label(root, text="Date (DD-MM-YYYY):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=3, column=1, pady=5)



tk.Label(root, text="Payment Method:").grid(row=5, column=0, sticky="w", padx=10, pady=5)
payment_var = tk.StringVar()
payment_var.set("Cash")
tk.Radiobutton(root, text="Cash", variable=payment_var, value="Cash").grid(row=5, column=1, sticky="w")
tk.Radiobutton(root, text="Card", variable=payment_var, value="Card").grid(row=6, column=1, sticky="w")



root.mainloop()
