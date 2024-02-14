import random
import string
import tkinter as tk
from tkinter import messagebox

mapping = {char: i for i, char in enumerate(string.ascii_lowercase)}
reverseMapping = {i: char for i, char in enumerate(string.ascii_lowercase)}

def generate_key(plaintext):
    return ''.join(' ' if char == ' ' else random.choice(string.ascii_lowercase) for char in plaintext)

def encrypt(plaintext, key, mapping, reverseMapping):
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i] == ' ':
            ciphertext += ' '
        else:
            xor_result = (mapping[plaintext[i]] ^ mapping[key[i]]) % 26
            ciphertext += reverseMapping[xor_result]
    return ciphertext

def decrypt(ciphertext, key, mapping, reverseMapping):
    original_text = ''
    for i in range(len(ciphertext)):
        if ciphertext[i] == ' ':
            original_text += ' '
        else:
            xor_result = (mapping[ciphertext[i]] ^ mapping[key[i]]) % 26
            original_text += reverseMapping[xor_result]
    return original_text

def encrypt_decrypt():
    text = text_entry.get("1.0", "end-1c")
    if not text:
        messagebox.showerror("Error", "Please enter some text to encrypt/decrypt.")
        return
    
    mode = mode_var.get()  # Check if encryption or decryption mode is selected
    
    if mode == "Encrypt":
        plaintext = ''.join(filter(lambda x: x.isalnum() or x.isspace(), text.lower()))
        key = generate_key(plaintext)
        result_text = encrypt(plaintext, key, mapping, reverseMapping)
        output_text_display.config(state=tk.NORMAL)
        output_text_display.delete("1.0", tk.END)
        output_text_display.insert(tk.END, result_text)
        output_text_display.config(state=tk.DISABLED)
    else:
        # Decryption mode
        key = key_entry.get().lower()
        if len(key) != len(text):
            messagebox.showerror("Error", "Key length does not match the length of the ciphertext.")
            return
        decrypted_text = decrypt(text, key, mapping, reverseMapping)
        output_text_display.config(state=tk.NORMAL)
        output_text_display.delete("1.0", tk.END)
        output_text_display.insert(tk.END, decrypted_text)
        output_text_display.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Text Encryption and Decryption")

# Text Entry
text_entry_label = tk.Label(root, text="Enter text:")
text_entry_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

text_entry = tk.Text(root, height=5, width=50)
text_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# Mode Selection
mode_var = tk.StringVar()
mode_var.set("Encrypt")
encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt")
encrypt_radio.grid(row=1, column=0, padx=5, pady=5)
decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt")
decrypt_radio.grid(row=1, column=1, padx=5, pady=5)

# Key Entry for Decryption
key_label = tk.Label(root, text="Decryption Key:")
key_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

key_entry = tk.Entry(root)
key_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# Buttons
process_button = tk.Button(root, text="Process", command=encrypt_decrypt)
process_button.grid(row=3, column=1, padx=5, pady=5)

# Display Output
output_text_label = tk.Label(root, text="Output:")
output_text_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

output_text_display = tk.Text(root, height=5, width=50, state=tk.DISABLED)
output_text_display.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

root.mainloop()
