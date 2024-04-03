def encrypt(text, shift):
    """Encrypts the given text using the Caesar Cipher algorithm."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """Decrypts the given text using the Caesar Cipher algorithm."""
    return encrypt(text, -shift)

def main():
    """Main function to handle user input and execute encryption or decryption."""
    print("Caesar Cipher Encryption/Decryption")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1/2): ")
    
    if choice not in ['1', '2']:
        print("Invalid choice. Please choose 1 for Encrypt or 2 for Decrypt.")
        return
    
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == '1':
        result = encrypt(text, shift)
        print("Encrypted Message:", result)
    else:
        result = decrypt(text, shift)
        print("Decrypted Message:", result)

if __name__ == "__main__":
    main()
