

class DbTable:


    def __init__(self, Database, Schema, Table):
        self.Database = Database
        self.Schema = Schema
        self.Table = Table
        self.SchemaTable = (Schema + "." + Table)


    def getColumnDefinitions(self):
        pass

    def getRowCount(self):
        pass

    def getMaxDate(self):
        pass

    def getMinDate(self):
        pass

    
