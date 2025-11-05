from app import app

def test_hello_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from Docker" in response.data

    # TODO: Вкажіть ваше прізвище для перевірки
   student_surname_bytes = b"ПРОЦУК"

    assert student_surname_bytes in response.data

