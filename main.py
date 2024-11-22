import tkinter as tk
from tkinter import ttk
def check_password_strength(*args):
    password = password_var.get()
    strength = 0
    conditions = {
        "Length": len(password) >= 8,
        "Uppercase": any(char.isupper() for char in password),
        "Lowercase": any(char.islower() for char in password),
        "Number": any(char.isdigit() for char in password),
        "Special": any(char in "!@#$%^&*()-_=+[]{};:'\"|\\,.<>?/" for char in password)
    }
    for condition, passed in conditions.items():
        if passed:
            strength += 1
    if strength == 0:
        strength_label["text"] = "Very Weak"
        strength_bar["value"] = 0
        strength_label["foreground"] = "red"
    elif strength <= 2:
        strength_label["text"] = "Weak"
        strength_bar["value"] = 25
        strength_label["foreground"] = "orange"
    elif strength == 3:
        strength_label["text"] = "Medium"
        strength_bar["value"] = 50
        strength_label["foreground"] = "gold"
    elif strength == 4:
        strength_label["text"] = "Strong"
        strength_bar["value"] = 75
        strength_label["foreground"] = "green"
    else:
        strength_label["text"] = "Very Strong"
        strength_bar["value"] = 100
        strength_label["foreground"] = "dark green"
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.resizable(False, False)
password_var = tk.StringVar()
password_var.trace("w", check_password_strength)
tk.Label(root, text="Enter Password:", font=("Arial", 14)).pack(pady=10)
password_entry = ttk.Entry(root, textvariable=password_var, font=("Arial", 12), show="*")
password_entry.pack(pady=10, padx=20, fill="x")
strength_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
strength_bar.pack(pady=10)
strength_label = tk.Label(root, text="", font=("Arial", 14))
strength_label.pack(pady=10)
root.mainloop()