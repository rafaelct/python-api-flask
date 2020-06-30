from models.Orders import Orders as ModelOrders
from controllers.utils.StatusReturn import StatusReturn
from flask import jsonify

class Orders :

    def methodGet(self,request) :

        orders = ModelOrders()

        id = request.args.get("id")
        customerId = request.args.get("customerId")
       
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

        customerId = request.args.get("customerId")

        statusReturn = StatusReturn()

        try :
            orders.add(customerId=customerId)
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )

        except Exception as error:
            
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )


    
    

