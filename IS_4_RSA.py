# Function to calculate GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Key generation
p, q = 61, 53  # Prime numbers
n = p * q
phi = (p - 1) * (q - 1)
e = 17  # Common choice for e
d = mod_inverse(e, phi)

public_key, private_key = (e, n), (d, n)

# Encryption function
def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

# Decryption function
def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Main
message = "Hi"
ciphertext = encrypt(message, public_key)
decrypted_message = decrypt(ciphertext, private_key)

print("Original:", message)
print("Encrypted:", ciphertext)
print("Decrypted:", decrypted_message)
