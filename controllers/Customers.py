from models.Customers import Customers as ModelCustomers
from controllers.utils.StatusReturn import StatusReturn
from controllers.utils.ValidateToken import ValidateToken
from controllers.utils.Cpf import Cpf
from flask import jsonify
from controllers.utils.getKey import getKey

class Customers :

    def methodGet(self,request) :
        customers = ModelCustomers()
        #data = ""

        #if request.method == 'GET' :
        token = request.args.get("token")
        id = request.args.get("id")

        validateToken = ValidateToken()
        dataReturn = validateToken.validate(token)

        if len(dataReturn) > 0 :
            return jsonify( dataReturn )
        
        statusReturn = StatusReturn()

        try :

            if id != None :
                data = customers.get(id)
                return jsonify(statusReturn.getStatus(codReturn=0,msgReturn="Success",data= data ) )
            else :
                data = customers.getAll()
                return jsonify(statusReturn.getStatus(codReturn=0,msgReturn="Success",data= data ) )

        except Exception as error :
            return jsonify(statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )


    def methodPost(self,request) :
        customers = ModelCustomers()

        data = request.get_json(silent=True)

        token = getKey(data,"token")
        id = getKey(data,"id")
        name = getKey(data,"name")
        fullname = getKey(data,"fullname")
        birth = getKey(data,"birth")
        document = getKey(data,"document")
        gender = getKey(data,"gender")
        

        #token = request.args.get("token")
        #name = request.args.get("name")
        #fullname = request.args.get("fullname")
        #birth = request.args.get("birth")
        #document = request.args.get("document")
        #gender = request.args.get("gender")

        validateToken = ValidateToken()
        dataReturn = validateToken.validate(token)

        if len(dataReturn) > 0 :
            return jsonify( dataReturn )

        statusReturn = StatusReturn()

        listErrors = self.validate(name=name,fullname=fullname,birth=birth,document=document,gender=gender)

        if len(listErrors) > 0 :
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn="Failed",data = listErrors) )

        try :
            customers.add(name=name,fullname=fullname,birth=birth,document=document,gender=gender)
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )

        except Exception as error :
            
            
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )

    def methodPut(self,request) :
        customers = ModelCustomers()

        data = request.get_json(silent=True)

        token = getKey(data,"token")
        id = getKey(data,"id")
        name = getKey(data,"name")
        fullname = getKey(data,"fullname")
        birth = getKey(data,"birth")
        document = getKey(data,"document")
        gender = getKey(data,"gender")

        #token = request.args.get("token")
        #id = request.args.get("id")
        #name = request.args.get("name")
        #fullname = request.args.get("fullname")
        #birth = request.args.get("birth")
        #document = request.args.get("document")
        #gender = request.args.get("gender")

        validateToken = ValidateToken()
        dataReturn = validateToken.validate(token)

        if len(dataReturn) > 0 :
            return jsonify( dataReturn )

        statusReturn = StatusReturn()

        listErrors = self.validate(name=name,fullname=fullname,birth=birth,document=document,gender=gender)

        if len(listErrors) > 0 :
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn="Failed",data = listErrors) )

        try :
            customers.update(id=id,name=name,fullname=fullname,birth=birth,document=document,gender=gender)
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )

        except Exception as error :
            
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )

    def methodDelete(self,request) :
        customers = ModelCustomers()

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
            customers.delete(id=id)
            
            return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )

        except Exception as error :
            
            statusReturn = StatusReturn()
            return jsonify( statusReturn.getStatus(codReturn=1,msgReturn=str(error) ) )
        
    def validate(self,name,fullname,birth,document,gender) :

        listErrors = []
        error = {}

        if len( str(name) ) == 0 :
            error['msgerro'] = "name is required"
            listErrors.append(error)
        if len( str(fullname) ) == 0 :
            error['msgerro'] = "fullname is required"
            listErrors.append(error)
        if len( str(birth) ) == 0 :
            error['msgerro'] = "birth is required"
            listErrors.append(error)
        if len( str(document) ) == 0 :
            error['msgerro'] = "document is required"
            listErrors.append(error)
        if len( str(gender) ) == 0 :
            error['msgerro'] = "gender is required"
            listErrors.append(error)
        if birth[2] != "/" or birth[5] != "/" or len(birth) != 10 :
            error['msgerro'] = "birth invalidad format wait MM/DD/YYYY"
            listErrors.append(error)
        
        cpf1 = Cpf(document)
        
        if cpf1.validate() == False :
            error['msgerro'] = "document is invalid"
            listErrors.append(error)

        if gender != "M" and gender != "F" :
            error['msgerro'] = "gender is invalid format wait M or F"
            listErrors.append(error)
        
        return listErrors
    













