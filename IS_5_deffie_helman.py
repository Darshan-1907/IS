# Function to perform modular exponentiation (g^private_key % p)
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Alice's side (Public & Private keys)
def alice_side(p, g, private_key):
    alice_public_key = mod_exp(g, private_key, p)
    return alice_public_key

# Bob's side (Public & Private keys)
def bob_side(p, g, private_key):
    bob_public_key = mod_exp(g, private_key, p)
    return bob_public_key

# Key generation for shared secret
def shared_secret(public_key, private_key, p):
    return mod_exp(public_key, private_key, p)

# Main program
if __name__ == "__main__":
    # Shared prime number and base (publicly known)
    p = 23  # A prime number
    g = 5   # A base number

    # Private keys (chosen by Alice and Bob)
    alice_private_key = 6  # Alice's secret key
    bob_private_key = 15   # Bob's secret key

    # Alice and Bob generate their public keys
    alice_public_key = alice_side(p, g, alice_private_key)
    bob_public_key = bob_side(p, g, bob_private_key)

    print("Alice's Public Key:", alice_public_key)
    print("Bob's Public Key:", bob_public_key)

    # Alice and Bob exchange their public keys and generate the shared secret
    alice_shared_secret = shared_secret(bob_public_key, alice_private_key, p)
    bob_shared_secret = shared_secret(alice_public_key, bob_private_key, p)

    print("Alice's Shared Secret:", alice_shared_secret)
    print("Bob's Shared Secret:", bob_shared_secret)

    # They should be the same
    assert alice_shared_secret == bob_shared_secret
    print("Shared Secret Established Successfully:", alice_shared_secret)
