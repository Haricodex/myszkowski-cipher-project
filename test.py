from cipher import encryptMessage, decryptMessage
from hash import custom_hash

msg = "HELLO WORLD"
key = "BANANA"

print("Plaintext:", msg)

cipher = encryptMessage(msg, key)
print("Ciphertext:", cipher)

h = custom_hash(cipher)
print("Hash:", h)

decrypted = decryptMessage(cipher, key)
print("Decrypted:", decrypted)

if decrypted == msg.replace(" ", "").upper():
    print("✅ Round-trip successful!")
else:
    print("❌ Error!")