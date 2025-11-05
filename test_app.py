from app import app

def test_hello_route():
    client = app.test_client()
    resp = client.get('/')

    assert resp.status_code == 200
    assert b"Hello from Docker" in resp.data

    # перевіряємо прізвище (рядок -> bytes у utf-8)
    assert "ПРОЦУК".encode("utf-8") in resp.data
