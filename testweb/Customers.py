
def get_customers_json(token,id) :
    data = {}
    data['token'] = token
    data['id'] = id
    data = str(data).replace("'",'"')
    return data

def getAll_customers_json(token) :
    data = {}
    data['token'] = token
    data = str(data).replace("'",'"')
    return data

def add_customers_json(token,name,fullname,birth,document,gender) :
    data = {}
    data['token'] = token
    data['name'] = name
    data['fullname'] = fullname
    data['birth'] = birth
    data['document'] = document
    data['gender'] = gender
    data = str(data).replace("'",'"')

    return data
    
def update_customers_json(id,token,name,fullname,birth,document,gender) :
    data = {}
    data['token'] = token
    data['id'] = id
    data['name'] = name
    data['fullname'] = fullname
    data['birth'] = birth
    data['document'] = document
    data['gender'] = gender
    data = str(data).replace("'",'"')

    return data
    
def delete_customers_json(token,id) :
    data = {}
    data['token'] = token
    data['id'] = id
    data = str(data).replace("'",'"')
    return data

