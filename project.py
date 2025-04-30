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

tk.Label(root, text="Priority (1-10):").grid(row=8, column=0, sticky="w", padx=10, pady=5)
priority_slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL)
priority_slider.grid(row=8, column=1, pady=5)

def save_exp():
    item = item_entry.get()
    amount = amount_entry.get()
    category = type_var.get()
    date = date_entry.get()
    payment_method = payment_var.get()
    priority = priority_slider.get()

    if item and amount and date:
        try:
            amount = float(amount)
            c.execute('''
                INSERT INTO expenses (item, amount, category, date, recurring, payment_method, priority)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (item, amount, type, date, recurring, payment_method, ))
            con.commit()

            item_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            recurring_var.set(0)
            payment_var.set("Cash")
            priority_slider.set(1)

            messagebox.showinfo("Success", "Expense was saved successfully!")
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number!")

root.mainloop()
