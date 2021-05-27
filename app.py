from flask import Flask, render_template, request

app = Flask(__name__)

@app.get("/")
def index():
    user = "Patrick"
    return render_template('index.html', user=user)
