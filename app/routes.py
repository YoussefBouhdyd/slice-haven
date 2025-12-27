from flask import render_template,request,redirect,url_for,jsonify
import os
from app.models import Pizza, Drink, Salad , Order


def register_routes(app,db):
    @app.route('/')
    def order():
        pizza_data = Pizza.query.all()
        drink_data = Drink.query.all()
        salad_data = Salad.query.all()    
        return render_template("order.html", pizza_data=pizza_data, drink_data=drink_data, salad_data=salad_data)
    
    @app.route('/POST',  methods=['GET', 'POST'])
    def insert():
        if request.form.get("form_type").split()[1] == "Pizza":
            pizza_type = request.form.get('type')
            price = request.form.get('price')
            image = request.files.get('image')
            if image:
                image_path = os.path.join("images/",image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'],image.filename))
            pizza = Pizza(type=pizza_type, price=price, image_path=image_path)
            db.session.add(pizza)
            db.session.commit()
        elif request.form.get("form_type").split()[1] == "Drink":
            drink_name = request.form.get('name')
            price = request.form.get('price')
            image = request.files.get('image')
            if image:
                image_path = os.path.join("images/",image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'],image.filename))
            drink = Drink(type=drink_name, price=price, image_path=image_path)
            db.session.add(drink)
            db.session.commit()
        elif request.form.get("form_type").split()[1] == "Salad":
            salad_name = request.form.get('name')
            price = request.form.get('price')
            image = request.files.get('image')
            if image:
                image_path = os.path.join("images/",image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'],image.filename))
            salad = Salad(name=salad_name, price=price, image_path=image_path)
            db.session.add(salad)
            db.session.commit()
        return redirect(url_for("order"))

    @app.route('/delete', methods=['POST'])
    def delete():
        product_id = request.json.get('id')
        product_id_type = request.json.get('idType')
        if product_id_type == "pizzaId":
            pizza = Pizza.query.get(int(product_id))
            if pizza:
                db.session.delete(pizza)
                db.session.commit()
        elif product_id_type == "drinkId":
            drink = Drink.query.get(int(product_id))
            if drink:
                db.session.delete(drink)
                db.session.commit()
        else:
            salad = Salad.query.get(int(product_id))
            if salad:
                db.session.delete(salad)
                db.session.commit()    
        return jsonify({'success':True}) , 200
    
    @app.route('/update', methods=['POST'])
    def update():
        # ----------------
        new_image_path = "" # reserved for updating image 
        # -----------------------
        product_id = request.json.get('id')
        product_id_type = request.json.get('idType')
        productNewName = request.json.get('productName')
        productNewPrice = request.json.get('productPrice')
        if product_id_type == "pizzaId":
            pizza = Pizza.query.get(int(product_id))
            if pizza:
                if productNewName:
                    pizza.type = productNewName
                if productNewPrice:
                    pizza.price = productNewPrice
                if new_image_path:
                    pizza.image_path = new_image_path
                db.session.commit()
        elif product_id_type == "drinkId":
            drink = Drink.query.get(int(product_id))
            if drink:
                if productNewName:
                    drink.type = productNewName
                if productNewPrice:
                    drink.price = productNewPrice
                if new_image_path:
                    drink.image_path = new_image_path
                db.session.commit()
        else:
            salad = Salad.query.get(int(product_id))
            if salad:
                if productNewName:
                    salad.name = productNewName
                if productNewPrice:
                    salad.price = productNewPrice
                if new_image_path:
                    salad.image_path = new_image_path
                db.session.commit()
        return jsonify({'success':True}) , 200
    
    @app.route('/order', methods=['POST'])
    def order_fill():
        client_name = request.json.get('clientName')
        client_phone = request.json.get('clientPhone')
        order_date = request.json.get('orderDate')
        order_total = request.json.get('orderTotal')

        order = Order(client=client_name, phone=client_phone, date=order_date, total=order_total)
        db.session.add(order)
        db.session.commit()
        
        return jsonify({'success':True}) , 200
    
    @app.route('/records')
    def records():
        order_data = Order.query.order_by(Order.id.desc()).all()
        return render_template("records.html",order_data = order_data)