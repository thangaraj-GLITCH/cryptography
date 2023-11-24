from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def cbc_encrypt(plaintext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    plaintext_padded = padder.update(plaintext) + padder.finalize()

    ciphertext = encryptor.update(plaintext_padded) + encryptor.finalize()

    return ciphertext

def cbc_decrypt(ciphertext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    plaintext_padded = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(plaintext_padded) + unpadder.finalize()

    return plaintext

key = os.urandom(16)
iv = os.urandom(16)

plaintext = b'This is a secret message.'

ciphertext = cbc_encrypt(plaintext, key, iv)
print(f'Encrypted Text: {ciphertext.hex()}')

decrypted_text = cbc_decrypt(ciphertext, key, iv)
print(f'Decrypted Text: {decrypted_text.decode("utf-8")}')
