import tkinter as tk
from tkinter import messagebox
import string
import random

# Function to generate the password
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")
        return

    characters = ""
    if var_letters.get():
        characters += string.ascii_letters
    if var_digits.get():
        characters += string.digits
    if var_special.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("No Options Selected", "Select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f0f8ff")

# Title
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#f0f8ff").pack(pady=10)

# Password length input
tk.Label(root, text="Enter password length:", bg="#f0f8ff", font=("Arial", 12)).pack()
length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

# Checkboxes
var_letters = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_special = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters (a-z, A-Z)", variable=var_letters, bg="#f0f8ff", font=("Arial", 11)).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Digits (0-9)", variable=var_digits, bg="#f0f8ff", font=("Arial", 11)).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Special Characters (!@#...)", variable=var_special, bg="#f0f8ff", font=("Arial", 11)).pack(anchor='w', padx=20)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4682B4", fg="white").pack(pady=10)

# Display password
password_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=30)
password_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 11), bg="#32CD32", fg="white").pack(pady=5)

root.mainloop()
