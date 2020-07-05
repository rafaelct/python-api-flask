from models.Auth import Auth
from controllers.utils.StatusReturn import StatusReturn

class ValidateToken :

    def validate(self,token) :
        auth = Auth()

        validReturn = auth.validate(token)

        if validReturn > 0 :
            statusReturn = StatusReturn()
            return statusReturn.getStatus(codReturn=1,msgReturn="Token expired or invalid.")
        return ""
 