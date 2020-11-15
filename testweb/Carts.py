
def add_carts_json(token,customerId,productId) :
    data = {}
    data['token'] = token
    data['customerId'] = customerId
    data['productId'] = productId
    data = str(data).replace("'",'"')

    return data

def get_carts_json(token,id) :
    data = {}
    data['token'] = token
    data['id'] = id
    data = str(data).replace("'",'"')

    return data

def getCustomer_carts_json(token,customerId) :
    data = {}
    data['token'] = token
    data['customerId'] = customerId
    data = str(data).replace("'",'"')

    return data

def getAll_carts_json(token) :
    data = {}
    data['token'] = token
    data = str(data).replace("'",'"')

    return data




       