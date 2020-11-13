from models.Registry import Registry as ModelRegistry
from controllers.utils.StatusReturn import StatusReturn
from flask import jsonify
from controllers.utils.getKey import getKey

class Registry :

    def methodPost(self,request) :
        
        registration = ModelRegistry()

        data = request.get_json(silent=True)

        login = getKey(data,"loginname")
        password = getKey(data,"password")
        fullname = getKey(data,"fullname")

        #login = request.args.get("loginname")
        #password = request.args.get("password")
        #fullname = request.args.get("fullname")

        statusReturn = StatusReturn()

        try :
            registration.add(login=login,password=password,fullname=fullname)
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )
        except Exception as error :
            
            return statusReturn.getStatus(codReturn=1,msgReturn=str(error) )

