from flask import Flask, render_template
import os

get_base_dir = lambda dir:  os.path.join(os.path.abspath('../'), dir)

app = Flask(__name__, 
  static_folder=get_base_dir('static'), 
  template_folder=get_base_dir('templates'))

@app.route('/')
def hello():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)