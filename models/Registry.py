import psycopg2
from .utils.InsertTable import InsertTable
from .utils.UpdateTable import UpdateTable
from config.Config import strDb

class Registry :

    def add(self,login,password,fullname) :
        
        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()

        self.insertTable = InsertTable("Auth")
        self.insertTable.addValue("login","'"+login+"'")
        self.insertTable.addValue("password","'"+password+"'")
        self.insertTable.addValue("fullname","'"+fullname+"'")
        self.insertTable.addValue("registration","current_date")
        self.cursor.execute( self.insertTable.getInsert() )

        self.conn.commit()
        self.cursor.close()
        self.conn.close()
         
