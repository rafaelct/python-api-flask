from models.Registry import Registry as ModelRegistry
from controllers.utils.StatusReturn import StatusReturn
from flask import jsonify

class Registry :

    def methodPost(self,request) :
        
        registration = ModelRegistry()

        login = request.args.get("login")
        password = request.args.get("password")
        fullname = request.args.get("fullname")

        statusReturn = StatusReturn()

        try :
            registration.add(login=login,password=password,fullname=fullname)
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )
        except Exception as error :
            
            return statusReturn.getStatus(codReturn=1,msgReturn=str(error) )

