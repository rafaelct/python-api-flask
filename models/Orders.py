import psycopg2
from .utils.InsertTable import InsertTable
from .utils.UpdateTable import UpdateTable
from .Carts import Carts
from config.Config import strDb

class Orders :

    def add(self,customerId) :
        
        carts = Carts()

        data = carts.getCustomer(customerId)

        

        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()

        

        for item in data :

            customerId = item['customerId']
            productId = item['productId']
            #registration = item['registration']

            self.insertTable = InsertTable("Orders")
            self.insertTable.addValue("customerId",str(customerId))
            self.insertTable.addValue("productId",str(productId))
            self.insertTable.addValue("registration","current_date")
            self.insertTable.addValue("orderstatus","'Aguardando Pagamento'")
            self.cursor.execute(self.insertTable.getInsert() )

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

        data = carts.deleteCustomer(customerId)

        return data

    def getAll(self) :
        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()
        self.cursor.execute("select id,customerId,productId,to_char(registration,'MM/DD/YYYY'),orderstatus from Orders")

        #self.data = {}
        self.listData = []

        for item in self.cursor.fetchall() :
            data = {}
            data['id'] = item[0]
            data['customerId'] = item[1]
            data['productId'] = item[2]
            data['registration'] = item[3]
            data['orderStatus'] = item[4]
 
            self.listData.append(data)
        
        self.cursor.close()
        self.conn.close()
        
        return self.listData

    def get(self,id) :
        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()
        self.cursor.execute("select id,customerId,productId,to_char(registration,'MM/DD/YYYY'),orderstatus from Orders where id = "+str(id))

        #self.data = {}
        self.listData = []

        for item in self.cursor.fetchall() :
            data = {}
            data['id'] = item[0]
            data['customerId'] = item[1]
            data['productId'] = item[2]
            data['registration'] = item[3]
            data['orderStatus'] = item[4]

            self.listData.append(data)
        
        self.cursor.close()
        self.conn.close()
        
        return self.listData

    def getCustomer(self,customerId) :
        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()
        self.cursor.execute("select id,customerId,productId,to_char(registration,'MM/DD/YYYY'),orderstatus from Orders where customerId = "+str(customerId))

        #self.data = {}
        self.listData = []

        for item in self.cursor.fetchall() :
            data = {}
            data['id'] = item[0]
            data['customerId'] = item[1]
            data['productId'] = item[2]
            data['registration'] = item[3]
            data['orderStatus'] = item[4]

            self.listData.append(data)
        
        self.cursor.close()
        self.conn.close()
        
        return self.listData

 
if __name__ == "__main__" :
    orders = Orders()
    #products.add("Notebook HP Core i3 16GB 1TB SSD","HP","06/27/2020",111,20,"/products/notebook_111.jpg")
    #products.add("Geladeira super power freeze","Brastemp","06/27/2020",112,15,'/products/geladeira_112.jpg')
    
    #print( products.get(2) )
    #print( products.update(2,"Geladeira max power freeze","Consul","06/25/2020",112,'/products/geladeira_112.jpg') )
    #print( carts.add(2,1,"06/28/2020") )
    #print( carts.add(2,1,"06/28/2020") )
    print( orders.getAll())
    #print( orders.add(1))
    print( orders.get(1))
    #print( orders.getCustomer(1))
    


