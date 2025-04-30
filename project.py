import tkinter as tk
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('budget.db')
c = con.cursor()

c.execute("PRAGMA table_info(expenses);")
columns = c.fetchall()

column_names = [column[1] for column in columns]
if 'type' not in column_names:
    c.execute('ALTER TABLE expenses ADD COLUMN type TEXT')
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
    type = type_var.get()
    date = date_entry.get()
    payment_method = payment_var.get()
    priority = priority_slider.get()

    if item and amount and date:
        try:
            amount = float(amount)
            c.execute('''
                INSERT INTO expenses (item, amount, type, date, payment_method, priority)
                VALUES (?, ?, ?, ?, ?,?)
            ''', (item, amount, type, date,payment_method ,priority, ))
            con.commit()

           
            item_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            payment_var.set("Cash")
            priority_slider.set(1)

            messagebox.showinfo("Success", "Expense was saved successfully!")
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number!")
    
def view_exp():
    view_window = tk.Toplevel(root)
    view_window.title("All Expenses")
    view_window.geometry("400x400")

    c.execute('SELECT * FROM expenses')
    records = c.fetchall()

    text = tk.Text(view_window)
    text.pack(expand=True, fill='both')

    if records:
        for record in records:
            text.insert(tk.END, f"ID: {record[0]}, Item: {record[1]}, Amount: €{record[2]}, "
                                f"Type: {record[3]}, Date: {record[4]}, "
                                f"Payment: {record[5]}, Priority: {record[6]}\n")
    else:
        text.insert(tk.END, "No expenses found.")


submit_btn = tk.Button(root, text="Add Expense", command=save_exp)
submit_btn.grid(row=9, column=0, columnspan=2, pady=10)

view_btn = tk.Button(root, text="View Expenses", command=view_exp)
view_btn.grid(row=10, column=0, columnspan=2, pady=10)




root.mainloop()
