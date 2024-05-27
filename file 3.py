import secrets
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_custom_password(length, num_letters, num_digits, num_punctuation):
    if num_letters + num_digits + num_punctuation != length:
        raise ValueError("The sum of num_letters, num_digits, and num_punctuation must equal the total length.")
    
    letters = ''.join(secrets.choice(string.ascii_letters) for i in range(num_letters))
    digits = ''.join(secrets.choice(string.digits) for i in range(num_digits))
    punctuation = ''.join(secrets.choice(string.punctuation) for i in range(num_punctuation))
    
    password = list(letters + digits + punctuation)
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def on_copy():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Clipboard", "Password copied to clipboard")

def on_generate_password():
    try:
        length = int(length_entry.get())
        num_letters = int(letters_entry.get())
        num_digits = int(digits_entry.get())
        num_punctuation = int(punctuation_entry.get())
        
        if num_letters + num_digits + num_punctuation != length:
            raise ValueError("The sum of num_letters, num_digits, and num_punctuation must equal the total length.")
        
        password = generate_custom_password(length, num_letters, num_digits, num_punctuation)
        password_entry.config(state='normal')
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state='readonly')
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main application window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")

# Create and place the labels and entry widgets
tk.Label(root, text="Length of password:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Number of letters:").grid(row=1, column=0, padx=10, pady=10)
letters_entry = tk.Entry(root)
letters_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Number of digits:").grid(row=2, column=0, padx=10, pady=10)
digits_entry = tk.Entry(root)
digits_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Number of punctuations:").grid(row=3, column=0, padx=10, pady=10)
punctuation_entry = tk.Entry(root)
punctuation_entry.grid(row=3, column=1, padx=10, pady=10)

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=on_generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Entry to display the generated password
tk.Label(root, text="Generated Password:").grid(row=5, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, state='readonly')
password_entry.grid(row=5, column=1, padx=10, pady=10)

# Button to copy the password to clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", command=on_copy)
copy_button.grid(row=6, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
