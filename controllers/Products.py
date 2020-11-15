from models.Products import Products as ModelProducts
from controllers.utils.StatusReturn import StatusReturn
from controllers.utils.ValidateToken import ValidateToken
from flask import jsonify
from controllers.utils.getKey import getKey

class Products :

    def methodGet(self,request) :
        products = ModelProducts()

        data = request.get_json(silent=True)

        token = getKey(data,"token")
        id = getKey(data,"id")

        #token = request.args.get("token")
        #id = request.args.get("id")

        validateToken = ValidateToken()
        dataReturn = validateToken.validate(token)

        if len(dataReturn) > 0 :
            return jsonify( dataReturn )


        statusReturn = StatusReturn()

        try :

            if id != None :
                #print("ID: "+id)
                data = products.get(id)
                return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success",data= data ) )
            else :
                data = products.getAll()
                return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success",data = data ) )

        except Exception as error :
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )



    def methodPost(self,request) :
        products = ModelProducts()

        data = request.get_json(silent=True)

        token = getKey(data,"token")
        name = getKey(data,"name")
        brand = getKey(data,"brand")
        codProduct = getKey(data,"codProduct")
        qtd = getKey(data,"qtd")
        linkImg = getKey(data,"linkImg")
        price = getKey(data,"price")

        #token = request.args.get("token")
        #name = request.args.get("name")
        #brand = request.args.get("brand")
        #codProduct = request.args.get("codProduct")
        #qtd = request.args.get("qtd")
        #linkImg = request.args.get("linkImg")

        validateToken = ValidateToken()
        dataReturn = validateToken.validate(token)

        if len(dataReturn) > 0 :
            return jsonify( dataReturn )

        statusReturn = StatusReturn()

        try :
            products.add(name=name,brand=brand,codProduct=codProduct,qtd=qtd,linkImg=linkImg,price=price)
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )

        except Exception as error:
            
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )

    def methodPut(self,request) :
        products = ModelProducts()

        data = request.get_json(silent=True)

        token = getKey(data,"token")
        id = getKey(data,"id")
        name = getKey(data,"name")
        brand = getKey(data,"brand")
        codProduct = getKey(data,"codProduct")
        qtd = getKey(data,"qtd")
        linkImg = getKey(data,"linkImg")
        price = getKey(data,"price")

        #token = request.args.get("token")
        #id = request.args.get("id")
        #name = request.args.get("name")
        #brand = request.args.get("brand")
        #codProduct = request.args.get("codProduct")
        #qtd = request.args.get("qtd")
        #linkImg = request.args.get("linkImg")

        validateToken = ValidateToken()
        dataReturn = validateToken.validate(token)

        if len(dataReturn) > 0 :
            return jsonify( dataReturn )

        statusReturn = StatusReturn()

        try :

            if id != None and qtd != None and name == None and brand == None and codProduct == None and linkImg == None :
                products.addQtd(id=id,qtd=qtd)
            else :
                products.update(id=id,name=name,brand=brand,codProduct=codProduct,linkImg=linkImg,price=price)
            
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )

        except Exception as error:
            
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )

    def methodDelete(self,request) :
        products = ModelProducts()

        data = request.get_json(silent=True)

        token = getKey(data,"token")
        name = getKey(data,"name")
        id = getKey(data,"id")
        brand = getKey(data,"brand")
        codProduct = getKey(data,"codProduct")
        qtd = getKey(data,"qtd")
        linkImg = getKey(data,"linkImg")
        price = getKey(data,"price")

        #token = request.args.get("token")
        #id = request.args.get("id")
        #name = request.args.get("name")
        #brand = request.args.get("brand")
        #registration = request.args.get("registration")
        #codProduct = request.args.get("codProduct")
        #qtd = request.args.get("qtd")
        #linkImg = request.args.get("linkImg")

        validateToken = ValidateToken()
        dataReturn = validateToken.validate(token)

        if len(dataReturn) > 0 :
            return jsonify( dataReturn )


        statusReturn = StatusReturn()

        try :

            if id != None and qtd != None and name == None and brand == None and codProduct == None and linkImg == None and price == None :
                products.removeQtd(id=id,qtd=qtd)
            else :
                products.delete(id=id)
            
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )

        except Exception as error:
            
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )

    def validate(self,name,brand,codProduct,qtd,linkImg,price) :

        listErrors = []
        error = {}

        if len(str(name) ) == 0 :
            error['msgerro'] = "name is required"
            listErrors.append(error)
        if len(str(brand)) == 0 :
            error['msgerro'] = "brand is required"
            listErrors.append(error)
        if len(str(codProduct)) == 0 :
            error['msgerro'] = "codProduct is required"
            listErrors.append(error)
        if len(str(qtd)) == 0 :
            error['msgerro'] = "qtd is required"
            listErrors.append(error)
        if len( str(linkImg) ) == 0 :
            error['msgerro'] = "linkImg is required"
            listErrors.append(error)
        if len( str(price) ) == 0 :
            error['msgerro'] = "price is required"


        return listErrors


