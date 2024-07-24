import random
import tkinter as tk
from tkinter import messagebox


uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "~!@#$%^&*()_+{}|:?[]\\;,./-="


def generate_passwords():
    upper = upper_var.get()
    lower = lower_var.get()
    nums = nums_var.get()
    syms = syms_var.get()
    
    try:
        length = int(length_entry.get())
        amount = int(amount_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Length and amount must be integers")
        return
    
    if length < 1 or amount < 1:
        messagebox.showerror("Invalid input", "Length and amount must be greater than 0")
        return
    
    all_chars = ""
    if upper:
        all_chars += uppercase_letters
    if lower:
        all_chars += lowercase_letters
    if nums:
        all_chars += digits
    if syms:
        all_chars += symbols
    
    if all_chars:
        passwords = []
        for _ in range(amount):
            passwords.append("".join(random.choice(all_chars) for _ in range(length)))
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "\n".join(passwords))
    else:
        messagebox.showerror("Invalid input", "At least one character type must be selected")

def copy_to_clipboard():
    passwords = result_text.get(1.0, tk.END).strip()
    if passwords:
        root.clipboard_clear()
        root.clipboard_append(passwords)
        messagebox.showinfo("Copied to clipboard", "Passwords copied to clipboard!")
    else:
        messagebox.showwarning("No passwords", "There are no passwords to copy!")

root = tk.Tk()
root.title("🔐 Password Generator")

tk.Label(root, text="Include Uppercase Letters").grid(row=0, column=0, sticky="w", padx=10, pady=5)
upper_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, variable=upper_var).grid(row=0, column=1, sticky="w", padx=10)

tk.Label(root, text="Include Lowercase Letters").grid(row=1, column=0, sticky="w", padx=10, pady=5)
lower_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, variable=lower_var).grid(row=1, column=1, sticky="w", padx=10)

tk.Label(root, text="Include Digits").grid(row=2, column=0, sticky="w", padx=10, pady=5)
nums_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, variable=nums_var).grid(row=2, column=1, sticky="w", padx=10)

tk.Label(root, text="Include Symbols").grid(row=3, column=0, sticky="w", padx=10, pady=5)
syms_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, variable=syms_var).grid(row=3, column=1, sticky="w", padx=10)

tk.Label(root, text="Password Length").grid(row=4, column=0, sticky="w", padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=4, column=1, padx=10)
length_entry.insert(0, "12")  

tk.Label(root, text="Number of Passwords").grid(row=5, column=0, sticky="w", padx=10, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=5, column=1, padx=10)
amount_entry.insert(0, "5") 


generate_button = tk.Button(root, text="Generate Passwords", command=generate_passwords, bg="green", fg="white")
generate_button.grid(row=6, column=0, columnspan=2, pady=10)


result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)


copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="blue", fg="white")
copy_button.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
