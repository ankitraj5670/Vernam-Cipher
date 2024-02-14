import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_key(plaintext):
    return ''.join(' ' if char == ' ' else random.choice(string.ascii_lowercase) for char in plaintext)

def encrypt(plaintext, key):
    plaintext = ''.join(filter(lambda x: x.isalnum() or x.isspace(), plaintext.lower()))
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i] == ' ':
            ciphertext += ' '
        else:
            xor_result = ((ord(plaintext[i]) - 97) ^ (ord(key[i]) - 97)) % 26
            ciphertext += chr(xor_result + 97)
    return ciphertext

def decrypt(ciphertext, key):
    original_text = ''
    for i in range(len(ciphertext)):
        if ciphertext[i] == ' ':
            original_text += ' '
        else:
            xor_result = ((ord(ciphertext[i]) - 97) ^ (ord(key[i]) - 97)) % 26
            original_text += chr(xor_result + 97)
    return original_text

def encrypt_decrypt():
    text = text_entry.get("1.0", "end-1c")
    if not text:
        messagebox.showerror("Error", "Please enter some text to encrypt/decrypt.")
        return

    key = generate_key(text)
    encrypted_text = encrypt(text, key)
    decrypted_text = decrypt(encrypted_text, key)

    encrypted_text_display.config(state=tk.NORMAL)
    encrypted_text_display.delete("1.0", tk.END)
    encrypted_text_display.insert(tk.END, encrypted_text)
    encrypted_text_display.config(state=tk.DISABLED)

    decrypted_text_display.config(state=tk.NORMAL)
    decrypted_text_display.delete("1.0", tk.END)
    decrypted_text_display.insert(tk.END, decrypted_text)
    decrypted_text_display.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Text Encryption and Decryption")

text_entry_label = tk.Label(root, text="Enter text:")
text_entry_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

text_entry = tk.Text(root, height=5, width=50)
text_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

encrypt_button = tk.Button(root, text="Encrypt/Decrypt", command=encrypt_decrypt)
encrypt_button.grid(row=1, column=1, padx=5, pady=5)

encrypted_text_label = tk.Label(root, text="Encrypted Text:")
encrypted_text_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

encrypted_text_display = tk.Text(root, height=5, width=50, state=tk.DISABLED)
encrypted_text_display.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

decrypted_text_label = tk.Label(root, text="Decrypted Text:")
decrypted_text_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

decrypted_text_display = tk.Text(root, height=5, width=50, state=tk.DISABLED)
decrypted_text_display.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

root.mainloop()