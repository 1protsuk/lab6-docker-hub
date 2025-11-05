from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    student_surname = "ПРОЦУК"   # ← те саме, що в тесті
    return f"<h1>Hello from Docker! V1</h1><p>Виконав: {student_surname}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
