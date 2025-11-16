from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# The function to connect to the MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      # add password here if MySQL has one
        database="productdb"
    )
    return conn

# The main page that shows all products
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    conn.close()
    return render_template('index.html', products=data)

# The page to add a new product
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        qty = request.form['quantity']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)", (name, price, qty))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add.html')

# The page to edit an existing product
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM products WHERE id=%s", (id,))
    product = cur.fetchone()

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        qty = request.form['quantity']
        cur.execute("UPDATE products SET name=%s, price=%s, quantity=%s WHERE id=%s", (name, price, qty, id))
        conn.commit()
        conn.close()
        return redirect('/')

    conn.close()
    return render_template('edit.html', product=product)

# The route is to delete a product
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

# The main starting point of the app
if __name__ == '__main__':
    app.run(debug=True)
