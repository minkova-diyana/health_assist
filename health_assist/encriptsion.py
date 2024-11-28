import os
from hashlib import sha256

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from django.conf import settings


def get_deterministic_iv(text):
    return sha256(text.encode()).digest()[:16]


def encrypt_data(text):
    sicret_key = settings.SECRET_KEY.encode()[:32]
    iv = get_deterministic_iv(text)

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(text.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(sicret_key), modes.CBC(iv), backend=default_backend())

    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return iv + encrypted_data


def decrypt_data(encrypted_text):
    secret_key = settings.SECRET_KEY.encode()[:32]
    iv = encrypted_text[:16]
    ciphertext = encrypted_text[16:]

    cipher = Cipher(algorithms.AES(secret_key), modes.CBC(iv), backend=default_backend())

    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plain_text = unpadder.update(padded_data) + unpadder.finalize()

    return plain_text.decode()
