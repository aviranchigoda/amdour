from fastapi.testclient import TestClient
from services.encryption_svc.main import app


def test_encrypt_and_decrypt():
    with TestClient(app) as client:
        resp = client.post("/encrypt", params={"data": "secret"})
        assert resp.status_code == 200
        ciphertext = resp.json()["ciphertext"]

        resp = client.post("/decrypt", params={"ciphertext": ciphertext})
        assert resp.status_code == 200
        assert resp.json()["data"] == "secret"
