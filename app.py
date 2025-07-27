from flask import Flask, render_template, request, jsonify
import json
import datetime

app = Flask(__name__)

# Product list
products = [
    {"id": 1, "title": "Cheese Burger",        "price": 350, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cheeseburger.jpg/1200px-Cheeseburger.jpg"},
    {"id": 2, "title": "Chicken Pizza",         "price": 600, "image": "https://chefadora.b-cdn.net/medium_1000529681_7684043161.jpg"},
    {"id": 3, "title": "Zinger Burger",         "price": 400, "image": "https://aroojshop.com/wp-content/uploads/2025/01/Serve.jpg"},
    {"id": 4, "title": "French Fries",          "price": 200, "image": "https://crownful.s3.amazonaws.com/recipe/6c46024a2d6a4a6499c5a1a62d8cdd5b.png"},
    {"id": 5, "title": "Grilled Sandwich",      "price": 250, "image": "https://wiproappliances.com/cdn/shop/articles/Veg_grilled_cheese_sandwich.jpg?v=1714126819"},
    {"id": 6, "title": "Chicken Wings",         "price": 450, "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTej2R3HlvU6Ty9b9Se2hCgRTIeLRbtOq-uTw3hXc1hAe7XtSSZJs8GIYpUQTCfini3DYg&usqp=CAU"},
    {"id": 7, "title": "Chicken Shawarma",      "price": 220, "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSTgicv8RYytNdSaqW-ColdVUKXog36QPopg&s"},
    {"id": 8, "title": "Club Sandwich",         "price": 280, "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnBlBfoF7g8TUKA3LTBiUYdbvF2rbi1YNeaA&s"},
    {"id": 9, "title": "Loaded Nachos",         "price": 350, "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQivwGhEFWgWyNDmtTri5E7N500EXY1kzLTzw&s"},
    {"id": 10, "title": "Hot Dog",              "price": 260, "image": "https://static01.nyt.com/images/2024/06/28/multimedia/28GRILL-HOTDOGS-REX-cqwj/01GRILL-HOTDOGS-REX-cqwj-tmagSF.jpg"},
    {"id": 11, "title": "Crispy Broast",        "price": 390, "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSeNybFv1NJxMJ8VSpeaaL76e-xLU_7wwNIE2afUxLNAfoIABwo-NF-eRH63lyD5i3zR0&usqp=CAU"},
    {"id": 12, "title": "Beef Burger",          "price": 380, "image": "https://ichef.bbci.co.uk/food/ic/food_16x9_1600/recipes/spicybeefburger_71357_16x9.jpg"},
    {"id": 13, "title": "Garlic Mayo Fries",    "price": 240, "image": "https://i.ytimg.com/vi/v2P63qtAiaI/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDLGLtqwQZaw5vKfSGprpdlTBBWvw"},
    {"id": 14, "title": "Stuffed Crust Pizza",  "price": 700, "image": "https://www.sugarsaltmagic.com/wp-content/uploads/2020/03/Stuffed-Crust-Pepperoni-Pizza-1.jpg"},
    {"id": 15, "title": "Hotdog Deluxe",         "price": 270, "image": "https://img.hellofresh.com/f_auto,fl_lossy,q_auto,w_1200/hellofresh_s3/image/HelloFresh_Y20_R2408_W20_BNL_KC6838-1_Main_F4low-7cb4f820.jpg"},
    {"id": 16, "title": "Mozzarella Sticks",    "price": 320, "image": "https://carlsbadcravings.com/wp-content/uploads/2025/01/Mozzarella-Sticks-18b.jpg"},
    {"id": 17, "title": "Fried Chicken Bucket", "price": 850, "image": "https://img.freepik.com/premium-photo/crispy-fried-chicken-bucket-chicken-bucket_434193-7699.jpg"},
    {"id": 18, "title": "Chicken Tikka Pizza",  "price": 620, "image": "https://caffeinobistro.com/cdn/shop/files/ff.webp?v=1739741980"},
    {"id": 19, "title": "Veggie Sandwich",      "price": 230, "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRr-jCTHvywQuOAiiEqAaZ90Q_i36oYtroy-vNS1ZV3WupEG5J0PEzwBAzzq6RDiJo1E8I&usqp=CAU"},
    {"id": 20, "title": "Spicy Chicken Soap",   "price": 290, "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR21l3VxZwtWn3_RTr0ZypbUiO5HsdrQ9J8dYfXhAvAMXcF3SwnaRKX5jHb2EaONQhtz38&usqp=CAU"}
]




@app.route('/')
def index():
    return render_template("index.html", products=products)

@app.route('/order', methods=['POST'])
def place_order():
    try:
        data = request.get_json()
        cart = data.get("cart", [])

        if not cart:
            return jsonify({"status": "error", "message": "Cart is empty!"}), 400

        total = sum(item['price'] for item in cart)

        order_data = {
            "timestamp": str(datetime.datetime.now()),
            "items": cart,
            "total_price": total
        }

        try:
            with open("order_history.json", "r") as file:
                order_history = json.load(file)
        except FileNotFoundError:
            order_history = []

        order_history.append(order_data)

        with open("order_history.json", "w") as file:
            json.dump(order_history, file, indent=2)

        return jsonify({"status": "success", "message": "✅ Order placed successfully!"})
    
    except Exception as e:
        print("Error placing order:", e)
        return jsonify({"status": "error", "message": "Successfully to place order."}), 500

if __name__ == '__main__':
    app.run(debug=True)
