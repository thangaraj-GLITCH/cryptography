from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_ecb_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def aes_ecb_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
    return decrypted_text

def main():
    key = get_random_bytes(16)  
    plaintext = "Hello, ECB!"  

    print(f"Key: {key.hex()}")
    print(f"Plaintext: {plaintext}")

    # Encryption
    ciphertext = aes_ecb_encrypt(key, plaintext)
    print(f"Ciphertext: {ciphertext.hex()}")

    # Decryption
    decrypted_text = aes_ecb_decrypt(key, ciphertext)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
