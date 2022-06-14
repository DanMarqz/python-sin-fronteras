from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)

import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='dani',
  password='passwd',
  database='my_test'
)

cursor = mydb.cursor(dictionary=True)

@app.route('/')
def index():
  return home()

# Pueden estar en una sola funcion GET y POST o estar separadas
@app.route('/post/<post_id>', methods=['GET','POST'])
def post(post_id):
  if request.method == 'GET':
    return 'El ID del post es: ' + post_id  
  else: 
    return 'Este es otro metodo que no es GET'

@app.route('/users', methods=['POST', 'GET'])
def users():
  cursor.execute('SELECT * FROM Usuario')
  usuarios = cursor.fetchall()
  print(usuarios)
  # abort(418)
  # return redirect(url_for('post', post_id = 6))
  # return render_template('users.html')
  return render_template('users.html', usuarios=usuarios)

@app.route('/home', methods=['GET'])
def home():
  return render_template('home.html', mensaje='Hola Mundo')

@app.route('/crear', methods=['GET', 'POST'])
def crear():
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    edad = request.form['edad']
    sql = 'INSERT INTO Usuario (username, email, edad) VALUES (%s, %s, %s)'
    values = (username, email, edad)
    cursor.execute(sql, values)
    mydb.commit()

    return redirect(url_for('users'))
  return render_template('crear.html')