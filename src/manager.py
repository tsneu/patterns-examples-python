import os
import configparser

class Manager:
    
    def __init__(self):
        self.env = os.getenv('STAGE')

    def config_db(self, schema):
        settings = configparser.ConfigParser()
        settings.read('./src/config.ini')
        db = settings.items(schema)
        if(self.env == 'prod'):
            db = settings.items(schema + '%s' % self.env)

        db = dict(db)
        return db
