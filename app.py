
from flask import Flask, render_template, abort

app = Flask(__name__)

# Sample menu data
SAMPLE_ITEMS = [
    {
        "id": 1,
        "name": "Café con Leche",
        "category": "Drinks",
        "description": "Traditional Cuban coffee with steamed milk.",
        "price_cents": 350
    },
    {
        "id": 2,
        "name": "Cuban Sandwich",
        "category": "Food",
        "description": "Roasted pork, ham, Swiss cheese, pickles, and mustard.",
        "price_cents": 850
    },
    {
        "id": 3,
        "name": "Guava Pastelito",
        "category": "Pastries",
        "description": "Flaky pastry filled with sweet guava.",
        "price_cents": 250
    },
    {
        "id": 4,
        "name": "Cuban Toast",
        "category": "Food",
        "description": "Fresh Cuban bread toasted with butter.",
        "price_cents": 200
    },
    {
        "id": 5,
        "name": "Cortadito",
        "category": "Drinks",
        "description": "Strong Cuban espresso with a touch of steamed milk.",
        "price_cents": 275
    },
    {
        "id": 6,
        "name": "Ham Croqueta",
        "category": "Food",
        "description": "Traditional Cuban ham croquette.",
        "price_cents": 175
    }
]


# Sample kitchen orders
SAMPLE_KITCHEN_ORDERS = [
    {
        "id": 1001,
        "customer": "Alex Rodriguez",
        "items": "Cuban Sandwich, 2 Pastelitos, Coffee",
        "status": "Preparing"
    },
    {
        "id": 1002,
        "customer": "Maria Lopez",
        "items": "2 Cuban Toast, Café con Leche",
        "status": "Pending"
    },
    {
        "id": 1003,
        "customer": "David Perez",
        "items": "3 Pastelitos, 2 Coffees",
        "status": "Ready"
    },
    {
        "id": 1004,
        "customer": "Sofia Garcia",
        "items": "Cuban Sandwich",
        "status": "Preparing"
    }
]


# Sample order history
SAMPLE_ORDERS = [
    {
        "id": 1001,
        "date": "October 29, 2026",
        "items": "Cuban Sandwich, Coffee, Pastelitos",
        "total_cents": 1700,
        "status": "Preparing"
    },
    {
        "id": 998,
        "date": "October 27, 2026",
        "items": "Café con Leche, Cuban Toast",
        "total_cents": 550,
        "status": "Completed"
    },
    {
        "id": 992,
        "date": "October 24, 2026",
        "items": "2 Cuban Sandwiches",
        "total_cents": 1700,
        "status": "Completed"
    }
]

#Sample order items
SAMPLE_ORDER_ITEMS = [
    {"name": "Café con Leche", "quantity": 1, "price_cents": 350},
    {"name": "Guava Pastelito", "quantity": 2, "price_cents": 250},
    {"name": "Cuban Sandwich", "quantity": 1, "price_cents": 850}
]


# Home page
@app.route("/")
def index():
    return render_template("index.html")


# Menu page
@app.route("/menu")
def menu():
    return render_template("menu.html", items=SAMPLE_ITEMS)


# Individual menu item
@app.route("/menu/<int:item_id>")
def item_detail(item_id):
    item = next(
        (item for item in SAMPLE_ITEMS if item["id"] == item_id),
        None
    )

    if item is None:
        abort(404)

    return render_template("item.html", item=item)


# New order page
@app.route("/order/new")
def new_order():
    total_cents = sum(
        item["quantity"] * item["price_cents"]
        for item in SAMPLE_ORDER_ITEMS
    )

    return render_template(
        "order.html",
        order_items=SAMPLE_ORDER_ITEMS,
        customer="Alex Rodriguez",
        total_cents=total_cents
    )

# Kitchen board
@app.route("/kitchen")
def kitchen():
    return render_template(
        "kitchen.html",
        orders=SAMPLE_KITCHEN_ORDERS
    )


# Order history
@app.route("/orders")
def orders():
    return render_template(
        "history.html",
        orders=SAMPLE_ORDERS
    )


# Order confirmation
@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")


# Menu administration
@app.route("/menu-admin")
def menu_admin():
    return render_template(
        "menu-admin.html",
        items=SAMPLE_ITEMS
    )


if __name__ == "__main__":
    app.run(debug=True)
