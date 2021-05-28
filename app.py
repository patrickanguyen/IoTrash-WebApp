from flask import Flask, render_template, request
from sensor_data import get_fullness, get_temp

app = Flask(__name__)


@app.get("/")
def index():
    fullness = get_fullness()
    temp = get_temp()

    return render_template('index.html', fullness_labels=fullness.labels, 
        fullness_values=fullness.values, temp_labels=temp.labels, temp_values=temp.values)

