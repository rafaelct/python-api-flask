from flask import Flask, jsonify, request
from controllers.Registry import Registry
from controllers.Auth import Auth
from controllers.Customers import Customers
from controllers.Products import Products
from controllers.Carts import Carts
from controllers.Orders import Orders
import os

app = Flask(__name__)

@app.route("/registry", methods=['POST'])
def epRegistryPOST():
    registry = Registry()

    return registry.methodPost(request=request)

@app.route("/auth", methods=['POST'])
def epAuthPOST():
    auth = Auth()

    return auth.methodPost(request=request)

@app.route("/customers/get", methods=['POST'])
def epCustomersGET():
    customers = Customers()

    return customers.methodGet(request=request)

@app.route("/customers", methods=['POST'])
def epCustomersPOST():
    customers = Customers()

    return customers.methodPost(request=request)

@app.route("/customers", methods=['PUT'])
def epCustomersPUT():
    customers = Customers()

    return customers.methodPut(request=request)

@app.route("/customers", methods=['DELETE'])
def epCustomersDELETE():
    customers = Customers()

    return customers.methodDelete(request=request)

@app.route("/products/get", methods=['POST'])
def epProductsGET():
    products = Products()

    return products.methodGet(request=request)

@app.route("/products", methods=['POST'])
def epProductsPOST():
    products = Products()

    return products.methodPost(request=request)

@app.route("/products", methods=['PUT'])
def epProductsPUT():
    products = Products()

    return products.methodPut(request=request)

@app.route("/products", methods=['DELETE'])
def epProductsDELETE():
    products = Products()

    return products.methodDelete(request=request)

@app.route("/orders/get", methods=['POST'])
def epOrdersGET():
    orders = Orders()

    return orders.methodGet(request=request)

@app.route("/orders", methods=['POST'])
def epOrdersPOST():
    orders = Orders()

    return orders.methodPost(request=request)

@app.route("/carts/get", methods=['POST'])
def epCartsGET():
    carts = Carts()

    return carts.methodGet(request=request)

@app.route("/carts", methods=['POST'])
def epCartsPOST():
    carts = Carts()

    return carts.methodPost(request=request)

@app.route("/carts", methods=['DELETE'])
def epCartsDELETE():
    carts = Carts()

    return carts.methodDelete(request=request)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port)
