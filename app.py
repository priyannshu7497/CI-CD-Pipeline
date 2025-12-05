from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask CI/CD Pipeline!"

# REMOVE debug and run() function because Gunicorn will handle it.


