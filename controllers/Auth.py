from models.Auth import Auth as ModelAuth
from controllers.utils.StatusReturn import StatusReturn
from flask import jsonify

class Auth :

    def methodPost(self,request) :
        
        auth = ModelAuth()

        login = request.args.get("loginname")
        password = request.args.get("password")

        statusReturn = StatusReturn()

        try :
            data = auth.get(login=login,password=password)
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success",data= data))
        except Exception as error :
            return statusReturn.getStatus(codReturn=1,msgReturn=str(error))
