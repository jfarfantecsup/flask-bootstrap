from flask import Flask, render_template,request,url_for,redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'plutondb'

mysql = MySQL(app)

app.secret_key='Tecsup123'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('select * from contactos')
    data = cur.fetchall()
    return render_template('index.html',contactos=data)

@app.route('/agregar',methods=['POST'])
def agregar():
    if request.method == 'POST':
        nom= request.form['nombres']
        tel= request.form['telefono']
        email= request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('insert into contactos(nombres,telefono,email) values (%s,%s,%s)',(nom,tel,email))
        mysql.connection.commit()
        return redirect(url_for('index'))

    return render_template('productos.html')

@app.route('/delete')
def categorias():
    return render_template('categorias.html')

if __name__ == '__main__':
    app.run(debug=True,port=3000, host='0.0.0.0')