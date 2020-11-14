import psycopg2
from .utils.InsertTable import InsertTable
from .utils.UpdateTable import UpdateTable
from config.Config import strDb

class Registry :

    def add(self,login,password,fullname) :
        
        self.conn = psycopg2.connect(strDb, sslmode='require')
        self.cursor = self.conn.cursor()

        self.insertTable = InsertTable("Auth")
        self.insertTable.addValue("loginname","'"+login+"'")
        self.insertTable.addValue("password","'"+password+"'")
        self.insertTable.addValue("fullname","'"+fullname+"'")
        self.insertTable.addValue("registration","current_date")

        try:

            self.cursor.execute( self.insertTable.getInsert() )

            self.conn.commit()
            self.cursor.close()
            self.conn.close()

        except Exception as error :
            return 1
        
        return 0   
         
