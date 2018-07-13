# -*- coding: utf-8 -*-
from flask import *

app = Flask(__name__)

@app.route('/<text>')
def index(text):
    print(text)
    return "Nope.. HAHA"


if __name__ == "__main__":
    app.run("0.0.0.0", 80, debug=True)
