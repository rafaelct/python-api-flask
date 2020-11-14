from models.Orders import Orders as ModelOrders
from controllers.utils.StatusReturn import StatusReturn
from controllers.utils.ValidateToken import ValidateToken
from flask import jsonify
from controllers.utils.getKey import getKey

class Orders :

    def methodGet(self,request) :

        orders = ModelOrders()

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
                print("ID: "+id)

                

                data = orders.get(id)
                return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success",data= data) )
            elif customerId != None :
                data = orders.getCustomer(customerId)
                return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success",data= data))
            else :
                data = orders.getAll()
                return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success",data= data) )

        except Exception as error :
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )

    def methodPost(self,request) :
        orders = ModelOrders()

        data = request.get_json(silent=True)

        token = getKey(data,"token")
        customerId = getKey(data,"customerId")
        
        #token = request.args.get("token")
        #customerId = request.args.get("customerId")

        validateToken = ValidateToken()
        dataReturn = validateToken.validate(token)

        if len(dataReturn) > 0 :
            return jsonify( dataReturn )


        statusReturn = StatusReturn()

        try :
            orders.add(customerId=customerId)
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )

        except Exception as error:
            
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )


    
    

