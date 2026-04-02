from cipher import encrypt, decrypt
from hash import polynomial_hash

def run_test():
    plaintext = "HELLO WORLD"
    key = "BANANA"

    print("Plaintext:", plaintext)

    cipher = encrypt(plaintext, key)
    print("Ciphertext:", cipher)

    hash_value = polynomial_hash(cipher)
    print("Hash:", hash_value)

    decrypted = decrypt(cipher, key)
    print("Decrypted:", decrypted)

    if decrypted == plaintext.replace(" ", "").upper():
        print("✅ Round-trip successful!")
    else:
        print("❌ Error in cipher implementation!")

if __name__ == "__main__":
    run_test()