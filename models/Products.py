import psycopg2
from .utils.InsertTable import InsertTable
from .utils.UpdateTable import UpdateTable


class Products :

    def add(self,name,brand,codProduct,qtd,linkImg) :
        
        self.conn = psycopg2.connect("dbname=store user=postgres password=admin")
        self.cursor = self.conn.cursor()

        self.insertTable = InsertTable("Products")
        self.insertTable.addValue("name","'"+name+"'")
        self.insertTable.addValue("brand","'"+brand+"'")
        self.insertTable.addValue("registration","current_date")
        self.insertTable.addValue("codProduct",str(codProduct))
        self.insertTable.addValue("linkImg","'"+linkImg+"'")
        self.insertTable.addValue("qtd",str(qtd))
        
        #self.cursor.execute("insert into Customers (name,fullname,birth,document,gender) values('"+name+"','"+fullname+"',to_date('"+birth+"','MM/DD/YYYY'),'"+document+"','"+gender[0]+"')")
        #print(self.insertTable.getInsert())
        self.cursor.execute(self.insertTable.getInsert() )

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def update(self,id,name,brand,codProduct,linkImg) :
        
        self.conn = psycopg2.connect("dbname=store user=postgres password=admin")
        self.cursor = self.conn.cursor()

        self.updateTable = UpdateTable("Products")
        self.updateTable.addValue("name","'"+name+"'")
        self.updateTable.addValue("brand","'"+brand+"'")
        #self.updateTable.addValue("registration","current_date")
        self.updateTable.addValue("codProduct",str(codProduct))
        self.updateTable.addValue("linkImg","'"+linkImg+"'")
        self.updateTable.addWhere("id = "+str(id) )
        
        #self.cursor.execute("insert into Customers (name,fullname,birth,document,gender) values('"+name+"','"+fullname+"',to_date('"+birth+"','MM/DD/YYYY'),'"+document+"','"+gender[0]+"')")
        #print(self.insertTable.getInsert())
        self.cursor.execute(self.updateTable.getUpdate() )

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def getAll(self) :
        self.conn = psycopg2.connect("dbname=store user=postgres password=admin")
        self.cursor = self.conn.cursor()
        self.cursor.execute("select id,name,brand,to_char(registration,'MM/DD/YYYY'),codProduct,linkImg,qtd from Products")

        #self.data = {}
        self.listData = []

        for item in self.cursor.fetchall() :
            data = {}
            data['id'] = item[0]
            data['name'] = item[1]
            data['brand'] = item[2]
            data['registration'] = item[3]
            data['codProduct'] = item[4]
            data['linkImg'] = item[5]
            data['qtd'] = item[6]

            self.listData.append(data)
        
        self.cursor.close()
        self.conn.close()
        
        return self.listData

    def get(self,id) :
        self.conn = psycopg2.connect("dbname=store user=postgres password=admin")
        self.cursor = self.conn.cursor()
        self.cursor.execute("select id,name,brand,to_char(registration,'MM/DD/YYYY'),codProduct,linkImg,qtd from Products where id = "+str(id))

        #self.data = {}
        self.listData = []

        for item in self.cursor.fetchall() :
            data = {}
            data['id'] = item[0]
            data['name'] = item[1]
            data['brand'] = item[2]
            data['registration'] = item[3]
            data['codProduct'] = item[4]
            data['linkImg'] = item[5]
            data['qtd'] = item[6]

            self.listData.append(data)
        
        self.cursor.close()
        self.conn.close()
        
        return self.listData

    def addQtd(self,id,qtd) :
        self.listData = self.get(id)
        self.conn = psycopg2.connect("dbname=store user=postgres password=admin")
        self.cursor = self.conn.cursor()
        #self.cursor.execute("select id,name,brand,to_char(registration,'MM/DD/YYYY'),codProduct,linkImg,qtd from Products where id = "+str(id))

        #self.data = {}
        #self.listData = self.get(id)
        self.qtdAtual = 0

        for item in self.listData :
            self.qtdAtual = item['qtd']

        self.qtdNova = self.qtdAtual + qtd
        self.cursor.execute("update Products set qtd = "+str(self.qtdNova)+" where id = "+str(id))
        self.conn.commit()

        self.cursor.close()
        self.conn.close()
        
        return self.get(id)

    def removeQtd(self,id,qtd) :
        self.listData = self.get(id)
        self.conn = psycopg2.connect("dbname=store user=postgres password=admin")
        self.cursor = self.conn.cursor()
        #self.cursor.execute("select id,name,brand,to_char(registration,'MM/DD/YYYY'),codProduct,linkImg,qtd from Products where id = "+str(id))

        #self.data = {}
        #self.listData = self.get(id)
        self.qtdAtual = 0

        for item in self.listData :
            self.qtdAtual = item['qtd']

        self.qtdNova = self.qtdAtual - qtd
        self.cursor.execute("update Products set qtd = "+str(self.qtdNova)+" where id = "+str(id))
        self.conn.commit()

        self.cursor.close()
        self.conn.close()
        
        return self.get(id)

    def delete(self,id) :

        returnSelectId = self.get(id)

        self.conn = psycopg2.connect("dbname=store user=postgres password=admin")
        self.cursor = self.conn.cursor()

        self.cursor.execute("delete from Products where id = "+str(id))
        self.conn.commit()

        self.cursor.close()
        self.conn.close()
        
        return returnSelectId

if __name__ == "__main__" :
    products = Products()
    #products.add("Notebook HP Core i3 16GB 1TB SSD","HP","06/27/2020",111,20,"/products/notebook_111.jpg")
    #products.add("Geladeira super power freeze","Brastemp","06/27/2020",112,15,'/products/geladeira_112.jpg')
    
    #print( products.get(2) )
    #print( products.update(2,"Geladeira max power freeze","Consul","06/25/2020",112,'/products/geladeira_112.jpg') )
    print( products.get(1))
    print( products.removeQtd(1,5))
    print( products.get(1))
    


