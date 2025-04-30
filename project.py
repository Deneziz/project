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
    category TEXT,
    date TEXT,
    recurring INTEGER,
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



root.mainloop()
