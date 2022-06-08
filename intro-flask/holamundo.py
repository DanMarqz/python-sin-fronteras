from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hola mundo'

@app.route('/lala')
def lala():
  return 'lala'

@app.route('/mixitos')
def mixitos():
  return 'mixitos'