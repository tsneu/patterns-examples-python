import pymssql
from src.manager import Manager
from src.abstract.storages import *
from src.exceptions import DataBaseError
from datetime import datetime, tzinfo, timedelta 

mm = Manager()

class SaoPaulo(tzinfo):
    
    def utcoffset(self, dt):
        return timedelta(hours=-3)
    
    def dst(self, dt):
        return timedelta(0)
    
    def tzname(self, dt):
        return "American/Sao Paulo"

def getdate():
    return datetime.now(tz=SaoPaulo())

class StorageBase(AbstractStorageBase):
    db_connection = None
    db_cursor = None

    def __init__(self):
        try:
            config = mm.config_db('db_sql_server')
            self.db_connection = pymssql.connect(
                host=config['host'], 
                user=config['username'], 
                password=config['password'], 
                database=config['database'])
              
            self.db_cursor = self.db_connection.cursor(as_dict=True)
        except:
            raise DataBaseError('connection')        

    def query_simple(self, sql):
        try:
            self.db_cursor = self.db_connection.cursor(as_dict=True)
            self.db_cursor.execute(sql)
        except Exception as e:
            #print(sql)
            print(e)            
            raise DataBaseError('query', 'SQL Simple ERROR')

    def query(self, query, params):
        try:
            self.db_cursor = self.db_connection.cursor(as_dict=True)
            self.db_cursor.execute(query, params)
        except Exception as e:
            #print(query % params)
            print(e)
            raise DataBaseError('query', 'SQL Error')

    def __del__(self):
        if self.db_connection is not None:
            self.db_connection.close()



class ComplexStorageList(StorageBase, AbstractComplexStorageList):
   
    def get_by_params(self, order_by, pagina, por_pagina):
        pass

    def get_total_registros(self):
        pass


class StorageSimpleList(StorageBase, AbstractStorageSimpleList):

    def get_by_parentid(self, id):
        pass


class Storage(StorageBase, AbstractStorage):

    def get_by_id(self, id):
        pass
