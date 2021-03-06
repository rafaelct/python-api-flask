import requests
from testweb.Customers import *
from testweb.Products import *
from testweb.Carts import *
from testweb.Orders import *


def get_headers() :
    headers = {}
    headers['content-type'] = "application/json"
    return headers

def test_registry_add() :

    data = {}
    data['loginname'] = "teste"
    data['password'] = "teste"
    data['fullname'] = "Teste o tal"

    data = str(data).replace("'",'"')

    print(data)


    headers = get_headers()

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/registry",headers=headers,data=data).json()
    print(txt)

    assert txt['codReturn'] == 0
    
def test_registry_add_unique_constraint() :


    data = {}
    data['loginname'] = "teste"
    data['password'] = "teste"
    data['fullname'] = "Teste o tal"
    
    data = str(data).replace("'",'"')

    print(data)


    headers = get_headers()

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/registry",headers=headers,data=data).json()
    print(txt)

    assert txt['codReturn'] == 1
    
def test_auth_get() :

    data = {}
    data['loginname'] = "teste"
    data['password'] = "teste"
    data['fullname'] = "Teste o tal"
    
    data = str(data).replace("'",'"')

    print(data)


    headers = get_headers()

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/auth",headers=headers,data=data).json()
    print(txt)

    assert txt['codReturn'] == 0
    
def auth_get(loginname,password) :

    data = {}
    data['loginname'] = loginname
    data['password'] = password
    
    data = str(data).replace("'",'"')

    print(data)


    headers = get_headers()

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/auth",headers=headers,data=data).json()
    print(txt)

    return txt['data']['token']
        
def test_Customers_add() :

    token = auth_get(loginname="teste",password="teste")

    #data = {}
    #data['token'] = token
    #data['name'] = "Fulano"
    #data['fullname'] = "Fulano de tal"
    #data['birth'] = "05/04/1960"
    #data['document'] = "25305309042"
    #data['gender'] = "M"
    
    data = add_customers_json(token=token,name="Fulano",fullname="Fulano de tal",birth="05/04/1960",document="25305309042",gender="M")
    #data = str(data).replace("'",'"')

    print(data)


    headers = get_headers()

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/customers",headers=headers,data=data).json()
    print(txt)

    assert txt['codReturn'] == 0
    
    #data = {}
    #data['token'] = token
    #data['name'] = "Siclano"
    #data['fullname'] = "Siclano de tali"
    #data['birth'] = "01/11/1977"
    #data['document'] = "14926960052"
    #data['gender'] = "M"
    
    #data = str(data).replace("'",'"')

    data = add_customers_json(token=token,name="Siclano",fullname="Siclano de tali",birth="01/11/1977",document="14926960052",gender="M")
    
    print(data)


    headers = get_headers()
    
    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/customers",headers=headers,data=data).json()
    print(txt)

    assert txt['codReturn'] == 0

def test_Customers_getAll() :
    
    token = auth_get(loginname="teste",password="teste")
    #data = {}
    #data['token'] = token
    #data = str(data).replace("'",'"')

    data = getAll_customers_json(token=token)

    headers = get_headers()

    arrayData = []

    dataWaited = {}
    dataWaited['name'] = "Fulano"
    dataWaited['fullname'] = "Fulano de tal"
    dataWaited['birth'] = "05/04/1960"
    dataWaited['document'] = "25305309042"
    dataWaited['gender'] = "M"

    arrayData.append(dataWaited)

    dataWaited = {}
    dataWaited['name'] = "Siclano"
    dataWaited['fullname'] = "Siclano de tali"
    dataWaited['birth'] = "01/11/1977"
    dataWaited['document'] = "14926960052"
    dataWaited['gender'] = "M"

    arrayData.append(dataWaited)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/customers/get",headers=headers,data=data).json()
    print(txt)
    listProducts = txt['data']


    i = 0

    for item in listProducts :
        assert item['name'] == arrayData[i]['name']
        assert item['fullname'] == arrayData[i]['fullname']
        assert item['birth'] == arrayData[i]['birth']
        assert item['document'] == arrayData[i]['document']
        assert item['gender'] == arrayData[i]['gender']
        i = i + 1



    assert len(listProducts) == 2

