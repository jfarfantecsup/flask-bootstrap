from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/categorias')
def categorias():
    return render_template('categorias.html')

if __name__ == '__main__':
    app.run(debug=True,port=3000)