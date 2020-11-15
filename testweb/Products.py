

def add_products_json(token,name,brand,qtd,codProduct,linkImg,price) :

    data = {}
    data['token'] = token
    data['name'] = name
    data['brand'] = brand
    data['qtd'] = qtd
    data['codProduct'] = codProduct
    data['linkImg'] = linkImg
    data['price'] = price
    data = str(data).replace("'",'"')
    return data

def update_products_json(token,id,name,brand,codProduct,linkImg,price) :

    data = {}
    data['token'] = token
    data['id'] = id
    data['name'] = name
    data['brand'] = brand
    #data['qtd'] = qtd
    data['codProduct'] = codProduct
    data['linkImg'] = linkImg
    data['price'] = price
    data = str(data).replace("'",'"')
    return data

def get_products_json(token,id) :

    data = {}
    data['token'] = token
    data['id'] = id
    data = str(data).replace("'",'"')
    return data

def getAll_products_json(token) :

    data = {}
    data['token'] = token
    data = str(data).replace("'",'"')
    return data

def addQtd_products_json(token,id,qtd) :
    data = {}
    data['token'] = token
    data['id'] = id
    data['qtd'] = qtd
    data = str(data).replace("'",'"')
    return data

def removeQtd_products_json(token,id,qtd) :
    data = {}
    data['token'] = token
    data['id'] = id
    data['qtd'] = qtd
    data = str(data).replace("'",'"')
    return data
