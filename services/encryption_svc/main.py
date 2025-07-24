import os
import base64
from fastapi import FastAPI, HTTPException
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


SECRET_KEY = os.getenv("ENCRYPTION_KEY", "A" * 32).encode()
IV = b"0123456789abcdef"

app = FastAPI(title="Encryption Service")


def _get_cipher() -> Cipher:
    return Cipher(
        algorithms.AES(SECRET_KEY), modes.CBC(IV), backend=default_backend()
    )


@app.post("/encrypt")
def encrypt_data(data: str):
    cipher = _get_cipher()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return {"ciphertext": base64.b64encode(ciphertext).decode()}


@app.post("/decrypt")
def decrypt_data(ciphertext: str):
    cipher = _get_cipher()
    decryptor = cipher.decryptor()
    try:
        decoded = base64.b64decode(ciphertext.encode())
        decrypted = decryptor.update(decoded) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        data = unpadder.update(decrypted) + unpadder.finalize()
    except Exception as e:  # pragma: no cover - defensive programming
        raise HTTPException(status_code=400, detail="Invalid ciphertext") from e
    return {"data": data.decode()}
