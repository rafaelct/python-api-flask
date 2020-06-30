
class StatusReturn :
    def getStatus(self,codReturn,msgReturn,data=[]) :
        listData = {}

        listData['codReturn'] = codReturn
        listData['msgReturn'] = msgReturn
        listData['data'] = data

        return listData
