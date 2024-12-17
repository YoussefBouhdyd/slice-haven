from flask import Flask, render_template, request ,redirect , url_for , jsonify
import sqlite3
import os

pizzeria = Flask(__name__)


UPLOAD_FOLDER = "static/images/"
pizzeria.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# create database for the app using SQLite

with sqlite3.connect("database/pizza_data.db") as database:
    cursor = database.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS pizza_data (
                    pizza_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT,
                    price INTEGER,
                    image_path TEXT
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS drink_data (
                    drink_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price INTEGER,
                    image_path TEXT
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS salad_data (
                    salad_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price INTEGER,
                    image_path TEXT
    )""")
    cursor.execute(""" CREATE TABLE IF NOT EXISTS order_data (
                    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    total INTEGER,
                    date TEXT,
                    client TEXT,
                    phone TEXT
    )""")
    database.commit()


@pizzeria.route('/')
def order():
    pizza_data = []
    drink_data = []
    salad_data = []
    with sqlite3.connect("database/pizza_data.db") as database:
        cursor = database.cursor()
        cursor.execute("SELECT pizza_id,type,price,image_path FROM pizza_data")
        pizza_data = cursor.fetchall()
        cursor.execute("SELECT drink_id,name,price,image_path FROM drink_data")
        drink_data = cursor.fetchall()
        cursor.execute("SELECT salad_id,name,price,image_path FROM salad_data")
        salad_data = cursor.fetchall()
    return render_template("order.html",pizza_data = pizza_data,drink_data = drink_data,salad_data = salad_data)

@pizzeria.route('/POST',  methods=['GET', 'POST'])
def insert():
    if request.form.get("form_type").split()[1] == "Pizza":
        pizza_type = request.form.get('type')
        price = request.form.get('price')
        image = request.files.get('image')
        if image:
            image_path = os.path.join("images/",image.filename)
            image.save(os.path.join(pizzeria.config['UPLOAD_FOLDER'],image.filename))
        with sqlite3.connect("database/pizza_data.db") as database:
            cursor = database.cursor()
            cursor.execute(f"INSERT INTO pizza_data (type,price,image_path) VALUES (? , ? , ?)",(pizza_type,price,image_path))
            database.commit()
    elif request.form.get("form_type").split()[1] == "Drink":
        drink_name = request.form.get('name')
        price = request.form.get('price')
        image = request.files.get('image')
        if image:
            image_path = os.path.join("images/",image.filename)
            image.save(os.path.join(pizzeria.config['UPLOAD_FOLDER'],image.filename))
        with sqlite3.connect("database/pizza_data.db") as database:
            cursor = database.cursor()
            cursor.execute(f"INSERT INTO drink_data (name,price,image_path) VALUES (? , ? , ?)",(drink_name,price,image_path))
            database.commit()
    elif request.form.get("form_type").split()[1] == "Salad":
        salad_name = request.form.get('name')
        price = request.form.get('price')
        image = request.files.get('image')
        if image:
            image_path = os.path.join("images/",image.filename)
            image.save(os.path.join(pizzeria.config['UPLOAD_FOLDER'],image.filename))
        with sqlite3.connect("database/pizza_data.db") as database:
            cursor = database.cursor()
            cursor.execute(f"INSERT INTO salad_data (name,price,image_path) VALUES (? , ? , ?)",(salad_name,price,image_path))
            database.commit()
    return redirect(url_for("order"))

@pizzeria.route('/delete', methods=['POST'])
def delete():
    product_id = request.json.get('id')
    product_id_type = request.json.get('idType')
    if (product_id_type == "pizzaId"):
        with sqlite3.connect("database/pizza_data.db") as database:
                cursor = database.cursor()
                cursor.execute("DELETE FROM pizza_data WHERE pizza_id = ?",(int(product_id),))
                database.commit()
    elif (product_id_type == "drinkId"):
            with sqlite3.connect("database/pizza_data.db") as database:
                cursor = database.cursor()
                cursor.execute("DELETE FROM drink_data WHERE drink_id = ?",(int(product_id),))
                database.commit()
    else:
        with sqlite3.connect("database/pizza_data.db") as database:
            cursor = database.cursor()
            cursor.execute("DELETE FROM salad_data WHERE salad_id = ?",(int(product_id),))
            database.commit()
    
    return jsonify({'success':True}) , 200

@pizzeria.route('/update', methods=['POST'])
def update():
    # ----------------
    new_image_path = "" # reserved for updating image 
    # -----------------------
    product_id = request.json.get('id')
    product_id_type = request.json.get('idType')
    productNewName = request.json.get('productName')
    productNewPrice = request.json.get('productPrice')
    if (product_id_type == "pizzaId"):
        with sqlite3.connect("database/pizza_data.db") as database:
                cursor = database.cursor()
                if (productNewName):
                    cursor.execute("UPDATE pizza_data SET type = ?  WHERE pizza_id = ?",(productNewName,int(product_id)))
                if (productNewPrice):
                    cursor.execute("UPDATE pizza_data SET price = ?  WHERE pizza_id = ?",(productNewPrice,int(product_id)))
                if (new_image_path):
                    cursor ("UPDATE pizza_data SET image_path = ? WHERE pizza_id = ?",(image_path,int(product_id)))
                database.commit()
    elif (product_id_type == "drinkId"):
            with sqlite3.connect("database/pizza_data.db") as database:
                cursor = database.cursor()
                if (productNewName):
                    cursor.execute("UPDATE drink_data SET name = ?  WHERE drink_id = ?",(productNewName,int(product_id)))
                if (productNewPrice):
                    cursor.execute("UPDATE drink_data SET price = ?  WHERE drink_id = ?",(productNewPrice,int(product_id)))
                if (new_image_path):
                    cursor ("UPDATE drink_data SET image_path = ? WHERE drink_id = ?",(image_path,int(product_id)))
                database.commit()
    else:
        with sqlite3.connect("database/pizza_data.db") as database:
                cursor = database.cursor()
                if (productNewName):
                    cursor.execute("UPDATE salad_data SET name = ?  WHERE salad_id = ?",(productNewName,int(product_id)))
                if (productNewPrice):
                    cursor.execute("UPDATE salad_data SET price = ?  WHERE salad_id = ?",(productNewPrice,int(product_id)))
                if (new_image_path):
                    cursor ("UPDATE salad_data SET image_path = ? WHERE salad_id = ?",(image_path,int(product_id)))
                database.commit()
    return jsonify({'success':True}) , 200

@pizzeria.route('/order', methods=['POST'])
def order_fill():
    client_name = request.json.get('clientName')
    client_phone = request.json.get('clientPhone')
    order_date = request.json.get('orderDate')
    order_total = request.json.get('orderTotal')

    with sqlite3.connect("database/pizza_data.db") as database:
        cursor = database.cursor()
        cursor.execute("INSERT INTO order_data (client,phone,date,total) VALUES (? , ? , ? , ?)",(client_name,client_phone,order_date,order_total))
        database.commit()
    
    return jsonify({'success':True}) , 200

@pizzeria.route('/records')
def records():
    order_data = []
    with sqlite3.connect("database/pizza_data.db") as database:
        cursor = database.cursor()
        cursor.execute("SELECT * FROM order_data ORDER BY order_id DESC")
        order_data = cursor.fetchall()
    return render_template("records.html",order_data = order_data)

if __name__ == '__main__':
    pizzeria.run(debug=True)
