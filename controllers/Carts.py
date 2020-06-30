from models.Carts import Carts as ModelCarts
from controllers.utils.StatusReturn import StatusReturn
from flask import jsonify

class Carts :

    def methodGet(self,request) :
        carts = ModelCarts()

        id = request.args.get("id")
        customerId = request.args.get("customerId")

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

        customerId = request.args.get("customerId")
        productId = request.args.get("productId")
        #registration = request.args.get("registration")

        statusReturn = StatusReturn()

        try :
            carts.add(customerId=customerId,productId=productId)
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )

        except Exception as error:
            
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )

    def methodDelete(self,request) :
        carts = ModelCarts()

        id = request.args.get("id")
        customerId = request.args.get("customerId")
        productId = request.args.get("productId")
        #registration = request.args.get("registration")

        statusReturn = StatusReturn()

        try :

            if id == None and customerId != None and productId == None :
                carts.deleteCustomer(customerId)
            else :
                carts.delete(id=id)
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )

        except Exception as error:
            
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )



    
    