def test_Customers_get() :
    token = auth_get(loginname="teste",password="teste")
    data = get_customers_json(token=token,id="1")
    #data = {}
    #data['token'] = token
    #data['id'] = "1"
    #data = str(data).replace("'",'"')

    headers = get_headers()

    arrayData = []

    dataWaited = {}
    dataWaited['name'] = "Fulano"
    dataWaited['fullname'] = "Fulano de tal"
    dataWaited['birth'] = "05/04/1960"
    dataWaited['document'] = "25305309042"
    dataWaited['gender'] = "M"

    arrayData.append(dataWaited)
    
    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/customers/get",headers=headers,data=data).json()
    print(txt)
    
    listProducts = txt['data']


    i = 0

    for item in listProducts :
        assert item['name'] == arrayData[i]['name']
        assert item['fullname'] == arrayData[i]['fullname']
        assert item['birth'] == arrayData[i]['birth']
        assert item['document'] == arrayData[i]['document']
        assert item['gender'] == arrayData[i]['gender']
        i = i + 1



    assert len(listProducts) == 1

def test_Customers_update() :

    token = auth_get(loginname="teste",password="teste")

    data = update_customers_json(id="1",token=token,name="Fulana",fullname="Fulana de tal",birth="05/05/1988",document="25305309042",gender="F")
    #data = {}
    #data['token'] = token
    #data['id'] = "1"
    #data['name'] = "Fulana"
    #data['fullname'] = "Fulana de tal"
    #data['birth'] = "05/05/1988"
    #data['document'] = "25305309042"
    #data['gender'] = "F"
    
    #data = str(data).replace("'",'"')

    print(data)

    
    headers = get_headers()
    
    txt = requests.put("https://calm-hamlet-60163.herokuapp.com/customers",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    #customersModel.update(id=1,name="Fulana",fullname="Fulana de tal",birth="05/05/1988",document="25305309042",gender="F")

    data = get_customers_json(token=token,id="1")

    #data = {}
    #data['token'] = token
    #data['id'] = "1"
    #data = str(data).replace("'",'"')

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/customers/get",headers=headers,data=data).json()
    print(txt)

    listProducts = txt['data']

    assert listProducts[0]['name'] == "Fulana"
    assert listProducts[0]['fullname'] == "Fulana de tal"
    assert listProducts[0]['birth'] == "05/05/1988"
    assert listProducts[0]['document'] == "25305309042"
    assert listProducts[0]['gender'] == "F"
    
def test_Products_add() :
    token = auth_get(loginname="teste",password="teste")

    data = add_products_json(token=token,name="Batedeira",brand="Arno",qtd="1",codProduct="1",linkImg="/1.png",price="1320.99")
    print(data)
    #codReturn = productsModel.add(name="Batedeira",brand="Arno",qtd="1",codProduct="1",linkImg="/1.png")
    headers = get_headers()

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/products",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    token = auth_get(loginname="teste",password="teste")
    
    data = add_products_json(token=token,name="Fogao",brand="Brastemp",qtd="2",codProduct="2",linkImg="/2.png",price="500.00")
    print(data)
    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/products",headers=headers,data=data).json()
    print(txt)
 
    assert txt['codReturn'] == 0

    #codReturn = productsModel.add(name="Fogão",brand="Brastemp",qtd="2",codProduct="2",linkImg="/2.png")

def test_Products_unique_constraint_codProduct_in_table_products():
    token = auth_get(loginname="teste",password="teste")

    data = add_products_json(token=token,name="Batedeira",brand="Arno",qtd="1",codProduct="1",linkImg="/1.png",price="1320.99")
    print(data)
    #codReturn = productsModel.add(name="Batedeira",brand="Arno",qtd="1",codProduct="1",linkImg="/1.png")
    headers = get_headers()
    #headers['content-type'] = "application/json"

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/products",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 1

    data = add_products_json(token=token,name="Fogao",brand="Brastemp",qtd="2",codProduct="2",linkImg="/2.png",price="500.00")
    
    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/products",headers=headers,data=data).json()
    print(txt)
 
    assert txt['codReturn'] == 1

def test_Products_get() :
    #productsModel = ProductsModel()

    token = auth_get(loginname="teste",password="teste")

    data = get_products_json(token=token,id="1")

    print(data)
    #codReturn = productsModel.add(name="Batedeira",brand="Arno",qtd="1",codProduct="1",linkImg="/1.png")
    headers = get_headers()
    #headers['content-type'] = "application/json"

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/products/get",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    listProducts = txt['data']

    arrayDados = []

    dataWaited = {}
    dataWaited['name'] = "Batedeira"
    dataWaited['brand'] = "Arno"
    dataWaited['qtd'] = 1
    dataWaited['codProduct'] = 1
    dataWaited['linkImg'] = "/1.png"
    dataWaited['price'] = "$1,320.99"

    arrayDados.append(dataWaited)

    
    #listProducts = productsModel.get(id=1)


    i = 0

    for item in listProducts :
        assert item['name'] == arrayDados[i]['name']
        assert item['brand'] == arrayDados[i]['brand']
        assert item['qtd'] == arrayDados[i]['qtd']
        assert item['codProduct'] == arrayDados[i]['codProduct']
        assert item['linkImg'] == arrayDados[i]['linkImg']
        assert item['price'] == arrayDados[i]['price']
        i = i + 1



    assert len(listProducts) == 1

def test_Products_getAll() :

    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = getAll_products_json(token=token)

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/products/get",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    listProducts = txt['data']

    arrayData = []

    dataWaited = {}
    dataWaited['name'] = "Batedeira"
    dataWaited['brand'] = "Arno"
    dataWaited['qtd'] = 1
    dataWaited['codProduct'] = 1
    dataWaited['linkImg'] = "/1.png"
    dataWaited['price'] = "$1,320.99"

    arrayData.append(dataWaited)

    dataWaited = {}
    dataWaited['name'] = "Fogao"
    dataWaited['brand'] = "Brastemp"
    dataWaited['qtd'] = 2
    dataWaited['codProduct'] = 2
    dataWaited['linkImg'] = "/2.png"
    dataWaited['price'] = "$500.00"

    arrayData.append(dataWaited)

    
    #listProducts = productsModel.getAll()


    i = 0

    for item in listProducts :
        assert item['name'] == arrayData[i]['name']
        assert item['brand'] == arrayData[i]['brand']
        assert item['qtd'] == arrayData[i]['qtd']
        assert item['codProduct'] == arrayData[i]['codProduct']
        assert item['linkImg'] == arrayData[i]['linkImg']
        assert item['price'] == arrayData[i]['price']
        i = i + 1



    assert len(listProducts) == 2


def test_Products_addQtd() :
    #productsModel = ProductsModel()

    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = addQtd_products_json(token=token,id="1",qtd="2")

    print(data)

    txt = requests.put("https://calm-hamlet-60163.herokuapp.com/products",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    #productsModel.addQtd(id=1,qtd=2)
    
    token = auth_get(loginname="teste",password="teste")

    data = addQtd_products_json(token=token,id="2",qtd="4")

    print(data)

    txt = requests.put("https://calm-hamlet-60163.herokuapp.com/products",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    #productsModel.addQtd(id=2,qtd=4)

    token = auth_get(loginname="teste",password="teste")

    data = get_products_json(token=token,id="1")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/products/get",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    arrayData = txt['data']

    #arrayData = productsModel.get(id=1)
    print(arrayData)
    assert arrayData[0]['qtd'] == 3
    
    token = auth_get(loginname="teste",password="teste")

    data = get_products_json(token=token,id="2")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/products/get",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    arrayData = txt['data']

    #arrayData = productsModel.get(id=2)
    assert arrayData[0]['qtd'] == 6
    
def test_Products_removeQtd() :
    #productsModel = ProductsModel()

    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = removeQtd_products_json(token=token,id="1",qtd="2")

    print(data)

    txt = requests.delete("https://calm-hamlet-60163.herokuapp.com/products",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0


    #productsModel.removeQtd(id=1,qtd=2)

    token = auth_get(loginname="teste",password="teste")

    data = removeQtd_products_json(token=token,id="2",qtd="2")

    print(data)

    txt = requests.delete("https://calm-hamlet-60163.herokuapp.com/products",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    #productsModel.removeQtd(id=2,qtd=2)

    token = auth_get(loginname="teste",password="teste")

    data = get_products_json(token=token,id="1")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/products/get",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    arrayData = txt['data']

    #arrayData = productsModel.get(id=1)
    assert arrayData[0]['qtd'] == 1

    token = auth_get(loginname="teste",password="teste")

    data = get_products_json(token=token,id="2")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/products/get",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    arrayData = txt['data']

    #arrayData = productsModel.get(id=2)
    assert arrayData[0]['qtd'] == 4

def test_Products_update() :
    #productsModel = ProductsModel()

    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = update_products_json(token=token,id="1",name="Batedeira",brand="Wallita",codProduct="1",linkImg="/1.png",price="1320.99")

    print(data)

    txt = requests.put("https://calm-hamlet-60163.herokuapp.com/products",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    token = auth_get(loginname="teste",password="teste")

    data = get_products_json(token=token,id="1")

    print(data)
   
    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/products/get",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    listProducts = txt['data']

    #productsModel.update(id=1,name="Batedeira",brand="Wallita",codProduct="1",linkImg="/1.png")

    #listProducts = productsModel.get(id=1)

    assert listProducts[0]['brand'] == "Wallita"

def test_Carts_add() :
    #cartsModel = CartsModel()

    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = add_carts_json(token=token,customerId="1",productId="1")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/carts",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0


    #codReturn = cartsModel.add(customerId=1,productId=1)
    #assert codReturn == 0

    token = auth_get(loginname="teste",password="teste")

    data = add_carts_json(token=token,customerId="2",productId="2")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/carts",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    #codReturn = cartsModel.add(customerId=2,productId=2)
    #assert codReturn == 0
    
    token = auth_get(loginname="teste",password="teste")

    data = add_carts_json(token=token,customerId="2",productId="1")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/carts",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    #codReturn = cartsModel.add(customerId=2,productId=1)
    #assert codReturn == 0

def test_Carts_getAll() :
    #cartsModel = CartsModel()

    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = getAll_carts_json(token=token)

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/carts/get",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    listCarts = txt['data']

    arrayData = []

    dataWaited = {}
    dataWaited['customerId'] = 1
    dataWaited['productId'] = 1

    arrayData.append(dataWaited)

    dataWaited = {}
    dataWaited['customerId'] = 2
    dataWaited['productId'] = 2

    arrayData.append(dataWaited)

    dataWaited = {}
    dataWaited['customerId'] = 2
    dataWaited['productId'] = 1

    arrayData.append(dataWaited)

    
    #listCarts = cartsModel.getAll()


    i = 0

    for item in listCarts :
        assert item['customerId'] == arrayData[i]['customerId']
        assert item['productId'] == arrayData[i]['productId']
        i = i + 1

    assert len(listCarts) == 3

def test_Carts_get() :
    #cartsModel = CartsModel()

    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = get_carts_json(token=token,id="1")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/carts/get",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    listCarts = txt['data']

    arrayData = []

    dataWaited = {}
    dataWaited['customerId'] = 1
    dataWaited['productId'] = 1

    arrayData.append(dataWaited)
    
    #listCarts = cartsModel.get(id=1)


    i = 0

    for item in listCarts :
        assert item['customerId'] == arrayData[i]['customerId']
        assert item['productId'] == arrayData[i]['productId']
        i = i + 1

    assert len(listCarts) == 1

def test_Carts_getCustomer() :
    #cartsModel = CartsModel()

    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = getCustomer_carts_json(token=token,customerId="2")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/carts/get",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    listCarts = txt['data']

    arrayData = []

    
    dataWaited = {}
    dataWaited['customerId'] = 2
    dataWaited['productId'] = 2

    arrayData.append(dataWaited)

    dataWaited = {}
    dataWaited['customerId'] = 2
    dataWaited['productId'] = 1

    arrayData.append(dataWaited)

    #listCarts = cartsModel.getCustomer(customerId=2)


    i = 0

    for item in listCarts :
        assert item['customerId'] == arrayData[i]['customerId']
        assert item['productId'] == arrayData[i]['productId']
        i = i + 1

    assert len(listCarts) == 2

def test_Orders_add() :
    #ordersModel = OrdersModel()

    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = add_orders_json(token=token,customerId="2")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/orders",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    token = auth_get(loginname="teste",password="teste")

    data = getCustomer_orders_json(token=token,customerId="2")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/orders/get",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    itemReturn = txt['data']

    #itemReturn = ordersModel.add(customerId=2)

    assert itemReturn[0]['customerId'] == 2
    assert itemReturn[0]['productId'] == 2

    assert itemReturn[1]['customerId'] == 2
    assert itemReturn[1]['productId'] == 1

def test_Orders_getAll() :
    #ordersModel = OrdersModel()

    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = getAll_orders_json(token=token)

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/orders/get",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    listOrders = txt['data']

    arrayData = []

    dataWaited = {}
    dataWaited['customerId'] = 2
    dataWaited['productId'] = 2

    arrayData.append(dataWaited)

    dataWaited = {}
    dataWaited['customerId'] = 2
    dataWaited['productId'] = 1

    arrayData.append(dataWaited)

    
    #listOrders = ordersModel.getAll()


    i = 0

    for item in listOrders :
        assert item['customerId'] == arrayData[i]['customerId']
        assert item['productId'] == arrayData[i]['productId']
        i = i + 1

    assert len(listOrders) == 2

def test_Carts_add2() :
    #cartsModel = CartsModel()

    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = add_carts_json(token=token,customerId="1",productId="1")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/carts",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0


    #codReturn = cartsModel.add(customerId=1,productId=1)
    #assert codReturn == 0

    token = auth_get(loginname="teste",password="teste")

    data = add_carts_json(token=token,customerId="2",productId="2")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/carts",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    #codReturn = cartsModel.add(customerId=2,productId=2)
    #assert codReturn == 0
    
    token = auth_get(loginname="teste",password="teste")

    data = add_carts_json(token=token,customerId="2",productId="1")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/carts",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

    #codReturn = cartsModel.add(customerId=2,productId=1)
    #assert codReturn == 0

def test_Customers_add2() :
    #customersModel = CustomersModel()

    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = add_customers_json(token=token,name="Juca",fullname="Juca o tal",birth="05/04/1965",document="30383365058",gender="M")

    print(data)

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/customers",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0


    #codReturn = customersModel.add(name="Juca",fullname="Juca o tal",birth="05/04/1965",document="30383365058",gender="M")
    #assert codReturn == 0

def test_Products_add2() :
    #productsModel = ProductsModel()
    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = add_products_json(token=token,name="PlayStation 5",brand="Sony",qtd="1",codProduct="3",linkImg="/3.png",price="10000.00")
    print(data)
    #codReturn = productsModel.add(name="Batedeira",brand="Arno",qtd="1",codProduct="1",linkImg="/1.png")

    txt = requests.post("https://calm-hamlet-60163.herokuapp.com/products",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0


    #codReturn = productsModel.add(name="PlayStation 5",brand="Sony",qtd="1",codProduct="3",linkImg="/3.png")

    #assert codReturn == 0



############# Tests DELETE Data TABLES #################

def test_Carts_delete() :
    #cartsModel = CartsModel()
    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = get_carts_json(token=token,id="1")

    print(data)

    txt = requests.delete("https://calm-hamlet-60163.herokuapp.com/carts",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

def test_Carts_deleteCustomer() :
    #cartsModel = CartsModel()
    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = getCustomer_carts_json(token=token,customerId="2")

    print(data)

    txt = requests.delete("https://calm-hamlet-60163.herokuapp.com/carts",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

def test_Products_delete() :
    #productsModel = ProductsModel()
    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = get_products_json(token=token,id="5")

    print(data)

    txt = requests.delete("https://calm-hamlet-60163.herokuapp.com/products",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0

def test_Customers_delete() :
    #customersModel = CustomersModel()

    headers = get_headers()

    token = auth_get(loginname="teste",password="teste")

    data = get_customers_json(token=token,id="3")

    print(data)

    txt = requests.delete("https://calm-hamlet-60163.herokuapp.com/customers",headers=headers,data=data).json()
    print(txt)
    
    assert txt['codReturn'] == 0
    

    
