**Text Encryption and Decryption Tool using Vernam Cipher**

This program provides a simple graphical user interface (GUI) for encrypting and decrypting text using the Vernam Cipher. The Vernam Cipher is a symmetric key cipher where each character of the plaintext is XORed with a corresponding character from a one-time pad key.

### How to Use:

1. **Installation:**
   - Ensure you have Python installed on your system.
   - The program utilizes the tkinter library for the GUI, which is usually included in standard Python installations.

2. **Execution:**
   - Run the script.
   - A window titled "Text Encryption and Decryption" will appear.

3. **Using the Application:**
   - **Enter Text:** Input the text you wish to encrypt or decrypt in the text entry box provided.
   - **Mode Selection:** Choose between encryption or decryption mode using the radio buttons. 
     - **Encrypt:** Select this mode to encrypt the entered text.
     - **Decrypt:** Select this mode to decrypt ciphertext. You must provide the decryption key for this mode.
   - **Decryption Key:** If decrypt mode is chosen, enter the decryption key in the designated entry box.
   - **Process:** Click the "Process" button to initiate the encryption or decryption process.
   - **Output:** The result of the encryption or decryption operation will be displayed in the output text box.

### About the Vernam Cipher:

- **Encryption:** In encryption mode, each character of the plaintext is combined with a corresponding character from a randomly generated key. The resulting ciphertext is produced by XORing each plaintext character with the corresponding key character.
- **Decryption:** Decryption is performed similarly, where each character of the ciphertext is XORed with the corresponding character from the provided key to retrieve the original plaintext.

### Notes:

- The program only supports basic alphanumeric characters and spaces. Other characters will be omitted from the encryption and decryption process.
- The length of the key matches the length of the plaintext, ensuring a one-time pad for each encryption operation.
- The GUI provides a user-friendly interface for utilizing the Vernam Cipher without needing to handle the encryption and decryption logic directly.
