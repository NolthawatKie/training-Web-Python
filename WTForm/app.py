from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
