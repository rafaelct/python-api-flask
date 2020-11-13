import psycopg2
import time
import random
from config.Config import strDb, expiredToken

class Auth :

    def get(self,login,password) :
        self.conn = psycopg2.connect(strDb, sslmode='require')
        self.cursor = self.conn.cursor()
        self.cursor.execute("select loginname,password from Auth where loginname='"+login+"' and password='"+password+"'")

        data = {}
        
        findLogin = self.cursor.rowcount

        if findLogin == 1 :
            lastRequest = str(time.time() ).split('.')[0]
            token = lastRequest + str(random.randint(1000,9999) )

            self.cursor.execute("update Auth set token='"+token+"', lastRequest="+lastRequest+" where loginname='"+login+"' and password='"+password+"'")
            self.conn.commit()
            data['token'] = token


        
        self.cursor.close()
        self.conn.close()
        
        return data

    def validate(self,token) :

        if token == None :
            return 1
            
        self.conn = psycopg2.connect(strDb)
        self.cursor = self.conn.cursor()
        self.cursor.execute("select loginname,lastRequest from Auth where token='"+token+"'")

        data = {}
        login = ""
        lastRequestBefore = ""

        for item in self.cursor.fetchall() :
            login = item[0]
            lastRequestBefore = item[1]
        
        if lastRequestBefore == "" :
            return 1

        lastRequestNow = str(time.time() ).split('.')[0]
        seconds = int(lastRequestNow) - int(lastRequestBefore)
        print("Seconds: "+ str(seconds))

        if seconds <= expiredToken :
            #lastRequest = str(time.time() ).split('.')[0]
            #token = lastRequest + str(random.randint(1000,9999) )

            self.cursor.execute("update Auth set lastRequest="+lastRequestNow+" where loginname='"+login+"'")
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

            return 0
        else :

            self.cursor.close()
            self.conn.close()

            return 1


if __name__ == "__main__" :
    auth = Auth()
    #print(auth.get(login="rafael",password="tctetscfe"))
    print( auth.validate("15934777067262"))
