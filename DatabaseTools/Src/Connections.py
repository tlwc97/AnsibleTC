import pyodbc as db
from AnsibleTC.DatabaseTools.Src.DbConstants import *

class DbConnection:


    def __init__(self, Database):
        self.Database = Database
        self.Con = self.getConnection(Database)
        self.Cur = self.Con.cursor()


    def getConnection(self, ConnectionName):

        conString = self.getConnectionList()[ConnectionName]

        return db.connect(conString)


    def getConnectionList(self):

        return conDict


    def closeConnection(self):
        self.Cur.close()
        self.Con.close()

        return 0

    def executeQuery(self, query):

        self.Cur.execute(query)
        self.Cur.commit()


        pass
        ## copy code from work version















#
