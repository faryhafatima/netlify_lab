
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (matches the products in the Odoo lab)
products = [
    {"id": 1, "name": "Laptop",   "price": 150000, "stock": 14},
    {"id": 2, "name": "Mouse",    "price": 2000,   "stock": 30},
    {"id": 3, "name": "Keyboard", "price": 4000,   "stock": 40},
]

@app.route("/")
def home():
    return jsonify({"message": "XYZ Traders backend is running"})

@app.route("/api/products")
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)
