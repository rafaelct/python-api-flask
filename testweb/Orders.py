
def add_orders_json(token,customerId) :
    data = {}
    data['token'] = token
    data['customerId'] = customerId
    data = str(data).replace("'",'"')

    return data

def getAll_orders_json(token) :
    data = {}
    data['token'] = token
    data = str(data).replace("'",'"')

    return data
   
def getCustomer_orders_json(token,customerId) :
    data = {}
    data['token'] = token
    data['customerId'] = customerId
    data = str(data).replace("'",'"')

    return data
   