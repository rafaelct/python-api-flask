
class InsertTable :

    glTableName = ""

    def __init__(self,tableName) :
        #print(tableName)
        self.tableName = tableName
        #self.tableName = ""
        self.listValues = []
        self.data = {}
    
    def addValue(self,columns,value) :
        data = {}
        data['columns'] = columns
        data['value'] = value
        self.listValues.append(data)

    def getInsert(self) :

        strColumns = ""
        strValues = ""

        #print(self.listValues)
        for item in self.listValues :
            strColumns += item['columns']+","
        
        strColumns = strColumns[:-1]

        for item in self.listValues :
            strValues += item['value']+","
        
        strValues = strValues[:-1]

        strCommand = "insert into "+self.tableName+" ("+strColumns+") values ("+strValues+")"

        return strCommand

