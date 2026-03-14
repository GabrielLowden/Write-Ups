from Crypto.Cipher import AES

# Key (16 bytes)
key = bytes([0xda, 0x23, 0xd1, 0xb2, 0xa9, 0x69, 0x37, 0xa4,
             0x27, 0xc8, 0x2c, 0xb8, 0x6a, 0xa2, 0xa0, 0x91])

# Ciphertext in hex
ciphertext_hex = "8f0e6d0f5b0dc1db201948b9e0cebd8f8c5f092ee437b94b998be7b14dbe7c0b38338e7e04fbddef0c6260a4eb758417"
ciphertext = bytes.fromhex(ciphertext_hex)

# Decrypt AES-ECB
cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)

# Print flag
print(plaintext.decode('utf-8', errors='ignore'))
