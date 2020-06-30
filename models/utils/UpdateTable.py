
class UpdateTable :

    glTableName = ""

    def __init__(self,tableName) :
        #print(tableName)
        self.tableName = tableName
        #self.tableName = ""
        self.listValues = []
        self.data = {}
        self.strWhere = ""
    
    def addValue(self,columns,value) :
        data = {}
        data['columns'] = columns
        data['value'] = value
        self.listValues.append(data)

    def addWhere(self,wherecommand) :
        self.strWhere = " where "+wherecommand

    def getUpdate(self) :

        strColumns = ""
        strValues = ""
        strSet = ""
        #print(self.listValues)
        for item in self.listValues :
            strSet += item['columns']+" = "+item['value']+","
        
        strSet = strSet[:-1]
        
        strCommand = "update "+self.tableName+" set "+strSet+ self.strWhere

        return strCommand

