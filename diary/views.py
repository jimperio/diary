from flask import render_template

from diary import app


@app.route('/')
def hello():
  return render_template('index.html')