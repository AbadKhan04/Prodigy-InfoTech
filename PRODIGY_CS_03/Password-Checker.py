import tkinter as tk
from tkinter import ttk
import re


def assess_password_strength(password):
  length = len(password)
  uppercase = any(char.isupper() for char in password)
  lowercase = any(char.islower() for char in password)
  numbers = any(char.isdigit() for char in password)
  special_characters = bool(
      re.match('[!@#$%^&*()_+=\-[\]{};:\'"|,.<>?]', password))
  strength = 0

  if length >= 8:
    strength += 1
  if length >= 12:
    strength += 1
  if length >= 16:
    strength += 1

  if uppercase:
    strength += 1
  if lowercase:
    strength += 1
  if numbers:
    strength += 1
  if special_characters:
    strength += 1

  return strength


def check_password_strength():
  password = password_entry.get()
  strength = assess_password_strength(password)
  strength_label.config(text=strength_labels[strength])


root = tk.Tk()
root.title("Password Strength Checker")

password_label = ttk.Label(root, text="Enter your password:")
password_label.grid(row=0, column=0, sticky="w")

password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=0, column=1)

strength_labels = {
    0: "Very Weak - It should be at least 8 characters long.",
    1:
    "Weak - It should be at least 8 characters long and include uppercase letters, lowercase letters, numbers, and special characters.",
    2:
    "Moderate - It should be at least 12 characters long and include uppercase letters, lowercase letters, numbers, and special characters.",
    3:
    "Strong - It should be at least 16 characters long and include uppercase letters, lowercase letters, numbers, and special characters.",
    4: "Very Strong - It meets all criteria for a strong password."
}

strength_label = ttk.Label(root, text="")
strength_label.grid(row=1, column=0, columnspan=2)

check_button = ttk.Button(root,
                          text="Check Strength",
                          command=check_password_strength)
check_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
