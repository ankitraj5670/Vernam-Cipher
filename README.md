# Vernam Cipher Encryption and Decryption Tool

This is a Python application built using Tkinter that enables users to encrypt and decrypt text using the Vernam cipher, also known as the one-time pad.

## Vernam Cipher

The Vernam cipher is a symmetric key encryption algorithm where each character in the plaintext is combined with a character from a secret random key using the XOR operation. The key must be as long as the plaintext and generated using a truly random process. When implemented correctly with a truly random key, the Vernam cipher is considered unbreakable.

## How It Works

The application generates a random key of the same length as the input text and uses it for both encryption and decryption.

### Encryption Process

1. The input text is converted to lowercase.
2. A random key is generated consisting of lowercase letters and spaces, with spaces preserved in their original positions.
3. Each character in the input text is encrypted using a bitwise XOR operation with the corresponding character in the key.
4. The resulting ciphertext is displayed.

### Decryption Process

1. Each character in the ciphertext is decrypted using the same XOR operation with the key.
2. The decrypted characters are concatenated to form the original text.

## Usage

1. Enter the text you want to encrypt/decrypt in the provided text entry field.
2. Click the "Encrypt/Decrypt" button.
3. The encrypted text will be displayed in the "Encrypted Text" field, and the decrypted text will be displayed in the "Decrypted Text" field.

## Dependencies

- Python 3.x
- Tkinter (usually included with Python distributions)
