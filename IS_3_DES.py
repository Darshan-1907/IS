from Crypto.Cipher import DES
import base64

# Function to encrypt data using DES
def encrypt(data, key):
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)  # ECB mode (Electronic Codebook)
    encrypted_data = cipher.encrypt(data.encode('utf-8').ljust(8))  # Padding data to 8 bytes
    return base64.b64encode(encrypted_data).decode('utf-8')

# Function to decrypt data using DES
def decrypt(encrypted_data, key):
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)  # ECB mode (Electronic Codebook)
    decoded_data = base64.b64decode(encrypted_data)
    decrypted_data = cipher.decrypt(decoded_data)
    return decrypted_data.strip().decode('utf-8')

# Main program
if __name__ == '__main__':
    key = '12345678'  # 8-byte key for DES (56 bits effective)
    data = 'Hello'

    print("Original Data: ", data)

    # Encrypt the data
    encrypted = encrypt(data, key)
    print("Encrypted Data: ", encrypted)

    # Decrypt the data
    decrypted = decrypt(encrypted, key)
    print("Decrypted Data: ", decrypted)
