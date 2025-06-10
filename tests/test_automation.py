import httpx
from fastapi.testclient import TestClient
from services.automation_svc.main import app, TASKS


def test_create_and_get_task(monkeypatch):
    async def fake_post(self, url, params=None, timeout=None):
        class FakeResponse:
            def __init__(self):
                self.status_code = 200
                self._json = {
                    "model": params["model"],
                    "prompt": params["prompt"],
                    "tenant": params["tenant"],
                    "result": "ok",
                }

            def raise_for_status(self):
                pass

            def json(self):
                return self._json

        return FakeResponse()

    monkeypatch.setattr(httpx.AsyncClient, "post", fake_post, raising=False)

    TASKS.clear()
    with TestClient(app) as client:
        resp = client.post(
            "/tasks",
            params={"model": "gpt", "prompt": "hi", "tenant": "1"},
        )
        assert resp.status_code == 200
        task_id = resp.json()["task_id"]

        resp = client.get(f"/tasks/{task_id}")
        assert resp.status_code == 200
        assert resp.json()["result"] == "ok"
