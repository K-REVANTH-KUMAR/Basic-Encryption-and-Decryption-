from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
# You must keep this key safe; if you lose it, you cannot decrypt your data
def generate_key():
    return Fernet.generate_key()

# Encrypt the message
def encrypt_message(key, message):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Decrypt the message
def decrypt_message(key, encrypted_message):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

def main():
    # Generate or load a key
    key = generate_key()
    print(f"Encryption Key: {key.decode()}")

    # Enter the message to encrypt
    message = input("Enter the message you want to encrypt: ")

    # Encrypt the message
    encrypted_message = encrypt_message(key, message)
    print(f"Encrypted Message: {encrypted_message.decode()}")

    # Decrypt the message
    decrypted_message = decrypt_message(key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
    