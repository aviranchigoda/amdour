import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1]))

from services.auth_svc.main import app


def test_signup_and_list_users(tmp_path, monkeypatch):
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{tmp_path/'test.db'}")
    with TestClient(app) as client:
        response = client.post(
            "/auth/signup",
            params={"username": "alice", "password": "secret", "tenant_name": "acme"},
        )
        assert response.status_code == 200
        token = response.json().get("token")
        assert token

        response = client.get("/tenants/1/users")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["username"] == "alice"
