from flask import Flask, render_template, request

app = Flask(__name__)

@app.get("/")
def index():
    data = [
        ("01-01-2020", 255),
        ("01-05-2020", 55),
        ("01-07-2020", 123),
        ("01-08-2020", 66),
        ("01-09-2020", 77),
        ("01-10-2020", 56),
        ("01-20-2020", 235),
        ("01-16-2020", 600),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template('index.html', fullness_labels=labels, fullness_values=values, temp_labels=labels, temp_values=values)
    