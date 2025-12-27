from app import create_app, db
from app.models import Pizza, Drink , Salad

app = create_app()

with app.app_context():
    pizzas = [
        Pizza(type="Basil Pizza", price=35, image_path="images/pizza-4.jpg"),
        Pizza(type="Brussels Sprouts", price=20, image_path="images/pizza-7.jpg"),
        Pizza(type="Mixed Veggie Pizza", price=35, image_path="images/pizza-10.jpg"),
        Pizza(type="Vegetarian", price=20, image_path="images/pizza-8.jpg"),
        Pizza(type="Hawaiian", price=25, image_path="images/pizza-13.jpg"),
        Pizza(type="Four Cheese", price=25, image_path="images/pizza-6.jpg"),
        Pizza(type="Pepperoni", price=30, image_path="images/pizza-11.jpg"),
    ]
    
    drinks = [
        Drink(type="Cola", price=5, image_path="images/cola.avif"),
        Drink(type="Orange Juice", price=4, image_path="images/juice.jpg"),
        Drink(type="Full Mixed Berry Blend", price=15, image_path="images/berry.webp"),
        Drink(type="Lemonade", price=6, image_path="images/lemonad.webp"),
        Drink(type="Pink Lemonade", price=8, image_path="images/pinkLemond.webp"),
        Drink(type="Choclate Milk", price=10, image_path="images/chocolate-milk.jpg"),
    ]
    
    salads = [
        Salad(name="Caesar Sala", price=20, image_path="images/Caesar.jpg"),
        Salad(name="Greek Salad", price=20, image_path="images/Greek.avif"),
        Salad(name="Caprese Salad", price=24, image_path="images/Caprese.webp"),
        Salad(name="Italian Salad", price=12, image_path="images/italian.avif"),
        Salad(name="Garden Salad", price=15, image_path="images/Garden.jpg"),
    ]
        
    db.session.add_all(pizzas + drinks + salads)
    db.session.commit()
