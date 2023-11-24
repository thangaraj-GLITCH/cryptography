from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def pad(text):

    while len(text) % 8 != 0:
        text += ' '
    return text

def triple_des_encrypt(key, plaintext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_text = pad(plaintext)
    ciphertext = cipher.encrypt(padded_text.encode('utf-8'))
    return ciphertext

def triple_des_decrypt(key, ciphertext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext).decode('utf-8').rstrip()
    return decrypted_text

def main():
    key = get_random_bytes(24)
    plaintext = "Hello, 3DES!" 

    print(f"Key: {key.hex()}")
    print(f"Plaintext: {plaintext}")

    ciphertext = triple_des_encrypt(key, plaintext)
    print(f"Ciphertext: {ciphertext.hex()}")

    decrypted_text = triple_des_decrypt(key, ciphertext)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
