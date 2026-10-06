from flask import Flask, request, jsonify

app = Flask(__name__)


# PRODUCT DATA

products = {
    1: {
        "name": "Laptop",
        "category": "Electronics",
        "price": 55000,
        "quantity": 10
    },
    2: {
        "name": "Mouse",
        "category": "Electronics",
        "price": 800,
        "quantity": 25
    },
    3: {
        "name": "Running Shoes",
        "category": "Footwear",
        "price": 2500,
        "quantity": 15
    }
}


# 1. HOME API

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "E-Commerce Flask API is working!"
    })


# 2. GET PRODUCT

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):

    if product_id not in products:

        return jsonify({
            "message": "Product not found"
        }), 404

    return jsonify(products[product_id])


# 3. SEARCH PRODUCTS

@app.route("/search", methods=["GET"])
def search_products():

    category = request.args.get("category")

    results = []

    for product in products.values():

        if product["category"].lower() == category.lower():

            results.append(product)

    return jsonify(results)


# 4. ADD PRODUCT

@app.route("/products", methods=["POST"])
def add_product():

    data = request.get_json()

    new_id = max(products.keys()) + 1

    products[new_id] = data

    return jsonify({
        "message": "Product added successfully",
        "product_id": new_id,
        "product": products[new_id]
    }), 201


# 5. UPDATE PRODUCT - PUT

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):

    if product_id not in products:

        return jsonify({
            "message": "Product not found"
        }), 404

    data = request.get_json()

    products[product_id] = data

    return jsonify({
        "message": "Product updated successfully",
        "product_id": product_id,
        "product": products[product_id]
    })


# 6. DELETE PRODUCT

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):

    if product_id not in products:

        return jsonify({
            "message": "Product not found"
        }), 404

    deleted_product = products.pop(product_id)

    return jsonify({
        "message": "Product deleted successfully",
        "product_id": product_id,
        "product": deleted_product
    })


# 7. PATCH PRODUCT

@app.route("/products/<int:product_id>", methods=["PATCH"])
def patch_product(product_id):

    if product_id not in products:

        return jsonify({
            "message": "Product not found"
        }), 404

    data = request.get_json()

    products[product_id].update(data)

    return jsonify({
        "message": "Product partially updated",
        "product_id": product_id,
        "product": products[product_id]
    })


# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":
    app.run(debug=True)