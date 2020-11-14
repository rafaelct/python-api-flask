from models.Products import Products as ProductsModel
from controllers.Products import Products as ProductsController
from models.Customers import Customers as CustomersModel
from controllers.Customers import Customers as CustomersController
from models.Carts import Carts as CartsModel
from models.Orders import Orders as OrdersModel
from models.Registry import Registry as RegistryModel
from models.Auth import Auth as AuthModel


def test_registry_add() :
    registryModel = RegistryModel()

    codReturn = registryModel.add(login="teste",password="teste",fullname="Teste o tal")
    assert codReturn == 0
    
def test_registry_add_unique_constraint() :
    registryModel = RegistryModel()

    codReturn = registryModel.add(login="teste",password="teste",fullname="Teste o tal")
    assert codReturn == 1

def test_auth_get() :
    authModel = AuthModel()

    dataReturn = authModel.get(login="teste",password="teste")
    token = dataReturn['token']
    
    assert len( dataReturn['token'] ) > 0
    
def test_auth_validate() :
    authModel = AuthModel()

    dataReturn = authModel.get(login="teste",password="teste")
    token = dataReturn['token']
    print(token)    

    codReturn = authModel.validate(token=token)

    assert codReturn == 0
    
def test_Customers_add() :
    customersModel = CustomersModel()

    codReturn = customersModel.add(name="Fulano",fullname="Fulano de tal",birth="05/04/1960",document="25305309042",gender="M")
    assert codReturn == 0
    codReturn = customersModel.add(name="Siclano",fullname="Siclano de tali",birth="01/11/1977",document="14926960052",gender="M")
    assert codReturn == 0

def test_Customers_getAll() :
    customersModel = CustomersModel()

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

    
    listProducts = customersModel.getAll()


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
    customersModel = CustomersModel()

    arrayData = []

    dataWaited = {}
    dataWaited['name'] = "Fulano"
    dataWaited['fullname'] = "Fulano de tal"
    dataWaited['birth'] = "05/04/1960"
    dataWaited['document'] = "25305309042"
    dataWaited['gender'] = "M"

    arrayData.append(dataWaited)
    
    listProducts = customersModel.get(id=1)


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
    customersModel = CustomersModel()

    customersModel.update(id=1,name="Fulana",fullname="Fulana de tal",birth="05/05/1988",document="25305309042",gender="F")


    listProducts = customersModel.get(id=1)

    assert listProducts[0]['name'] == "Fulana"
    assert listProducts[0]['fullname'] == "Fulana de tal"
    assert listProducts[0]['birth'] == "05/05/1988"
    assert listProducts[0]['document'] == "25305309042"
    assert listProducts[0]['gender'] == "F"

def test_Products_legal() :
    productsModel = ProductsModel()
    assert productsModel.alo() == "legal"
    #assert products.alo() == "legalddd"
    
def test_Products_add() :
    productsModel = ProductsModel()

    codReturn = productsModel.add(name="Batedeira",brand="Arno",qtd="1",codProduct="1",linkImg="/1.png")

    assert codReturn == 0

    codReturn = productsModel.add(name="Fogão",brand="Brastemp",qtd="2",codProduct="2",linkImg="/2.png")

    assert codReturn == 0


def test_Products_unique_constraint_codProduct_in_table_products():
    productsModel = ProductsModel()

    codReturn = productsModel.add(name="Batedeira",brand="Arno",qtd="1",codProduct="1",linkImg="/1.png")

    assert codReturn == 1

    codReturn = productsModel.add(name="Fogão",brand="Brastemp",qtd="2",codProduct="2",linkImg="/2.png")

    assert codReturn == 1

def test_Products_get() :
    productsModel = ProductsModel()

    arrayDados = []

    dadoEsperado = {}
    dadoEsperado['name'] = "Batedeira"
    dadoEsperado['brand'] = "Arno"
    dadoEsperado['qtd'] = 1
    dadoEsperado['codProduct'] = 1
    dadoEsperado['linkImg'] = "/1.png"

    arrayDados.append(dadoEsperado)

    
    listProducts = productsModel.get(id=1)


    i = 0

    for item in listProducts :
        assert item['name'] == arrayDados[i]['name']
        assert item['brand'] == arrayDados[i]['brand']
        assert item['qtd'] == arrayDados[i]['qtd']
        assert item['codProduct'] == arrayDados[i]['codProduct']
        assert item['linkImg'] == arrayDados[i]['linkImg']
        i = i + 1



    assert len(listProducts) == 1

def test_Products_getAll() :
    productsModel = ProductsModel()

    arrayData = []

    dataWaited = {}
    dataWaited['name'] = "Batedeira"
    dataWaited['brand'] = "Arno"
    dataWaited['qtd'] = 1
    dataWaited['codProduct'] = 1
    dataWaited['linkImg'] = "/1.png"

    arrayData.append(dataWaited)

    dataWaited = {}
    dataWaited['name'] = "Fogão"
    dataWaited['brand'] = "Brastemp"
    dataWaited['qtd'] = 2
    dataWaited['codProduct'] = 2
    dataWaited['linkImg'] = "/2.png"

    arrayData.append(dataWaited)

    
    listProducts = productsModel.getAll()


    i = 0

    for item in listProducts :
        assert item['name'] == arrayData[i]['name']
        assert item['brand'] == arrayData[i]['brand']
        assert item['qtd'] == arrayData[i]['qtd']
        assert item['codProduct'] == arrayData[i]['codProduct']
        assert item['linkImg'] == arrayData[i]['linkImg']
        i = i + 1



    assert len(listProducts) == 2


