import psycopg2
from .utils.InsertTable import InsertTable
from .utils.UpdateTable import UpdateTable
from config.Config import strDb


class Customers :

    def add(self,name,fullname,birth,document,gender) :
        
        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()

        self.insertTable = InsertTable("Customers")
        self.insertTable.addValue("name","'"+name+"'")
        self.insertTable.addValue("fullname","'"+fullname+"'")
        self.insertTable.addValue("birth","to_date('"+birth+"','MM/DD/YYYY')")
        self.insertTable.addValue("gender","'"+gender+"'")
        self.insertTable.addValue("document","'"+document+"'")
        
        #self.cursor.execute("insert into Customers (name,fullname,birth,document,gender) values('"+name+"','"+fullname+"',to_date('"+birth+"','MM/DD/YYYY'),'"+document+"','"+gender[0]+"')")
        #print(self.insertTable.getInsert())
        self.cursor.execute(self.insertTable.getInsert() )

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def update(self,id,name,fullname,birth,document,gender) :
        
        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()

        self.updateTable = UpdateTable("Customers")
        self.updateTable.addValue("name","'"+name+"'")
        self.updateTable.addValue("fullname","'"+fullname+"'")
        self.updateTable.addValue("birth","to_date('"+birth+"','MM/DD/YYYY')")
        self.updateTable.addValue("gender","'"+gender+"'")
        self.updateTable.addValue("document","'"+document+"'")
        self.updateTable.addWhere("id = "+str(id) )
        
        #self.cursor.execute("insert into Customers (name,fullname,birth,document,gender) values('"+name+"','"+fullname+"',to_date('"+birth+"','MM/DD/YYYY'),'"+document+"','"+gender[0]+"')")
        #print(self.insertTable.getInsert())
        self.cursor.execute(self.updateTable.getUpdate() )

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def getAll(self) :
        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()
        self.cursor.execute("select id,name,fullname,to_char(birth,'MM/DD/YYYY'),gender,document from Customers")

        #self.data = {}
        self.listData = []

        for item in self.cursor.fetchall() :
            data = {}
            data['id'] = item[0]
            data['name'] = item[1]
            data['fullname'] = item[2]
            data['birth'] = item[3]
            data['gender'] = item[4]
            data['document'] = item[5]
            self.listData.append(data)
        
        self.cursor.close()
        self.conn.close()
        
        return self.listData

    def get(self,id) :
        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()
        self.cursor.execute("select id,name,fullname,to_char(birth,'MM/DD/YYYY'),gender,document from Customers where id = "+str(id))

        #self.data = {}
        self.listData = []

        for item in self.cursor.fetchall() :
            data = {}
            data['id'] = item[0]
            data['name'] = item[1]
            data['fullname'] = item[2]
            data['birth'] = item[3]
            data['gender'] = item[4]
            data['document'] = item[5]
            self.listData.append(data)
        
        self.cursor.close()
        self.conn.close()
        
        return self.listData

    def delete(self,id) :

        returnSelectId = self.get(id)

        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()

        self.cursor.execute("delete from Customers where id = "+str(id))
        self.conn.commit()

        self.cursor.close()
        self.conn.close()
        
        return returnSelectId

if __name__ == "__main__" :
    customers = Customers()
    print( customers.get(13))
    print(customers.get(13))
    print(customers.delete(13) )
    print(customers.get(13))
    
    #customers.update(12,"Toninho","Toninho Completo","03/30/2000","12398745690","M")
    #print(customers.get(12))
