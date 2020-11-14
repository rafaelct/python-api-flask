from models.Carts import Carts as ModelCarts
from controllers.utils.StatusReturn import StatusReturn
from controllers.utils.ValidateToken import ValidateToken
from flask import jsonify
from controllers.utils.getKey import getKey

class Carts :

    def methodGet(self,request) :
        carts = ModelCarts()

        data = request.get_json(silent=True)

        token = getKey(data,"token")
        id = getKey(data,"id")
        customerId = getKey(data,"customerId")

        #token = request.args.get("token")
        #id = request.args.get("id")
        #customerId = request.args.get("customerId")

        validateToken = ValidateToken()
        dataReturn = validateToken.validate(token)

        if len(dataReturn) > 0 :
            return jsonify( dataReturn )

        statusReturn = StatusReturn()

        try :

            if id != None :
                data = carts.get(id)
                return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success",data= data ))
            elif customerId != None :
                data = carts.getCustomer(customerId)
                return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success", data= data ))
            else :
                data = carts.getAll()
                return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success",data= data ))

        except Exception as error :
                return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )

    def methodPost(self,request) :
        carts = ModelCarts()

        data = request.get_json(silent=True)

        token = getKey(data,"token")
        customerId = getKey(data,"customerId")
        productId = getKey(data,"productId")
        
        #token = request.args.get("token")
        #customerId = request.args.get("customerId")
        #productId = request.args.get("productId")

        validateToken = ValidateToken()
        dataReturn = validateToken.validate(token)

        if len(dataReturn) > 0 :
            return jsonify( dataReturn )


        statusReturn = StatusReturn()

        try :
            carts.add(customerId=customerId,productId=productId)
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )

        except Exception as error:
            
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )

    def methodDelete(self,request) :
        carts = ModelCarts()

        data = request.get_json(silent=True)

        token = getKey(data,"token")
        id = getKey(data,"id")
        customerId = getKey(data,"customerId")
        productId = getKey(data,"productId")

        #token = request.args.get("token")
        #id = request.args.get("id")
        #customerId = request.args.get("customerId")
        #productId = request.args.get("productId")
        

        validateToken = ValidateToken()
        dataReturn = validateToken.validate(token)

        if len(dataReturn) > 0 :
            return jsonify( dataReturn )

        statusReturn = StatusReturn()

        try :

            if id == None and customerId != None and productId == None :
                carts.deleteCustomer(customerId)
            else :
                carts.delete(id=id)
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )

        except Exception as error:
            
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )



    
    