def test_Products_addQtd() :
    productsModel = ProductsModel()

    productsModel.addQtd(id=1,qtd=2)
    productsModel.addQtd(id=2,qtd=4)

    arrayData = productsModel.get(id=1)
    print(arrayData)
    assert arrayData[0]['qtd'] == 3
    
    arrayData = productsModel.get(id=2)
    assert arrayData[0]['qtd'] == 6
    
def test_Products_removeQtd() :
    productsModel = ProductsModel()

    productsModel.removeQtd(id=1,qtd=2)
    productsModel.removeQtd(id=2,qtd=2)

    arrayData = productsModel.get(id=1)
    assert arrayData[0]['qtd'] == 1
    
    arrayData = productsModel.get(id=2)
    assert arrayData[0]['qtd'] == 4

def test_Products_update() :
    productsModel = ProductsModel()

    productsModel.update(id=1,name="Batedeira",brand="Wallita",codProduct="1",linkImg="/1.png")

    listProducts = productsModel.get(id=1)

    assert listProducts[0]['brand'] == "Wallita"

def test_Carts_add() :
    cartsModel = CartsModel()

    codReturn = cartsModel.add(customerId=1,productId=1)
    assert codReturn == 0
    codReturn = cartsModel.add(customerId=2,productId=2)
    assert codReturn == 0
    codReturn = cartsModel.add(customerId=2,productId=1)
    assert codReturn == 0

def test_Carts_getAll() :
    cartsModel = CartsModel()

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

    
    listCarts = cartsModel.getAll()


    i = 0

    for item in listCarts :
        assert item['customerId'] == arrayData[i]['customerId']
        assert item['productId'] == arrayData[i]['productId']
        i = i + 1

    assert len(listCarts) == 3

def test_Carts_get() :
    cartsModel = CartsModel()

    arrayData = []

    dataWaited = {}
    dataWaited['customerId'] = 1
    dataWaited['productId'] = 1

    arrayData.append(dataWaited)
    
    listCarts = cartsModel.get(id=1)


    i = 0

    for item in listCarts :
        assert item['customerId'] == arrayData[i]['customerId']
        assert item['productId'] == arrayData[i]['productId']
        i = i + 1

    assert len(listCarts) == 1

def test_Carts_getCustomer() :
    cartsModel = CartsModel()

    arrayData = []

    
    dataWaited = {}
    dataWaited['customerId'] = 2
    dataWaited['productId'] = 2

    arrayData.append(dataWaited)

    dataWaited = {}
    dataWaited['customerId'] = 2
    dataWaited['productId'] = 1

    arrayData.append(dataWaited)

    listCarts = cartsModel.getCustomer(customerId=2)


    i = 0

    for item in listCarts :
        assert item['customerId'] == arrayData[i]['customerId']
        assert item['productId'] == arrayData[i]['productId']
        i = i + 1

    assert len(listCarts) == 2

def test_Orders_add() :
    ordersModel = OrdersModel()

    itemReturn = ordersModel.add(customerId=2)

    assert itemReturn[0]['customerId'] == 2
    assert itemReturn[0]['productId'] == 2

    assert itemReturn[1]['customerId'] == 2
    assert itemReturn[1]['productId'] == 1

def test_Orders_getAll() :
    ordersModel = OrdersModel()

    arrayData = []

    dataWaited = {}
    dataWaited['customerId'] = 2
    dataWaited['productId'] = 2

    arrayData.append(dataWaited)

    dataWaited = {}
    dataWaited['customerId'] = 2
    dataWaited['productId'] = 1

    arrayData.append(dataWaited)

    
    listOrders = ordersModel.getAll()


    i = 0

    for item in listOrders :
        assert item['customerId'] == arrayData[i]['customerId']
        assert item['productId'] == arrayData[i]['productId']
        i = i + 1

    assert len(listOrders) == 2

def test_Carts_add2() :
    cartsModel = CartsModel()

    codReturn = cartsModel.add(customerId=1,productId=1)
    assert codReturn == 0
    codReturn = cartsModel.add(customerId=2,productId=2)
    assert codReturn == 0
    codReturn = cartsModel.add(customerId=2,productId=1)
    assert codReturn == 0

def test_Customers_add2() :
    customersModel = CustomersModel()

    codReturn = customersModel.add(name="Juca",fullname="Juca o tal",birth="05/04/1965",document="30383365058",gender="M")
    assert codReturn == 0

def test_Products_add2() :
    productsModel = ProductsModel()

    codReturn = productsModel.add(name="PlayStation 5",brand="Sony",qtd="1",codProduct="3",linkImg="/3.png")

    assert codReturn == 0



############# Tests DELETE Data TABLES #################3

def test_Carts_delete() :
    cartsModel = CartsModel()

    itemReturn = cartsModel.delete(id=1)
    assert itemReturn[0]['id'] == 1
    assert itemReturn[0]['customerId'] == 1
    assert itemReturn[0]['productId'] == 1

def test_Carts_deleteCustomer() :
    cartsModel = CartsModel()

    itemReturn = cartsModel.deleteCustomer(customerId=2)

    assert itemReturn[0]['customerId'] == 2
    assert itemReturn[0]['productId'] == 2

    assert itemReturn[1]['customerId'] == 2
    assert itemReturn[1]['productId'] == 1

def test_Products_delete() :
    productsModel = ProductsModel()

    itemReturn = productsModel.delete(id=5)
    assert itemReturn[0]['id'] == 5

def test_Customers_delete() :
    customersModel = CustomersModel()

    itemReturn = customersModel.delete(id=3)
    assert itemReturn[0]['id'] == 3
    

    
