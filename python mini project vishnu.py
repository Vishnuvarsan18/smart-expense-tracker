import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# -------------------------------
# Main Window
# -------------------------------
root = tk.Tk()
root.title("Smart Expense Tracker")
root.geometry("900x600")
root.config(bg="#f0f2f5")

# -------------------------------
# Data Storage
# -------------------------------
expenses = []

# -------------------------------
# Functions
# -------------------------------
def add_expense():
    amount = amount_entry.get()
    category = category_box.get()
    date = date_entry.get()
    description = desc_entry.get()

    # Check empty fields
    if amount == "" or category == "" or date == "":
        messagebox.showwarning("Warning", "Please fill all required fields.")
        return

    # Check amount number
    try:
        amount = float(amount)
    except:
        messagebox.showerror("Error", "Enter valid amount.")
        return

    # Add data to list
    expenses.append([amount, category, date, description])

    # Show in table
    refresh_table()

    # Clear boxes
    amount_entry.delete(0, tk.END)
    category_box.set("")
    date_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)

def refresh_table():
    # Remove old rows
    for row in table.get_children():
        table.delete(row)

    total = 0

    # Insert new rows
    for i, item in enumerate(expenses, start=1):
        table.insert("", "end", values=(i, item[0], item[1], item[2], item[3]))
        total += item[0]

    total_label.config(text="₹ " + str(total))

def delete_expense():
    selected = table.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a row to delete.")
        return

    item = table.index(selected[0])
    expenses.pop(item)

    refresh_table()

def show_report():
    total = 0
    category_total = {}

    for item in expenses:
        amount = item[0]
        category = item[1]

        total += amount

        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount

    report = "TOTAL EXPENSE = ₹" + str(total) + "\n\n"

    for cat, amt in category_total.items():
        report += cat + " = ₹" + str(amt) + "\n"

    messagebox.showinfo("Expense Report", report)

# -------------------------------
# Title
# -------------------------------
title = tk.Label(
    root,
    text="Smart Expense Tracker",
    font=("Arial", 22, "bold"),
    bg="#1565c0",
    fg="white",
    pady=10
)
title.pack(fill="x")

# -------------------------------
# Input Frame
# -------------------------------
frame1 = tk.Frame(root, bg="white", bd=2, relief="groove")
frame1.pack(padx=20, pady=20, fill="x")

tk.Label(frame1, text="Amount (₹)", bg="white", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(frame1, width=15)
amount_entry.grid(row=1, column=0, padx=10)

tk.Label(frame1, text="Category", bg="white", font=("Arial", 12)).grid(row=0, column=1, padx=10)
category_box = ttk.Combobox(frame1, width=15)
category_box["values"] = ("Food", "Travel", "Shopping", "Bills", "Other")
category_box.grid(row=1, column=1, padx=10)

tk.Label(frame1, text="Date", bg="white", font=("Arial", 12)).grid(row=0, column=2, padx=10)
date_entry = tk.Entry(frame1, width=15)
date_entry.grid(row=1, column=2, padx=10)
date_entry.insert(0, datetime.today().strftime("%d-%m-%Y"))

tk.Label(frame1, text="Description", bg="white", font=("Arial", 12)).grid(row=0, column=3, padx=10)
desc_entry = tk.Entry(frame1, width=20)
desc_entry.grid(row=1, column=3, padx=10)

add_btn = tk.Button(
    frame1,
    text="Add Expense",
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    command=add_expense
)
add_btn.grid(row=1, column=4, padx=10)

# -------------------------------
# Table Frame
# -------------------------------
frame2 = tk.Frame(root, bg="white", bd=2, relief="groove")
frame2.pack(padx=20, pady=10, fill="both", expand=True)

columns = ("No", "Amount", "Category", "Date", "Description")

table = ttk.Treeview(frame2, columns=columns, show="headings", height=12)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=150, anchor="center")

table.pack(padx=10, pady=10)

# -------------------------------
# Buttons
# -------------------------------
btn_frame = tk.Frame(root, bg="#f0f2f5")
btn_frame.pack(pady=10)

delete_btn = tk.Button(
    btn_frame,
    text="Delete Selected",
    bg="red",
    fg="white",
    font=("Arial", 11, "bold"),
    command=delete_expense
)
delete_btn.grid(row=0, column=0, padx=10)

report_btn = tk.Button(
    btn_frame,
    text="Generate Report",
    bg="#1565c0",
    fg="white",
    font=("Arial", 11, "bold"),
    command=show_report
)
report_btn.grid(row=0, column=1, padx=10)

# -------------------------------
# Total Expense
# -------------------------------
bottom = tk.Frame(root, bg="#dff0d8", height=50)
bottom.pack(fill="x", padx=20, pady=10)

tk.Label(
    bottom,
    text="Total Expense:",
    font=("Arial", 16, "bold"),
    bg="#dff0d8",
    fg="green"
).pack(side="left", padx=20, pady=10)

total_label = tk.Label(
    bottom,
    text="₹ 0",
    font=("Arial", 16, "bold"),
    bg="#dff0d8",
    fg="green"
)
total_label.pack(side="left")

# -------------------------------
# Run Window
# -------------------------------
root.mainloop()
