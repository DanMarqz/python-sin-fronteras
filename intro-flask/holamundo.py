from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)

import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='user',
  password='passwd',
  database='my_test'
)

cursor = mydb.cursor(dictionary=True)

@app.route('/')
def index():
  return 'Hola mundo'

# Pueden estar en una sola funcion GET y POST o estar separadas
@app.route('/post/<post_id>', methods=['GET','POST'])
def post(post_id):
  if request.method == 'GET':
    return 'El ID del post es: ' + post_id  
  else: 
    return 'Este es otro metodo que no es GET'

@app.route('/form', methods=['POST', 'GET'])
def form():
  cursor.execute('SELECT * FROM Usuario')
  usuarios = cursor.fetchall()
  print(usuarios)
  # abort(418)
  # return redirect(url_for('post', post_id = 6))
  # return render_template('form.html')
  return render_template('form.html', usuarios=usuarios)

@app.route('/home', methods=['GET'])
def home():
  return render_template('home.html', mensaje='Hola Mundo')
