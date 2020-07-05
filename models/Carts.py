import psycopg2
from .utils.InsertTable import InsertTable
from .utils.UpdateTable import UpdateTable
from config.Config import strDb

class Carts :

    def add(self,customerId,productId) :
        
        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()

        self.insertTable = InsertTable("Carts")
        self.insertTable.addValue("customerId",str(customerId))
        self.insertTable.addValue("productId",str(productId))
        self.insertTable.addValue("registration","current_date")
       
        #self.cursor.execute("insert into Customers (name,fullname,birth,document,gender) values('"+name+"','"+fullname+"',to_date('"+birth+"','MM/DD/YYYY'),'"+document+"','"+gender[0]+"')")
        #print(self.insertTable.getInsert())
        self.cursor.execute(self.insertTable.getInsert() )

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def getAll(self) :
        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()
        self.cursor.execute("select id,customerId,productId,to_char(registration,'MM/DD/YYYY') from Carts")

        #self.data = {}
        self.listData = []

        for item in self.cursor.fetchall() :
            data = {}
            data['id'] = item[0]
            data['customerId'] = item[1]
            data['productId'] = item[2]
            data['registration'] = item[3]
 
            self.listData.append(data)
        
        self.cursor.close()
        self.conn.close()
        
        return self.listData

    def get(self,id) :
        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()
        self.cursor.execute("select id,customerId,productId,to_char(registration,'MM/DD/YYYY') from Carts where id = "+str(id))

        #self.data = {}
        self.listData = []

        for item in self.cursor.fetchall() :
            data = {}
            data['id'] = item[0]
            data['customerId'] = item[1]
            data['productId'] = item[2]
            data['registration'] = item[3]

            self.listData.append(data)
        
        self.cursor.close()
        self.conn.close()
        
        return self.listData

    def getCustomer(self,customerId) :
        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()
        self.cursor.execute("select id,customerId,productId,to_char(registration,'MM/DD/YYYY') from Carts where customerId = "+str(customerId))

        #self.data = {}
        self.listData = []

        for item in self.cursor.fetchall() :
            data = {}
            data['id'] = item[0]
            data['customerId'] = item[1]
            data['productId'] = item[2]
            data['registration'] = item[3]

            self.listData.append(data)
        
        self.cursor.close()
        self.conn.close()
        
        return self.listData

 
    def delete(self,id) :

        returnSelectId = self.get(id)

        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()

        self.cursor.execute("delete from Carts where id = "+str(id))
        self.conn.commit()

        self.cursor.close()
        self.conn.close()
        
        return returnSelectId

    def deleteCustomer(self,customerId) :

        returnSelectId = self.getCustomer(customerId)

        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()

        self.cursor.execute("delete from Carts where customerId = "+str(customerId))
        self.conn.commit()

        self.cursor.close()
        self.conn.close()
        
        return returnSelectId

if __name__ == "__main__" :
    carts = Carts()
    #products.add("Notebook HP Core i3 16GB 1TB SSD","HP","06/27/2020",111,20,"/products/notebook_111.jpg")
    #products.add("Geladeira super power freeze","Brastemp","06/27/2020",112,15,'/products/geladeira_112.jpg')
    
    #print( products.get(2) )
    #print( products.update(2,"Geladeira max power freeze","Consul","06/25/2020",112,'/products/geladeira_112.jpg') )
    #print( carts.add(2,1,"06/28/2020") )
    #print( carts.add(2,1,"06/28/2020") )
    print( carts.getCustomer(2))
    print( carts.deleteCustomer(2))
    #print( carts.getAll())
    print( carts.getCustomer(2))
    


